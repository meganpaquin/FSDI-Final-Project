from django.views.generic import TemplateView
from tasks.models import Task, Status, Priority
from projects.models import Project
from datetime import datetime
from django.db.models import Q
from accounts.models import CustomUser, Team
from django.shortcuts import render
from accounts.models import Team

class IndexPageView(TemplateView):
    template_name = "pages/index.html"

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        loggedin = self.request.user
        context = super().get_context_data(**kwargs)

        assigned = Status.objects.get(name="assigned")
        context['assigned_tasks'] = Task.objects.filter(status=assigned).filter(assignee=loggedin.id).order_by('deadline_date').reverse().order_by('priority')[0:3]

        progress = Status.objects.get(name="in-progress")
        context['progress_tasks'] = Task.objects.filter(status=progress).filter(assignee=loggedin.id).order_by('deadline_date').reverse()[0:3]

        context['projects'] = Project.objects.filter(author=loggedin.id).order_by('deadline')
        context['project_members'] = Project.objects.filter(members=loggedin.id)

        context['images'] = CustomUser.objects.all()

        context['teams'] = Team.objects.filter(leader=loggedin.id)        
        return context
        
class DashboardPageView(TemplateView):
    template_name = "pages/dashboard.html"
    
    def get_context_data(self, **kwargs):
        loggedin = self.request.user
        context = super().get_context_data(**kwargs)

        context['projects'] = Project.objects.filter(author=loggedin)
        context['team_workload'] = Team.objects.filter(leader=loggedin)
        context['tasks'] = Task.objects.all()
        
        return context

class ListPageView(TemplateView):
    template_name = "pages/list.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        assigned = Status.objects.get(name="assigned")
        context['assigned_tasks'] = Task.objects.filter(status=assigned).order_by('deadline_date').reverse().filter(deadline_date__gt=datetime.today()).order_by('priority')

        progress = Status.objects.get(name="in-progress")
        context['progress_tasks'] = Task.objects.filter(status=progress).order_by('deadline_date').reverse().filter(deadline_date__gt=datetime.today())

        complete = Status.objects.get(name="complete")
        context['complete_tasks'] = Task.objects.filter(status=complete).order_by('deadline_date').reverse()

        context['overdue_tasks'] = Task.objects.filter(deadline_date__lt=datetime.today()).filter(~Q(status=complete))

        return context


class CalendarPageView(TemplateView):
    template_name = "pages/calendar.html"
    model = Task
