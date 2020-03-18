from django.urls import path
from .views import (
    AllGoalList,
    PersonalGoalList,
    OtherGoalDetail,
    PersonalGoalDetail,
    GoalCreate,
    GoalUpdate,
    GoalDelete,
)

app_name = 'budget'
urlpatterns = [
    path('goals/public/', AllGoalList.as_view(), name="all_goals"),
    # for personal goals list, id of user is passed to query string
    path('goals/private/<int:pk>/', PersonalGoalList.as_view(),
         name="personal_goals"),
    path('goals/public/<slug:slug>', OtherGoalDetail.as_view(),
         name='goal_detail_other'),
    path('goals/private/<slug:slug>/', PersonalGoalDetail.as_view(),
         name="goal_detail_personal"),
    path('goals/create/', GoalCreate.as_view(), name="goal_create"),
    path('goals/update/<slug:slug>/', GoalUpdate.as_view(),
         name="goal_update"),
    path('goals/delete/<slug:slug>/', GoalDelete.as_view(),
         name="goal_delete"),
]
