from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

# Create your views here.


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class UserChangeView(UpdateView):
    template_name = 'registration/change_user.html'
    form_class = UserChangeForm
    model = User
