# Generated by Django 3.2.6 on 2021-08-26 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_mark_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='mark_complete',
        ),
    ]
