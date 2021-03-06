from django import forms
from .models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "photo",
            "price",
            "web_link",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = [
            "author",
            "modified",
        ]
