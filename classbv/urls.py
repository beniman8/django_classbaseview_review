from django.urls import path
from django.views.generic import TemplateView
from .views import HomeTemplateView


app_name = 'website'

urlpatterns = [
    
    path('', TemplateView.as_view(template_name='classbv/index.html',extra_context={'title':'Custom Title'})),
    path('home/',HomeTemplateView.as_view()),
]
