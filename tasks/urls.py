from django.urls import path
from .views import TaskListView, TaskDelView, TaskCreateView, TaskUpdateView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name="tasks"),
    path('<int:pk>', TaskDetailView.as_view(), name="task-detail"),
    path('<int:pk>/delete', TaskDelView.as_view(), name="task-delete"),
    path('<int:pk>/edit', TaskUpdateView.as_view(), name="task-update"),
    path('new/', TaskCreateView.as_view(), name="task-new"),
]