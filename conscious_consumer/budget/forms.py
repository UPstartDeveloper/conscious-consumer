from django import forms
from .models import Goal, Comment


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = [
            "author",
            "slug",
            "created",
            "modified",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "headline",
            "description",
        ]
