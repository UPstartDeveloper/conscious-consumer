from django.urls import path
from .views import (
    AllGoalList,
    PersonalGoalList,
    PersonalGoalDetail,
    PublicGoalDetail,
    GoalCreate,
    GoalUpdate,
    GoalDelete,
)

app_name = "budget"
urlpatterns = [
    # Goal-related CRUD URLs - id of user is passed to query string on personal
    path("goals/public/", AllGoalList.as_view(), name="goal_list_public"),
    path("goals/create/", GoalCreate.as_view(), name="goal_create"),
    path("goals/update/<slug:slug>/", GoalUpdate.as_view(), name="goal_update"),
    path("goal/delete/<slug:slug>/", GoalDelete.as_view(), name="goal_delete"),
    path("goals/<slug:slug>/", PublicGoalDetail.as_view(), name="goal_detail_public"),
    path(
        "goals/<int:pk>/<slug:slug>/",
        PersonalGoalDetail.as_view(),
        name="goal_detail_personal",
    ),
    path("<int:pk>/", PersonalGoalList.as_view(), name="goal_list_personal"),
]
