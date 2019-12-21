from django import forms
from .models import CreativeUser


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