from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_name', 'emp_designation', 'emp_dept', 'emp_pan', 'emp_voter')
