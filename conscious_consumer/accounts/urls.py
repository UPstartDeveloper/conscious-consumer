from django.urls import path
import django.contrib.auth.views as auth_views
from .views import (
    SignupView,
    ProfileDetail,
    ProfileUpdate,
)

app_name = 'accounts'
urlpatterns = [
    # auth related views
    path('login/', auth_views.LoginView.as_view(
            template_name='accounts/auth/login.html'), name="login"),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # profile related views
    path('<int:pk>/change-profile-image/', ProfileUpdate.as_view(),
         name='change_image'),
    path('<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]
