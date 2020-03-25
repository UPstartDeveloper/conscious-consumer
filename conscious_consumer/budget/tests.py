from django.test import TestCase, Client
from django.test.client import RequestFactory
from .views import (
    AllGoalList,
    PersonalGoalList,
    PersonalGoalDetail,
    PublicGoalDetail,
    GoalCreate,
    GoalUpdate,
    GoalDelete,
)
from django.contrib.auth.models import User
from .models import Goal


class AllGoalListTests(TestCase):
    def setUp(self):
        '''Instaniate relevant model instances reused in tests.'''
        self.user = (
            User.objects.create_user('zainraza',
                                     'zainr7989@gmail.com',
                                     'who_is_typing_this_9')
        )
        self.goal = Goal.objects.create(
            title='Daily Commute',
            author=self.user,
            description='Make driving greener',
            achievements=12,
            fails=6,
            category=Goal.TRAVEL_CAT,
            monthly_target=Goal.MIN_VALUE
        )
        self.url = 'budget:goal_list_public'


class PersonalGoalListTests(TestCase):
    pass


class PersonalGoalDetailTests(TestCase):
    pass


class PublicGoalDetailTests(TestCase):
    pass


class GoalCreateTests(TestCase):
    pass


class GoalUpdateTests(TestCase):
    pass


class GoalDeleteTests(TestCase):
    pass
