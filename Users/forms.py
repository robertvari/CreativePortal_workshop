from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
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