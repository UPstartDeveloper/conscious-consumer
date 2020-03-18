from django.urls import path
from .views import GoalData

app_name = 'api'
urlpatterns = [
    # Returns achievement and fail data for a Goal
    path('<int:pk>/chart/data/', GoalData.as_view(), name="goal_data"),
]
