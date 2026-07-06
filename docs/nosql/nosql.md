# NoSQL — Frostia Games

## Objectif du document

Ce document présente la partie **NoSQL** du projet **Frostia Games**.

L’objectif est d’expliquer pourquoi une structure NoSQL légère a été ajoutée dans la V1 renforcée du projet, comment elle est utilisée et quelles sont ses limites.

La V1 utilise toujours **SQLite** comme base principale.

Le NoSQL est utilisé sous forme d’expérimentation légère avec un fichier **JSON structuré**, compatible avec une logique documentaire de type **TinyDB**.

Ce document remplace l’ancienne version qui présentait le NoSQL uniquement comme une piste future.

---

# 1. Situation actuelle du projet

La V1 de Frostia Games repose principalement sur une architecture Django classique.

Elle comprend :

* des pages publiques ;
* une base SQLite ;
* des modèles Django ;
* des migrations ;
* une administration Django ;
* un affichage dynamique des données ;
* un menu mobile JavaScript ;
* un lancement local ;
* un lancement avec Docker ;
* un déploiement en ligne sur Render ;
* une documentation technique ;
* des preuves de fonctionnement.

À cette base SQL principale s’ajoute maintenant une expérimentation NoSQL légère.

Cette expérimentation repose sur :

```text
Docs/nosql/project_notes.json
Docs/nosql/read_project_notes.py
```

Le fichier JSON contient des documents.

Le script Python lit ces documents, les filtre et les affiche dans le terminal.

Cette approche permet de démontrer une logique NoSQL documentaire sans complexifier l’architecture.

---

# 2. Choix retenu pour la V1 renforcée

Le choix technique retenu est le suivant :

| Besoin | Solution utilisée |
| ------ | ----------------- |
| Données principales structurées | SQLite avec Django ORM |
| Créations | Modèle Django `Creation` |
| Projets jouables | Modèle Django `PlayableProject` |
| Administration | Django Admin |
| Notes de progression souples | JSON structuré |
| Logique NoSQL légère | Structure documentaire compatible TinyDB |
| Démonstration NoSQL | Script Python de lecture |

Cette organisation permet de montrer à la fois :

* une base relationnelle classique ;
* une logique documentaire NoSQL légère ;
* une séparation claire entre données structurées et données plus libres.

---

# 3. Rôle de SQLite

SQLite reste la base relationnelle principale du projet.

Elle permet de stocker les données nécessaires au fonctionnement de la V1.

Les données sont manipulées avec Django ORM, ce qui permet :

* de définir les modèles dans le code Python ;
* de générer les migrations ;
* de créer les tables ;
* de gérer les données depuis l'administration Django ;
* d'afficher les informations dans les templates.

SQLite est utilisé pour les données structurées, notamment :

* les créations ;
* les projets jouables ;
* les statuts ;
* la visibilité ;
* les dates de création ;
* les dates de modification.

Ces données correspondent bien à une structure relationnelle classique.

---

# 4. Rôle de la partie NoSQL

La partie NoSQL sert à démontrer une logique de documents JSON.

Dans Frostia Games, elle sert principalement à représenter des notes de progression.

Exemples de données adaptées à cette approche :

* notes de conception ;
* notes de progression ;
* éléments de suivi ;
* informations souples ;
* contenus de démonstration ;
* données qui n’ont pas forcément besoin d’une table SQL complète.

Cette approche est cohérente pour une V1, car elle ne demande pas de serveur externe.

Elle permet de montrer le principe du NoSQL sans ajouter une architecture trop lourde comme MongoDB.

---

# 5. Fichiers concernés

La partie NoSQL est documentée et testée dans le dossier :

```text
Docs/nosql/
```

Fichiers concernés :

```text
Docs/nosql/nosql.md
Docs/nosql/project_notes.json
Docs/nosql/read_project_notes.py
Docs/nosql/structure-nosql.md
Docs/nosql/tinydb-integration.md
```

Le principe est le suivant :

```text
document JSON
→ script Python
→ récupération des notes
→ filtrage par projet
→ affichage terminal
```

Cette chaîne permet de produire une preuve simple et vérifiable.

---

# 6. Exemple de document NoSQL

Un document NoSQL peut représenter une note de progression.

Exemple :

```json
{
  "project_code": "frostia-games",
  "title": "Intégration NoSQL légère",
  "content": "Ajout d’une structure documentaire JSON et d’un script Python de lecture pour démontrer une approche NoSQL légère compatible avec TinyDB.",
  "status": "done",
  "tags": [
    "nosql",
    "tinydb",
    "json",
    "python"
  ],
  "created_at": "2026-06-30"
}
```

Ce type de structure est plus souple qu’une table SQL classique.

Il permet d’ajouter ou de modifier certains champs sans devoir créer immédiatement une nouvelle migration Django.

---

# 7. Différence entre SQL et NoSQL dans Frostia Games

## SQL actuel

La base SQLite sert à stocker les données principales du site.

Elle est adaptée pour :

* les créations ;
* les projets jouables ;
* les statuts ;
* la visibilité ;
* les dates de création ;
* les dates de modification ;
* les données structurées.

Ces données correspondent bien à des tables relationnelles.

---

## NoSQL léger

La partie NoSQL sert à stocker des contenus plus flexibles.

Elle est adaptée pour :

* des notes ;
* des blocs de contenu libres ;
* des informations de suivi ;
* des brouillons ;
* des données de démonstration ;
* des documents JSON simples.

Elle ne remplace pas la base relationnelle.

Elle complète le projet pour démontrer une logique documentaire légère.

---

# 8. Exemple de séparation SQL / NoSQL

Dans la V1 renforcée, l’organisation peut être comprise ainsi :

| Type de donnée | Solution utilisée |
| -------------- | ----------------- |
| Créations principales | SQLite |
| Projets jouables | SQLite |
| Statuts | SQLite |
| Visibilité | SQLite |
| Données administrables | Django Admin + SQLite |
| Notes de progression | JSON structuré |
| Documents de démonstration | NoSQL léger |
| Contenus très flexibles futurs | NoSQL plus avancé possible |

Cette séparation permet d’utiliser chaque technologie pour un rôle adapté.

---

# 9. Script de lecture NoSQL

Le script suivant permet de lire les notes stockées dans le fichier JSON :

```text
Docs/nosql/read_project_notes.py
```

Son rôle est de :

* charger le fichier `project_notes.json` ;
* vérifier que le fichier existe ;
* vérifier que le JSON contient une liste de documents ;
* filtrer les notes liées au projet `frostia-games` ;
* afficher les notes dans le terminal.

Commande de test :

```powershell
python Docs/nosql/read_project_notes.py
```

Cette commande doit afficher les notes de progression du projet.

Cette preuve montre que les données NoSQL ne sont pas seulement décrites dans la documentation, mais également lues par un script Python.

---

# 10. Exemple de logique compatible TinyDB

TinyDB peut aussi lire un fichier JSON comme petite base documentaire.

Exemple de logique TinyDB :

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
* la lecture de données souples ;
* l’affichage des résultats.

Dans la V1, le script `read_project_notes.py` permet déjà de démontrer la lecture du fichier documentaire.

TinyDB reste la solution légère retenue ou compatible pour une évolution immédiate sans infrastructure externe.

---

# 11. Exemple d’utilisation dans une logique Django

Dans une logique Django, les notes peuvent être récupérées puis transmises à un template.

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

Cette logique montre comment une donnée documentaire peut être utilisée dans une page Django.

Pour la V1, cette intégration complète dans le rendu public peut rester limitée ou démonstrative.

---

# 12. Pourquoi une solution légère plutôt que MongoDB

MongoDB aurait pu être utilisé pour une vraie base NoSQL plus avancée.

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

# 13. Limites de la solution retenue

La solution NoSQL actuelle reste légère.

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

Ce choix permet d’éviter une architecture confuse.

---

# 16. Évolution possible vers un NoSQL plus avancé

Une future version pourrait utiliser MongoDB ou une autre base NoSQL pour gérer des contenus plus variables.

Exemples de contenus concernés :

* fiches longues de projets ;
* sections variables selon les jeux ;
* journaux de développement ;
* notes de conception ;
* métadonnées de médias ;
* blocs de contenu personnalisés.

Exemple de document futur :

```json
{
  "slug": "kryoncore",
  "title": "KryonCore",
  "status": "En préparation",
  "sections": [
    {
      "title": "Présentation",
      "content": "Présentation du projet."
    },
    {
      "title": "Gameplay",
      "content": "Description du gameplay."
    }
  ],
  "tags": [
    "jeu vidéo",
    "prototype"
  ]
}
```

Ce type de structure pourrait devenir utile si les fiches projets deviennent très différentes les unes des autres.

---

# 17. Risques d'une intégration NoSQL avancée

Une future intégration NoSQL avancée devra être étudiée avec prudence.

Les principaux risques seraient :

* complexifier inutilement l'architecture ;
* multiplier les sources de données ;
* rendre les sauvegardes plus difficiles ;
* devoir sécuriser une deuxième base ;
* augmenter les tests nécessaires ;
* créer une dépendance technique supplémentaire ;
* rendre le projet moins lisible.

Avant d'intégrer une solution NoSQL plus lourde, il faudra vérifier que le besoin est réel.

---

# 18. Critères avant une future évolution NoSQL

Avant d'ajouter une base NoSQL plus avancée, plusieurs questions devront être posées :

* Les données sont-elles vraiment variables ?
* Une base SQL ne suffit-elle plus ?
* Les fiches projets nécessitent-elles des structures très différentes ?
* L'ajout de NoSQL améliore-t-il réellement le projet ?
* La sécurité est-elle maîtrisée ?
* La documentation reste-t-elle claire ?
* Le projet reste-t-il maintenable ?
* L'intégration ne transforme-t-elle pas le projet en architecture trop lourde ?

Si le besoin n'est pas confirmé, l'idée devra être reportée.

---

# 19. Preuves à intégrer dans le dossier

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

# 20. Formulation correcte pour le dossier projet

La formulation correcte est :

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

# 21. Conclusion

La V1 de Frostia Games utilise principalement une base relationnelle SQLite avec Django ORM.

Une expérimentation NoSQL légère a été ajoutée afin de démontrer le stockage et la lecture de documents JSON.

Ce choix permet de montrer une compétence NoSQL sans alourdir fortement l’architecture du projet.

La solution actuelle reste limitée à une démonstration non critique.

SQLite reste la base principale du projet.

Cette séparation permet de conserver une V1 stable, claire et défendable, tout en ouvrant une évolution possible vers une solution NoSQL plus avancée si le besoin devient réel.
