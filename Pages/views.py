from django.views.generic import TemplateView, DetailView, ListView
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