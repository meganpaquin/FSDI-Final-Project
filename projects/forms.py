from django import forms
from django.forms import ModelForm

from .models import Project

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'summary', 'deadline', 'assignee', 'status']
        widgets = {
            'deadline' : DateInput()
        }