from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = "/accounts/login/"


class ProfileView(TemplateView):
    template_name = "users/profile.html"
