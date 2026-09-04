from django import forms

from .models import Category


class CategoryForm(forms.ModelForm[Category]):
    class Meta:
        model = Category
        fields = ["name", "slug"]
