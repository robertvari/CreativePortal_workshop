from django.urls import path, include

from .views import SignUpView, ProfileView, submit_comment_view, submit_like_view

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),

    # ajax calls
    path("ajax/comment_submit/", submit_comment_view),
    path("ajax/like_submit/", submit_like_view)
]