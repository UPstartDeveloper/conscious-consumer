from django.test import TestCase, Client
from django.test.client import RequestFactory
from .serializers import GoalSerializer
from .views import GoalData


class GoalDataTests(TestCase):
    def setUp(self):
        '''User has already inserted a Goal into the db.'''
        pass

    def test_retrieve_achievement_failure_data():
        '''The view returns achievement and failure data for a given Goal.'''
        pass
