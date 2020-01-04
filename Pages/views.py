from django.views.generic import TemplateView, DetailView

from Users.models import Post


class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["top_row_list"] = Post.objects.all().filter(picked=True)
        return context


class PostDetailsView(DetailView):
    model = Post
    template_name = 'users/post_details.html'
    context_object_name = "post"