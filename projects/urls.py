from django.urls import path
from .views import ProjectListView, ProjectDelView, ProjectCreateView, ProjectUpdateView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name="projects"),
    path('<int:pk>', ProjectDetailView.as_view(), name="project-detail"),
    path('<int:pk>/delete', ProjectDelView.as_view(), name="project-delete"),
    path('<int:pk>/edit', ProjectUpdateView.as_view(), name="project-update"),
    path('new/', ProjectCreateView.as_view(), name="project-new"),
]