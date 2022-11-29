from django.views.generic import TemplateView
from tasks.models import Task, Status
from projects.models import Project
from datetime import datetime
from django.db.models import Q

class IndexPageView(TemplateView):
    template_name = "pages/index.html"

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        assigned = Status.objects.get(name="assigned")

        context['assigned_tasks'] = Task.objects.filter(status=assigned).order_by('deadline').reverse().order_by('priority')[0:3]

        progress = Status.objects.get(name="in-progress")

        context['progress_tasks'] = Task.objects.filter(status=progress).order_by('deadline').reverse()[0:3]

        context['projects'] = Project.objects.order_by('deadline')
        
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
        context['assigned_tasks'] = Task.objects.filter(status=assigned).order_by('deadline').reverse().filter(deadline__gt=datetime.today()).filter

        progress = Status.objects.get(name="in-progress")
        context['progress_tasks'] = Task.objects.filter(status=progress).order_by('deadline').reverse()

        complete = Status.objects.get(name="complete")
        context['complete_tasks'] = Task.objects.filter(status=complete).order_by('deadline').reverse()

        context['overdue_tasks'] = Task.objects.filter(deadline__lt=datetime.today()).filter(~Q(status=complete))

        return context


class CalendarPageView(TemplateView):
    template_name = "pages/calendar.html"
    model = Task
