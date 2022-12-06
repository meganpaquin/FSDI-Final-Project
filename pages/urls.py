from django.urls import path
from .views import HomePageView, IndexPageView, DashboardPageView, ListPageView, CalendarPageView
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('home', HomePageView.as_view(), name="home"),
    path('dashboard', DashboardPageView.as_view(), name="dashboard"),
    path('list', ListPageView.as_view(), name="list"),
    path('calendar',CalendarPageView.as_view(), name="calendar"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)