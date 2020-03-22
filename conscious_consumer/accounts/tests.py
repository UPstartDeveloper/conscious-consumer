from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from .models import Profile
from .views import (
    SignupView,
    ProfileDetail,
)


class SignupViewTests(TestCase):
    '''User signup for an account and also receive a profile in the db.'''
    def setUp(self):
        '''Site visitor information relevant  to each test.'''
        pass


class ProfileDetailTests(TestCase):
    '''User is able to see the details specific to their own account.'''
    def setUp(self):
        '''User information relevant to each test.'''
        pass
