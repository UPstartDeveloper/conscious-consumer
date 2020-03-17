from django.shortcuts import render
from django.conf import settings as dj_conf_settings
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import SignUpForm


class SignupView(SuccessMessageMixin, CreateView):
    '''User is able to signup with a username, email, and password.'''
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/auth/signup.html'
    success_message = "Congratulations! You may now log in."

    def form_valid(self, form):
        '''Save the new User, and set up their profile as well.'''
        self.object = form.save()
        profile = Profile.objects.create(user=self.object)
        profile.save()
        return super().form_valid(form)
