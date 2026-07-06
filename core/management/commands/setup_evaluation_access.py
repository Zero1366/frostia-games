from __future__ import annotations

import os
from typing import Any, cast

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Configure le compte d'évaluation en lecture seule."

    def add_arguments(self, parser: Any) -> None:
        parser.add_argument(
            "--username",
            default=os.getenv("EVALUATION_USER_USERNAME", "evaluation_temp"),
        )
        parser.add_argument(
            "--email",
            default=os.getenv("EVALUATION_USER_EMAIL", "evaluation@example.com"),
        )
        parser.add_argument(
            "--password",
            default=os.getenv("EVALUATION_USER_PASSWORD"),
        )

    def handle(self, *args: Any, **options: Any) -> None:
        username = options["username"]
        email = options["email"]
        password = options["password"]

        if not password:
            self.stdout.write(
                self.style.WARNING(
                    "Aucun mot de passe fourni. "
                    "Compte d'évaluation non configuré."
                )
            )
            return

        UserModel = get_user_model()
        user = cast(Any, UserModel.objects.get_or_create(username=username)[0])

        user.email = email
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.user_permissions.clear()

        group, group_created = Group.objects.get_or_create(
            name="Evaluation lecture seule"
        )
        group.permissions.clear()

        view_creation = Permission.objects.get(
            content_type__app_label="creations",
            codename="view_creation",
        )

        view_playable = Permission.objects.get(
            content_type__app_label="playable",
            codename="view_playableproject",
        )

        group.permissions.add(view_creation, view_playable)

        user.groups.clear()
        user.groups.add(group)
        user.save()

        self.stdout.write(self.style.SUCCESS("Accès d'évaluation configuré."))
        self.stdout.write(f"Utilisateur : {username}")
        self.stdout.write(f"Groupe créé : {'oui' if group_created else 'non'}")
        self.stdout.write("Droits : lecture seule")
        self.stdout.write("Staff : oui")
        self.stdout.write("Superutilisateur : non")
