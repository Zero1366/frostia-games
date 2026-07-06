from __future__ import annotations

import os
from typing import Any, cast

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand, CommandParser

from creations.models import Creation
from playable.models import PlayableProject


class Command(BaseCommand):
    help = "Configure les données initiales Render et le compte d'évaluation."

    def add_arguments(self: Command, parser: CommandParser) -> None:
        parser.add_argument(
            "--password",
            default=os.getenv("EVALUATION_USER_PASSWORD"),
            help="Mot de passe du compte d'évaluation.",
        )

    def handle(self: Command, *args: Any, **options: Any) -> None:
        password = cast(str | None, options["password"])

        self.create_initial_content()
        self.create_evaluation_access(password)

    def create_initial_content(self: Command) -> None:
        Creation.objects.update_or_create(
            slug="frostia-games",
            defaults={
                "title": "Frostia Games",
                "alphabet_letter": "F",
                "code_name": "FROSTIA",
                "project_type": "Portfolio Django",
                "status": "V1 en développement",
                "short_description": (
                    "Portfolio Django permettant de présenter les projets "
                    "vidéoludiques en cours de création."
                ),
                "is_visible": True,
            },
        )

        PlayableProject.objects.update_or_create(
            slug="prototype-jouable-a-venir",
            defaults={
                "title": "Prototype jouable à venir",
                "status": "Prévu",
                "content_type": "Démonstration",
                "short_description": ("Projet jouable prévu pour une future évolution du site."),
                "availability_message": ("Aucune version jouable n'est disponible actuellement."),
                "is_available": False,
                "is_visible": True,
            },
        )

        self.stdout.write(self.style.SUCCESS("Données initiales créées."))

    def create_evaluation_access(
        self: Command,
        password: str | None,
    ) -> None:
        if not password:
            self.stdout.write(
                self.style.WARNING("Aucun mot de passe fourni pour le compte d'évaluation.")
            )
            return

        UserModel = get_user_model()

        user = cast(
            Any,
            UserModel.objects.get_or_create(username="evaluation_temp")[0],
        )

        user.email = "evaluation@example.com"
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.user_permissions.clear()

        group, _ = Group.objects.get_or_create(name="Evaluation lecture seule")
        group.permissions.clear()

        view_creation = Permission.objects.get(
            content_type__app_label="creations",
            codename="view_creation",
        )

        view_playable_project = Permission.objects.get(
            content_type__app_label="playable",
            codename="view_playableproject",
        )

        group.permissions.add(
            view_creation,
            view_playable_project,
        )

        user.groups.clear()
        user.groups.add(group)
        user.save()

        self.stdout.write(self.style.SUCCESS("Accès d'évaluation configuré."))
        self.stdout.write("Utilisateur : evaluation_temp")
        self.stdout.write("Droits : lecture seule")
        self.stdout.write("Staff : oui")
        self.stdout.write("Superutilisateur : non")
