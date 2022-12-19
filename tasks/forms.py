from django import forms
from django.forms import ModelForm, TextInput, TimeInput
from .models import Task, Comment

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_summary', 'task_details', 'deadline_date', 'deadline_time', 'assignee', 'project', 'status', 'priority']
        widgets = {
            'deadline_date' : DateInput(),
            'deadline_time' : TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        
        
        self.fields['assignee'].required= False
        self.fields['status'].required=True
        self.fields['deadline_date'].required=True
        self.fields['deadline_time'].required=True
        self.fields['project'].required=True
        self.fields['priority'].required=True
        

class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': TextInput(attrs={
                'placeholder' : 'Type your comment here...'
            })
        }