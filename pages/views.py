from django.views.generic import TemplateView
from tasks.models import Task, Status, Priority
from projects.models import Project
from datetime import datetime
from django.db.models import Q
from accounts.models import CustomUser, Team
from django.shortcuts import render

class IndexPageView(TemplateView):
    template_name = "pages/index.html"

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        loggedin = self.request.user
        context = super().get_context_data(**kwargs)

        assigned = Status.objects.get(name="assigned")
        context['assigned_tasks'] = Task.objects.filter(status=assigned).order_by('deadline').reverse().order_by('priority')[0:3]

        progress = Status.objects.get(name="in-progress")
        context['progress_tasks'] = Task.objects.filter(status=progress).order_by('deadline').reverse()[0:3]

        context['projects'] = Project.objects.order_by('deadline')
        context['project_members'] = Project.objects.filter(members=loggedin.id)

        context['images'] = CustomUser.objects.all()

        context['teams'] = Team.objects.filter(leader=loggedin.id)
        
        return context
        
class DashboardPageView(TemplateView):
    template_name = "pages/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by('created_on')
        return context

class ListPageView(TemplateView):
    template_name = "pages/list.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        assigned = Status.objects.get(name="assigned")
        context['assigned_tasks'] = Task.objects.filter(status=assigned).order_by('deadline').reverse().filter(deadline__gt=datetime.today()).order_by('priority')

        progress = Status.objects.get(name="in-progress")
        context['progress_tasks'] = Task.objects.filter(status=progress).order_by('deadline').reverse().filter(deadline__gt=datetime.today())

        complete = Status.objects.get(name="complete")
        context['complete_tasks'] = Task.objects.filter(status=complete).order_by('deadline').reverse()

        context['overdue_tasks'] = Task.objects.filter(deadline__lt=datetime.today()).filter(~Q(status=complete))

        return context


class CalendarPageView(TemplateView):
    template_name = "pages/calendar.html"
    model = Task
