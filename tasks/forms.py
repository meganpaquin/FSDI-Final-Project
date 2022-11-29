from django import forms
from django.forms import ModelForm

from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_summary', 'task_details', 'deadline', 'assignee', 'project', 'status', 'priority']
        widgets = {
            'deadline' : DateInput()
        }