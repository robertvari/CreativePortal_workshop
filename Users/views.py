from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse

from .forms import ProfileForm
from .models import CreativeUser, Post, Comment


# ajax request views
def submit_comment_view(request):
    comment = request.GET.get("comment")
    post_pk = request.GET.get("post_pk")
    user = request.user
    post = Post.objects.get(pk=post_pk)

    new_comment = Comment(
        post=post,
        user=user,
        comment=comment
    )
    new_comment.save()

    return JsonResponse({"greeting": "Hello there!"})



class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


class ProfileView(LoginRequiredMixin, UpdateView):
    model = CreativeUser
    form_class = ProfileForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("home")

    login_url = reverse_lazy("login")
