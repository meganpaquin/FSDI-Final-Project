from django.urls import path
from .views import HomePageView, IndexPageView, DashboardPageView, ListPageView, CalendarPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('home', HomePageView.as_view(), name="home"),
    path('dashboard', DashboardPageView.as_view(), name="dashboard"),
    path('list', ListPageView.as_view(), name="list"),
    path('calendar',CalendarPageView.as_view(), name="calendar"),
]