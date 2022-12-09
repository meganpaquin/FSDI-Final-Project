from django.urls import path
from .views import SignUpView, UserChangeView,PermissionChangeView, PermissionListView, NewTeamView, TeamListView, TeamUpdateView, TeamDeleteView
from . import views 
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/<int:pk>/edit', UserChangeView.as_view(), name="change_user"),
    path('permissions', PermissionListView.as_view(), name="permissions"),
    path('permissions/<int:pk>/edit', PermissionChangeView.as_view(), name="permissions-edit"),
    path('teams', TeamListView.as_view(), name="teams"),
    path('team/<int:pk>/edit', TeamUpdateView.as_view(), name="team-edit"),
    path('team/new', NewTeamView.as_view(), name="team-new"),
    path('team/<int:pk>/delete', views.TeamDeleteView.as_view(), name="team-delete")
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)