# Generated by Django 4.1.5 on 2023-02-12 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_on_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='on_subject',
        ),
    ]
