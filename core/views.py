from __future__ import annotations

from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.services.nosql_notes import find_notes_by_project, seed_project_notes
from creations.models import Creation
from playable.models import PlayableProject

DEFAULT_PROJECT_NOTES: list[dict[str, Any]] = [
    {
        "title": "Mise en place de la V1",
        "content": (
            "Création du portfolio Django, structuration du projet, "
            "déploiement Render et organisation des preuves."
        ),
        "tags": ["django", "portfolio", "v1", "render"],
        "status": "done",
    },
    {
        "title": "Renforcement du dossier projet",
        "content": (
            "Ajout de la conception, du SQL natif, du JavaScript documenté et de la partie NoSQL."
        ),
        "tags": ["dossier-projet", "conception", "sql", "nosql"],
        "status": "in_progress",
    },
    {
        "title": "Préparation de la V3",
        "content": "Ajout des éléments demandés après le retour formateur.",
        "tags": ["v3", "formation", "preuves"],
        "status": "planned",
    },
]


def get_project_notes_safe() -> list[dict[str, Any]]:
    try:
        seed_project_notes()
        notes = find_notes_by_project("frostia-games")

        if notes:
            return notes

        return DEFAULT_PROJECT_NOTES
    except Exception:
        return DEFAULT_PROJECT_NOTES


def home(request: HttpRequest) -> HttpResponse:
    latest_creations = Creation.objects.filter(is_visible=True).order_by(
        "alphabet_letter",
        "title",
    )[:3]

    latest_playable_projects = PlayableProject.objects.filter(
        is_visible=True,
    ).order_by("title")[:3]

    project_notes = get_project_notes_safe()

    return render(
        request,
        "pages/home.html",
        {
            "latest_creations": latest_creations,
            "latest_playable_projects": latest_playable_projects,
            "project_notes": project_notes,
        },
    )


def creations(request: HttpRequest) -> HttpResponse:
    creations_list = Creation.objects.filter(is_visible=True).order_by(
        "alphabet_letter",
        "title",
    )

    return render(
        request,
        "pages/creation.html",
        {
            "creations": creations_list,
        },
    )


def projets_jouables(request: HttpRequest) -> HttpResponse:
    playable_projects = PlayableProject.objects.filter(
        is_visible=True,
    ).order_by("title")

    return render(
        request,
        "pages/projet_jouable.html",
        {
            "playable_projects": playable_projects,
        },
    )
