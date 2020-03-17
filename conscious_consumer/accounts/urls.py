from django.urls import path
import django.contrib.auth.views as auth_views
from .views import (
    SignupView,
)

app_name = 'accounts'
urlpatterns = [
    # auth related views
    path('login/', auth_views.LoginView.as_view(
            template_name='accounts/auth/login.html'), name="login"),
    path('signup/', SignupView.as_view(), name='signup'),
    # profile related views
]
