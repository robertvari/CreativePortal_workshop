from django.urls import path

from .views import HomeView, PostDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/<str:slug>', PostDetailsView.as_view(), name='post_details'),
]
