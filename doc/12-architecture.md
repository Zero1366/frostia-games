# Architecture du projet - Frostia Games

## Objectif du document

Ce document présente l'architecture du projet **Frostia Games**.

L'objectif est d'expliquer comment le projet est organisé, quels sont les rôles des principaux dossiers et fichiers, et comment les différentes parties du site fonctionnent ensemble.

Le projet est une application web développée avec **Django**. Il sert de portfolio pour présenter des projets de jeux vidéo actuels et futurs.

---

## Vue d'ensemble du projet

Frostia Games est organisé autour d'une architecture Django simple.

Le projet contient :

* une configuration Django principale ;
* une application Django dédiée aux pages du site ;
* des templates HTML ;
* des fichiers statiques CSS, JavaScript et images ;
* une base de données SQLite pour la V1 ;
* des fichiers de déploiement ;
* une documentation technique.

Cette structure permet de garder un projet lisible, facile à maintenir et évolutif.

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
├── playable/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── main.css
│   ├── images/
│   └── js/
│       └── menu.js
│
├── staticfiles/
│
├── templates/
│   ├── pages/
│   │   ├── home.html
│   │   ├── creation.html
│   │   └── projet_jouable.html
│   ├── partials/
│   └── base.html
│
├── build.sh
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── pyproject.toml
├── requirements.txt
├── schema.sql
└── documentation/
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

### `settings.py`

Le fichier `settings.py` contient la configuration principale du projet.

Il gère notamment :

* les applications installées ;
* les middlewares ;
* la base de données ;
* les fichiers statiques ;
* les templates ;
* les hôtes autorisés ;
* le mode debug ;
* la clé secrète Django.

Exemples d'éléments configurés :

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "playable",
]
```

---

### `urls.py`

Le fichier `urls.py` définit les routes principales du projet.

Il permet de connecter les URL du site aux vues Django.

Exemple de rôle :

```txt
URL demandée par le visiteur
        ↓
urls.py
        ↓
vue Django
        ↓
template HTML
        ↓
page affichée
```

Il contient aussi l'accès à l'administration Django via `/admin/`.

---

### `wsgi.py`

Le fichier `wsgi.py` sert de point d'entrée pour lancer le projet Django en production.

Render utilise Gunicorn avec cette commande :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande indique à Gunicorn d'utiliser l'application Django définie dans `frostia_config.wsgi`.

---

## `playable`

Le dossier `playable` est une application Django du projet.

Son rôle est de gérer les pages publiques du site Frostia Games.

Même si le nom `playable` évoque les futurs projets jouables, dans la V1 il sert principalement à organiser les vues du site.

### Fichiers importants

| Fichier       | Rôle                                                 |
| ------------- | ---------------------------------------------------- |
| `views.py`    | Contient les fonctions qui affichent les pages       |
| `models.py`   | Prévu pour les futurs modèles de données             |
| `admin.py`    | Permet d'enregistrer des modèles dans l'admin Django |
| `apps.py`     | Configuration de l'application Django                |
| `tests.py`    | Fichier prévu pour les tests                         |
| `migrations/` | Dossier des migrations de base de données            |

---

### `views.py`

Le fichier `views.py` contient les vues Django.

Une vue reçoit une requête HTTP et retourne une réponse, souvent une page HTML.

Exemple de logique :

```python
def home(request):
    return render(request, "pages/home.html")
```

Dans cette V1, les vues servent surtout à afficher les pages publiques du portfolio.

---

### `models.py`

Le fichier `models.py` est prévu pour définir les modèles de données du projet.

Pour la V1, le projet reste volontairement simple. Les données ne sont pas encore toutes gérées dynamiquement depuis la base de données.

Plus tard, ce fichier pourra contenir des modèles comme :

```txt
Projet
Version
Article
Capture
Lien
Statut
```

Cela permettra de rendre le portfolio plus dynamique.

---

### `admin.py`

Le fichier `admin.py` permet d'afficher les modèles dans l'administration Django.

Dans la V1, l'administration Django est fonctionnelle, mais l'espace admin personnalisé n'est pas encore développé.

L'objectif actuel est surtout de vérifier que l'administration Django fonctionne correctement en ligne.

---

## `templates`

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

### `base.html`

Le fichier `base.html` sert de modèle principal.

Il contient les éléments communs à toutes les pages :

* structure HTML globale ;
* chargement du CSS ;
* navigation ;
* zones réutilisables ;
* chargement du JavaScript ;
* structure de base du site.

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

### `templates/pages`

Le dossier `pages` contient les pages principales du site.

Pages actuelles :

| Page                  | Rôle                                     |
| --------------------- | ---------------------------------------- |
| `home.html`           | Page d'accueil du portfolio              |
| `creation.html`       | Présentation des futures créations       |
| `projet_jouable.html` | Page dédiée aux projets jouables à venir |

Ces pages représentent le contenu visible par les visiteurs.

---

### `templates/partials`

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

## `static`

Le dossier `static` contient les fichiers statiques du projet.

Ces fichiers sont utilisés côté navigateur.

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

### `static/css/main.css`

Le fichier `main.css` contient le style principal du site.

Il gère notamment :

* la mise en page ;
* les couleurs ;
* les cartes ;
* les sections ;
* la navigation ;
* le responsive ;
* l'apparence générale du portfolio.

Pour la V1, le style est volontairement centralisé afin de faciliter les modifications rapides.

---

### `static/js/menu.js`

Le fichier `menu.js` contient le JavaScript lié au comportement du menu.

Il peut notamment servir pour :

* ouvrir ou fermer une sidebar mobile ;
* gérer une navigation responsive ;
* améliorer l'expérience utilisateur sur petits écrans.

Le JavaScript reste limité afin de garder un projet simple et maintenable.

---

### `static/images`

Le dossier `images` est prévu pour stocker les images du site.

Il pourra contenir :

* logo temporaire ;
* captures de projets ;
* illustrations ;
* images de présentation ;
* visuels liés aux futures créations.

---

## `staticfiles`

Le dossier `staticfiles` est généré par Django lors de la commande :

```bash
python manage.py collectstatic --noinput
```

Il regroupe les fichiers statiques collectés pour la production.

Ce dossier est utilisé lors du déploiement afin que les fichiers CSS, JavaScript et images soient accessibles correctement.

---

## Base de données

Pour la V1, le projet utilise SQLite.

Fichier utilisé :

```txt
db.sqlite3
```

SQLite est suffisant pour une première version simple, car le projet sert principalement de portfolio de présentation.

### Limite de SQLite

SQLite n'est pas idéal pour une vraie production avec beaucoup de données ou plusieurs utilisateurs.

Pour une version plus avancée, une migration vers PostgreSQL pourra être envisagée.

---

## Administration Django

Le projet utilise l'administration intégrée de Django.

Adresse locale :

```txt
http://127.0.0.1:8000/admin/
```

Adresse en ligne :

```txt
https://frostia-games.onrender.com/admin/
```

L'administration permet de vérifier que le projet Django fonctionne correctement, y compris après le déploiement.

Pour des raisons de sécurité, les identifiants administrateur ne sont pas publiés dans GitHub ni dans la documentation.

Un compte jury temporaire pourra être créé plus tard si le projet est validé comme second projet ou si un accès direct est demandé.

---

## Fichiers de déploiement

## `requirements.txt`

Le fichier `requirements.txt` contient les dépendances Python du projet.

Dépendances importantes :

```txt
Django
gunicorn
whitenoise
```

Rôle des dépendances :

| Dépendance | Rôle                                         |
| ---------- | -------------------------------------------- |
| Django     | Framework web principal                      |
| gunicorn   | Serveur de production                        |
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
4. de créer un compte administrateur si nécessaire.

---

## `Dockerfile` et `docker-compose.yml`

Le projet contient également des fichiers Docker.

Ils permettent de préparer une exécution conteneurisée du projet.

Dans la V1, Docker sert surtout de support technique et de documentation de lancement. Le déploiement principal est effectué avec Render.

---

## `schema.sql`

Le fichier `schema.sql` peut servir à documenter ou conserver une trace de la structure de base de données.

Il peut être utile pour comprendre l'organisation des tables ou préparer une évolution future de la base de données.

---

## `pyproject.toml`

Le fichier `pyproject.toml` peut contenir des informations de configuration Python.

Il peut être utilisé par certains outils modernes liés à Python, au formatage ou à la gestion du projet.

---

## Fonctionnement général du site

Le fonctionnement général du site suit le cycle classique d'une application Django.

```txt
Visiteur
   ↓
URL demandée
   ↓
frostia_config/urls.py
   ↓
playable/views.py
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

## Exemple de parcours utilisateur

Un visiteur arrive sur la page d'accueil :

```txt
https://frostia-games.onrender.com
```

Django reçoit la requête.

La route correspondante est trouvée dans `urls.py`.

La vue associée dans `playable/views.py` est exécutée.

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

## Architecture front-end

La partie front-end repose sur :

* HTML avec les templates Django ;
* CSS dans `main.css` ;
* JavaScript léger dans `menu.js`.

Cette approche permet de garder un projet simple, sans framework JavaScript lourd.

Le choix est adapté à une V1 de portfolio, car le site n'a pas encore besoin d'une interface très interactive ou d'une logique front-end complexe.

---

## Architecture back-end

La partie back-end repose sur Django.

Django gère :

* le routage ;
* les vues ;
* les templates ;
* l'administration ;
* la base de données ;
* les fichiers statiques ;
* la configuration de production.

Le back-end reste volontairement simple dans cette V1.

L'objectif n'est pas encore de créer une plateforme complète, mais une base stable et extensible.

---

## Architecture de déploiement

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
Start Command : gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
   ↓
Site accessible en ligne
```

URL de production :

```txt
https://frostia-games.onrender.com
```

---

## Sécurité dans l'architecture

Pour cette V1, plusieurs règles de sécurité sont appliquées :

* la clé secrète Django est stockée dans Render ;
* les mots de passe ne sont pas publiés ;
* les identifiants administrateur ne sont pas présents dans GitHub ;
* le mode debug est désactivé sur Render ;
* les variables sensibles sont placées dans les variables d'environnement ;
* l'accès admin reste privé.

Cette sécurité est suffisante pour une V1 de démonstration, mais pourra être renforcée dans une version future.

---

## Choix d'architecture

Le projet utilise une architecture simple pour plusieurs raisons :

* éviter une complexité inutile ;
* garder le projet maintenable ;
* faciliter le déploiement ;
* permettre une documentation claire ;
* pouvoir évoluer progressivement ;
* éviter le scope creep ;
* produire une V1 stable.

Le choix a été fait de ne pas intégrer immédiatement :

* PostgreSQL ;
* un compte jury temporaire ;
* une interface d'administration personnalisée ;
* un système dynamique complet ;
* un jeu jouable dans le navigateur ;
* un tableau de bord avancé.

Ces éléments sont reportés volontairement.

---

## Limites actuelles

L'architecture actuelle présente plusieurs limites :

* la base de données reste en SQLite ;
* les projets ne sont pas encore tous gérés dynamiquement ;
* l'administration Django n'est pas personnalisée ;
* les données du portfolio ne sont pas encore modifiables depuis une interface dédiée ;
* la partie responsive peut encore être améliorée ;
* le site ne propose pas encore de projet jouable directement dans le navigateur.

Ces limites sont acceptées dans le cadre de la V1.

---

## Évolutions possibles

L'architecture actuelle permet plusieurs évolutions :

* migration vers PostgreSQL ;
* création d'un modèle `Projet` ;
* ajout dynamique de projets depuis l'administration ;
* création de fiches projets détaillées ;
* ajout d'un compte jury temporaire en lecture seule ;
* amélioration du responsive ;
* ajout de graphiques avec Plotly.js ;
* intégration future de démos jouables ;
* création d'un espace privé ;
* amélioration de la gestion des médias.

Ces évolutions pourront être ajoutées progressivement si le projet devient un second projet validé ou une base plus avancée.

---

## Bilan

L'architecture actuelle de Frostia Games est simple, claire et adaptée à une V1.

Elle permet :

* d'afficher un site public ;
* d'utiliser Django proprement ;
* de gérer des templates ;
* de charger des fichiers statiques ;
* d'accéder à l'administration Django ;
* de déployer le projet sur Render ;
* de documenter facilement le fonctionnement du projet ;
* de préparer des évolutions futures sans repartir de zéro.

Cette architecture correspond à l'objectif actuel : obtenir une base stable, déployée et défendable.
