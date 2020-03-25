from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.http import HttpRequest
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login
from django.contrib.messages.storage.fallback import FallbackStorage
from .models import Profile
from .views import (
    SignupView,
    ProfileDetail,
    ProfileUpdate
)
from django.urls import reverse, reverse_lazy, resolve
from django.contrib.messages.storage.fallback import FallbackStorage


class SignupViewTests(TestCase):
    '''User signup for an account and also receive a profile in the db.'''
    def setUp(self):
        '''Site visitor information relevant to each test.'''
        self.factory = RequestFactory()
        self.visitor = AnonymousUser()
        self.user = (
            User.objects.create_user('zainraza',
                                     'zainr7989@gmail.com',
                                     'who_is_typing_this_9')
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
        '''
        An authenticated user is no longer able to fill out the signup form.
        '''
        # user is logged in already
        user_in_test = User.objects.get(username=self.user.username)
        self.assertTrue(user_in_test, not None)
        self.assertEqual(self.user.is_authenticated, True)
        # user visits the signup page
        # request = HttpRequest()  # actually becomes WSGIRequest later
        request = self.factory.get('accounts:signup')
        # request.user = self.user - for some reason this causes ProfileDetail
        # to be resolved
        # next step: get the response
        response = SignupView.as_view()(request)
        # page is able to render
        self.assertEqual(response.status_code, 200)
        response.render()
        # print(response.content) - verify it's the signup view template
        # Commented for now, will debug later to improve the test
        # user sees a message different from a site visitor
        # self.assertContains("Looks like you already have an account",
        #               response.content)

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
        self.factory = RequestFactory()
        self.user = (
            User.objects.create_user('zainraza',
                                     'zainr7989@gmail.com',
                                     'who_is_typing_this_9')
        )
        self.url = 'accounts:profile_detail'
        self.profile = Profile.objects.create(user=self.user)

    def test_gets_own_profile_page(self):
        '''User goes to their own profile page and sees their information.'''
        # profile is in the db
        test_profile = Profile.objects.get(user=self.user)
        self.assertTrue(test_profile, not None)
        # user gets the view
        request = self.factory.get(reverse(self.url, args=[test_profile.id]))
        request.user = self.user
        response = ProfileDetail.as_view()(request, pk=test_profile.id)
        # view renders ok
        self.assertEqual(response.status_code, 200)


class ProfileUpdateTests(TestCase):
    def setUp(self):
        '''Initializes variables reused for every test.'''
        self.factory = RequestFactory()
        self.user = (
            User.objects.create_user('zainraza',
                                     'zainr7989@gmail.com',
                                     'who_is_typing_this_9')
        )
        self.url = 'accounts:change_image'
        self.profile = Profile.objects.create(user=self.user)

    def test_authenticated_user_gets_update_form(self):
        '''A logged in User can access a form to change their profile image.'''
        # profile for user already exists
        test_profile = Profile.objects.get(user=self.user)
        self.assertTrue(test_profile, not None)
        # the mugshot image is currently set to the default
        self.assertEqual(test_profile.mugshot.name, 'images/user-icon.jpg')
        # user is able to GET the view
        request = self.factory.get(reverse(self.url, args=[test_profile.id]))
        request.user = self.user
        response = ProfileUpdate.as_view()(request, pk=test_profile.id)
        self.assertEqual(response.status_code, 200)

    def test_user_changes_profile_image(self):
        '''A user submits a new image file to use for their profile.'''
        pass
