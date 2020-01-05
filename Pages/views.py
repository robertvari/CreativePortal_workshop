from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Count
from Users.models import Post


class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["top_row_list"] = Post.objects.all().filter(picked=True)
        return context


class PostFilterView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = "posts"

    def get_queryset(self):
        sorting = self.request.GET.get('sorting')

        if sorting == 'community':
            return self.model.objects.annotate(like_count=Count('likes')).order_by('-like_count')

        elif sorting == 'trending':
            return self.model.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')

        elif sorting == 'picks':
            return self.model.objects.all().filter(picked=True)

        else:
            return self.model.objects.all()


class PostDetailsView(DetailView):
    model = Post
    template_name = 'users/post_details.html'
    context_object_name = "post"


class PostUploadView(LoginRequiredMixin, CreateView):
    model = Post
    fields = (
        'title',
        'photo',
        'description'
    )

    template_name = 'users/post_upload.html'
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_details', kwargs={'slug': self.object.slug})
