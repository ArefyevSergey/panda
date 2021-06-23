from django.urls import path

from apps.frequently_asked_questions.views import FAQListView

urlpatterns = [
    path('', FAQListView.as_view(), name='frequently_asked_questions'),
]
