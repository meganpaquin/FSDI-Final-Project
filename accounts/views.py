from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CustomUserChangeForm, NewTeamForm, AdminUserChangeForm
from django.urls import reverse_lazy
from .models import CustomUser, Team
from django.views.generic import ListView
from bootstrap_modal_forms.generic import BSModalDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class UserChangeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'registration/change_user.html'
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy("home")

    def test_func(self):
        id = self.kwargs['pk']
        if self.request.user.is_superuser:
            return True
        elif self.request.user.id == id:
            return True
     

class PermissionListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "accounts/permissions.html"
    model = CustomUser

    def test_func(self):
        return self.request.user.is_superuser

class PermissionChangeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "accounts/permissions-edit.html"
    form_class = AdminUserChangeForm
    model = CustomUser
    success_url = reverse_lazy("permissions")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected'] = CustomUser.objects.get(id=self.kwargs['pk'])
        return context

    def test_func(self):
        return self.request.user.is_superuser

class TeamListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name= 'accounts/teams.html'
    model = Team

    def test_func(self):
        return self.request.user.is_staff

class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "accounts/team-edit.html"
    model = Team
    fields = ['name', 'leader', 'members']

    def test_func(self):
        return self.request.user.is_staff

class NewTeamView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "accounts/team-new.html"
    form_class = NewTeamForm
    success_url = reverse_lazy('teams')

    def test_func(self):
        return self.request.user.is_staff

class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    template_name = 'accounts/team-delete.html'
    model = Team
    success_url = reverse_lazy("teams")

    def test_func(self):
        return self.request.user.is_staff

