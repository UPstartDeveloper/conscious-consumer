from rest_framework.serializers import ModelSerializer
from budget.models import Goal


class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            "achievements",
            "fails",
        ]
