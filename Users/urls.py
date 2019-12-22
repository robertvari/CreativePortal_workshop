from django.urls import path, include

from .views import SignUpView, ProfileView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
]