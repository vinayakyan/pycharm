from django.urls import path
from .views import add_department, show_departments

urlpatterns = [
    path('department/', add_department, name='add-dept'),
    path('show_dept/', show_departments, name='show-dept'),
]