from django.test import TestCase, Client
from django.test.client import RequestFactory
from .serializers import GoalSerializer
from .views import GoalData
from budget.models import Goal
from django.contrib.auth.models import User
from django.shortcuts import reverse


class GoalDataTests(TestCase):
    def setUp(self):
        '''User has already inserted a Goal into the db.'''
        self.factory = RequestFactory()
        self.user = self.user = (
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

    def test_retrieve_achievement_failure_data(self):
        '''The view returns achievement and failure data for a given Goal.'''
        # Goal instance already in the db
        test_goal = Goal.objects.get(title=self.goal.title)
        self.assertTrue(test_goal, not None)
        # request is made to GoalData view
        request = self.factory.get('/api/1/chart/data/')
        response = GoalData.as_view()(request, test_goal.id)
        # response is returned ok
        self.assertEqual(response.status_code, 200)
        # test the response has the right data
        self.assertEquals(response.data.get('labels'),
                          ['Achievements', 'Fails'])
        self.assertEquals(response.data.get('values'),
                          [test_goal.achievements, test_goal.fails])
