from django import forms
from django.forms import ModelForm

from .models import Task, Comment
from accounts.models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_summary', 'task_details', 'deadline', 'assignee', 'project', 'status', 'priority']
        widgets = {
            'deadline' : DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        
        self.fields['assignee'].required= False
        self.fields['status'].required=True

class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']