"""
Lecture des notes NoSQL — Frostia Games

Ce script lit le fichier project_notes.json placé dans le même dossier
et affiche les notes de progression du projet dans le terminal.

Objectif :
- prouver la présence d'une structure documentaire JSON ;
- montrer une lecture de données souples de type NoSQL ;
- produire une sortie terminal exploitable comme preuve de fonctionnement.

Commande :
    python Docs/nosql/read_project_notes.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CURRENT_DIR = Path(__file__).resolve().parent
NOTES_FILE = CURRENT_DIR / "project_notes.json"
DEFAULT_PROJECT_CODE = "frostia-games"


def load_project_notes(file_path: Path = NOTES_FILE) -> list[dict[str, Any]]:
    """
    Charge les notes de progression depuis un fichier JSON.

    Le fichier attendu contient une liste de documents JSON.
    Chaque document représente une note de progression liée à un projet.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Le fichier JSON doit contenir une liste de documents.")

    notes: list[dict[str, Any]] = []

    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"La note numéro {index} n'est pas un objet JSON valide.")

        notes.append(item)

    return notes


def filter_notes_by_project(
    notes: list[dict[str, Any]],
    project_code: str = DEFAULT_PROJECT_CODE,
) -> list[dict[str, Any]]:
    """
    Filtre les notes pour ne conserver que celles du projet demandé.
    """

    return [note for note in notes if note.get("project_code") == project_code]


def format_tags(tags: Any) -> str:
    """
    Formate la liste des tags pour l'affichage terminal.
    """

    if isinstance(tags, list):
        return ", ".join(str(tag) for tag in tags)

    if isinstance(tags, str):
        return tags

    return "Aucun tag"


def display_project_notes(notes: list[dict[str, Any]]) -> None:
    """
    Affiche les notes dans le terminal.
    """

    print("Notes de progression NoSQL — Frostia Games")
    print("=" * 60)

    if not notes:
        print("Aucune note trouvée pour ce projet.")
        return

    for number, note in enumerate(notes, start=1):
        print(f"Note {number}")
        print(f"Projet  : {note.get('project_code', 'Non renseigné')}")
        print(f"Titre   : {note.get('title', 'Non renseigné')}")
        print(f"Statut  : {note.get('status', 'Non renseigné')}")
        print(f"Tags    : {format_tags(note.get('tags', []))}")
        print(f"Date    : {note.get('created_at', 'Non renseignée')}")
        print(f"Contenu : {note.get('content', 'Non renseigné')}")
        print("-" * 60)

    print(f"Total des notes affichées : {len(notes)}")


def main() -> None:
    """
    Point d'entrée du script.
    """

    try:
        all_notes = load_project_notes()
        project_notes = filter_notes_by_project(all_notes)
        display_project_notes(project_notes)

    except FileNotFoundError as error:
        print("Erreur : fichier JSON introuvable.")
        print(error)

    except json.JSONDecodeError as error:
        print("Erreur : le fichier JSON est mal formé.")
        print(error)

    except ValueError as error:
        print("Erreur : structure JSON invalide.")
        print(error)


if __name__ == "__main__":
    main()
