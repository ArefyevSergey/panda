from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='frequently_asked_questions/frequently_asked_questions.html'),
         name='frequently_asked_questions'),
]
