# Generated by Django 4.1.3 on 2022-12-07 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_remove_project_assignee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_project', to='projects.project')),
            ],
        ),
    ]
