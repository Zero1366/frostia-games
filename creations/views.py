"""Vues de l'application creations.

Contient le CRUD manuel des entités Category et Tag (liste, création,
modification, suppression), codé sans passer par Django Admin,
pour démontrer la maîtrise des vues, formulaires et templates Django.
"""

from __future__ import annotations

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, TagForm
from .models import Category, Tag

# ---------- Category (relation 1,N) ----------


def category_list(request: HttpRequest) -> HttpResponse:
    """Affiche la liste de toutes les catégories."""
    categories = Category.objects.all().order_by("name")

    return render(
        request,
        "pages/category_list.html",
        {"categories": categories},
    )


def category_create(request: HttpRequest) -> HttpResponse:
    """Crée une nouvelle catégorie via un formulaire."""
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Catégorie créée avec succès.")
            return redirect("creations:category_list")
    else:
        form = CategoryForm()

    return render(
        request,
        "pages/category_form.html",
        {"form": form, "mode": "create"},
    )


def category_update(request: HttpRequest, pk: int) -> HttpResponse:
    """Modifie une catégorie existante."""
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            messages.success(request, "Catégorie modifiée avec succès.")
            return redirect("creations:category_list")
    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        "pages/category_form.html",
        {"form": form, "mode": "update", "category": category},
    )


def category_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Supprime une catégorie, avec confirmation préalable."""
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        messages.success(request, "Catégorie supprimée avec succès.")
        return redirect("creations:category_list")

    return render(
        request,
        "pages/category_confirm_delete.html",
        {"category": category},
    )


# ---------- Tag (relation N,N) ----------


def tag_list(request: HttpRequest) -> HttpResponse:
    """Affiche la liste de tous les tags."""
    tags = Tag.objects.all().order_by("name")

    return render(
        request,
        "pages/tag_list.html",
        {"tags": tags},
    )


def tag_create(request: HttpRequest) -> HttpResponse:
    """Crée un nouveau tag via un formulaire."""
    if request.method == "POST":
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Tag créé avec succès.")
            return redirect("creations:tag_list")
    else:
        form = TagForm()

    return render(
        request,
        "pages/tag_form.html",
        {"form": form, "mode": "create"},
    )


def tag_update(request: HttpRequest, pk: int) -> HttpResponse:
    """Modifie un tag existant."""
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            messages.success(request, "Tag modifié avec succès.")
            return redirect("creations:tag_list")
    else:
        form = TagForm(instance=tag)

    return render(
        request,
        "pages/tag_form.html",
        {"form": form, "mode": "update", "tag": tag},
    )


def tag_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Supprime un tag, avec confirmation préalable."""
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == "POST":
        tag.delete()
        messages.success(request, "Tag supprimé avec succès.")
        return redirect("creations:tag_list")

    return render(
        request,
        "pages/tag_confirm_delete.html",
        {"tag": tag},
    )
