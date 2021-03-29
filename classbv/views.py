from django.shortcuts import render
from django.views.generic import TemplateView
from classbv.models import Post


class HomeTemplateView(TemplateView):

    template_name='classbv/index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] =  Post.objects.all()
        context["data"] = "This is data for the second page"
        return context
    