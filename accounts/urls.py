from django.urls import path
from .views import UserChangeView, PasswordChangeView
from . import views 

urlpatterns = [
    path('signup/', views.register_request, name='signup'),
    path('users/<int:pk>/edit', UserChangeView.as_view(), name="change_user"),
    path('password_change/', PasswordChangeView.as_view(), name='password_change')

    ]