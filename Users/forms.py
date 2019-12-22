from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CreativeUser


class CustomUserSignupForm(UserCreationForm):
    class Meta:
        model = CreativeUser
        fields = (
            'email',
            'full_name',
            'password1',
            'password2'
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CreativeUser
        fields = (
            "full_name",
            "profile_pic",
            "bio",
            "location",
            "birth_date",
            "facebook",
            "twitter",
            "instagram",
            "linkedin",
        )