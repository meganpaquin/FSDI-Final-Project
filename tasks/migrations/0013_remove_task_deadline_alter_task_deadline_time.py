# Generated by Django 4.1.3 on 2022-12-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_task_deadline_date_task_deadline_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline_time',
            field=models.TimeField(default='14:52'),
        ),
    ]
