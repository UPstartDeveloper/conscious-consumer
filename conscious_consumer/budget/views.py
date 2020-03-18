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


class GoalDetail(DetailView):
    '''User sees details specific to a single goal.'''
    model = Goal
    personal_template_name = 'budget/goal/detail-personal.html'
    public_template_name = 'budget/goal/detail-public.html'

    def get(self, request, pk, slug):
        """Renders a page to show the details for a specific Goal.
           If the user is viewing a goal another user wrote, they will see both
           the goal and comments associated with it.
           If the user views a goal they authored, they will be able to see the
           goal, along with some data visualizations of how well they've kept
           on track.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           pk(int): unique id value of the user
           slug(slug): unique slug of the Goal being requested

           Returns:
           HttpResponse: the view of either the personal or public template

        """
        # determine if the request user is the author or not
        user = User.objects.get(id=pk)
        goal = Goal.objects.get(slug__iexact=slug)
        # if they are, display the personal template
        if goal.author == user:
            template = self.personal_template_name
        # otherwise display the public template
        else:
            template = self.public_template_name
        context = {
            'goal': goal
        }
        return render(request, template, context)


class GoalCreate(UserPassesTestMixin, CreateView):
    '''User submits a form to add a new goal for themself.'''
    model = Goal
    form_class = GoalForm
    template_name = 'budget/goal/create.html'
    queryset = Goal.objects.all()

    def form_valid(self, form):
        '''Initializes the author based on who submitted the form.'''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''Restrict viewing of the form to authenticated users.'''
        return self.request.user.is_authenticated is True


class GoalUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''User submits a form to edit one of their goal.'''
    model = Goal
    form_class = GoalForm
    template_name = 'budget/goal/update.html'
    queryset = Goal.objects.all()

    def test_func(self):
        '''Ensures the user editing the goal is its author.'''
        goal = self.get_object()
        return (self.request.user == goal.author)


class GoalDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''User submits a form to delete one of their goals.'''
    model = Goal
    template_name = 'budget/goal/delete.html'
    success_url = reverse_lazy('budget:all_goals')
    queryset = Goal.objects.all()

    def get(self, request, slug):
        """Renders a short preview of thr goal, along with form to delete.

           Parameters:
           request(HttpRequest): the GET request sent to the server
           slug(slug): unique slug field value of the Goal instance

           Returns:
           HttpResponse: the view of the detail template

        """
        goal = self.get_queryset().get(slug__iexact=goal)
        context = {
            'goal': goal
        }
        return render(request, self.template_name, context)

    def test_func(self):
        '''Ensures the user removing the goal is its author.'''
        goal = self.get_object()
        return (self.request.user == goal.author)
