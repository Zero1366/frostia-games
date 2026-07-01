from core.services.nosql_notes import (
    find_notes_by_project,
    seed_project_notes,
)


def main() -> None:
    seed_project_notes()

    notes = find_notes_by_project("frostia-games")

    print("Preuve NoSQL TinyDB — Frostia Games")
    print("=" * 50)

    for note in notes:
        print(f"Titre : {note.get('title')}")
        print(f"Statut : {note.get('status')}")
        print(f"Tags : {', '.join(note.get('tags', []))}")
        print(f"Contenu : {note.get('content')}")
        print("-" * 50)


if __name__ == "__main__":
    main()
