# Generated by Django 4.1.3 on 2022-12-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='Type your comment here...', max_length=300),
        ),
    ]
