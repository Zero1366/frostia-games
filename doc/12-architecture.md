# Architecture du projet - Frostia Games

## Objectif du document

Ce document présente l'architecture du projet **Frostia Games**.

L'objectif est d'expliquer comment le projet est organisé, quel est le rôle des principaux dossiers et fichiers, et comment les différentes parties du site fonctionnent ensemble.

Le projet est une application web développée avec **Django**.

Il sert de portfolio pour présenter des projets de jeux vidéo actuels ou futurs, avec une interface publique simple, une base SQLite, une administration Django, une documentation technique et un déploiement en ligne sur Render.

---

## Vue d'ensemble du projet

Frostia Games est organisé autour d'une architecture Django simple et volontairement limitée.

Le projet contient :

* une configuration Django principale ;
* une application dédiée aux pages principales ;
* une application dédiée aux créations ;
* une application dédiée aux futurs projets jouables ;
* des templates HTML ;
* des fichiers statiques CSS, JavaScript et images ;
* une base de données SQLite pour la V1 ;
* une administration Django ;
* des fichiers Docker ;
* des fichiers de déploiement Render ;
* une documentation technique complète.

Cette structure permet de garder un projet lisible, maintenable et évolutif.

L'objectif de la V1 n'est pas de créer une plateforme complète, mais de produire une base stable, fonctionnelle, documentée et déployée.

---

## Structure générale du projet

Structure simplifiée du projet :

```txt
frostia-games/
├── frostia_config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/
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
│   └── 18-plan-finalisation-v1.md
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

## Rôle des dossiers principaux

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

## `settings.py`

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

---

## `urls.py`

Le fichier `urls.py` définit les routes principales du projet.

Il permet de connecter les URL du site aux vues Django.

Il contient également l'accès à l'administration Django via :

```txt
/admin/
```

Fonctionnement simplifié :

```txt
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

## `wsgi.py`

Le fichier `wsgi.py` sert de point d'entrée pour lancer le projet Django en production.

Render utilise Gunicorn avec cette commande :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande indique à Gunicorn d'utiliser l'application Django définie dans `frostia_config.wsgi`.

---

# Application `core`

L'application `core` gère les pages principales du site.

Elle contient principalement les vues et les routes publiques du portfolio.

## Rôle de `core`

L'application `core` sert à organiser :

* la page d'accueil ;
* la page Mes créations ;
* la page Projets jouables ;
* les routes publiques ;
* les vues qui récupèrent les données nécessaires aux templates.

## Fichiers importants

| Fichier         | Rôle                                    |
| --------------- | --------------------------------------- |
| `core/views.py` | Contient les vues des pages principales |
| `core/urls.py`  | Contient les routes publiques du site   |
| `core/apps.py`  | Configuration de l'application          |
| `core/tests.py` | Fichier prévu pour les tests            |

---

## `core/views.py`

Le fichier `core/views.py` contient les vues Django.

Une vue reçoit une requête HTTP et retourne une réponse, souvent une page HTML.

Les vues permettent notamment :

* d'afficher la page d'accueil ;
* d'afficher la page Mes créations ;
* d'afficher la page Projets jouables ;
* de récupérer certaines données depuis les modèles Django ;
* d'envoyer ces données aux templates.

Exemple de fonctionnement :

```txt
Requête visiteur
   ↓
Vue Django
   ↓
Récupération éventuelle de données
   ↓
Template HTML
   ↓
Réponse envoyée au navigateur
```

---

## `core/urls.py`

Le fichier `core/urls.py` contient les routes publiques du site.

Il permet de relier les adresses du site aux vues.

Pages principales :

```txt
/
 /mes-creations/
 /projets-jouables/
```

Ces routes permettent d'accéder aux trois pages principales de la V1.

---

# Application `creations`

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

## Modèle `Creation`

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

## Administration de `Creation`

Le fichier `creations/admin.py` permet d'afficher le modèle `Creation` dans l'administration Django.

L'administration permet notamment :

* d'ajouter une création ;
* de modifier une création ;
* de masquer une création ;
* de rendre une création visible ;
* de gérer les données sans modifier directement le HTML.

---

# Application `playable`

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

## Modèle `PlayableProject`

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

## Administration de `PlayableProject`

Le fichier `playable/admin.py` permet d'afficher le modèle `PlayableProject` dans l'administration Django.

L'administration permet notamment :

* d'ajouter un futur projet jouable ;
* de modifier son statut ;
* de modifier son message de disponibilité ;
* de masquer ou afficher l'entrée sur le site.

---

# Templates Django

Le dossier `templates` contient les fichiers HTML utilisés par Django.

Il permet de séparer la structure des pages du code Python.

Structure utilisée :

```txt
templates/
├── base.html
├── pages/
│   ├── home.html
│   ├── creation.html
│   └── projet_jouable.html
└── partials/
```

---

## `base.html`

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

```txt
base.html
   ↑
pages/home.html
pages/creation.html
pages/projet_jouable.html
```

---

## `templates/pages`

Le dossier `pages` contient les pages principales du site.

| Page                  | Rôle                        |
| --------------------- | --------------------------- |
| `home.html`           | Page d'accueil du portfolio |
| `creation.html`       | Page Mes créations          |
| `projet_jouable.html` | Page Projets jouables       |

Ces pages représentent le contenu visible par les visiteurs.

---

## `templates/partials`

Le dossier `partials` est prévu pour contenir des morceaux de templates réutilisables.

Exemples possibles :

```txt
header.html
footer.html
sidebar.html
project-card.html
```

Dans une évolution future, cela permettra de mieux organiser l'interface et d'éviter les répétitions dans les templates.

---

# Fichiers statiques

Le dossier `static` contient les fichiers utilisés côté navigateur.

Structure :

```txt
static/
├── css/
│   └── main.css
├── images/
└── js/
    └── menu.js
```

---

## `static/css/main.css`

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

## `static/js/menu.js`

Le fichier `menu.js` contient le JavaScript lié au comportement du menu.

Il sert notamment à gérer le menu mobile.

Le JavaScript reste limité afin de garder un projet simple et maintenable.

---

## `static/images`

Le dossier `images` est prévu pour stocker les images du site.

Il peut contenir :

* logo temporaire ;
* captures de projets ;
* illustrations ;
* images de présentation ;
* visuels liés aux futures créations.

---

# Dossier `staticfiles`

Le dossier `staticfiles` est généré par Django lors de la commande :

```bash
python manage.py collectstatic --noinput
```

Il regroupe les fichiers statiques collectés pour la production.

Ce dossier est utilisé lors du déploiement afin que les fichiers CSS, JavaScript et images soient accessibles correctement.

Il ne doit pas être modifié manuellement.

Il peut être ignoré par Git, car il est généré automatiquement.

---

# Base de données

Pour la V1, le projet utilise SQLite.

Fichier utilisé :

```txt
db.sqlite3
```

SQLite est suffisant pour cette première version, car le projet sert principalement de portfolio de présentation.

La base contient actuellement les données liées :

* aux créations ;
* aux futurs projets jouables ;
* aux tables internes de Django ;
* à l'administration Django.

---

## Tables principales

Les deux tables principales liées au projet sont :

```txt
creations_creation
playable_playableproject
```

La table `creations_creation` correspond au modèle `Creation`.

La table `playable_playableproject` correspond au modèle `PlayableProject`.

Dans la V1, ces deux modèles sont indépendants.

Une future version pourra ajouter des relations entre créations, médias, versions et projets jouables.

---

## Limite de SQLite

SQLite est adapté à une V1 simple.

Il n'est pas idéal pour une version plus avancée avec beaucoup de données, plusieurs utilisateurs ou une production durable.

Pour une version future, une migration vers PostgreSQL pourra être envisagée.

Ce choix est reporté afin de conserver une V1 simple et maîtrisable.

---

# Administration Django

Le projet utilise l'administration intégrée de Django.

Adresse locale :

```txt
http://127.0.0.1:8000/admin/
```

Adresse en ligne :

```txt
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

Un compte jury temporaire pourra être créé plus tard uniquement si le projet est validé comme second projet ou si un accès direct est demandé.

---

# Documentation du projet

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
* le plan de finalisation V1.

Le dossier `doc/sql` contient :

* `schema.sql` ;
* `nosql.md`.

Le fichier `schema.sql` sert à documenter la structure SQL de la base.

Le fichier `nosql.md` explique pourquoi NoSQL n'est pas intégré dans la V1 et dans quels cas il pourrait être envisagé plus tard.

---

# Fichiers importants à la racine

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
* pourquoi NoSQL n'est pas implanté artificiellement ;
* pourquoi certaines fonctionnalités sont volontairement limitées.

Ce fichier permet de montrer que les choix techniques sont réfléchis.

---

## `.env.example`

Le fichier `.env.example` documente les variables d'environnement nécessaires sans exposer les vraies valeurs sensibles.

Exemple :

```txt
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

---

## `requirements.txt`

Le fichier `requirements.txt` contient les dépendances Python du projet.

Dépendances importantes :

```txt
Django
gunicorn
whitenoise
```

| Dépendance | Rôle                                         |
| ---------- | -------------------------------------------- |
| Django     | Framework web principal                      |
| gunicorn   | Serveur utilisé pour Render                  |
| whitenoise | Gestion des fichiers statiques en production |

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

# Fonctionnement général du site

Le fonctionnement général du site suit le cycle classique d'une application Django.

```txt
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
templates/pages/*.html
   ↓
base.html
   ↓
CSS / JS / images
   ↓
Page affichée dans le navigateur
```

---

# Exemple de parcours utilisateur

Un visiteur arrive sur la page d'accueil :

```txt
https://frostia-games.onrender.com
```

Django reçoit la requête.

La route correspondante est trouvée dans `urls.py`.

La vue associée dans `core/views.py` est exécutée.

Django charge le template correspondant.

La page HTML est envoyée au navigateur.

Le navigateur charge ensuite les fichiers statiques :

```txt
main.css
menu.js
images
```

La page complète s'affiche à l'utilisateur.

---

# Parcours avec données dynamiques

Pour la page **Mes créations**, le fonctionnement est différent car certaines données viennent de la base.

```txt
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

```txt
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

# Architecture front-end

La partie front-end repose sur :

* HTML avec les templates Django ;
* CSS dans `main.css` ;
* JavaScript léger dans `menu.js`.

Cette approche permet de garder un projet simple, sans framework JavaScript lourd.

Le choix est adapté à une V1 de portfolio, car le site n'a pas encore besoin d'une interface très interactive ou d'une logique front-end complexe.

La modernisation graphique avancée est reportée à une version future.

---

# Architecture back-end

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

---

# Architecture de déploiement

Le projet est déployé avec Render.

Fonctionnement :

```txt
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

```txt
https://frostia-games.onrender.com
```

---

# Docker dans l'architecture

Docker est présent dans le projet, mais il n'est pas utilisé comme mode de production principal.

Son rôle est de fournir un environnement de lancement reproductible.

Commande principale :

```powershell
docker compose up --build
```

Le site est ensuite accessible localement :

```txt
http://127.0.0.1:8000/
```

Docker permet de montrer que le projet peut être lancé dans un environnement isolé.

La documentation Docker est détaillée dans le fichier :

```txt
04-docker-et-lancement.md
```

---

# Sécurité dans l'architecture

Pour cette V1, plusieurs règles de sécurité sont appliquées :

* la clé secrète Django est stockée dans Render ;
* les mots de passe ne sont pas publiés ;
* les identifiants administrateur ne sont pas présents dans GitHub ;
* le mode debug est désactivé sur Render ;
* les variables sensibles sont placées dans les variables d'environnement ;
* l'accès admin reste privé ;
* l'ORM Django est utilisé au lieu de SQL brut ;
* aucun vrai upload serveur n'est implanté dans la V1 ;
* `.env.example` documente les variables sans exposer les vraies valeurs.

Cette sécurité est cohérente avec le périmètre d'une V1.

Elle pourra être renforcée dans une version future.

---

# Choix d'architecture

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
* un compte jury temporaire ;
* une interface d'administration personnalisée ;
* un vrai upload serveur ;
* un jeu jouable dans le navigateur ;
* un tableau de bord avancé ;
* une API REST ;
* un espace privé complet.

Ces éléments sont reportés volontairement.

---

# Limites actuelles

L'architecture actuelle présente plusieurs limites :

* la base de données reste en SQLite ;
* l'administration Django n'est pas personnalisée ;
* les fiches projet détaillées ne sont pas encore intégrées ;
* les médias ne sont pas encore gérés dynamiquement ;
* il n'existe pas encore de table de versions ;
* la partie responsive peut encore être améliorée ;
* le site ne propose pas encore de projet jouable directement dans le navigateur ;
* aucun vrai upload serveur n'est implanté ;
* les tests automatisés complets ne sont pas encore présents.

Ces limites sont acceptées dans le cadre de la V1.

Elles sont documentées afin de distinguer ce qui est réalisé de ce qui est prévu plus tard.

---

# Évolutions possibles

L'architecture actuelle permet plusieurs évolutions :

* migration vers PostgreSQL ;
* ajout d'une table de fiches détaillées ;
* ajout d'une table de médias ;
* ajout d'une table de versions ;
* relation entre une création et un projet jouable ;
* ajout d'un compte jury temporaire en lecture seule ;
* amélioration du responsive ;
* ajout de graphiques avec Plotly.js ;
* intégration future de démos jouables ;
* création d'un espace privé ;
* amélioration de la gestion des médias ;
* ajout de tests automatisés ;
* ajout d'un système de sauvegarde automatique ;
* ajout d'un système de restauration des contenus.

Ces évolutions pourront être ajoutées progressivement si le projet devient un second projet validé ou une base plus avancée.

---

# Bilan

L'architecture actuelle de Frostia Games est simple, claire et adaptée à une V1.

Elle permet :

* d'afficher un site public ;
* d'utiliser Django proprement ;
* de gérer des templates ;
* de charger des fichiers statiques ;
* d'utiliser une base SQLite ;
* d'afficher des données dynamiques ;
* d'accéder à l'administration Django ;
* de lancer le projet localement ;
* de lancer le projet avec Docker ;
* de déployer le projet sur Render ;
* de documenter facilement le fonctionnement du projet ;
* de préparer des évolutions futures sans repartir de zéro.

Cette architecture correspond à l'objectif actuel : obtenir une base stable, déployée, documentée et défendable.
