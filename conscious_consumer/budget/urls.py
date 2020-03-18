from django.urls import path
from .views import (
    AllGoalList,
    PersonalGoalList,
    GoalDetail,
    GoalCreate,
    GoalUpdate,
    GoalDelete,
)

app_name = 'budget'
urlpatterns = [
    path('goals/public/', AllGoalList.as_view(), name="all_goals"),
    # for personal goals list, id of user is passed to query string
    path('goals/person/<int:pk>/', PersonalGoalList.as_view(),
         name="personal_goals"),
    path('goals/<int:pk>/<slug:slug>/', GoalDetail.as_view(),
         name='goal_detail'),
    path('goals/create/', GoalCreate.as_view(), name="goal_create"),
    path('goals/update/<slug:slug>/', GoalUpdate.as_view(),
         name="goal_update"),
    path('goals/delete/<slug:slug>/', GoalDelete.as_view(),
         name="goal_delete"),
]
