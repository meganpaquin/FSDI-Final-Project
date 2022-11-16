from django.urls import path
from .views import SignUpView, UserChangeView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/<int:pk>/edit', UserChangeView.as_view(), name="change_user"),
]