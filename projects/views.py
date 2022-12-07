from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import Project, Comment
from .forms import ProjectForm, CommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from django.views import View

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


