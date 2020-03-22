from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from .models import Profile
from .views import (
    SignupView,
    ProfileDetail,
)


class SignupViewTests(TestCase):
    '''User signup for an account and also receive a profile in the db.'''
    def setUp(self):
        '''Site visitor information relevant to each test.'''
        self.visitor = AnonymousUser()
        self.visitor_info = {
            'username': 'zainraza',
            'email': 'zainr7989@gmail.com',
            'pass_1': 'who_is_typing_this_9'
        }
        self.user = (
            User.objects.create(username=self.visitor_info.get('username'),
                                email=self.visitor_info.get('email'),
                                password=self.visitor_info.get('pass_1'))
        )

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

    def test_authenticated_user_accesses_form(self):
        """
        An authenticated user is no longer able to fill out the signup form.
        """
        pass


class ProfileDetailTests(TestCase):
    '''User is able to see the details specific to their own account.'''
    def setUp(self):
        '''User information relevant to each test.'''
        pass
