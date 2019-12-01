from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = "/accounts/login/"
