from django.urls import path

from apps.main.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
