from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pictures", blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        if self.profile_pic:
            image_path = self.profile_pic.path
            img = Image.open(image_path)

            if img.size[0] > 300 or img.size[1] > 300:
                img.thumbnail((300, 300))
                img.save(image_path)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    instance.profile.save()
