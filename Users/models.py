from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from PIL import Image
import os, shutil, time


def photo_directory_path(instance, filename):
    return f'posts/{instance.author}/{filename}'


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to=photo_directory_path)

    # social feaures
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")
    picked = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    slug = models.SlugField(max_length=200, blank=True)

    updated_on = models.DateTimeField(auto_now=True)
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_on',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'Comment: {self.comment[:50]}... by {self.user}'


class CreativeUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, superuser=False):
        if not email:
            raise ValueError("User must have an email!")

        if not full_name:
            raise ValueError("User must have Full name!")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )

        user.set_password(password)

        if superuser:
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True

        user.save(using=self._db)

        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email,
            full_name,
            password,
            superuser=True
        )

        return user


class CreativeUser(AbstractBaseUser):
    # for allauth
    username = models.CharField(max_length=200, blank=True)

    # required for registration
    email = models.EmailField(max_length=200, unique=True)
    USERNAME_FIELD = 'email'

    full_name = models.CharField(max_length=200)
    REQUIRED_FIELDS = ('full_name',)

    # profile
    profile_pic = models.ImageField(upload_to="profile_pictures", blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    # social features
    follows = models.ManyToManyField('self', related_name='followers', blank=True, symmetrical=False)
    # likes = models.ManyToManyField(Post, related_name='likes', blank=True)

    # required for BaseUser
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CreativeUserManager()

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        try:
            user = CreativeUser.objects.get(id=self.id)
            if user:
                if user.profile_pic.name != self.profile_pic.name:
                    user.profile_pic.delete(save=False)
        except Exception as e:
            print(e)
            pass

        super().save(*args, **kwargs)

        if self.profile_pic:
            image_path = self.profile_pic.path
            img = Image.open(image_path)

            if img.size[0] > 300 or img.size[1] > 300:
                img.thumbnail((300, 300))
                img.save(image_path)

    def delete(self, *args, **kwargs):
        if self.profile_pic:
            self.profile_pic.delete(save=False)

        super().delete(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(pre_save, sender=Post)
def slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = f'{slugify(instance.title)}-{int(time.time())}'


@receiver(post_delete, sender=CreativeUser)
def file_cleanup(sender, instance, **kwargs):
    if instance.profile_pic:
        os.remove(instance.profile_pic.path)


@receiver(post_delete, sender=Post)
def photo_cleanup(sender, instance, **kwargs):
    if instance.photo:
        user_folder = os.path.dirname(instance.photo.path)
        os.remove(instance.photo.path)

        if not os.listdir(user_folder):
            shutil.rmtree(user_folder, ignore_errors=True)
