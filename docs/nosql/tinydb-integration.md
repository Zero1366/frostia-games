# Intégration NoSQL TinyDB — Frostia Games

## Objectif du document

Ce document présente l’intégration NoSQL ajoutée au projet **Frostia Games**.

L’objectif n’est pas de remplacer la base relationnelle SQLite, mais d’ajouter une solution NoSQL légère pour stocker des données plus souples.

La V1 conserve donc deux approches complémentaires :

* SQLite pour les données principales et structurées du site ;
* une structure documentaire JSON compatible TinyDB pour les notes de progression et les métadonnées variables.

Cette intégration reste volontairement limitée afin de renforcer le dossier projet sans transformer la V1 en architecture trop lourde.

---

# 1. Pourquoi TinyDB ?

TinyDB est une base de données NoSQL légère qui stocke les données sous forme de documents JSON.

Elle est adaptée à cette V1 car elle permet de démontrer une logique NoSQL sans ajouter une infrastructure lourde comme MongoDB.

Ce choix permet de garder un périmètre :

* simple ;
* stable ;
* testable ;
* documentable ;
* cohérent avec une V1.

TinyDB est donc présenté comme une solution NoSQL légère et compatible avec la structure retenue.

La V1 utilise principalement un fichier JSON structuré et un script Python de lecture.

Cette approche permet de démontrer le principe documentaire sans complexifier l’architecture.

---

# 2. Rôle du NoSQL dans Frostia Games

Dans Frostia Games, la partie NoSQL est utilisée pour stocker des notes de progression liées au projet.

Ces notes peuvent contenir des informations variables :

* titre ;
* contenu ;
* statut ;
* tags ;
* date ;
* code du projet.

Ces données sont plus souples que les données principales stockées dans SQLite.

Elles correspondent bien à une logique documentaire, car chaque note peut contenir des informations qui évoluent plus librement qu’une table SQL classique.

---

# 3. Complémentarité SQL / NoSQL

| Données | Technologie | Justification |
| ------- | ----------- | ------------- |
| Créations du portfolio | SQLite / Django ORM | Données structurées et stables |
| Projets jouables | SQLite / Django ORM | Données principales du site |
| Notes de progression | JSON structuré compatible TinyDB | Données souples au format document |
| Métadonnées variables | JSON structuré compatible TinyDB | Champs pouvant évoluer selon les besoins |

SQLite reste la base principale.

La partie NoSQL est utilisée comme complément léger pour montrer une approche documentaire.

---

# 4. Fichiers concernés

Dans la documentation complémentaire, les fichiers NoSQL sont regroupés dans :

```text
Docs/nosql/
```

Fichiers concernés :

| Fichier | Rôle |
| ------- | ---- |
| `Docs/nosql/project_notes.json` | Données NoSQL de démonstration |
| `Docs/nosql/read_project_notes.py` | Script Python permettant de lire les notes |
| `Docs/nosql/structure-nosql.md` | Documentation de la structure des documents |
| `Docs/nosql/tinydb-integration.md` | Documentation de l’intégration TinyDB / JSON |
| `Docs/nosql/nosql.md` | Présentation générale de la partie NoSQL |

Le principe reste le même :

```text
document JSON
→ lecture Python
→ filtrage par projet
→ affichage dans le terminal
```

---

# 5. Structure d’une note NoSQL

Une note de progression peut être représentée sous forme de document JSON.

Exemple :

```json
{
  "project_code": "frostia-games",
  "title": "Intégration NoSQL légère",
  "content": "Ajout d’une structure documentaire JSON et d’un script Python de lecture pour démontrer une approche NoSQL légère compatible avec TinyDB.",
  "tags": ["nosql", "tinydb", "json", "python"],
  "status": "done",
  "created_at": "2026-06-30"
}
```

Cette structure permet de stocker plusieurs informations dans un même document.

Elle est plus souple qu’une table SQL si les champs changent ou si les notes deviennent plus variables.

---

# 6. Fonctionnement général

Le fonctionnement peut être résumé ainsi :

```text
project_notes.json
→ read_project_notes.py
→ lecture des documents
→ filtrage par project_code
→ affichage des notes
```

Le script Python lit les données du fichier JSON, filtre les notes liées au projet `frostia-games`, puis affiche les informations utiles.

Cette logique montre un composant d’accès aux données NoSQL simple.

---

# 7. Lecture Python utilisée dans la V1

La V1 utilise un script Python de lecture placé dans :

```text
Docs/nosql/read_project_notes.py
```

Ce script permet de :

* charger le fichier `project_notes.json` ;
* vérifier que le fichier existe ;
* vérifier que le JSON contient une liste de documents ;
* filtrer les notes liées au projet ;
* afficher les résultats dans le terminal.

Exemple de logique :

```python
import json
from pathlib import Path

NOTES_FILE = Path("Docs/nosql/project_notes.json")

def read_project_notes(project_code):
    with NOTES_FILE.open("r", encoding="utf-8") as file:
        notes = json.load(file)

    return [
        note for note in notes
        if note.get("project_code") == project_code
    ]
```

Ce code montre :

* l’ouverture du fichier JSON ;
* la lecture des documents ;
* le filtrage des notes ;
* la récupération des données liées à un projet.

---

# 8. Exemple compatible TinyDB

TinyDB peut aussi être utilisé directement avec la même logique documentaire.

Exemple :

```python
from tinydb import TinyDB, Query

db = TinyDB("Docs/nosql/project_notes.json")
Note = Query()

notes = db.search(Note.project_code == "frostia-games")

for note in notes:
    print(note["title"])
    print(note["status"])
    print(note["content"])
```

Cette logique montre :

* l’ouverture d’une base TinyDB ;
* la recherche dans des documents JSON ;
* la lecture des données ;
* l’affichage des résultats.

Dans la V1, la preuve principale repose sur le fichier JSON et le script Python.

TinyDB reste la solution légère compatible avec cette structure documentaire.

---

# 9. Commande de test

La preuve de fonctionnement peut être obtenue avec la commande suivante :

```powershell
python Docs/nosql/read_project_notes.py
```

Le résultat attendu est l’affichage des notes stockées dans le fichier JSON.

---

# 10. Preuve obtenue

Le test doit afficher les informations suivantes :

* titre de la note ;
* statut ;
* tags ;
* contenu ;
* date de création si elle est utilisée.

Cela montre que les données NoSQL sont bien stockées, lues et exploitées par un script Python du projet.

---

# 11. Lien possible avec Django

Dans une logique Django, les notes peuvent être récupérées dans une vue puis envoyées au template.

Exemple simplifié :

```python
def home(request):
    project_notes = read_project_notes("frostia-games")

    return render(request, "pages/home.html", {
        "project_notes": project_notes,
    })
```

Le template peut ensuite afficher les notes :

```django
{% for note in project_notes %}
    <article>
        <h2>{{ note.title }}</h2>
        <p>{{ note.content }}</p>
        <p>{{ note.status }}</p>
    </article>
{% endfor %}
```

Cette logique permet de relier la donnée NoSQL au rendu final.

Pour la V1, l’intégration peut rester démonstrative.

---

# 12. Pourquoi ne pas utiliser MongoDB maintenant

MongoDB aurait pu être utilisé comme base NoSQL plus avancée.

Cependant, MongoDB aurait demandé :

* une base externe ;
* une configuration dédiée ;
* des variables d’environnement supplémentaires ;
* une gestion de connexion ;
* une sécurisation plus poussée ;
* une documentation supplémentaire ;
* des tests supplémentaires.

Pour une V1, ce niveau de complexité n’était pas nécessaire.

Une structure JSON compatible TinyDB permet de démontrer le principe NoSQL avec une solution plus simple.

---

# 13. Limites de la solution

La solution NoSQL retenue reste légère.

Elle ne doit pas être présentée comme une base NoSQL de production complète.

Limites principales :

* stockage local dans un fichier JSON ;
* pas adapté à une forte charge ;
* pas adapté à plusieurs écritures simultanées importantes ;
* pas prévu pour stocker des données sensibles ;
* pas destiné à remplacer SQLite ;
* persistance limitée selon l’environnement d’hébergement.

Sur Render, il faut rester prudent avec les fichiers locaux, surtout sur une offre gratuite.

Le fichier JSON doit être considéré comme une démonstration ou une donnée non critique.

---

# 14. Sécurité

La partie NoSQL ne doit contenir aucune donnée sensible.

Ne pas stocker dans `project_notes.json` :

* mot de passe ;
* clé secrète ;
* jeton privé ;
* clé API ;
* donnée personnelle sensible ;
* identifiant administrateur ;
* variable d’environnement.

Le fichier JSON doit contenir uniquement des données de démonstration ou des notes non sensibles.

---

# 15. Pourquoi ne pas tout mettre en NoSQL

Les données principales du projet sont structurées.

Les créations et les projets jouables ont des champs réguliers :

* titre ;
* slug ;
* statut ;
* visibilité ;
* description ;
* dates.

Ces données sont mieux adaptées à SQL.

Le choix cohérent est donc :

```text
SQLite pour les données principales.
JSON / TinyDB pour une démonstration NoSQL légère.
```

Ce choix évite une architecture confuse.

---

# 16. Évolution possible

Une future version pourrait utiliser MongoDB ou une autre base NoSQL pour gérer des contenus plus variables.

Exemples de contenus concernés :

* fiches longues de projets ;
* sections variables selon les jeux ;
* journaux de développement ;
* notes de conception ;
* métadonnées de médias ;
* blocs de contenu personnalisés.

Cette évolution n’est pas nécessaire pour la V1.

---

# 17. Preuves à intégrer dans le dossier

Pour cette partie, les preuves utiles sont :

| Élément | Preuve |
| ------- | ------ |
| Fichier JSON | Capture de `Docs/nosql/project_notes.json` |
| Script de lecture | Capture de `Docs/nosql/read_project_notes.py` |
| Structure NoSQL | Capture de `Docs/nosql/structure-nosql.md` |
| Documentation NoSQL | Capture de `Docs/nosql/nosql.md` |
| Documentation TinyDB | Capture de `Docs/nosql/tinydb-integration.md` |
| Résultat terminal | Capture de l’exécution du script |
| Sécurité | Vérification qu’aucune donnée sensible n’est présente |

Dossier conseillé :

```text
Preuve De Fonctionnement/NoSQL/
```

Captures conseillées :

```text
capture-nosql-json.png
capture-nosql-script.png
capture-nosql-terminal.png
```

---

# 18. Formulation correcte pour le dossier projet

Formulation correcte :

```text
Le projet utilise SQLite comme base principale. Une expérimentation NoSQL légère a été ajoutée avec une structure documentaire JSON compatible TinyDB afin de stocker et lire des notes de progression.
```

Formulation à éviter :

```text
Le projet utilise une architecture NoSQL complète.
```

Autre formulation à éviter :

```text
Le NoSQL remplace SQLite.
```

Ces formulations seraient trop larges ou incorrectes.

---

# 19. Intérêt pour le dossier projet

Cette intégration permet de montrer une utilisation concrète d’une logique NoSQL dans Frostia Games.

Elle répond au besoin de démontrer la compétence liée aux composants d’accès aux données SQL et NoSQL, tout en conservant un périmètre raisonnable.

SQLite reste utilisé pour les données principales du site.

La structure JSON compatible TinyDB sert à stocker et lire des données plus flexibles.

Cette séparation permet de montrer la complémentarité entre une base relationnelle et une logique documentaire.

---

# 20. Conclusion

La V1 de Frostia Games utilise principalement une base relationnelle SQLite avec Django ORM.

Une expérimentation NoSQL légère a été ajoutée afin de démontrer le stockage et la lecture de documents JSON.

Ce choix permet de montrer une compétence NoSQL sans alourdir fortement l’architecture du projet.

La solution reste limitée à une démonstration non critique.

SQLite reste la base principale du projet.

Cette séparation permet de conserver une V1 stable, claire et défendable, tout en ouvrant une évolution possible vers une solution NoSQL plus avancée si le besoin devient réel.


