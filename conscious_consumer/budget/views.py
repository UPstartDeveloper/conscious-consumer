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
    pass


class PersonalGoalList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    '''User sees goals only pertaining to themself.'''
    pass


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
