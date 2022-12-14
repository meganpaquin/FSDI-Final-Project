# Generated by Django 4.1.3 on 2022-12-06 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=120)),
                ('task_summary', models.TextField()),
                ('task_details', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assignee', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
