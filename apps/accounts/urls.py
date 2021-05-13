from django.urls import path
from .views import RegisterFormView, LoginFormView, LogoutView, ProfileView

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
