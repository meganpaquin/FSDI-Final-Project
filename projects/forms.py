from django import forms
from django.forms import ModelForm
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Project, Comment

class DateInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'summary', 'deadline', 'status', 'members']
        widgets = {
            'deadline' : DateInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ProjectModelForm(BSModalModelForm):
    class Meta:
        model = Project
        exclude = ['timestamp']

    
