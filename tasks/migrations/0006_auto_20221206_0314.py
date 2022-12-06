from django.db import migrations

def populate_priority(apps, schemaeditor):
    entries = {
        "low" : "Task is not critical to completion of project",
        "medium" : "Task should be completed in a timely manner",
        "high" : "Task should be completed within 24 hours",
        "urgent" : "task should be completed within 4 hours"
    }
    Priority = apps.get_model("tasks", "Priority")

    for name, desc in entries.items():
        priority_obj = Priority(name=name, description=desc)
        priority_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_priority'),
    ]

    operations = [migrations.RunPython(populate_priority)]