# MCD — Frostia Games

## Objectif du MCD

Ce document présente le **modèle conceptuel de données** du projet **Frostia Games**.

L’objectif est de représenter les principales données utilisées par la V1 du site.

Le projet repose principalement sur une base relationnelle **SQLite**, gérée avec **Django ORM**.

Dans cette V1, deux entités relationnelles principales sont utilisées :

* `Creation` : représente une création ou un projet présenté dans la page **Mes créations** ;
* `PlayableProject` : représente un projet jouable ou une démonstration prévue.

Le projet contient aussi une expérimentation NoSQL légère avec TinyDB pour les notes de progression. Cette partie est présentée séparément, car elle ne fait pas partie du modèle relationnel SQLite principal.

---

# 1. Vue d’ensemble du modèle

La V1 utilise une structure volontairement simple.

Le modèle relationnel principal repose sur deux entités indépendantes :

| Entité | Rôle |
| ------ | ---- |
| `Creation` | Stocker les créations ou projets présentés dans le portfolio. |
| `PlayableProject` | Stocker les futurs projets jouables ou démonstrations prévues. |

Dans la V1 actuelle, ces deux entités ne sont pas encore reliées entre elles.

Ce choix permet de garder une base simple, stable et facile à expliquer.

---

# 2. Entité `Creation`

## Rôle

L’entité `Creation` permet de stocker les informations liées aux créations présentées sur le portfolio.

Elle alimente principalement la page :

```text
/mes-creations/
```

Elle permet de présenter un projet, une création, un prototype ou une idée liée à l’univers Frostia Games.

---

## Attributs

| Attribut | Type logique | Rôle |
| -------- | ------------ | ---- |
| `id` | entier | Identifiant unique de la création |
| `title` | texte court | Titre de la création |
| `slug` | texte court unique | Identifiant textuel utilisé pour les URLs ou références internes |
| `alphabet_letter` | texte court | Lettre utilisée pour le classement alphabétique |
| `code_name` | texte court | Nom de code du projet |
| `project_type` | texte court | Type de projet |
| `status` | texte court | État d’avancement du projet |
| `short_description` | texte long | Description courte du projet |
| `is_visible` | booléen | Indique si la création est visible publiquement |
| `created_at` | date / heure | Date de création de l’enregistrement |
| `updated_at` | date / heure | Date de dernière modification |

---

## Utilité dans la V1

Le champ `is_visible` permet de préparer une création dans l’administration Django sans forcément l’afficher immédiatement sur le site public.

Cela permet de séparer :

* les données préparées côté administration ;
* les données réellement visibles par le visiteur.

---

# 3. Entité `PlayableProject`

## Rôle

L’entité `PlayableProject` permet de stocker les informations liées aux projets jouables ou aux futures démonstrations.

Elle alimente principalement la page :

```text
/projets-jouables/
```

Dans la V1, aucun vrai jeu jouable dans le navigateur n’est encore intégré.

Cette entité sert à préparer la structure future sans annoncer une fonctionnalité qui n’est pas encore disponible.

---

## Attributs

| Attribut | Type logique | Rôle |
| -------- | ------------ | ---- |
| `id` | entier | Identifiant unique du projet jouable |
| `title` | texte court | Titre du projet jouable |
| `slug` | texte court unique | Identifiant textuel utilisé pour les URLs ou références internes |
| `status` | texte court | État du projet jouable |
| `content_type` | texte court | Type de contenu prévu |
| `short_description` | texte long | Description courte |
| `availability_message` | texte long | Message indiquant la disponibilité ou l’indisponibilité |
| `is_available` | booléen | Indique si le projet est réellement disponible |
| `is_visible` | booléen | Indique si le projet est visible publiquement |
| `created_at` | date / heure | Date de création de l’enregistrement |
| `updated_at` | date / heure | Date de dernière modification |

---

## Utilité dans la V1

Le modèle `PlayableProject` permet d’être honnête sur l’état des projets jouables.

Un projet peut être visible dans la page publique tout en indiquant clairement qu’aucune version jouable n’est encore disponible.

Le champ `is_available` permet de distinguer :

* un projet présenté comme prévu ;
* un projet réellement disponible ;
* une future démonstration.

---

# 4. Relations entre les entités

Dans la V1 actuelle, les entités `Creation` et `PlayableProject` sont indépendantes.

Il n’existe pas encore de relation directe entre elles.

Cette absence de relation est volontaire.

Elle permet de conserver une structure :

* simple ;
* lisible ;
* stable ;
* adaptée à une V1 ;
* facile à maintenir.

---

## Relations futures possibles

Les futures évolutions pourront ajouter des relations, par exemple :

* associer un projet jouable à une création ;
* ajouter des catégories ;
* ajouter des tags ;
* ajouter des médias ;
* ajouter des versions de projet ;
* ajouter une page détaillée par création ;
* ajouter un journal de développement ;
* ajouter des notes de progression reliées aux projets.

Ces évolutions ne sont pas nécessaires pour la V1.

---

# 5. Représentation Mermaid

```mermaid
erDiagram
    CREATION {
        int id PK
        string title
        string slug
        string alphabet_letter
        string code_name
        string project_type
        string status
        text short_description
        boolean is_visible
        datetime created_at
        datetime updated_at
    }

    PLAYABLE_PROJECT {
        int id PK
        string title
        string slug
        string status
        string content_type
        text short_description
        text availability_message
        boolean is_available
        boolean is_visible
        datetime created_at
        datetime updated_at
    }
```

---

# 6. Lien avec Django ORM

Dans Django, les entités du MCD sont traduites en modèles Python.

Fichiers concernés :

```text
creations/models.py
playable/models.py
```

Correspondance :

| Entité du MCD | Modèle Django | Table SQL |
| ------------- | ------------- | --------- |
| `Creation` | `Creation` | `creations_creation` |
| `PlayableProject` | `PlayableProject` | `playable_playableproject` |

Django ORM permet de manipuler ces données avec du code Python.

Exemple :

```python
Creation.objects.filter(is_visible=True)
```

Cet exemple récupère uniquement les créations visibles côté public.

---

# 7. Lien avec SQL

Les modèles Django génèrent des tables SQL grâce aux migrations.

Fichiers SQL documentaires :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers permettent de montrer la correspondance entre :

* le modèle conceptuel ;
* les modèles Django ;
* les migrations ;
* les tables SQL ;
* les exemples d’insertion.

Le SQL natif reste documentaire.

Dans le fonctionnement réel du projet, les tables sont créées et mises à jour par les migrations Django.

---

# 8. Partie NoSQL hors MCD relationnel

Le projet contient aussi une expérimentation NoSQL légère avec TinyDB.

Cette partie ne fait pas partie du MCD relationnel principal, car elle repose sur un fichier JSON.

Fichiers concernés :

```text
Docs/nosql/project_notes.json
Docs/nosql/read_project_notes.py
Docs/nosql/structure-nosql.md
Docs/nosql/tinydb-integration.md
```

TinyDB sert à stocker des notes de progression sous forme de documents JSON.

Exemple logique d’un document NoSQL :

```json
{
  "project_code": "frostia-games",
  "title": "Renforcement du dossier projet",
  "content": "Ajout des documents de conception, SQL et NoSQL.",
  "status": "in_progress",
  "tags": ["dossier", "conception", "sql", "nosql"]
}
```

Cette structure est volontairement séparée du modèle relationnel principal.

SQLite reste la base principale de la V1.

TinyDB sert uniquement de preuve NoSQL légère.

---

# 9. Justification des choix

La base relationnelle SQLite est utilisée pour stocker les données principales du site, car les informations sont structurées et stables.

Django ORM permet de manipuler ces données à partir des modèles Python, tout en générant les migrations nécessaires à la création des tables.

Le choix de séparer `Creation` et `PlayableProject` permet de garder une organisation claire :

* les créations servent à présenter l’univers et les projets du portfolio ;
* les projets jouables servent à présenter les démonstrations ou versions jouables prévues.

Cette séparation rend la V1 plus simple à maintenir.

Elle laisse aussi la possibilité d’ajouter des relations plus tard si le projet évolue.

---

# 10. Limites du MCD actuel

Le MCD actuel est volontairement limité.

Il ne contient pas encore :

* table de catégories ;
* table de tags ;
* table de médias ;
* table de versions ;
* table de journal de développement ;
* table de commentaires ;
* table de statistiques ;
* table de fichiers uploadés ;
* relation entre `Creation` et `PlayableProject`.

Ces éléments sont reportés afin de conserver une V1 stable.

---

# 11. Évolutions possibles du MCD

Une future version pourrait ajouter de nouvelles entités :

```text
ProjectDetail
ProjectVersion
MediaAsset
DevelopmentLog
ProjectTag
ProjectLink
```

Une relation possible pourrait être ajoutée entre `Creation` et `PlayableProject`.

Exemple futur :

```mermaid
erDiagram
    CREATION ||--o{ PLAYABLE_PROJECT : "peut avoir"
```

Cette évolution permettrait d’associer un ou plusieurs projets jouables à une création principale.

Elle n’est pas intégrée maintenant afin de ne pas complexifier inutilement la V1.

---

# 12. Preuves à intégrer dans le dossier

Pour cette partie, les preuves utiles sont :

| Élément | Preuve possible |
| ------- | --------------- |
| MCD Mermaid | Capture ou export du diagramme |
| Modèle `Creation` | Capture de `creations/models.py` |
| Modèle `PlayableProject` | Capture de `playable/models.py` |
| Table SQL `Creation` | Capture de `docs/sql/create_tables_creations.sql` |
| Table SQL `PlayableProject` | Capture de `docs/sql/create_tables_playable.sql` |
| Exemples SQL | Capture de `docs/sql/exemples_insert.sql` |
| Administration Django | Capture des modèles visibles dans `/admin/` |
| Rendu final | Capture des pages utilisant les données |

---

# 13. Conclusion

Le MCD de Frostia Games montre une structure volontairement simple.

La V1 repose principalement sur deux entités relationnelles :

* `Creation` ;
* `PlayableProject`.

Ces entités suffisent pour présenter les créations et les futurs projets jouables du portfolio.

TinyDB est traité séparément comme une expérimentation NoSQL légère.

Cette organisation permet de garder un projet stable, lisible et évolutif, tout en montrant une vraie réflexion sur les données utilisées par l’application.
