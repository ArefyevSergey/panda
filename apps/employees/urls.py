from django.urls import path

from apps.employees.views import EmployeesListView


urlpatterns = [
    path('', EmployeesListView.as_view(), name='employees'),
]
