from django.urls import path
from .views import TaskDelView, TaskCreateView, TaskUpdateView, TaskDetailView
from . import views

urlpatterns = [
    path('<int:pk>', TaskDetailView.as_view(), name="task-detail"),
    path('<int:pk>/delete', TaskDelView.as_view(), name="task-delete"),
    path('<int:pk>/edit', TaskUpdateView.as_view(), name="task-update"),
    path('new/', TaskCreateView.as_view(), name="task-new"),
    path('mark_complete/<int:pk>/', views.mark_completed, name="mark_completed"),
    path('mark_complete_list/<int:pk>/', views.complete_list, name="complete_list"),
    path('mark_complete_detail/<int:pk>/', views.mark_complete_detail, name="complete_detail"),
    path('mark_assigned_detail/<int:pk>/', views.mark_assigned_detail, name="assigned_detail"),
    path('mark_progress_detail/<int:pk>/', views.mark_progress_detail, name="progress_detail"),
    path('mark_archived_detail/<int:pk>/', views.mark_archived_detail, name="archived_detail"),
]