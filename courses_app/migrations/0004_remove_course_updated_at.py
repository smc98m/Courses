# Generated by Django 2.2 on 2020-05-02 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0003_course_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='updated_at',
        ),
    ]
