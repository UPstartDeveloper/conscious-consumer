from django.urls import path
import django.contrib.auth.views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='accounts/auth/login.html'), name="login"),
]
