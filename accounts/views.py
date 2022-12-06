from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import CustomUser


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

class UserChangeView(UpdateView):
    template_name = 'registration/change_user.html'
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy("home")