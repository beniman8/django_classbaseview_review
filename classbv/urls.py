from django.urls import path
from django.views.generic import TemplateView


app_name = 'website'

urlpatterns = [
    path('first/', TemplateView.as_view()),
]
