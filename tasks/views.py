from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import Task
from .forms import TaskForm

class TaskListView(LoginRequiredMixin, ListView):
    template_name = "tasks/tasks.html"
    model = Task

class TaskDetailView(DetailView):
    template_name = "tasks/task-detail.html"
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/task-new.html"
    model = Task
    form_class = TaskForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "tasks/task-update.html"
    model = Task
    fields = []

    def test_func(self):
        ticket_obj = self.get_object()
        return ticket_obj.author == self.request.user

class TaskDelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "tasks/task-delete.html"
    model = Task
    success_url = reverse_lazy("tasks")
    
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


