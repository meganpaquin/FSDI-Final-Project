from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Team
from django.forms.widgets import TextInput
from django.urls import reverse_lazy
from django.forms import ModelForm
from bootstrap_modal_forms.forms import BSModalModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'image', 'phone', 'color')
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }

class NewTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'leader', 'members']

class TeamModelForm(BSModalModelForm):
    class Meta:
        model = Team
        exclude = ['timestamp']
