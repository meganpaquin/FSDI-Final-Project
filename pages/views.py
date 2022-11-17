from django.views.generic import TemplateView

class IndexPageView(TemplateView):
    template_name = "pages/index.html"

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class DashboardPageView(TemplateView):
    template_name = "pages/dashboard.html"