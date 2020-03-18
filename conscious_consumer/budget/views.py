from django.shortcuts import render, get_object_or_404, redirect
from .models import Goal
from .forms import GoalForm
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class AllGoalList(ListView):
    '''User sees goal from all users on the site.'''
    model = Goal
    template_name = 'budget/goal/list-all.html'

    def get(self, request):
        '''Render a context containing all Goal instances.'''
        goals = self.get_queryset().all()
        return render(request, self.template_name, {
            'goals': goals
        })


class PersonalGoalList(ListView):
    '''User sees goals only pertaining to themself.'''
    model = Goal
    template_name = 'budget/goal/list-personal.html'

    def get(self, request, pk):
        '''Render a context containing all Goal specific to the user.'''
        user = User.objects.get(id=pk)
        goals = self.get_queryset().filter(author=user)
        return render(request, self.template_name, {
            'goals': goals
        })


class OtherGoalDetail(DetailView):
    '''User sees details specific to a single goal set by another user.'''
    pass


class PersonalGoalDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    '''User sees details related to one of their own goals.'''
    pass


class GoalCreate(LoginRequiredMixin, CreateView):
    '''User submits a form to add a new goal for themself.'''
    pass


class GoalUpdate(LoginRequiredMixin, UpdateView):
    '''User submits a form to edit one of their goal.'''
    pass


class GoalDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''User submits a form to delete one of their goals.'''
    pass
