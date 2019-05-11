from django.shortcuts import render
from django.views import generic
from core.models import Post


# Create your views here.
class HomeView(generic.TemplateView):
    print("Hello World")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
