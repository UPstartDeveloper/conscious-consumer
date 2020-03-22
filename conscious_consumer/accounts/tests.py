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
        '''Site visitor information relevant to each test.'''

    def test_get_signup_form(self):
        '''Site visitor is able to see the form to sign up for an account.'''
        pass

    def test_form_valid_submission(self):
        """
        The visitor enters valid data, the User and Profile objects are made,
        and then the site visitor is redirected to the login page.
        """
        pass

    def test_form_password_no_match(self):
        """
        The site visitor fails to confirm their password, and the form renders
        itself again with an error message.
        """
        pass


class ProfileDetailTests(TestCase):
    '''User is able to see the details specific to their own account.'''
    def setUp(self):
        '''User information relevant to each test.'''
        pass
