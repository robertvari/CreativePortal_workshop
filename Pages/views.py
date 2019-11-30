from django.views.generic import TemplateView

from .random_content import get_posts


class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["top_row_list"] = get_posts(10)
        return context
