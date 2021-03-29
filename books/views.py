from django.shortcuts import render
from django.views.generic import DetailView,TemplateView
from .models import Book
from django.db.models import F
from django.utils import timezone

class IndexView(TemplateView):
    template_name = "books/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
        return context
    

class BookDetailView(DetailView):
    model = Book
    template_name='books/detail.html'
    context_object_name='book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Book.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)
        context["time"] = timezone.now()
        return context
    
