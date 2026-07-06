# Architecture du projet - Frostia Games

## Objectif du document

Ce document présente l'architecture du projet **Frostia Games**.

L'objectif est d'expliquer comment le projet est organisé, quel est le rôle des principaux dossiers et fichiers, et comment les différentes parties du site fonctionnent ensemble.

Le projet est une application web développée avec **Django**.

Il sert de portfolio pour présenter des projets de jeux vidéo actuels ou futurs, avec une interface publique simple, une base SQLite, une expérimentation NoSQL légère avec TinyDB, une administration Django, une documentation technique et un déploiement en ligne sur Render.

Ce document a été mis à jour après le renforcement du dossier projet afin d'intégrer :

* TinyDB ;
* les notes de progression affichées sur l'accueil ;
* le compte temporaire de lecture seule ;
* les fichiers SQL natifs complémentaires ;
* la documentation `docs/` ;
* la documentation JavaScript ;
* la documentation backend complémentaire ;
* les nouvelles preuves à préparer.

---

# 1. Vue d'ensemble du projet

Frostia Games est organisé autour d'une architecture Django simple et volontairement limitée.

Le projet contient :

* une configuration Django principale ;
* une application dédiée aux pages principales ;
* une application dédiée aux créations ;
* une application dédiée aux futurs projets jouables ;
* des services internes Python ;
* des scripts de démonstration ;
* des templates HTML ;
* des fichiers statiques CSS, JavaScript et images ;
* une base de données SQLite pour les données principales ;
* une base NoSQL TinyDB pour des notes de progression ;
* une administration Django ;
* un compte temporaire de lecture seule ;
* des fichiers Docker ;
* des fichiers de déploiement Render ;
* une documentation technique principale ;
* une documentation complémentaire de conception, SQL, NoSQL, frontend et backend.

Cette structure permet de garder un projet lisible, maintenable et évolutif.

L'objectif de la V1 n'est pas de créer une plateforme complète, mais de produire une base stable, fonctionnelle, documentée et déployée.

---

# 2. Structure générale du projet

Structure simplifiée du projet :

```text
frostia-games/
├── frostia_config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/
│   ├── services/
│   │   └── nosql_notes.py
│   ├── urls.py
│   ├── views.py
│   ├── apps.py
│   └── tests.py
│
├── creations/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── playable/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── scripts/
│   ├── __init__.py
│   └── demo_tinydb_notes.py
│
├── data/
│   └── nosql/
│       └── project_notes_db.json
│
├── templates/
│   ├── base.html
│   ├── pages/
│   │   ├── home.html
│   │   ├── creation.html
│   │   └── projet_jouable.html
│   └── partials/
│
├── static/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── menu.js
│   └── images/
│
├── staticfiles/
│
├── doc/
│   ├── sql/
│   │   ├── schema.sql
│   │   └── nosql.md
│   ├── 00-index-documentation.md
│   ├── 01-modernisation-interface.md
│   ├── 02-journal-de-bord.md
│   ├── 03-modelisation-backend.md
│   ├── 04-docker-et-lancement.md
│   ├── 05-securite-backend.md
│   ├── 06-manuel-utilisateur.md
│   ├── 07-base-de-donnees.md
│   ├── 08-changelog.md
│   ├── 09-deploiement-render.md
│   ├── 10-bilan-v1-frostia-games.md
│   ├── 11-installation-locale.md
│   ├── 12-architecture.md
│   ├── 13-test-et-vérification.md
│   ├── 14-Capture-et Preuve.md
│   ├── 15-limites-et-évolutions.md
│   ├── 16-presentation-projet-2.md
│   ├── 17-pistes-explorees-et-non-retenues.md
│   ├── 18-plan-finalisation-v1.md
│   └── 19-renforcement-dossier-projet.md
│
├── docs/
│   ├── backend/
│   │   ├── modeles-django.md
│   │   └── vues-et-routes.md
│   ├── conception/
│   │   ├── cas-utilisation.md
│   │   ├── diagramme-sequence.md
│   │   └── mcd.md
│   ├── frontend/
│   │   └── javascript-menu-mobile.md
│   ├── nosql/
│   │   └── tinydb-integration.md
│   ├── preuves/
│   └── sql/
│       ├── create_tables_creations.sql
│       ├── create_tables_playable.sql
│       ├── exemples_insert.sql
│       └── sql-natif.md
│
├── .dockerignore
├── .env.example
├── .gitignore
├── build.sh
├── CHOIX_TECHNIQUES.md
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

# 3. Rôle des dossiers principaux

## `frostia_config`

Le dossier `frostia_config` contient la configuration principale du projet Django.

Il représente le cœur technique du projet.

### Fichiers importants

| Fichier       | Rôle                                                          |
| ------------- | ------------------------------------------------------------- |
| `settings.py` | Configuration générale du projet                              |
| `urls.py`     | Déclaration des routes principales                            |
| `wsgi.py`     | Point d'entrée pour le déploiement avec Gunicorn              |
| `asgi.py`     | Point d'entrée ASGI, utile pour certains déploiements avancés |

---

# 4. `settings.py`

Le fichier `settings.py` contient la configuration principale du projet.

Il gère notamment :

* les applications installées ;
* les middlewares ;
* la base de données ;
* les fichiers statiques ;
* les templates ;
* les hôtes autorisés ;
* le mode debug ;
* la clé secrète Django ;
* la configuration liée à Render ;
* la configuration liée aux fichiers statiques.

Les applications internes du projet sont notamment :

```python
"core",
"creations",
"playable",
```

Ces applications séparent les responsabilités du projet.

Les données TinyDB ne sont pas gérées par une application Django dédiée.

Elles sont gérées par un service Python placé dans `core/services/`.

---

# 5. `urls.py`

Le fichier `urls.py` définit les routes principales du projet.

Il permet de connecter les URL du site aux vues Django.

Il contient également l'accès à l'administration Django via :

```text
/admin/
```

Fonctionnement simplifié :

```text
URL demandée par le visiteur
        ↓
frostia_config/urls.py
        ↓
core/urls.py
        ↓
vue Django
        ↓
template HTML
        ↓
page affichée
```

---

# 6. `wsgi.py`

Le fichier `wsgi.py` sert de point d'entrée pour lancer le projet Django en production.

Render utilise Gunicorn avec cette commande :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande indique à Gunicorn d'utiliser l'application Django définie dans `frostia_config.wsgi`.

---

# 7. Application `core`

L'application `core` gère les pages principales du site.

Elle contient principalement les vues et les routes publiques du portfolio.

Elle contient aussi le service utilisé pour l'expérimentation NoSQL TinyDB.

## Rôle de `core`

L'application `core` sert à organiser :

* la page d'accueil ;
* la page Mes créations ;
* la page Projets jouables ;
* les routes publiques ;
* les vues qui récupèrent les données nécessaires aux templates ;
* la récupération des notes TinyDB sur l'accueil.

## Fichiers importants

| Fichier                         | Rôle                                         |
| ------------------------------- | -------------------------------------------- |
| `core/views.py`                 | Contient les vues des pages principales      |
| `core/urls.py`                  | Contient les routes publiques du site        |
| `core/apps.py`                  | Configuration de l'application               |
| `core/tests.py`                 | Fichier prévu pour les tests                 |
| `core/services/nosql_notes.py`  | Service Python lié à TinyDB                  |

---

# 8. `core/views.py`

Le fichier `core/views.py` contient les vues Django.

Une vue reçoit une requête HTTP et retourne une réponse, souvent une page HTML.

Les vues permettent notamment :

* d'afficher la page d'accueil ;
* d'afficher la page Mes créations ;
* d'afficher la page Projets jouables ;
* de récupérer certaines données depuis les modèles Django ;
* de récupérer les notes TinyDB ;
* d'envoyer ces données aux templates.

Exemple de fonctionnement :

```text
Requête visiteur
   ↓
Vue Django
   ↓
Récupération éventuelle de données SQLite
   ↓
Récupération éventuelle de notes TinyDB
   ↓
Template HTML
   ↓
Réponse envoyée au navigateur
```

---

# 9. `core/urls.py`

Le fichier `core/urls.py` contient les routes publiques du site.

Il permet de relier les adresses du site aux vues.

Pages principales :

```text
/
/mes-creations/
/projets-jouables/
```

Ces routes permettent d'accéder aux trois pages principales de la V1.

---

# 10. Service NoSQL `nosql_notes.py`

Le fichier suivant gère l'expérimentation NoSQL :

```text
core/services/nosql_notes.py
```

Ce service permet :

* de définir l'emplacement de la base TinyDB ;
* de créer le dossier `data/nosql/` si nécessaire ;
* d'ouvrir la base TinyDB ;
* de créer des notes de démonstration ;
* de lister les notes ;
* de rechercher les notes liées à un projet ;
* de fermer la base proprement.

TinyDB est utilisé pour stocker des notes de progression dans un fichier JSON.

Fichier de données :

```text
data/nosql/project_notes_db.json
```

TinyDB ne remplace pas SQLite.

Il sert uniquement de complément documentaire pour démontrer une logique NoSQL légère.

---

# 11. Application `creations`

L'application `creations` gère les créations affichées dans la page **Mes créations**.

Elle contient un modèle Django réel utilisé dans la V1.

## Rôle de `creations`

L'application `creations` sert à stocker et administrer les projets ou créations du portfolio.

Elle permet de ne pas écrire toutes les données directement dans les templates HTML.

Le contenu peut être ajouté ou modifié depuis l'administration Django.

## Fichiers importants

| Fichier                 | Rôle                                                  |
| ----------------------- | ----------------------------------------------------- |
| `creations/models.py`   | Contient le modèle `Creation`                         |
| `creations/admin.py`    | Configure l'affichage du modèle dans l'administration |
| `creations/apps.py`     | Configuration de l'application                        |
| `creations/migrations/` | Contient les migrations de base de données            |
| `creations/tests.py`    | Fichier prévu pour les tests                          |

---

# 12. Modèle `Creation`

Le modèle `Creation` représente une création ou un projet présenté dans le portfolio.

Il contient notamment :

* un titre ;
* un slug ;
* une lettre alphabétique ;
* un nom de code ;
* un type de projet ;
* un statut ;
* une description courte ;
* un champ de visibilité ;
* des dates de création et de modification.

Ce modèle permet d'afficher dynamiquement certaines créations dans la page **Mes créations**.

---

# 13. Administration de `Creation`

Le fichier `creations/admin.py` permet d'afficher le modèle `Creation` dans l'administration Django.

L'administration permet notamment :

* d'ajouter une création ;
* de modifier une création ;
* de masquer une création ;
* de rendre une création visible ;
* de gérer les données sans modifier directement le HTML.

Le compte temporaire de lecture seule peut uniquement consulter ce modèle si la permission de lecture est accordée.

---

# 14. Application `playable`

L'application `playable` gère les futurs projets jouables ou contenus prévus dans la page **Projets jouables**.

Elle contient un modèle Django réel utilisé dans la V1.

## Rôle de `playable`

L'application `playable` sert à représenter des contenus futurs :

* prototype ;
* teaser ;
* vidéo ;
* démonstration prévue ;
* projet jouable à venir.

Dans la V1, aucun vrai upload serveur ni vrai jeu jouable dans le navigateur n'est implanté.

L'application permet simplement de préparer la structure future tout en gardant le projet stable.

## Fichiers importants

| Fichier                | Rôle                                                  |
| ---------------------- | ----------------------------------------------------- |
| `playable/models.py`   | Contient le modèle `PlayableProject`                  |
| `playable/admin.py`    | Configure l'affichage du modèle dans l'administration |
| `playable/apps.py`     | Configuration de l'application                        |
| `playable/migrations/` | Contient les migrations de base de données            |
| `playable/tests.py`    | Fichier prévu pour les tests                          |

---

# 15. Modèle `PlayableProject`

Le modèle `PlayableProject` représente un futur contenu jouable ou une démonstration prévue.

Il contient notamment :

* un titre ;
* un slug ;
* un statut ;
* un type de contenu prévu ;
* une description courte ;
* un message de disponibilité ;
* un état de disponibilité ;
* un champ de visibilité ;
* des dates de création et de modification.

Ce modèle permet d'afficher des informations sur les futurs contenus jouables sans annoncer une fonctionnalité qui n'est pas encore disponible.

---

# 16. Administration de `PlayableProject`

Le fichier `playable/admin.py` permet d'afficher le modèle `PlayableProject` dans l'administration Django.

L'administration permet notamment :

* d'ajouter un futur projet jouable ;
* de modifier son statut ;
* de modifier son message de disponibilité ;
* de masquer ou afficher l'entrée sur le site.

Le compte temporaire de lecture seule peut uniquement consulter ce modèle si la permission de lecture est accordée.

---

# 17. Templates Django

Le dossier `templates` contient les fichiers HTML utilisés par Django.

Il permet de séparer la structure des pages du code Python.

Structure utilisée :

```text
templates/
├── base.html
├── pages/
│   ├── home.html
│   ├── creation.html
│   └── projet_jouable.html
└── partials/
```

---

# 18. `base.html`

Le fichier `base.html` sert de modèle principal.

Il contient les éléments communs à toutes les pages :

* structure HTML globale ;
* chargement du CSS ;
* navigation ;
* sidebar ;
* footer ;
* zones réutilisables ;
* chargement du JavaScript ;
* structure générale du site.

Les autres pages héritent de ce fichier afin d'éviter de répéter le même code HTML.

Principe :

```text
base.html
   ↑
pages/home.html
pages/creation.html
pages/projet_jouable.html
```

Le fichier `base.html` charge aussi le script :

```text
static/js/menu.js
```

---

# 19. `templates/pages`

Le dossier `pages` contient les pages principales du site.

| Page                  | Rôle                                      |
| --------------------- | ----------------------------------------- |
| `home.html`           | Page d'accueil du portfolio               |
| `creation.html`       | Page Mes créations                        |
| `projet_jouable.html` | Page Projets jouables                     |

Ces pages représentent le contenu visible par les visiteurs.

La page `home.html` affiche également les notes de progression issues de TinyDB.

---

# 20. `templates/partials`

Le dossier `partials` est prévu pour contenir des morceaux de templates réutilisables.

Exemples possibles :

```text
header.html
footer.html
sidebar.html
project-card.html
```

Dans une évolution future, cela permettra de mieux organiser l'interface et d'éviter les répétitions dans les templates.

---

# 21. Fichiers statiques

Le dossier `static` contient les fichiers utilisés côté navigateur.

Structure :

```text
static/
├── css/
│   └── main.css
├── images/
└── js/
    └── menu.js
```

---

# 22. `static/css/main.css`

Le fichier `main.css` contient le style principal du site.

Il gère notamment :

* la mise en page ;
* les couleurs ;
* les cartes ;
* les sections ;
* la navigation ;
* la sidebar ;
* le responsive ;
* l'apparence générale du portfolio.

Pour la V1, le style est volontairement centralisé afin de faciliter les modifications rapides.

---

# 23. `static/js/menu.js`

Le fichier `menu.js` contient le JavaScript lié au comportement du menu mobile.

Il sert notamment à :

* détecter le bouton de menu ;
* détecter la sidebar ;
* ouvrir ou fermer le menu ;
* mettre à jour l'attribut `aria-expanded` ;
* fermer le menu après un clic sur un lien.

Le JavaScript reste limité afin de garder un projet simple et maintenable.

Il est documenté dans :

```text
docs/frontend/javascript-menu-mobile.md
```

---

# 24. `static/images`

Le dossier `images` est prévu pour stocker les images du site.

Il peut contenir :

* logo temporaire ;
* captures de projets ;
* illustrations ;
* images de présentation ;
* visuels liés aux futures créations.

---

# 25. Dossier `staticfiles`

Le dossier `staticfiles` est généré par Django lors de la commande :

```bash
python manage.py collectstatic --noinput
```

Il regroupe les fichiers statiques collectés pour la production.

Ce dossier est utilisé lors du déploiement afin que les fichiers CSS, JavaScript et images soient accessibles correctement.

Il ne doit pas être modifié manuellement.

Il peut être ignoré par Git, car il est généré automatiquement.

---

# 26. Base de données SQLite

Pour la V1, le projet utilise SQLite comme base principale.

Fichier utilisé :

```text
db.sqlite3
```

SQLite est suffisant pour cette première version, car le projet sert principalement de portfolio de présentation.

La base contient actuellement les données liées :

* aux créations ;
* aux futurs projets jouables ;
* aux tables internes de Django ;
* à l'administration Django ;
* aux utilisateurs et permissions Django.

---

# 27. Tables principales

Les deux tables principales liées au projet sont :

```text
creations_creation
playable_playableproject
```

La table `creations_creation` correspond au modèle `Creation`.

La table `playable_playableproject` correspond au modèle `PlayableProject`.

Dans la V1, ces deux modèles sont indépendants.

Une future version pourra ajouter des relations entre créations, médias, versions et projets jouables.

---

# 28. Limite de SQLite

SQLite est adapté à une V1 simple.

Il n'est pas idéal pour une version plus avancée avec beaucoup de données, plusieurs utilisateurs ou une production durable.

Pour une version future, une migration vers PostgreSQL pourra être envisagée.

Ce choix est reporté afin de conserver une V1 simple et maîtrisable.

---

# 29. Base NoSQL TinyDB

Le projet contient également une expérimentation NoSQL légère avec TinyDB.

Fichier de données :

```text
data/nosql/project_notes_db.json
```

Fichiers Python concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
```

TinyDB sert à stocker des notes de progression sous forme de documents JSON.

Exemple logique :

```json
{
  "project_code": "frostia-games",
  "title": "Renforcement du dossier projet",
  "status": "in_progress",
  "tags": ["dossier-projet", "conception", "sql", "nosql"]
}
```

TinyDB ne remplace pas SQLite.

SQLite reste la base principale du projet.

TinyDB sert uniquement de preuve NoSQL légère dans le cadre de la V1 renforcée.

---

# 30. Fonctionnement TinyDB

La chaîne technique TinyDB est la suivante :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

Commande de test :

```powershell
python -m scripts.demo_tinydb_notes
```

Cette commande affiche les notes de progression dans le terminal.

Elle permet de vérifier que TinyDB fonctionne.

---

# 31. Administration Django

Le projet utilise l'administration intégrée de Django.

Adresse locale :

```text
https://frostia-games.onrender.com/admin/
```

Adresse en ligne :

```text
https://frostia-games.onrender.com/admin/
```

L'administration permet de gérer les contenus dynamiques du site.

Elle permet notamment :

* d'ajouter une création ;
* de modifier une création ;
* de masquer une création ;
* d'ajouter un futur projet jouable ;
* de modifier un projet jouable ;
* de contrôler ce qui est visible sur le site.

Pour des raisons de sécurité, les identifiants administrateur ne sont pas publiés dans GitHub ni dans la documentation.

---

# 32. Compte temporaire de lecture seule

Un compte temporaire de lecture seule a été ajouté pour permettre une consultation limitée de l'administration Django.

Ce compte :

* est actif ;
* peut accéder à l'administration ;
* n'est pas superutilisateur ;
* appartient à un groupe de lecture seule ;
* peut consulter les créations ;
* peut consulter les projets jouables ;
* ne doit pas modifier les données ;
* ne doit pas accéder aux utilisateurs, groupes ou permissions sensibles.

Les identifiants réels de ce compte ne doivent pas être écrits dans la documentation publique.

Ils peuvent être transmis séparément uniquement si nécessaire.

---

# 33. Documentation du projet

Le dossier `doc` contient la documentation technique, fonctionnelle et organisationnelle du projet.

Il contient notamment :

* l'index de documentation ;
* la modernisation de l'interface ;
* le journal de bord ;
* la modélisation backend ;
* Docker et lancement ;
* la sécurité backend ;
* le manuel utilisateur ;
* la base de données ;
* le changelog ;
* le déploiement Render ;
* le bilan V1 ;
* l'installation locale ;
* l'architecture ;
* les tests et vérifications ;
* les captures et preuves ;
* les limites et évolutions ;
* la présentation du projet 2 ;
* les pistes explorées et non retenues ;
* le plan de finalisation V1 ;
* le renforcement du dossier projet.

Le dossier `doc/sql` contient :

* `schema.sql` ;
* `nosql.md`.

Le fichier `schema.sql` sert à documenter la structure SQL de la base.

Le fichier `nosql.md` explique la réflexion NoSQL initiale et les usages possibles.

---

# 34. Documentation complémentaire `docs/`

Le dossier `docs/` contient les documents techniques ajoutés lors du renforcement du dossier projet.

Structure :

```text
docs/
├── backend/
├── conception/
├── frontend/
├── nosql/
├── preuves/
└── sql/
```

## `docs/backend/`

Contient :

```text
modeles-django.md
vues-et-routes.md
```

Ces fichiers expliquent les modèles, les vues et les routes.

## `docs/conception/`

Contient :

```text
mcd.md
cas-utilisation.md
diagramme-sequence.md
```

Ces fichiers renforcent la partie conception.

## `docs/frontend/`

Contient :

```text
javascript-menu-mobile.md
```

Ce fichier documente le JavaScript du menu mobile.

## `docs/nosql/`

Contient :

```text
tinydb-integration.md
```

Ce fichier explique l'intégration TinyDB.

## `docs/sql/`

Contient :

```text
create_tables_creations.sql
create_tables_playable.sql
exemples_insert.sql
sql-natif.md
```

Ces fichiers documentent le SQL natif.

---

# 35. Fichiers importants à la racine

## `README.md`

Le fichier `README.md` présente rapidement le projet.

Il explique notamment :

* le rôle du projet ;
* les technologies utilisées ;
* l'installation locale ;
* le lancement Docker ;
* le déploiement Render ;
* les limites de la V1 ;
* les évolutions prévues.

Il sert de point d'entrée pour une personne qui découvre le dépôt GitHub.

---

## `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` explique les choix techniques du projet.

Il présente notamment :

* pourquoi Django a été retenu ;
* pourquoi C# / ASP.NET / Razor a été envisagé mais reporté ;
* pourquoi PostgreSQL est reporté ;
* pourquoi TinyDB est utilisé de manière limitée ;
* pourquoi certaines fonctionnalités sont volontairement limitées.

Ce fichier permet de montrer que les choix techniques sont réfléchis.

---

## `.env.example`

Le fichier `.env.example` documente les variables d'environnement nécessaires sans exposer les vraies valeurs sensibles.

Exemple :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Les vraies valeurs sont placées dans l'environnement local ou dans Render.

Elles ne doivent pas être publiées dans GitHub.

---

## `.gitignore`

Le fichier `.gitignore` permet d'éviter d'envoyer dans GitHub des fichiers inutiles ou sensibles.

Il peut ignorer notamment :

* `.venv/` ;
* `__pycache__/` ;
* `*.pyc` ;
* `db.sqlite3` ;
* `staticfiles/` ;
* `media/` ;
* `.env` ;
* `.env.local`.

Ce fichier participe à la sécurité du projet.

Le fichier TinyDB peut être conservé uniquement s'il contient des données de démonstration non sensibles.

---

## `requirements.txt`

Le fichier `requirements.txt` contient les dépendances Python du projet.

Dépendances importantes :

```text
Django
gunicorn
whitenoise
tinydb
```

| Dépendance | Rôle                                         |
| ---------- | -------------------------------------------- |
| Django     | Framework web principal                      |
| gunicorn   | Serveur utilisé pour Render                  |
| whitenoise | Gestion des fichiers statiques en production |
| tinydb     | Expérimentation NoSQL légère                 |

---

## `build.sh`

Le fichier `build.sh` est utilisé par Render pour préparer le projet avant le lancement.

Contenu :

```bash
#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true
```

Ce script permet :

1. d'installer les dépendances ;
2. de collecter les fichiers statiques ;
3. d'appliquer les migrations ;
4. de créer un compte administrateur si les variables d'environnement sont présentes.

---

## `Dockerfile` et `docker-compose.yml`

Le projet contient également des fichiers Docker.

Ils permettent de lancer le projet dans un environnement conteneurisé.

Dans la V1, Docker sert surtout à :

* reproduire l'environnement local ;
* tester le projet ;
* documenter une procédure de lancement ;
* montrer que le projet peut fonctionner dans un environnement isolé.

Le déploiement principal est effectué avec Render, pas avec Docker.

---

## `pyproject.toml`

Le fichier `pyproject.toml` peut contenir des informations de configuration Python.

Il peut être utilisé par certains outils modernes liés à Python, au formatage ou à la gestion du projet.

---

# 36. Fonctionnement général du site

Le fonctionnement général du site suit le cycle classique d'une application Django.

```text
Visiteur
   ↓
URL demandée
   ↓
frostia_config/urls.py
   ↓
core/urls.py
   ↓
core/views.py
   ↓
modèles Django si nécessaire
   ↓
base SQLite si nécessaire
   ↓
service TinyDB si nécessaire
   ↓
templates/pages/*.html
   ↓
base.html
   ↓
CSS / JS / images
   ↓
Page affichée dans le navigateur
```

---

# 37. Exemple de parcours utilisateur

Un visiteur arrive sur la page d'accueil :

```text
https://frostia-games.onrender.com
```

Django reçoit la requête.

La route correspondante est trouvée dans `urls.py`.

La vue associée dans `core/views.py` est exécutée.

La vue peut récupérer les notes TinyDB.

Django charge le template correspondant.

La page HTML est envoyée au navigateur.

Le navigateur charge ensuite les fichiers statiques :

```text
main.css
menu.js
images
```

La page complète s'affiche à l'utilisateur.

---

# 38. Parcours avec données SQLite

Pour la page **Mes créations**, le fonctionnement est le suivant :

```text
Visiteur
   ↓
/mes-creations/
   ↓
core/urls.py
   ↓
core/views.py
   ↓
Creation.objects.filter(is_visible=True)
   ↓
Base SQLite
   ↓
templates/pages/creation.html
   ↓
Page affichée
```

Pour la page **Projets jouables**, le principe est similaire :

```text
Visiteur
   ↓
/projets-jouables/
   ↓
core/urls.py
   ↓
core/views.py
   ↓
PlayableProject.objects.filter(is_visible=True)
   ↓
Base SQLite
   ↓
templates/pages/projet_jouable.html
   ↓
Page affichée
```

Cela montre que le site n'est pas uniquement statique.

---

# 39. Parcours avec données TinyDB

Pour la page d'accueil, le fonctionnement TinyDB est le suivant :

```text
Visiteur
   ↓
/
   ↓
core/urls.py
   ↓
core/views.py
   ↓
seed_project_notes()
   ↓
find_notes_by_project("frostia-games")
   ↓
data/nosql/project_notes_db.json
   ↓
templates/pages/home.html
   ↓
Notes affichées sur l'accueil
```

Cette partie démontre une logique NoSQL simple.

Elle reste volontairement limitée.

---

# 40. Architecture front-end

La partie front-end repose sur :

* HTML avec les templates Django ;
* CSS dans `main.css` ;
* JavaScript léger dans `menu.js`.

Cette approche permet de garder un projet simple, sans framework JavaScript lourd.

Le choix est adapté à une V1 de portfolio, car le site n'a pas encore besoin d'une interface très interactive ou d'une logique front-end complexe.

La modernisation graphique avancée est reportée à une version future.

---

# 41. Architecture back-end

La partie back-end repose sur Django.

Django gère :

* le routage ;
* les vues ;
* les modèles ;
* les migrations ;
* l'administration ;
* la base de données ;
* les fichiers statiques ;
* la configuration de production.

Le backend reste volontairement simple dans cette V1.

L'objectif n'est pas encore de créer une plateforme complète, mais une base stable et extensible.

TinyDB est ajouté comme service complémentaire, sans transformer l'architecture principale.

---

# 42. Architecture de déploiement

Le projet est déployé avec Render.

Fonctionnement :

```text
GitHub
   ↓
Render
   ↓
Build Command : bash build.sh
   ↓
Installation des dépendances
   ↓
Collecte des fichiers statiques
   ↓
Migrations Django
   ↓
Création éventuelle du superutilisateur
   ↓
Start Command : gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
   ↓
Site accessible en ligne
```

URL de production :

```text
https://frostia-games.onrender.com
```

---

# 43. Docker dans l'architecture

Docker est présent dans le projet, mais il n'est pas utilisé comme mode de production principal.

Son rôle est de fournir un environnement de lancement reproductible.

Commande principale :

```powershell
docker compose up --build
```

Le site est ensuite accessible localement :

```text
https://frostia-games.onrender.com/
```

Tests utiles dans Docker :

```powershell
docker compose exec web python manage.py check
docker compose exec web python -m scripts.demo_tinydb_notes
```

Docker permet de montrer que le projet peut être lancé dans un environnement isolé.

La documentation Docker est détaillée dans le fichier :

```text
04-docker-et-lancement.md
```

---

# 44. Sécurité dans l'architecture

Pour cette V1, plusieurs règles de sécurité sont appliquées :

* la clé secrète Django est stockée dans Render ;
* les mots de passe ne sont pas publiés ;
* les identifiants administrateur ne sont pas présents dans GitHub ;
* les identifiants du compte temporaire ne sont pas écrits dans la documentation publique ;
* le mode debug est désactivé sur Render ;
* les variables sensibles sont placées dans les variables d'environnement ;
* l'accès admin reste privé ;
* un compte lecture seule limite les droits de consultation ;
* l'ORM Django est utilisé au lieu de SQL brut dans les vues ;
* TinyDB ne doit contenir aucune donnée sensible ;
* aucun vrai upload serveur n'est implanté dans la V1 ;
* `.env.example` documente les variables sans exposer les vraies valeurs.

Cette sécurité est cohérente avec le périmètre d'une V1.

Elle pourra être renforcée dans une version future.

---

# 45. Choix d'architecture

Le projet utilise une architecture simple pour plusieurs raisons :

* éviter une complexité inutile ;
* garder le projet maintenable ;
* faciliter le déploiement ;
* permettre une documentation claire ;
* pouvoir évoluer progressivement ;
* éviter le scope creep ;
* produire une V1 stable ;
* ne pas transformer le projet en usine à gaz.

Le choix a été fait de ne pas intégrer immédiatement :

* PostgreSQL ;
* une interface d'administration personnalisée ;
* un vrai upload serveur ;
* un jeu jouable dans le navigateur ;
* un tableau de bord avancé ;
* une API REST ;
* un espace privé complet ;
* une base NoSQL avancée comme MongoDB.

Ces éléments sont reportés volontairement.

Certains éléments ont été ajoutés de manière limitée et contrôlée :

* compte temporaire de lecture seule ;
* TinyDB ;
* SQL natif documentaire ;
* documentation frontend et backend complémentaire.

---

# 46. Limites actuelles

L'architecture actuelle présente plusieurs limites :

* la base de données reste en SQLite ;
* TinyDB reste une expérimentation légère ;
* l'administration Django n'est pas personnalisée ;
* les fiches projet détaillées ne sont pas encore intégrées ;
* les médias ne sont pas encore gérés dynamiquement ;
* il n'existe pas encore de table de versions ;
* la partie responsive peut encore être améliorée ;
* le site ne propose pas encore de projet jouable directement dans le navigateur ;
* aucun vrai upload serveur n'est implanté ;
* les tests automatisés complets ne sont pas encore présents ;
* le compte lecture seule n'est pas un système de rôles avancé complet.

Ces limites sont acceptées dans le cadre de la V1.

Elles sont documentées afin de distinguer ce qui est réalisé de ce qui est prévu plus tard.

---

# 47. Évolutions possibles

L'architecture actuelle permet plusieurs évolutions :

* migration vers PostgreSQL ;
* ajout d'une table de fiches détaillées ;
* ajout d'une table de médias ;
* ajout d'une table de versions ;
* relation entre une création et un projet jouable ;
* amélioration du responsive ;
* ajout de graphiques avec Plotly.js ;
* intégration future de démos jouables ;
* création d'un espace privé ;
* amélioration de la gestion des médias ;
* ajout de tests automatisés ;
* ajout d'un système de sauvegarde automatique ;
* ajout d'un système de restauration des contenus ;
* étude d'une base NoSQL plus avancée si les contenus deviennent très variables.

Ces évolutions pourront être ajoutées progressivement si le projet devient un second projet validé ou une base plus avancée.

---

# 48. Captures et preuves utiles

Pour justifier l'architecture dans le dossier projet, plusieurs preuves peuvent être préparées :

* structure du projet dans VS Code ;
* fichier `settings.py` ;
* fichier `urls.py` ;
* fichier `core/views.py` ;
* modèles `Creation` et `PlayableProject` ;
* fichiers `admin.py` ;
* fichier `static/js/menu.js` ;
* fichier `core/services/nosql_notes.py` ;
* script `scripts/demo_tinydb_notes.py` ;
* fichier `requirements.txt` ;
* fichiers SQL natifs ;
* documentation de conception ;
* page d'accueil avec notes TinyDB ;
* administration Django ;
* compte temporaire de lecture seule ;
* terminal avec `python manage.py check` ;
* terminal avec `python -m scripts.demo_tinydb_notes`.

Aucune capture ne doit afficher :

* mot de passe ;
* clé secrète ;
* vraie variable d'environnement ;
* identifiant sensible ;
* information privée inutile.

---

# 49. Bilan

L'architecture actuelle de Frostia Games est simple, claire et adaptée à une V1.

Elle permet :

* d'afficher un site public ;
* d'utiliser Django proprement ;
* de gérer des templates ;
* de charger des fichiers statiques ;
* d'utiliser une base SQLite ;
* d'afficher des données dynamiques ;
* d'utiliser TinyDB comme expérimentation NoSQL légère ;
* d'afficher des notes de progression sur l'accueil ;
* d'accéder à l'administration Django ;
* de proposer un compte temporaire de lecture seule ;
* de lancer le projet localement ;
* de lancer le projet avec Docker ;
* de déployer le projet sur Render ;
* de documenter facilement le fonctionnement du projet ;
* de préparer des évolutions futures sans repartir de zéro.

Cette architecture correspond à l'objectif actuel : obtenir une base stable, déployée, documentée, renforcée et défendable.

À ce stade, la priorité n'est plus d'élargir l'architecture, mais de finaliser les captures, les preuves et le dossier projet final.


