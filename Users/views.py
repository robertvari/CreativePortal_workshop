from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"
    login_url = reverse_lazy("login")
