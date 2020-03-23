from django.shortcuts import render
from django.conf import settings as dj_conf_settings
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.mixins import UserPassesTestMixin


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


class ProfileDetail(UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile/detail.html'

    def get(self, request, pk):
        """Renders a page to show the details for a specific User and the
           related profile.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           pk(int: unique id of the Profile being requested

           Returns:
           HttpResponse: the view of public template

        """
        profile = self.model.objects.get(id=pk)
        context = {
            'profile': profile
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensure that the user is viewing their own profile.'''
        profile = self.get_object()
        return profile.user == self.request.user


class ProfileUpdate(UserPassesTestMixin, UpdateView):
    '''A user uploads their profile image through a form.'''
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile/change-picture.html'
    queryset = Profile.objects.all()

    def test_func(self):
        '''Ensure that the user is viewing their own profile.'''
        profile = self.get_object()
        return profile.id == self.request.user.profile.id
