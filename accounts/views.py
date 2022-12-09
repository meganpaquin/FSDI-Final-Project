from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CustomUserChangeForm, NewTeamForm
from django.urls import reverse_lazy
from .models import CustomUser, Team
from django.views.generic import ListView
from bootstrap_modal_forms.generic import BSModalDeleteView

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

class UserChangeView(UpdateView):
    template_name = 'registration/change_user.html'
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy("home")

class PermissionListView(ListView):
    template_name = "accounts/permissions.html"
    model = CustomUser

class PermissionChangeView(UpdateView):
    template_name = "accounts/permissions-edit.html"
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy("permissions")

class TeamListView(ListView):
    template_name= 'accounts/teams.html'
    model = Team

class TeamUpdateView(UpdateView):
    template_name = "accounts/team-edit.html"
    model = Team
    fields = ['name', 'leader', 'members']

class NewTeamView(CreateView):
    template_name = "accounts/team-new.html"
    form_class = NewTeamForm
    success_url = reverse_lazy('teams')

class TeamDeleteView(BSModalDeleteView):
    template_name = 'accounts/team-delete.html'
    model = Team
    success_url = reverse_lazy("teams")
