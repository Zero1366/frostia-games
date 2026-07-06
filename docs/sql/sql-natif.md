# SQL natif — Frostia Games

## Objectif du document

Ce document présente les extraits SQL natifs liés au projet **Frostia Games**.

L’objectif est de montrer la structure réelle des tables générées par Django, ainsi que des exemples d’insertion de données avec des requêtes `INSERT INTO`.

Le projet utilise SQLite comme base relationnelle principale pour la V1.

Dans le fonctionnement réel du projet, les tables sont créées par les migrations Django.

Les fichiers SQL présents dans ce dossier sont donc utilisés comme **preuves documentaires** pour montrer la compréhension de la base relationnelle et du SQL natif.

---

# 1. Emplacement des fichiers SQL

Les fichiers SQL complémentaires sont placés dans :

```text
Docs/sql/
```

Fichiers concernés :

```text
Docs/sql/create_tables_creations.sql
Docs/sql/create_tables_playable.sql
Docs/sql/exemples_insert.sql
Docs/sql/sql-natif.md
```

---

# 2. Tables principales

Deux tables principales sont utilisées pour les contenus du site :

| Table | Rôle |
| ----- | ---- |
| `creations_creation` | Stocke les créations présentées dans la page “Mes créations”. |
| `playable_playableproject` | Stocke les projets jouables ou démonstrations prévues. |

Ces tables sont liées aux modèles Django du projet.

---

# 3. Lien avec les modèles Django

Les tables SQL proviennent des modèles Django suivants :

| Modèle Django | Fichier | Table générée |
| ------------- | ------- | ------------- |
| `Creation` | `creations/models.py` | `creations_creation` |
| `PlayableProject` | `playable/models.py` | `playable_playableproject` |

Django ORM permet de manipuler les données avec du code Python.

Les migrations permettent ensuite de générer et mettre à jour la structure SQL.

---

# 4. Génération des tables

Les scripts SQL de création des tables peuvent être générés avec les commandes Django suivantes :

```powershell
python manage.py sqlmigrate creations 0001
python manage.py sqlmigrate playable 0001
```

Ces commandes permettent d’obtenir le SQL réellement produit par Django à partir des migrations du projet.

Les résultats ont été placés dans :

```text
Docs/sql/create_tables_creations.sql
Docs/sql/create_tables_playable.sql
```

---

# 5. Table `creations_creation`

La table `creations_creation` contient les informations nécessaires pour présenter une création dans le portfolio.

Elle contient notamment :

* un identifiant unique ;
* un titre ;
* un slug ;
* une lettre de classement alphabétique ;
* un nom de code ;
* un type de projet ;
* un état d’avancement ;
* une description courte ;
* un indicateur de visibilité ;
* les dates de création et de modification.

Cette table permet d’alimenter la page “Mes créations”.

Extrait SQL documentaire :

```sql
CREATE TABLE "creations_creation" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(120) NOT NULL,
    "slug" varchar(140) NOT NULL UNIQUE,
    "alphabet_letter" varchar(1) NOT NULL,
    "code_name" varchar(120) NOT NULL,
    "project_type" varchar(100) NOT NULL,
    "status" varchar(100) NOT NULL,
    "short_description" text NOT NULL,
    "is_visible" bool NOT NULL,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);
```

---

# 6. Table `playable_playableproject`

La table `playable_playableproject` contient les informations liées aux projets jouables ou aux futures démonstrations.

Elle contient notamment :

* un identifiant unique ;
* un titre ;
* un slug ;
* un état ;
* un type de contenu ;
* une description courte ;
* un message de disponibilité ;
* un indicateur de disponibilité ;
* un indicateur de visibilité ;
* les dates de création et de modification.

Cette table permet de présenter les projets jouables prévus dans la V1 du site.

Extrait SQL documentaire :

```sql
CREATE TABLE "playable_playableproject" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(120) NOT NULL,
    "slug" varchar(140) NOT NULL UNIQUE,
    "status" varchar(100) NOT NULL,
    "content_type" varchar(100) NOT NULL,
    "short_description" text NOT NULL,
    "availability_message" text NOT NULL,
    "is_available" bool NOT NULL,
    "is_visible" bool NOT NULL,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);
```

---

# 7. Exemples `INSERT INTO`

Des exemples d’insertion SQL native sont présents dans le fichier suivant :

```text
Docs/sql/exemples_insert.sql
```

Ces exemples montrent comment ajouter manuellement une création et un projet jouable dans les tables principales.

Exemple d’insertion dans `creations_creation` :

```sql
INSERT INTO creations_creation (
    title,
    slug,
    alphabet_letter,
    code_name,
    project_type,
    status,
    short_description,
    is_visible,
    created_at,
    updated_at
)
VALUES (
    'Frostia Games',
    'frostia-games',
    'F',
    'FROSTIA',
    'Portfolio Django',
    'V1 en développement',
    'Portfolio Django permettant de présenter les projets vidéoludiques et les futures créations.',
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
```

Exemple d’insertion dans `playable_playableproject` :

```sql
INSERT INTO playable_playableproject (
    title,
    slug,
    status,
    content_type,
    short_description,
    availability_message,
    is_available,
    is_visible,
    created_at,
    updated_at
)
VALUES (
    'Prototype jouable à venir',
    'prototype-jouable-a-venir',
    'Prévu',
    'Démonstration',
    'Projet jouable prévu pour une future évolution du site.',
    'Aucune version jouable n’est disponible actuellement. Cette section prépare les futures démonstrations.',
    0,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
```

---

# 8. Rôle de Django ORM

Le projet ne manipule pas directement les tables SQL dans le code courant.

Les données sont principalement gérées avec :

* les modèles Django ;
* l’interface d’administration Django ;
* les vues Django ;
* les requêtes ORM ;
* les migrations.

Exemple de logique ORM :

```python
Creation.objects.filter(is_visible=True)
```

Cette logique permet de récupérer les créations visibles sans écrire directement une requête SQL dans le code applicatif.

---

# 9. Pourquoi documenter le SQL natif

La documentation SQL native permet de montrer que le projet ne se limite pas à l’utilisation automatique de Django.

Elle permet de démontrer la compréhension de :

* la création des tables ;
* le typage des champs ;
* les contraintes principales ;
* les clés primaires ;
* les champs uniques ;
* les champs booléens ;
* les dates ;
* les insertions SQL ;
* la correspondance entre ORM et base relationnelle.

Cette partie répond directement au besoin de valoriser la compétence liée à la base de données relationnelle.

---

# 10. Complémentarité avec la partie NoSQL

La V1 contient également une partie NoSQL légère avec TinyDB.

La séparation est la suivante :

| Données | Technologie | Rôle |
| ------- | ----------- | ---- |
| Créations principales | SQLite / Django ORM | Données structurées |
| Projets jouables | SQLite / Django ORM | Données structurées |
| Notes de progression | TinyDB / JSON | Données souples |
| Métadonnées variables | TinyDB / JSON | Données documentaires |

Le SQL reste utilisé pour les données principales du site.

Le NoSQL sert uniquement de complément léger.

---

# 11. Limite volontaire

Les fichiers SQL présents dans `Docs/sql/` ne remplacent pas les migrations Django.

Ils servent de support documentaire et de preuve technique.

Le fonctionnement réel de la V1 reste :

```text
modèles Django
→ migrations Django
→ SQLite
→ administration Django
→ vues Django
→ templates HTML
```

Cette approche reste plus cohérente pour un projet Django.

---

# 12. Preuves à intégrer dans le dossier

Pour cette partie, les preuves utiles sont :

| Élément | Preuve |
| ------- | ------ |
| Modèle `Creation` | Capture de `creations/models.py` |
| Modèle `PlayableProject` | Capture de `playable/models.py` |
| SQL `CREATE TABLE` | Capture de `Docs/sql/create_tables_creations.sql` |
| SQL `CREATE TABLE` | Capture de `Docs/sql/create_tables_playable.sql` |
| SQL `INSERT INTO` | Capture de `Docs/sql/exemples_insert.sql` |
| Commande Django | Capture ou mention de `python manage.py sqlmigrate` |
| Interface admin | Capture des modèles visibles dans Django admin |
| Rendu final | Capture des pages utilisant les données |

---

# 13. Intérêt pour le dossier projet

Ces extraits SQL permettent de montrer que le projet repose sur une vraie structure relationnelle.

Ils permettent aussi de démontrer la structure utilisée par l’application :

* création des tables ;
* typage des champs ;
* contraintes principales ;
* exemples d’insertion de données ;
* lien entre Django ORM et SQL natif.

Cette partie valorise les compétences liées à la base de données relationnelle et au SQL natif.

Elle complète aussi les autres preuves du dossier :

* modèles Django ;
* vues et routes ;
* interface d’administration ;
* rendu navigateur ;
* documentation NoSQL.

---

# 14. Conclusion

La partie SQL native de Frostia Games permet de documenter clairement la structure relationnelle de la V1.

Les fichiers `CREATE TABLE` montrent les tables principales générées par Django.

Le fichier `exemples_insert.sql` montre des exemples d’ajout de données.

Le projet conserve Django ORM et les migrations comme fonctionnement principal.

Les extraits SQL servent de preuves techniques pour renforcer le dossier projet et démontrer la compréhension de la couche base de données.


