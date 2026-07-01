import json
from pathlib import Path
from typing import Any


def load_project_notes() -> list[dict[str, Any]]:
    file_path = Path(__file__).parent / "project_notes.json"

    with open(file_path, encoding="utf-8") as file:
        notes: list[dict[str, Any]] = json.load(file)

    return notes


def display_project_notes(notes: list[dict[str, Any]]) -> None:
    print("Notes de progression NoSQL — Frostia Games")
    print("=" * 50)

    for note in notes:
        print(f"Projet : {note.get('project_code')}")
        print(f"Titre : {note.get('title')}")
        print(f"Statut : {note.get('status')}")
        print(f"Tags : {', '.join(note.get('tags', []))}")
        print(f"Date : {note.get('created_at')}")
        print(f"Contenu : {note.get('content')}")
        print("-" * 50)


if __name__ == "__main__":
    project_notes = load_project_notes()
    display_project_notes(project_notes)
