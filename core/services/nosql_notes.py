from pathlib import Path
from typing import Any, cast

from tinydb import Query, TinyDB  # type: ignore[import-not-found]

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "nosql" / "project_notes_db.json"


def get_notes_db() -> TinyDB:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return TinyDB(DB_PATH, ensure_ascii=False, indent=2)


def seed_project_notes() -> None:
    db = get_notes_db()
    notes_table = db.table("project_notes")

    if notes_table.all():
        db.close()
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

    db.close()


def list_project_notes() -> list[dict[str, Any]]:
    db = get_notes_db()
    notes = cast(list[dict[str, Any]], db.table("project_notes").all())
    db.close()
    return notes


def find_notes_by_project(project_code: str) -> list[dict[str, Any]]:
    db = get_notes_db()
    note_query = Query()
    notes = cast(
        list[dict[str, Any]],
        db.table("project_notes").search(note_query.project_code == project_code),
    )
    db.close()
    return notes
