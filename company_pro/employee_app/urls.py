from django.urls import path
from .views import add_employee

urlpatterns = [
    path('add_employee/', add_employee, name='add-emp'),
]