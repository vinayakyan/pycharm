from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.conf import settings
from django.core.files import File
import os


def add_employee(request):
    template_name = 'employee_app/add_employee.html'
    if request.method == 'POST':
        name = request.POST.get('name')
        desg = request.POST.get('designation')
        dept = request.POST.get('dept')
        pan = request.FILES.get('pan')
        voter = request.FILES.get('voter')
        pan_file = os.path.join(settings.MEDIA_ROOT, 'emp_pan\\'+name+pan.name)
        voter_file = os.path.join(settings.MEDIA_ROOT, 'emp_voter\\' + name + voter.name)
        with open(pan_file, 'wb') as fp, open(voter_file, 'wb') as f:
            fp.write(pan.read())
            f.write(voter.read())
        with connection.cursor() as cursor:
            sql = 'insert into employee_app_employee(emp_name,emp_designation,emp_dept_id,emp_pan,emp_voter)'\
                    'values(%s, %s, %s, %s, %s)'
            row = cursor.execute(sql, (name, desg, dept, pan_file, voter_file))
            connection.commit()
            cursor.close()
        if row:
            return HttpResponse('<h2>SuccessFul!!!!</h2>')
    depts = []
    with connection.cursor() as cursor:
        sql = 'select id from departments_app_departments'
        cursor.execute(sql)
        for ele in cursor.fetchall():
            depts.append({'id': ele[0]})
        cursor.close()
    context = {'depts': depts}

    return render(request, template_name, context)
