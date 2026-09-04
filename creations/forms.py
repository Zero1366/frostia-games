from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):  # type: ignore[type-arg]
    class Meta:
        model = Category
        fields = ["name", "slug"]
