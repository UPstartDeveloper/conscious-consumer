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
        self.factory = RequestFactory()
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
        """
        An authenticated user is no longer able to fill out the signup form.
        """
        # user is logged in already
        self.assertEqual(self.user.is_authenticated, True)
        # user visits the signup page
        request = self.factory.get(self.url)
        request.user = self.user
        response = SignupView.as_view()(request)
        # page is able to render
        self.assertEqual(response.status_code, 200)
        # user sees a message different from a site visitor
        self.assertContains(response,
                            "Looks like you already have an account. " +
                            "We appreciate you for joining us!")

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
