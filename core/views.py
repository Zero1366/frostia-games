from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.services.nosql_notes import find_notes_by_project, seed_project_notes
from creations.models import Creation
from playable.models import PlayableProject


def home(request: HttpRequest) -> HttpResponse:
    latest_creations = Creation.objects.filter(is_visible=True).order_by(
        "alphabet_letter",
        "title",
    )[:3]

    latest_playable_projects = PlayableProject.objects.filter(
        is_visible=True,
    ).order_by("title")[:3]

    seed_project_notes()
    project_notes = find_notes_by_project("frostia-games")

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
    playable_projects = PlayableProject.objects.filter(is_visible=True).order_by(
        "title",
    )

    return render(
        request,
        "pages/projet_jouable.html",
        {
            "playable_projects": playable_projects,
        },
    )
