from django.views.generic import ListView

from apps.about.models import Contacts
from apps.employees.models import Employees


class EmployeesListView(ListView):
    model = Employees
    template_name = 'employees/employees.html'
    ordering = 'relevance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()[0]
        return context
