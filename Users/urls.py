from django.urls import path, include

from .views import SignUpView, ProfileView

urlpatterns = [
    path("accounts/", include('django.contrib.auth.urls')),
    path("signup/", SignUpView.as_view(), name="register"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
]