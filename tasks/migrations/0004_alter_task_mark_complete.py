# Generated by Django 3.2.6 on 2021-08-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_mark_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='mark_complete',
            field=models.BooleanField(),
        ),
    ]
