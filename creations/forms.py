from django import forms

from .models import Category, Tag


class CategoryForm(forms.ModelForm):  # type: ignore[type-arg]
    class Meta:
        model = Category
        fields = ["name", "slug"]


class TagForm(forms.ModelForm):  # type: ignore[type-arg]
    class Meta:
        model = Tag
        fields = ["name"]
