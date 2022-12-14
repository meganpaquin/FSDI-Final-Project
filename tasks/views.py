from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, Comment, Status
from .forms import TaskForm, TaskCommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.shortcuts import redirect

class TaskDetailView(FormMixin, UserPassesTestMixin, DetailView):
    template_name = "tasks/task-detail.html"
    model = Task
    form_class = TaskCommentForm

    def get_success_url(self):
        return reverse('task-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('created_on').reverse()

        context['form'] = TaskCommentForm(initial={'task': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.task = Task.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(TaskDetailView, self).form_valid(form)

    def test_func(self):
        ticket_obj = self.get_object()
        return ticket_obj.author == self.request.user

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/task-new.html"
    model = Task
    form_class = TaskForm

    def form_valid(self,form):
        form.instance.author = self.request.user

        if not self.request.user.is_superuser:
            form.instance.assignee = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "tasks/task-update.html"
    model = Task
    fields = ['task_name', 'task_summary', 'task_details', 'deadline', 'assignee', 'status', 'project', 'priority']

    def test_func(self):
        ticket_obj = self.get_object()
        return ticket_obj.author == self.request.user

class TaskDelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "tasks/task-delete.html"
    model = Task
    success_url = reverse_lazy("home")
    
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user



def mark_completed(request, pk):
    task = Task.objects.get(pk=pk)
    completed = Status.objects.get(name="complete")

    task.status = completed
    task.save()

    return redirect('home')

def complete_list(request, pk):
    task = Task.objects.get(pk=pk)
    completed = Status.objects.get(name="complete")

    task.status = completed
    task.save()

    return redirect('list')

def mark_complete_detail(request, pk):
    task = Task.objects.get(pk=pk)
    assigned = Status.objects.get(name="complete")

    task.status = assigned
    task.save()

    return redirect(reverse('task-detail', kwargs={'pk':task.pk}))

def mark_assigned_detail(request, pk):
    task = Task.objects.get(pk=pk)
    assigned = Status.objects.get(name="assigned")

    task.status = assigned
    task.save()

    return redirect(reverse('task-detail', kwargs={'pk':task.pk}))

def mark_progress_detail(request, pk):
    task = Task.objects.get(pk=pk)
    progress = Status.objects.get(name="in-progress")
    
    task.status = progress
    task.save()

    return redirect(reverse('task-detail', kwargs={'pk':task.pk}))

def mark_archived_detail(request, pk):
    task = Task.objects.get(pk=pk)
    progress = Status.objects.get(name="archived")
    
    task.status = progress
    task.save()

    return redirect(reverse('task-detail', kwargs={'pk':task.pk}))
