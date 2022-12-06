from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
    ]
