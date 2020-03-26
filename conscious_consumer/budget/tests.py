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
from django.urls import reverse


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
        self.client = Client()

    def test_user_views_goal_list_public(self):
        '''User sees all Goal instances present on the AllGoalList view.'''
        # goal instance is already in db
        test_goal = Goal.objects.get(title=self.goal.title)
        self.assertTrue(test_goal, not None)
        # user requests the view and gets a valid response
        response = self.client.get(reverse(self.url))
        self.assertEqual(response.status_code, 200)
        # response contains appropiate data about Goal
        self.assertContains(response, test_goal.title)


class PersonalGoalListTests(TestCase):
    def setUp(self):
        '''Instaniate relevant model instances reused in tests.'''
        # instaniate separate users
        self.user = (
            User.objects.create_user('zainraza',
                                     'zainr7989@gmail.com',
                                     'who_is_typing_this_9')
        )
        self.other_user = (
            User.objects.create_user('zurich',
                                     'zurich@gmail.com',
                                     'who_is_typing_this_7')
        )
        # instantiate separate goals
        self.goal = Goal.objects.create(
            title='Daily Commute',
            author=self.user,
            description='Make driving greener',
            achievements=12,
            fails=6,
            category=Goal.TRAVEL_CAT,
            monthly_target=Goal.MIN_VALUE
        )
        self.other_goal = Goal.objects.create(
            title='Weekly Commute',
            author=self.other_user,
            description='Make driving greener',
            achievements=12,
            fails=6,
            category=Goal.TRAVEL_CAT,
            monthly_target=Goal.MIN_VALUE
        )
        self.url = 'budget:goal_list_personal'
        self.client = Client()
        self.factory = RequestFactory()

    def test_user_view_personal_list_own(self):
        '''A user is able to see s list of Goals they authored.'''
        # there are two different users in the db
        test_user = User.objects.get(id=self.user.id)
        self.assertTrue(test_user, not None)
        test_other_user = User.objects.get(id=self.other_user.id)
        self.assertTrue(test_other_user, not None)
        # there are two different goals
        test_goal = Goal.objects.get(id=self.goal.id)
        self.assertTrue(test_goal, not None)
        test_other_goal = Goal.objects.get(id=self.other_goal.id)
        self.assertTrue(test_other_goal, not None)
        # the goals have different authors
        self.assertEqual(self.goal.author, self.user)
        self.assertEqual(self.other_goal.author, self.other_user)
        # user accesses the personal goals list
        request = self.factory.get(reverse(self.url, args=[self.goal.id]))
        # response is returned ok
        response = PersonalGoalList.as_view()(request, pk=self.goal.id)
        self.assertEqual(response.status_code, 200)
        # user sees their own goal on the view
        self.assertContains(response, self.goal.title)
        # user does not see goals by other users
        self.assertNotIn(b'{self.other_goal.title}', response.content)


class PersonalGoalDetailTests(TestCase):
    def setUp(self):
        '''Instaniate relevant model instances reused in tests.'''
        # instaniate separate users
        self.user = (
            User.objects.create_user('zainraza',
                                     'zainr7989@gmail.com',
                                     'who_is_typing_this_9')
        )
        self.other_user = (
            User.objects.create_user('zurich',
                                     'zurich@gmail.com',
                                     'who_is_typing_this_7')
        )
        # instantiate separate goals
        self.goal = Goal.objects.create(
            title='Daily Commute',
            author=self.user,
            description='Make driving greener',
            achievements=12,
            fails=6,
            category=Goal.TRAVEL_CAT,
            monthly_target=Goal.MIN_VALUE
        )
        self.other_goal = Goal.objects.create(
            title='Weekly Commute',
            author=self.other_user,
            description='Make driving greener',
            achievements=12,
            fails=6,
            category=Goal.TRAVEL_CAT,
            monthly_target=Goal.MIN_VALUE
        )
        self.url = 'budget:goal_detail_personal'
        self.client = Client()
        self.factory = RequestFactory()

    def test_user_get_personal_detail_own_goal(self):
        """
        User sees details personally available for the goals they authored.
        """

    def test_user_get_personal_detail_other_goal(self):
        """
        User tries to see personal details of other user's goal, and is
        redirected to the publicly available detail view.
        """
        pass


class PublicGoalDetailTests(TestCase):
    pass


class GoalCreateTests(TestCase):
    pass


class GoalUpdateTests(TestCase):
    pass


class GoalDeleteTests(TestCase):
    pass
