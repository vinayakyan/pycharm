from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection


def add_department(request):
    template_name = "departments_app/add_department.html"
    if request.method == 'POST':
        department_name = request.POST.get('department_name')
        department_location = request.POST.get('department_location')
        with connection.cursor() as cursor:
            sql = 'insert into departments_app_departments(department_name,department_location) values(%s, %s)'
            row = cursor.execute(sql, (department_name, department_location))
            connection.commit()
        if row:
            cursor.close()
            return redirect('show-dept')

    return render(request, template_name)


def show_departments(request):
    template_name = 'departments_app/display_departments.html'
    with connection.cursor() as cursor:
        sql = 'select * from departments_app_departments'
        cursor.execute(sql)
        data = []
        for obj in cursor.fetchall():
            d = {'id': obj[0], 'department_name': obj[1], 'department_location': obj[2]}
            data.append(d)
        cursor.close()
    return render(request, template_name, {'data': data})
