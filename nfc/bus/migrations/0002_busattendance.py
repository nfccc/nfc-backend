# Generated by Django 5.0.6 on 2024-11-03 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
        ('students', '0004_alter_student_date_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Present', max_length=10)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.bus')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
            options={
                'verbose_name': 'Bus Attendance',
                'verbose_name_plural': 'Bus Attendance Records',
                'unique_together': {('student', 'bus', 'timestamp')},
            },
        ),
    ]