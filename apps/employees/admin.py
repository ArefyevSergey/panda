from django.contrib import admin

from apps.employees.models import Employees


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    pass
