from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import Project
from .forms import TaskForm

class ProjectListView(LoginRequiredMixin, ListView):
    template_name = "projects/projects.html"
    model = Project

class ProjectDetailView(DetailView):
    template_name = "projects/project-detail.html"
    model = Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/project-new.html"
    model = Project
    form_class = TaskForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "projects/project-update.html"
    model = Project
    fields = []

    def test_func(self):
        ticket_obj = self.get_object()
        return ticket_obj.author == self.request.user

class ProjectDelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "projects/project-delete.html"
    model = Project
    success_url = reverse_lazy("projects")
    
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


