from django.urls import path
from .views import ProjectListView, ProjectDelView, ProjectCreateView, ProjectUpdateView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name="Projects"),
    path('<int:pk>', ProjectDetailView.as_view(), name="Project-detail"),
    path('<int:pk>/delete', ProjectDelView.as_view(), name="Project-delete"),
    path('<int:pk>/edit', ProjectUpdateView.as_view(), name="Project-update"),
    path('new/', ProjectCreateView.as_view(), name="Project-new"),
]