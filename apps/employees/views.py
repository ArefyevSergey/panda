from django.views.generic import ListView

from apps.employees.models import Employees


class EmployeesListView(ListView):
    model = Employees
    template_name = 'employees/employees.html'
    ordering = 'relevance'
