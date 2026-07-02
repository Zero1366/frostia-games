from pathlib import Path
from typing import Any, cast

from tinydb import Query, TinyDB

ProjectNote = dict[str, Any]

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "nosql" / "project_notes_db.json"


def get_notes_db() -> TinyDB:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return TinyDB(str(DB_PATH), ensure_ascii=False, indent=2)


def seed_project_notes() -> None:
    db = get_notes_db()

    try:
        notes_table = db.table("project_notes")

        if notes_table.all():
            return

        notes_table.insert_multiple(
            [
                {
                    "project_code": "frostia-games",
                    "title": "Mise en place de la V1",
                    "content": (
                        "Création du portfolio Django, structuration du projet, "
                        "déploiement Render et organisation des preuves."
                    ),
                    "tags": ["django", "portfolio", "v1", "render"],
                    "status": "done",
                    "created_at": "2026-06-30",
                },
                {
                    "project_code": "frostia-games",
                    "title": "Renforcement du dossier projet",
                    "content": (
                        "Ajout de la conception, du SQL natif, du JavaScript "
                        "documenté et de la partie NoSQL."
                    ),
                    "tags": ["dossier-projet", "conception", "sql", "nosql"],
                    "status": "in_progress",
                    "created_at": "2026-06-30",
                },
                {
                    "project_code": "frostia-games",
                    "title": "Préparation de la V3",
                    "content": ("Ajout des éléments demandés après le retour formateur."),
                    "tags": ["v3", "formation", "preuves"],
                    "status": "planned",
                    "created_at": "2026-06-30",
                },
            ]
        )
    finally:
        db.close()


def list_project_notes() -> list[ProjectNote]:
    db = get_notes_db()

    try:
        notes = db.table("project_notes").all()
        return cast(list[ProjectNote], notes)
    finally:
        db.close()


def find_notes_by_project(project_code: str) -> list[ProjectNote]:
    db = get_notes_db()

    try:
        note_query = Query()
        notes = db.table("project_notes").search(note_query.project_code == project_code)
        return cast(list[ProjectNote], notes)
    finally:
        db.close()
