from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from django.shortcuts import  render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages


from django.contrib.auth.forms import PasswordResetForm

from django.views.generic.edit import FormView
from django.urls import reverse_lazy 

class UserChangeView(UpdateView):
    template_name = 'registration/change_user.html'
    form_class = UserChangeForm
    model = User

def register_request(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignUpForm()
	return render (request=request, template_name="registration/signup.html", context={"signup":form})


class PasswordChangeView(FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'