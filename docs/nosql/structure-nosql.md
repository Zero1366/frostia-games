# Structure NoSQL — Frostia Games

## Objectif

Cette partie présente la structure NoSQL utilisée dans le projet **Frostia Games**.

L’objectif n’est pas de remplacer la base relationnelle SQLite, mais d’ajouter une structure complémentaire pour stocker des données plus souples.

La base SQL reste utilisée pour les données principales :

* créations ;
* projets jouables ;
* administration Django ;
* données structurées.

La partie NoSQL est utilisée comme expérimentation légère avec **TinyDB** pour stocker des notes de progression ou des métadonnées variables liées au projet.

---

# 1. Rôle de la structure NoSQL

Certaines données du projet peuvent évoluer de manière plus libre qu’une table relationnelle classique.

Exemples :

* notes de développement ;
* journal de progression ;
* tags variables ;
* remarques libres ;
* étapes de conception ;
* informations temporaires sur un projet ;
* métadonnées de suivi.

Ces données n’ont pas toujours besoin d’un schéma relationnel strict.

Le NoSQL est donc utilisé comme complément pour stocker des documents plus flexibles.

Dans cette V1, le choix a été de rester sur une solution légère afin de ne pas complexifier l’architecture.

---

# 2. Technologie utilisée

La solution retenue est :

```text
TinyDB
```

TinyDB permet de stocker des documents dans un fichier JSON.

Dans le projet, les données NoSQL sont stockées dans :

```text
Docs/nosql/project_notes.json
```

Le script de lecture est placé dans :

```text
Docs/nosql/read_project_notes.py
```

La documentation de l’intégration est complétée par :

```text
Docs/nosql/nosql.md
Docs/nosql/structure-nosql.md
Docs/nosql/tinydb-integration.md
```

---

# 3. Exemple de document NoSQL

Exemple de document NoSQL utilisé pour une note de progression :

```json
{
  "project_code": "frostia-games",
  "title": "Mise en place de la V1",
  "content": "Création du portfolio Django, déploiement Render et structuration des preuves.",
  "tags": ["django", "portfolio", "v1", "render"],
  "status": "done",
  "created_at": "2026-06-30"
}
```

Ce document représente une note liée au projet **Frostia Games**.

Il n’a pas besoin d’une table SQL dédiée dans la V1.

---

# 4. Rôle des champs

| Champ | Rôle |
| ----- | ---- |
| `project_code` | Identifie le projet concerné |
| `title` | Titre de la note |
| `content` | Contenu ou description de la note |
| `tags` | Liste de mots-clés associés |
| `status` | État de la note ou de l’étape |
| `created_at` | Date de création de la note |

Cette structure permet de conserver une trace d’une étape du projet sans modifier la structure SQL principale.

---

# 5. Souplesse de la structure

Les champs peuvent varier selon les besoins.

Par exemple :

* certaines notes peuvent avoir plusieurs tags ;
* certaines notes peuvent avoir un statut ;
* certaines notes peuvent contenir des remarques plus longues ;
* certaines notes peuvent seulement contenir un titre et un contenu ;
* de futurs documents pourraient contenir des métadonnées supplémentaires.

Cette souplesse est l’intérêt principal d’une approche NoSQL.

Elle évite d’ajouter une nouvelle table SQL pour une donnée légère ou variable.

---

# 6. Complémentarité SQL / NoSQL

| Type de données | Technologie | Justification |
| --------------- | ----------- | ------------- |
| Créations principales | SQLite | Données structurées et stables |
| Projets jouables | SQLite | Données relationnelles simples |
| Administration Django | SQLite | Fonctionnement standard de Django |
| Notes de progression | TinyDB | Données souples et variables |
| Métadonnées libres | TinyDB | Structure flexible |
| Données sensibles | Aucune dans TinyDB | Sécurité et séparation des responsabilités |

La base SQLite reste la source principale des données du site.

TinyDB sert uniquement de complément documentaire et technique.

---

# 7. Exemple de lecture des documents

Le script de lecture peut récupérer les notes liées au projet `frostia-games`.

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

Cette logique montre :

* l’ouverture du fichier JSON ;
* la lecture des documents ;
* le filtrage par projet ;
* la récupération des notes utiles.

---

# 8. Exemple avec TinyDB

TinyDB peut aussi être utilisé directement avec une logique de requête.

Exemple :

```python
from tinydb import TinyDB, Query

db = TinyDB("Docs/nosql/project_notes.json")
Note = Query()

notes = db.search(Note.project_code == "frostia-games")
```

Cette syntaxe montre une approche documentaire simple.

Le fichier JSON devient une petite base NoSQL locale.

---

# 9. Commande de test

La lecture NoSQL peut être testée avec le script prévu.

Exemple :

```powershell
python Docs/nosql/read_project_notes.py
```

Si une version module existe dans le projet, la commande peut aussi être :

```powershell
python -m scripts.demo_tinydb_notes
```

Le résultat attendu est l’affichage des notes liées au projet.

---

# 10. Lien possible avec Django

Les notes NoSQL peuvent être utilisées dans une vue Django.

Exemple logique :

```python
def home(request):
    project_notes = read_project_notes("frostia-games")

    return render(request, "pages/home.html", {
        "project_notes": project_notes,
    })
```

Le template peut ensuite afficher les notes sur la page d’accueil.

Cette logique permet de relier :

```text
document JSON
→ lecture Python
→ vue Django
→ template HTML
→ rendu navigateur
```

---

# 11. Limite volontaire

L’intégration NoSQL reste volontairement limitée.

Le but est de démontrer la complémentarité entre SQL et NoSQL sans transformer la V1 en projet trop complexe.

TinyDB ne doit pas être présenté comme une base NoSQL de production complète.

Il s’agit d’une preuve légère et suffisante pour montrer :

* une structure documentaire ;
* une lecture de données JSON ;
* une séparation entre SQL et NoSQL ;
* une capacité à documenter une architecture de données.

---

# 12. Sécurité

La structure NoSQL ne doit contenir aucune donnée sensible.

Ne jamais stocker dans `project_notes.json` :

* mot de passe ;
* clé secrète ;
* token ;
* clé API ;
* identifiant administrateur ;
* variable d’environnement ;
* donnée personnelle inutile.

Les notes doivent rester des données de démonstration ou de suivi non sensibles.

---

# 13. Évolutions possibles

Dans une version future, une base NoSQL plus avancée comme MongoDB pourrait être étudiée si le projet a besoin de gérer :

* fiches longues de projets ;
* sections variables selon les jeux ;
* journaux de développement détaillés ;
* métadonnées de médias ;
* contenus non uniformes ;
* notes de conception plus complexes.

Cette évolution n’est pas nécessaire pour la V1.

TinyDB suffit pour démontrer une approche NoSQL légère.

---

# 14. Preuves à intégrer dans le dossier

Pour cette partie, les preuves utiles sont :

| Élément | Preuve |
| ------- | ------ |
| Structure JSON | Capture de `Docs/nosql/project_notes.json` |
| Script de lecture | Capture de `Docs/nosql/read_project_notes.py` |
| Documentation NoSQL | Capture de `Docs/nosql/structure-nosql.md` |
| Intégration TinyDB | Capture de `Docs/nosql/tinydb-integration.md` |
| Résultat terminal | Capture du script affichant les notes |
| Rendu final si utilisé | Capture des notes affichées sur l’accueil |

---

# 15. Conclusion

La structure NoSQL de Frostia Games repose sur une approche simple avec TinyDB et un fichier JSON.

Elle permet de stocker des notes de progression sans modifier la base relationnelle principale.

SQLite reste utilisé pour les données structurées du site.

TinyDB sert de complément léger pour démontrer une logique documentaire.

Cette séparation permet de conserver une V1 stable, claire et défendable, tout en montrant une première utilisation concrète du NoSQL.


