from django.db import models
from departments_app.models import Departments


class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_designation = models.CharField(max_length=20)
    emp_dept = models.ForeignKey(Departments, on_delete=models.CASCADE)
    emp_pan = models.FileField(upload_to='emp_pan/', blank=True)
    emp_voter = models.FileField(upload_to='emp_voter/', blank=True)

    def __str__(self):
        return f'{self.emp_name}'


