from django.urls import path
from .views import SignUpView, UserChangeView
from . import views 
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/<int:pk>/edit', UserChangeView.as_view(), name="change_user"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)