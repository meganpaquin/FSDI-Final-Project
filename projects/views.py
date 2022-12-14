from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Project, Comment, Status
from .forms import ProjectForm, CommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from bootstrap_modal_forms.generic import BSModalDeleteView
from django.shortcuts import redirect
from tasks.models import Task, Status

class ProjectListView(LoginRequiredMixin, ListView):
    template_name = "projects/projects.html"
    model = Project

class ProjectDetailView(FormMixin, DetailView):
    template_name = "projects/project-detail.html"
    model = Project
    form_class = CommentForm

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('created_on').reverse()

        context['form'] = CommentForm(initial={'project': self.object})

        progress = Status.objects.get(name="in-progress")
        assigned = Status.objects.get(name="assigned")
        completed = Status.objects.get(name="complete")
        project = Project.objects.get(id=self.kwargs['pk'])

        context['tasks_progress'] = Task.objects.filter(status=progress).filter(project=project).order_by('priority')
        context['tasks_assigned'] = Task.objects.filter(status=assigned).filter(project=project).order_by('priority')
        context['completed'] = Task.objects.filter(status=completed).filter(project=project).order_by('priority')
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
        form.instance.project = Project.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ProjectDetailView, self).form_valid(form)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/project-new.html"
    model = Project
    form_class = ProjectForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "projects/project-update.html"
    model = Project
    fields = ['title', 'summary', 'deadline', 'status', 'members']

    def test_func(self):
        ticket_obj = self.get_object()
        return ticket_obj.author == self.request.user

class ProjectDelView(LoginRequiredMixin, UserPassesTestMixin, BSModalDeleteView):
    template_name = "projects/project-delete.html"
    model = Project
    success_url = reverse_lazy("home")
    
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


def mark_complete_detail(request, pk):
    project = Project.objects.get(pk=pk)
    assigned = Status.objects.get(name="complete")

    project.status = assigned
    project.save()

    return redirect(reverse('project-detail', kwargs={'pk':project.pk}))

def mark_assigned_detail(request, pk):
    project = Project.objects.get(pk=pk)
    assigned = Status.objects.get(name="assigned")

    project.status = assigned
    project.save()

    return redirect(reverse('project-detail', kwargs={'pk':project.pk}))

def mark_progress_detail(request, pk):
    project = Project.objects.get(pk=pk)
    progress = Status.objects.get(name="in-progress")
    
    project.status = progress
    project.save()

    return redirect(reverse('project-detail', kwargs={'pk':project.pk}))

def mark_archived_detail(request, pk):
    project = Project.objects.get(pk=pk)
    progress = Status.objects.get(name="archived")
    
    project.status = progress
    project.save()

    return redirect(reverse('project-detail', kwargs={'pk':project.pk}))
