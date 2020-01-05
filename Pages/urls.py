from django.urls import path

from .views import HomeView, PostDetailsView, PostFilterView, PostUploadView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostFilterView.as_view(), name='post_filters'),
    path('posts/<str:slug>', PostDetailsView.as_view(), name='post_details'),
    path('upload/', PostUploadView.as_view(), name="upload")
]
