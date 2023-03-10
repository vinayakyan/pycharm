# Generated by Django 4.1.4 on 2022-12-29 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_designation', models.CharField(max_length=20)),
                ('emp_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments_app.departments')),
            ],
        ),
    ]
