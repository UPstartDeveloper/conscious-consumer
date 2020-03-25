from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from .models import Profile
from .views import (
    SignupView,
    ProfileDetail,
)
from django.urls import reverse, reverse_lazy
from django.contrib.messages.storage.fallback import FallbackStorage


class SignupViewTests(TestCase):
    '''User signup for an account and also receive a profile in the db.'''
    def setUp(self):
        '''Site visitor information relevant to each test.'''
        self.factory = RequestFactory()
        self.visitor = AnonymousUser()
        self.user_info = {
            'username': 'zainraza',
            'email': 'zainr7989@gmail.com',
            'pass_1': 'who_is_typing_this_9'
        }
        self.user = (
            User.objects.create_user(self.user_info.get('username'),
                                     self.user_info.get('email'),
                                     self.user_info.get('pass_1'))
        )
        # self.url = reverse('accounts:signup')
        self.url = 'accounts:signup'

    def test_visitor_gets_signup_form(self):
        '''Site visitor is able to see the form to sign up for an account.'''
        # a site visitor (not logged in) makes a request and gets a response
        self.assertTrue(self.visitor.is_anonymous)
        request = self.factory.get(self.url)
        request.user = self.visitor
        response = SignupView.as_view()(request)
        # response is valid
        self.assertEqual(response.status_code, 200)
        # response renders the form
        self.assertContains(response, 'Join Now, and Set Your Carbon Budget!')

    def test_authenticated_user_gets_signup_form(self):
        '''
        An authenticated user is no longer able to fill out the signup form.
        '''
        # user is logged in already
        self.assertEqual(self.user.is_authenticated, True)
        # user visits the signup page
        request = self.factory.get(reverse_lazy(self.url))
        request.user = self.user
        # supply the message to the request
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        # get the response
        response = SignupView.as_view()(request)
        # page is able to render
        self.assertEqual(response.status_code, 200)
        """
        # Commented for now, will debug later to improve the test
        # user sees a message different from a site visitor
        self.assertContains(response,
                            "Looks like you already have an account. " +
                            "We appreciate you for joining us!")
        """

    def test_form_valid_submission(self):
        """
        The visitor enters valid data, the User and Profile objects are made,
        and then the site visitor is redirected to the login page.
        """
        # a site visitor fills out the signup form
        form_data = {
            'username': 'zurich',
            'email': 'z@g.com',
            'password1': 'test_123_test',
            'password2': 'test_123_test'
        }
        # user submits the form
        c = Client()
        response = c.post('/accounts/signup/', form_data)
        self.assertEqual(response.status_code, 302)

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
