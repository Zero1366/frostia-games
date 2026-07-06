# Journal de bord — Frostia Games

## Objectif du document

Ce document consigne les étapes réalisées pendant le développement du projet **Frostia Games**.

L’objectif est de garder une trace claire :

* de l’avancement du projet ;
* des choix réalisés ;
* des fichiers modifiés ;
* des problèmes rencontrés ;
* des validations effectuées ;
* des limites volontaires de la V1 ;
* des technologies envisagées mais non retenues ;
* du déploiement en ligne ;
* de la documentation produite ;
* des fichiers importants ajoutés à la racine du projet.

Ce journal permet aussi d’expliquer que certaines décisions techniques ont été prises pour protéger la stabilité du projet, éviter de repartir de zéro et conserver un périmètre réaliste.

---

# Étape 01 — Mise en place du socle Django

**Date :** 19/06/2026
**Statut :** validé

## Objectif

Mettre en place un premier socle technique propre pour le projet Frostia Games avec Python et Django.

Cette étape sert à préparer une base stable avant de commencer le développement des pages du site.

---

## Actions réalisées

* Création du dossier du projet **Frostia Games**.

* Création d’un environnement virtuel Python nommé `.venv`.

* Activation de l’environnement virtuel dans le terminal VS Code.

* Installation de Django.

* Création du projet Django principal : `frostia_config`.

* Création des applications Django :

  * `core` ;
  * `creations` ;
  * `playable`.

* Création des dossiers de structure :

  * `templates` ;
  * `templates/pages` ;
  * `templates/partials` ;
  * `static` ;
  * `static/css` ;
  * `static/js` ;
  * `static/images` ;
  * `media` ;
  * `doc` ;
  * `.vscode`.

---

## Configuration réalisée

Le fichier `frostia_config/settings.py` a été modifié afin de configurer :

* les applications internes du projet ;
* le dossier des templates ;
* les fichiers statiques ;
* le dossier média ;
* la langue française ;
* le fuseau horaire `Europe/Paris`.

Les applications ajoutées sont :

```python
"core",
"creations",
"playable",
```

Le dossier des templates est configuré avec :

```python
"DIRS": [BASE_DIR / "templates"],
```

Les fichiers statiques et médias sont configurés avec :

```python
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

---

## Vérifications effectuées

Commande utilisée :

```powershell
python manage.py check
```

Résultat obtenu :

```text
System check identified no issues (0 silenced).
```

---

## Fichiers concernés

* `manage.py`
* `frostia_config/settings.py`
* `frostia_config/urls.py`
* `core/views.py`
* `core/urls.py`
* `.vscode/settings.json`

---

## Problèmes rencontrés

Plusieurs problèmes ont été rencontrés pendant l’installation :

* environnement virtuel créé partiellement après une interruption ;
* difficulté d’activation du `.venv` dans PowerShell ;
* commande invalide tapée par erreur dans le terminal ;
* alertes de typage inutiles dans VS Code liées à Django ;
* besoin de distinguer les vraies erreurs Django des faux positifs de l’éditeur.

---

## Décision prise

Le projet ne devait pas commencer par une accumulation de fonctionnalités.

La priorité a été de mettre en place une base Django stable, compréhensible et documentée avant d’aller plus loin.

---

# Étape 02 — Réflexion sur les technologies envisagées

**Date :** 19/06/2026
**Statut :** documenté

## Objectif

Cette étape permet d’expliquer les technologies envisagées pour le projet et les raisons pour lesquelles certaines pistes n’ont pas été retenues dans la V1.

Ce point est important, car il montre que le choix technique n’a pas été fait au hasard. Il a été fait en tenant compte :

* du temps disponible ;
* du périmètre du projet ;
* de la stabilité attendue ;
* de la documentation à produire ;
* de la capacité à terminer une V1 présentable.

---

## Technologies envisagées

Plusieurs pistes techniques ont été envisagées avant de stabiliser le projet avec Django :

* une approche plus orientée C# ;
* une solution ASP.NET / Razor ;
* une technologie plus fortement typée ;
* une architecture backend plus structurée dès le départ ;
* une solution plus proche de futurs projets de jeux vidéo ;
* une organisation plus proche d’un environnement applicatif C#.

Ces pistes restent intéressantes pour de futurs projets, car elles correspondent davantage à certaines préférences personnelles en matière de structure, de typage et de lisibilité du code.

---

## Point de vue technique personnel

Une attention particulière a été portée à l’élégance technique.

Par élégance, on entend ici :

* une syntaxe claire ;
* une structure logique ;
* un typage rassurant ;
* une séparation propre des responsabilités ;
* une architecture qui évite les solutions trop dispersées ;
* un langage qui aide le développeur à garder un code stable.

De ce point de vue, certaines technologies envisagées semblaient intéressantes, notamment C# avec ASP.NET ou Razor.

Cependant, ce projet devait rester réaliste, livrable et terminé dans un délai raisonnable.

---

## Pourquoi ne pas avoir changé de technologie

Même si certaines pistes paraissaient plus proches des préférences techniques initiales, elles n’ont pas été retenues pour cette V1.

Changer de technologie à ce stade aurait obligé à repartir de zéro ou à reconstruire une grande partie du projet.

Ce choix aurait créé plusieurs risques :

* perte de temps importante ;
* instabilité du projet ;
* documentation à refaire ;
* augmentation du périmètre ;
* complexité inutile ;
* risque de ne pas terminer une version présentable ;
* transformation du projet en expérimentation technique au lieu d’un livrable stable.

La décision a donc été de ne pas repartir de zéro.

Ce choix est important, car il montre une capacité à limiter le périmètre et à terminer un projet plutôt qu’à suivre uniquement une préférence technique.

---

## Choix final de Django et Python

Le choix final s’est porté sur Django avec Python.

Python reste un langage assez permissif. Cela peut parfois donner moins de sécurité qu’un langage plus strict ou plus fortement typé.

Cependant, dans le cadre de cette V1, Django apporte une structure claire :

* routes ;
* vues ;
* modèles ;
* migrations ;
* administration ;
* templates ;
* base SQLite ;
* séparation entre code, données et affichage.

Même si Python n’est pas le langage le plus strict, Django permet d’encadrer le projet avec une architecture compréhensible.

Python reste également lisible, rapide à mettre en place et suffisamment efficace lorsqu’il est utilisé avec méthode, documentation et règles de validation.

---

## Garde-fous ajoutés

Pour compenser la permissivité de Python, plusieurs garde-fous ont été ajoutés progressivement :

* documentation régulière ;
* journal de bord ;
* changelog ;
* commandes de vérification Django ;
* séparation des fichiers ;
* environnement virtuel `.venv` ;
* utilisation de migrations Django ;
* validation avec `python manage.py check` ;
* organisation des templates ;
* fichiers statiques séparés ;
* documentation des limites ;
* documentation des choix techniques ;
* utilisation de variables d’environnement ;
* fichier `.env.example` pour documenter la configuration sans exposer les secrets.

---

## Décision retenue

La décision prise est donc la suivante :

* conserver Django pour la V1 ;
* ne pas repartir de zéro avec une nouvelle technologie ;
* documenter les limites du choix technique ;
* reporter les expérimentations C# / ASP.NET / Razor à de futurs projets ;
* privilégier une version fonctionnelle, testable et maintenable ;
* éviter le changement de technologie en cours de route ;
* renforcer le projet avec de la documentation, des vérifications et des garde-fous.

Ce choix permet de protéger le projet contre le risque de dérive technique.

---

## Bilan de cette réflexion

Cette réflexion est un point positif du projet.

Elle montre que les technologies mises de côté ne l’ont pas été par oubli, mais par choix de périmètre.

Le projet aurait pu partir vers une technologie plus proche de certaines préférences techniques, mais cela aurait augmenté le risque de ne pas terminer correctement la V1.

Le choix final est donc un compromis entre :

* les préférences techniques ;
* la stabilité du projet ;
* le temps disponible ;
* la capacité à documenter ;
* la capacité à livrer une version présentable.

---

# Étape 03 — Création de l’interface principale

**Date :** 19/06/2026
**Statut :** validé

## Objectif

Créer les pages principales du portfolio Frostia Games avec une interface simple, moderne et responsive.

---

## Actions réalisées

Création des trois pages principales :

* Accueil ;
* Mes créations ;
* Projets jouables.

Mise en place :

* du template commun `base.html` ;
* de la navigation principale ;
* de la sidebar desktop ;
* du menu mobile ;
* du fichier CSS principal ;
* du fichier JavaScript pour le menu.

---

## Fichiers concernés

* `templates/base.html`
* `templates/pages/home.html`
* `templates/pages/creation.html`
* `templates/pages/projet_jouable.html`
* `static/css/main.css`
* `static/js/menu.js`
* `core/views.py`
* `core/urls.py`

---

## Résultat obtenu

Le site dispose maintenant :

* d’une page d’accueil ;
* d’une page Mes créations ;
* d’une page Projets jouables ;
* d’une navigation active ;
* d’un menu mobile ;
* d’une interface responsive ;
* d’un thème bleu cohérent avec le nom Frostia Games.

---

## Vérifications effectuées

Pages testées :

```text
/
/mes-creations/
/projets-jouables/
```

Résultat :

* les pages s’ouvrent ;
* la navigation fonctionne ;
* le menu mobile fonctionne ;
* le rendu est exploitable pour une V1.

---

# Étape 04 — Modernisation de l’interface

**Date :** 20/06/2026
**Statut :** validé

## Objectif

Améliorer l’apparence du site sans utiliser de template Django lourd.

L’objectif est de conserver le contrôle du code, du CSS et de la structure.

---

## Actions réalisées

* Harmonisation des couleurs bleues.
* Ajout d’un fond dégradé.
* Amélioration des cartes.
* Ajout d’ombres et de bordures plus modernes.
* Amélioration de la sidebar.
* Amélioration du footer.
* Amélioration de l’état actif dans le menu.
* Préparation du responsive mobile.
* Adaptation progressive de l’interface à l’affichage des données provenant du backend.

---

## Fichiers concernés

* `static/css/main.css`
* `templates/base.html`
* `templates/pages/home.html`
* `templates/pages/creation.html`
* `templates/pages/projet_jouable.html`

---

## Problèmes rencontrés

* Certaines classes CSS ne correspondaient pas encore au HTML.
* Certains styles étaient placés dans le mauvais bloc responsive.
* Le footer ne s’intégrait pas correctement à la page.
* Certains textes étaient trop petits ou mal hiérarchisés.
* Certaines parties de l’interface ont dû être adaptées après l’ajout du backend.

---

## Résultat obtenu

L’interface est devenue plus propre, plus lisible et plus professionnelle.

Elle reste volontairement simple afin de conserver une V1 stable, maintenable et compatible avec le backend Django.

La modernisation lourde est reportée à une version future.

---

# Étape 05 — Création du backend SQL

**Date :** 24/06/2026
**Statut :** validé

## Objectif

Ajouter un backend Django minimal mais réel afin que le site ne soit pas uniquement statique.

L’objectif est de connecter certaines pages à une base SQLite via les modèles Django.

---

## Actions réalisées

Création des modèles :

* `Creation` ;
* `PlayableProject`.

Ajout des modèles dans l’administration Django.

Création et application des migrations.

Ajout de données depuis l’admin Django.

Connexion des vues aux modèles.

Affichage des données dans les templates.

---

## Fichiers concernés

* `creations/models.py`
* `creations/admin.py`
* `playable/models.py`
* `playable/admin.py`
* `core/views.py`
* `templates/pages/creation.html`
* `templates/pages/projet_jouable.html`
* `frostia_config/settings.py`

---

## Modèle Creation

Le modèle `Creation` permet de gérer les créations affichées dans la page **Mes créations**.

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

---

## Modèle PlayableProject

Le modèle `PlayableProject` permet de gérer les futurs contenus de la page **Projets jouables**.

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

---

## Vérifications effectuées

Commandes utilisées :

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

Résultat obtenu :

```text
System check identified no issues (0 silenced).
```

Pages testées :

```text
/mes-creations/
/projets-jouables/
/admin/
```

Résultat :

* l’administration Django fonctionne ;
* les données sont enregistrées en base ;
* les données remontent dans les templates ;
* les pages restent accessibles.

---

# Étape 06 — Mise en place de l’administration Django

**Date :** 24/06/2026
**Statut :** validé

## Objectif

Permettre la gestion des contenus dynamiques depuis l’administration Django.

---

## Actions réalisées

Pour le modèle `Creation` :

* ajout de `list_display` ;
* ajout de `list_filter` ;
* ajout de `search_fields` ;
* ajout de `prepopulated_fields` ;
* ajout de `readonly_fields`.

Pour le modèle `PlayableProject` :

* ajout de `list_display` ;
* ajout de `list_filter` ;
* ajout de `search_fields` ;
* ajout de `prepopulated_fields` ;
* ajout de `readonly_fields`.

---

## Fichiers concernés

* `creations/admin.py`
* `playable/admin.py`

---

## Problème rencontré

VS Code / Pylance signalait des erreurs inutiles sur `admin.ModelAdmin`.

Ces alertes n’étaient pas des erreurs Django.

Elles ont été traitées avec :

```python
# type: ignore[type-arg]
```

et avec un réglage plus adapté de Pylance pour un projet Django.

---

## Validation

L’administration Django est accessible à l’adresse :

```text
/admin/
```

Actions testées :

* ajout d’une création ;
* modification d’une création ;
* ajout d’un projet jouable ;
* modification d’un projet jouable ;
* affichage des données côté site.

---

# Étape 07 — Interface préparatoire des projets jouables

**Date :** 24/06/2026
**Statut :** validé

## Objectif

Préparer la page **Projets jouables** sans intégrer de vrai upload serveur.

L’objectif est de montrer une interface prévue pour une future évolution, tout en restant honnête sur les limites de la V1.

---

## Actions réalisées

* Ajout d’une zone de lecteur préparatoire.
* Ajout d’un bouton Lecture affichant un message.
* Ajout d’un bouton de sélection de fichier local.
* Affichage du nom du fichier sélectionné.
* Message indiquant clairement que l’upload n’est pas implanté.
* Affichage des données `PlayableProject` depuis la base.

---

## Fichiers concernés

* `templates/pages/projet_jouable.html`
* `static/css/main.css`
* `core/views.py`
* `playable/models.py`

---

## Limite volontaire

Aucun vrai upload serveur n’est implanté dans cette V1.

Cela signifie que :

* aucun fichier n’est envoyé au serveur ;
* aucun fichier n’est stocké ;
* aucun fichier n’est exécuté ;
* aucun vrai lecteur vidéo n’est actif.

Ce choix évite d’ajouter une fonctionnalité sensible sans sécurité suffisante.

---

## Validation

Tests effectués :

* page Projets jouables accessible ;
* données SQL affichées ;
* bouton Lecture fonctionnel ;
* bouton de sélection de fichier fonctionnel ;
* message d’upload non implanté visible ;
* aucun vrai upload serveur.

---

# Étape 08 — Nettoyage des alertes inutiles

**Date :** 24/06/2026
**Statut :** validé

## Objectif

Supprimer les fausses erreurs affichées par VS Code afin de ne conserver que les alertes réellement utiles.

---

## Problème rencontré

Le mode strict de Pylance générait de nombreuses alertes sur les champs Django :

* `CharField` ;
* `SlugField` ;
* `BooleanField` ;
* `ModelAdmin`.

Ces alertes étaient liées au typage interne de Django et ne bloquaient pas l’exécution.

---

## Actions réalisées

Modification de `.vscode/settings.json` :

* passage de `strict` à `basic` ;
* désactivation des faux positifs liés aux types inconnus ;
* conservation de Ruff pour le formatage et les imports ;
* conservation de `python manage.py check` comme validation principale Django.

---

## Fichiers concernés

* `.vscode/settings.json`
* `creations/admin.py`
* `playable/admin.py`

---

## Validation

Les alertes inutiles ont disparu.

Le projet reste validé avec :

```powershell
python manage.py check
```

---

# Étape 09 — Ajout de Docker

**Date :** 24/06/2026
**Statut :** validé

## Objectif

Ajouter Docker afin de rendre l’environnement de développement reproductible.

---

## Actions réalisées

Création des fichiers :

* `Dockerfile` ;
* `docker-compose.yml` ;
* `.dockerignore` ;
* `requirements.txt`.

Test du lancement avec Docker Compose.

---

## Fichiers concernés

* `Dockerfile`
* `docker-compose.yml`
* `.dockerignore`
* `requirements.txt`

---

## Commande utilisée

```powershell
docker compose up --build
```

---

## Problèmes rencontrés

Plusieurs erreurs ont été corrigées :

* erreur YAML dans `docker-compose.yml` ;
* Docker Desktop non lancé ;
* erreur de nom de fichier dans le `Dockerfile` ;
* nécessité de lancer le serveur depuis Docker avant de tester la page.

---

## Validation

Docker construit l’image correctement.

Le conteneur se lance.

Le serveur Django démarre dans Docker.

Le site est accessible via :

```text
https://frostia-games.onrender.com/
```

---

# Étape 10 — Ajout de la documentation backend

**Date :** 24/06/2026
**Statut :** validé

## Objectif

Ajouter les documents nécessaires pour répondre aux attendus du dossier projet.

---

## Documents créés ou mis à jour

* `doc/00-index-documentation.md`
* `doc/01-modernisation-interface.md`
* `doc/02-journal-de-bord.md`
* `doc/03-modelisation-backend.md`
* `doc/04-docker-et-lancement.md`
* `doc/05-securite-backend.md`
* `doc/06-manuel-utilisateur.md`
* `doc/07-base-de-donnees.md`
* `doc/08-changelog.md`
* `doc/sql/schema.sql`
* `doc/sql/nosql.md`

---

## Contenu ajouté

* MCD simplifié.
* Cas d’utilisation.
* Diagrammes de séquence.
* Schéma SQL documentaire.
* Exemples `CREATE TABLE`.
* Exemples `INSERT INTO`.
* Réflexion NoSQL.
* Documentation Docker.
* Documentation sécurité.
* Manuel utilisateur.
* Changelog.
* Mise à jour de l’index.
* Mise à jour du journal de bord.

---

## Validation

Les fichiers de documentation sont présents dans le dossier `doc`.

Ils permettent de justifier :

* la base SQL ;
* le backend Django ;
* Docker ;
* la sécurité ;
* les limites de la V1 ;
* les évolutions prévues ;
* les choix techniques ;
* les technologies volontairement mises de côté.

---

# Étape 11 — Préparation du déploiement Render

**Date :** 25/06/2026
**Statut :** validé

## Objectif

Préparer le projet Django pour un déploiement en ligne avec Render.

L’objectif était de rendre le site accessible hors de l’environnement local, tout en conservant une configuration simple et documentée.

---

## Actions réalisées

* Ajout ou vérification du fichier `requirements.txt`.
* Ajout de Gunicorn.
* Ajout ou vérification de WhiteNoise.
* Création ou adaptation du fichier `build.sh`.
* Configuration des variables d’environnement Render.
* Vérification du fichier `wsgi.py`.
* Configuration du Build Command Render.
* Configuration du Start Command Render.
* Vérification de l’accès au site en ligne.
* Vérification de l’accès à l’administration Django.

---

## Fichiers concernés

* `requirements.txt`
* `build.sh`
* `frostia_config/settings.py`
* `frostia_config/wsgi.py`
* `.gitignore`
* `.env.example`
* `doc/09-deploiement-render.md`

---

## Commande de build Render

```bash
bash build.sh
```

## Commande de démarrage Render

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

---

## Problèmes rencontrés

Plusieurs problèmes ou confusions ont été rencontrés :

* confusion initiale avec une commande de type Flask ;
* erreur locale sous PowerShell avec `bash build.sh` ;
* confusion entre les commandes Render et les variables d’environnement ;
* nécessité d’utiliser `frostia_config.wsgi:application` pour un projet Django ;
* nécessité de ne pas exposer les valeurs sensibles dans GitHub.

---

## Décisions prises

Les commandes de déploiement doivent rester dans la configuration Render :

* `bash build.sh` dans **Build Command** ;
* `gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT` dans **Start Command**.

Les secrets doivent rester dans les variables d’environnement Render :

* `DJANGO_DEBUG` ;
* `DJANGO_SECRET_KEY` ;
* `DJANGO_SUPERUSER_USERNAME` ;
* `DJANGO_SUPERUSER_EMAIL` ;
* `DJANGO_SUPERUSER_PASSWORD`.

---

## Validation

Le site est déployé en ligne avec succès.

URL de production :

```text
https://frostia-games.onrender.com
```

Render indique que le service est actif.

L’administration Django est également accessible via :

```text
/admin/
```

---

# Étape 12 — Documentation du déploiement Render

**Date :** 25/06/2026
**Statut :** validé

## Objectif

Documenter le déploiement Render afin de garder une trace complète de la mise en ligne.

---

## Actions réalisées

Création du fichier :

* `doc/09-deploiement-render.md`

Ce document explique :

* l’objectif du déploiement ;
* la plateforme utilisée ;
* la structure du projet ;
* les prérequis ;
* les fichiers importants ;
* la configuration Django ;
* les variables d’environnement Render ;
* le rôle de `build.sh` ;
* la configuration Render ;
* les vérifications après déploiement ;
* les problèmes rencontrés ;
* les limites de l’offre gratuite Render.

---

## Validation

Le document permet de comprendre comment le projet a été mis en ligne.

Il peut être utilisé comme support pour le dossier projet ou pour relancer une configuration similaire plus tard.

---

# Étape 13 — Bilan V1 avec pourcentages

**Date :** 25/06/2026
**Statut :** validé

## Objectif

Créer un bilan clair de l’état de la V1 avec une estimation par pourcentage.

---

## Actions réalisées

Création du fichier :

* `doc/10-bilan-v1-frostia-games.md`

Ce fichier permet de présenter :

* l’objectif de la V1 ;
* l’état global du projet ;
* les parties terminées ;
* les parties encore améliorables ;
* les éléments volontairement reportés ;
* une estimation globale de l’avancement.

---

## Résultat

La V1 est estimée comme fonctionnelle et avancée, mais pas comme une version finale complète.

Le projet est présenté comme une base Django stable, déployée, documentée et évolutive.

---

# Étape 14 — Complément de documentation finale

**Date :** 25/06/2026
**Statut :** validé

## Objectif

Compléter la documentation afin de rendre le projet plus lisible, défendable et présentable.

---

## Documents ajoutés

* `doc/11-installation-locale.md`
* `doc/12-architecture.md`
* `doc/13-test-et-vérification.md`
* `doc/14-Capture-et Preuve.md`
* `doc/15-limites-et-évolutions.md`
* `doc/16-presentation-projet-2.md`
* `doc/17-pistes-explorees-et-non-retenues.md`
* `doc/18-plan-finalisation-v1.md`

---

## Rôle des documents ajoutés

`11-installation-locale.md` explique comment installer et relancer le projet localement.

`12-architecture.md` présente l’organisation du projet et le rôle des dossiers et fichiers principaux.

`13-test-et-vérification.md` liste les tests et vérifications réalisés.

`14-Capture-et Preuve.md` prépare les captures d’écran nécessaires pour le dossier.

`15-limites-et-évolutions.md` explique ce qui est volontairement limité ou reporté.

`16-presentation-projet-2.md` présente Frostia Games comme proposition de second projet.

`17-pistes-explorees-et-non-retenues.md` explique les pistes envisagées mais non intégrées.

`18-plan-finalisation-v1.md` sert de checklist pour terminer proprement la V1.

---

## Validation

La documentation du dossier `doc` couvre maintenant :

* l’installation ;
* l’interface ;
* le backend ;
* la base de données ;
* Docker ;
* la sécurité ;
* le déploiement ;
* les tests ;
* les captures ;
* les limites ;
* les pistes non retenues ;
* la finalisation.

---

# Étape 15 — Ajout des fichiers racine du projet

**Date :** 25/06/2026
**Statut :** validé

## Objectif

Ajouter des fichiers à la racine du projet afin de rendre le dépôt GitHub plus clair et plus professionnel.

---

## Fichiers ajoutés ou mis à jour

* `README.md`
* `CHOIX_TECHNIQUES.md`
* `.env.example`
* `.gitignore`

---

## Rôle du README

Le fichier `README.md` sert de point d’entrée pour le dépôt GitHub.

Il présente :

* le projet ;
* l’objectif de la V1 ;
* les technologies utilisées ;
* les pages principales ;
* l’installation locale ;
* le lancement du serveur ;
* le lancement Docker ;
* le déploiement Render ;
* les variables d’environnement ;
* l’administration Django ;
* les limites de la V1 ;
* les évolutions prévues.

Ce fichier permet à une personne extérieure de comprendre rapidement le projet.

---

## Rôle du fichier CHOIX_TECHNIQUES.md

Le fichier `CHOIX_TECHNIQUES.md` explique les décisions techniques du projet.

Il présente notamment :

* pourquoi Django a été retenu ;
* pourquoi C# / Razor a été envisagé mais reporté ;
* pourquoi Python nécessite des garde-fous ;
* pourquoi certaines fonctionnalités ont été reportées ;
* pourquoi le projet a été limité pour éviter une usine à gaz.

Ce fichier permet de montrer que les choix techniques sont réfléchis et documentés.

---

## Rôle du fichier .env.example

Le fichier `.env.example` indique les variables d’environnement nécessaires au projet sans exposer les vraies valeurs sensibles.

Exemple :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Ce fichier permet de documenter la configuration attendue sans publier de secret.

---

## Rôle du fichier .gitignore

Le fichier `.gitignore` protège les fichiers qui ne doivent pas être envoyés sur GitHub.

Il permet notamment d’ignorer :

* `.env` ;
* `.env.local` ;
* `.venv/` ;
* `db.sqlite3` ;
* `staticfiles/` ;
* `media/` ;
* les caches Python ;
* les fichiers temporaires.

---

## Validation

Les fichiers racine rendent le projet plus lisible sur GitHub.

Ils complètent la documentation du dossier `doc`.

Le dépôt contient maintenant une présentation rapide, une justification des choix techniques et un exemple de configuration d’environnement.

---

# Étape 16 — Mise à jour de l’index de documentation

**Date :** 25/06/2026
**Statut :** validé

## Objectif

Mettre à jour l’index de documentation afin qu’il corresponde à l’état réel du projet.

---

## Actions réalisées

Le fichier suivant a été mis à jour :

* `doc/00-index-documentation.md`

L’ancienne version de l’index ne listait pas encore tous les documents récents.

La nouvelle version inclut maintenant les documents `09` à `18`, ainsi que les fichiers importants à la racine :

* `README.md` ;
* `CHOIX_TECHNIQUES.md` ;
* `.env.example` ;
* `build.sh` ;
* `requirements.txt`.

---

## Correction importante

L’ancien fichier `installation-django.md` a été remplacé par :

```text
11-installation-locale.md
```

Cette modification permet d’avoir une documentation plus cohérente, car le fichier ne concerne pas seulement Django, mais l’installation locale complète du projet.

---

## Validation

L’index correspond maintenant à la structure actuelle du dossier `doc`.

Il sert de point d’entrée fiable pour la documentation du projet.

---

# Étape 17 — Sauvegarde Git et synchronisation GitHub

**Date :** 25/06/2026
**Statut :** validé

## Objectif

Sauvegarder toutes les modifications dans Git et synchroniser le projet avec GitHub.

---

## Actions réalisées

Commandes utilisées :

```powershell
git status
git add .
git commit -m "Complete Frostia Games documentation"
git push
```

Puis vérification :

```powershell
git status
```

Résultat attendu :

```text
nothing to commit, working tree clean
```

---

## Résultat

Le dépôt local est propre.

Les fichiers sont envoyés sur GitHub.

Le projet est synchronisé avec la branche `main`.

---

# Étape 18 — État actuel du projet

**Date :** 25/06/2026
**Statut :** en finalisation V1

## Ce qui fonctionne

* Le serveur Django local fonctionne.
* Le serveur Docker fonctionne.
* Les pages principales sont accessibles.
* L’administration Django est accessible.
* Les données SQL sont conservées.
* Les données SQL remontent dans les templates.
* L’interface préparatoire des projets jouables fonctionne.
* `python manage.py check` ne signale pas d’erreur.
* Les fausses alertes Pylance ont été nettoyées.
* Le site est déployé sur Render.
* Le site en ligne est accessible.
* Le README racine existe.
* Le fichier `CHOIX_TECHNIQUES.md` existe.
* Le fichier `.env.example` existe.
* La documentation du dossier `doc` est complète jusqu’au fichier 18.
* Le dépôt Git est propre.

---

## Ce qu’il reste à faire

Les prochaines actions sont maintenant limitées à la finalisation :

* relire les pages publiques ;
* vérifier le responsive mobile ;
* préparer les captures d’écran ;
* vérifier le README racine ;
* vérifier le fichier `CHOIX_TECHNIQUES.md` ;
* préparer les maquettes Figma si nécessaire ;
* vérifier le site en local ;
* vérifier le site sur Render ;
* vérifier l’administration Django ;
* préparer le dossier projet final.

---

## Ce qui ne doit plus être ajouté dans cette V1

Pour éviter d’élargir le périmètre, les éléments suivants sont reportés :

* PostgreSQL ;
* compte jury temporaire ;
* administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* Plotly.js ;
* espace privé complet ;
* système de sauvegarde automatique ;
* refonte graphique complète ;
* tests automatisés complets.

Ces éléments sont documentés comme pistes futures.

---

# Bilan

Le projet Frostia Games dispose maintenant d’une V1 Django fonctionnelle, documentée et déployée.

Il contient :

* une interface responsive ;
* un backend Django ;
* une base SQLite ;
* une administration ;
* un affichage dynamique ;
* Docker ;
* un déploiement Render ;
* un README racine ;
* un fichier de choix techniques ;
* un exemple de variables d’environnement ;
* une documentation SQL ;
* une réflexion NoSQL ;
* une documentation de sécurité ;
* un manuel utilisateur ;
* un changelog ;
* une documentation de tests ;
* une documentation de déploiement ;
* une documentation des limites ;
* une documentation des pistes explorées ;
* un plan de finalisation V1.

Le projet reste volontairement limité afin d’éviter une complexité inutile.

Le choix de ne pas changer de technologie en cours de route est une décision importante du projet.

Même si certaines technologies auraient pu correspondre davantage à des préférences personnelles, la priorité a été donnée à une V1 terminée, stable, documentée, déployée et présentable.

L’objectif est maintenant de finaliser les captures, relire les textes, vérifier le responsive et préparer la présentation du projet.
---

# Mise à jour du journal — Renforcement après retour formateur

Cette partie complète le journal de bord initial.

Elle ne remplace pas les étapes précédentes : elle ajoute les corrections, renforcements et validations réalisés après la première V1 documentée.

L'objectif de cette mise à jour est de garder une trace des ajouts récents sans effacer l'historique du projet.

---

# Étape 19 — Création d'une branche de renforcement du dossier

**Date :** 30/06/2026  
**Statut :** validé

## Objectif

Créer une branche dédiée afin de renforcer le projet sans modifier directement la branche principale.

L'objectif était de pouvoir ajouter les éléments demandés après le retour formateur tout en conservant une trace claire du travail effectué.

---

## Actions réalisées

* Création d'une branche dédiée au renforcement du dossier.
* Séparation entre la V1 déjà fonctionnelle et les ajouts de preuve.
* Travail progressif sur les documents, les captures et les compléments techniques.
* Vérification régulière avec Git.

---

## Commandes utilisées

```powershell
git status
git checkout -b v3-renforcement-dossier
```

---

## Décision prise

Le renforcement ne devait pas transformer Frostia Games en nouveau projet.

La branche avait pour objectif de compléter les preuves, pas d'ouvrir un nouveau chantier fonctionnel.

---

## Validation

Le travail a été réalisé sur une branche séparée, avec des commits réguliers.

Le projet est resté stable pendant les ajouts.

---

# Étape 20 — Création d'une documentation complémentaire de renforcement

**Date :** 30/06/2026  
**Statut :** validé

## Objectif

Ajouter une documentation complémentaire pour répondre aux remarques du retour formateur.

Le dossier projet devait mieux montrer :

* la conception ;
* le SQL natif ;
* le JavaScript dynamique ;
* les extraits de code ;
* les preuves visuelles ;
* les annexes ;
* la règle des trois piliers.

---

## Dossiers créés

```text
docs/
├─ backend/
├─ conception/
├─ frontend/
├─ nosql/
├─ preuves/
└─ sql/
```

---

## Rôle de ces dossiers

Le dossier `doc/` reste la documentation principale historique du projet.

Le dossier `docs/` sert de documentation complémentaire de renforcement.

Cette séparation permet d'éviter de casser l'organisation déjà en place.

---

## Décision prise

La documentation principale n'a pas été renommée.

Les nouveaux documents ont été ajoutés comme compléments pour le dossier projet final.

---

# Étape 21 — Ajout des livrables de conception

**Date :** 30/06/2026  
**Statut :** validé

## Objectif

Répondre au manque de conception signalé dans le retour formateur.

Les éléments attendus étaient :

* un MCD ;
* un diagramme de cas d'utilisation ;
* un diagramme de séquence.

---

## Documents créés

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
```

---

## Contenu ajouté

Le MCD présente les entités principales :

* `Creation` ;
* `PlayableProject`.

Le diagramme de cas d'utilisation présente les acteurs :

* visiteur ;
* administrateur ;
* compte temporaire de lecture seule.

Le diagramme de séquence présente le parcours d'un visiteur :

* ouverture d'une page ;
* appel d'une route Django ;
* traitement par une vue ;
* récupération des données ;
* rendu du template ;
* affichage dans le navigateur.

---

## Validation

Ces documents renforcent la partie conception du dossier projet.

Ils montrent que le projet n'est pas seulement codé, mais aussi pensé et structuré.

---

# Étape 22 — Ajout des extraits SQL natifs

**Date :** 30/06/2026  
**Statut :** validé

## Objectif

Répondre à la demande de mieux montrer le SQL dans le dossier projet.

Le projet utilise l'ORM Django, mais le dossier devait aussi présenter des extraits SQL natifs.

---

## Documents créés

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

---

## Actions réalisées

* Génération ou récupération des instructions SQL liées aux migrations Django.
* Ajout d'exemples `CREATE TABLE`.
* Ajout d'exemples `INSERT INTO`.
* Explication du lien entre les modèles Django et les tables SQL.
* Explication de la différence entre ORM Django et SQL natif documentaire.

---

## Exemples de contenu

Le dossier SQL contient notamment :

* une table liée aux créations ;
* une table liée aux projets jouables ;
* des exemples d'insertion de données ;
* une explication du rôle des migrations.

---

## Validation

Les extraits SQL permettent maintenant de mieux prouver la compétence base de données.

Ils complètent le fichier `doc/sql/schema.sql` déjà présent.

---

# Étape 23 — Renforcement du JavaScript dynamique

**Date :** 30/06/2026  
**Statut :** validé

## Objectif

Valoriser le JavaScript dynamique déjà présent dans le projet.

Le menu mobile existait, mais il n'était pas assez expliqué dans le dossier projet.

---

## Fichiers vérifiés

```text
static/js/menu.js
templates/base.html
```

---

## Document créé

```text
docs/frontend/javascript-menu-mobile.md
```

---

## Fonctionnement documenté

Le JavaScript :

* récupère le bouton du menu ;
* récupère la sidebar ;
* écoute le clic utilisateur ;
* ajoute ou retire la classe `is-open` ;
* modifie l'attribut `aria-expanded` ;
* referme le menu après un clic sur un lien.

---

## Validation

Le fichier `static/js/menu.js` est bien chargé avec `defer` dans le template principal.

Le menu mobile fonctionne et peut être prouvé par captures :

* menu fermé ;
* menu ouvert ;
* extrait du JavaScript ;
* explication du fonctionnement.

---

# Étape 24 — Ajout de la documentation backend complémentaire

**Date :** 30/06/2026  
**Statut :** validé

## Objectif

Mieux expliquer la partie backend Django dans le dossier projet.

Le code existait déjà, mais il devait être davantage relié à des explications claires.

---

## Documents créés

```text
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

---

## Contenu ajouté

La documentation backend explique :

* le rôle du modèle `Creation` ;
* le rôle du modèle `PlayableProject` ;
* le lien entre les modèles et les tables SQL ;
* le rôle des migrations ;
* le rôle des vues Django ;
* le lien entre les routes, les vues et les templates.

---

## Validation

Ces documents permettent d'appuyer les captures de code dans le dossier projet.

Ils donnent une explication lisible au lieu de simplement montrer du code.

---

# Étape 25 — Intégration NoSQL légère avec TinyDB

**Date :** 30/06/2026 au 03/07/2026  
**Statut :** validé

## Objectif

Ajouter une preuve NoSQL simple et contrôlée.

L'objectif n'était pas de remplacer SQLite, mais de montrer une expérimentation NoSQL cohérente avec le projet.

---

## Actions réalisées

* Installation de TinyDB.
* Ajout de TinyDB dans `requirements.txt`.
* Création d'un service Python dédié.
* Création d'un script de démonstration.
* Création d'une base JSON générée par TinyDB.
* Lecture des notes de progression.
* Affichage des notes sur la page d'accueil.

---

## Fichiers concernés

```text
requirements.txt
core/services/nosql_notes.py
scripts/__init__.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
core/views.py
templates/pages/home.html
docs/nosql/tinydb-integration.md
```

---

## Chaîne technique

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

---

## Décision prise

SQLite reste la base principale.

TinyDB sert uniquement à stocker des notes de progression sous forme documentaire NoSQL.

Cette intégration reste volontairement limitée pour éviter de complexifier la V1.

---

# Étape 26 — Corrections réalisées pendant l'intégration TinyDB

**Date :** 30/06/2026 au 03/07/2026  
**Statut :** validé

## Objectif

Corriger les problèmes rencontrés pendant l'intégration NoSQL afin d'obtenir une version propre et stable.

---

## Problèmes rencontrés

Plusieurs points ont dû être corrigés :

* chemin de la base TinyDB à stabiliser ;
* création du dossier `data/nosql/` ;
* gestion propre de l'ouverture et de la fermeture de la base ;
* typage Python trop vague ;
* nécessité de convertir les résultats TinyDB en liste exploitable ;
* lancement correct du script avec `python -m` ;
* ajout du fichier `scripts/__init__.py` ;
* vérification que TinyDB ne casse pas Django.

---

## Corrections appliquées

Le service NoSQL a été organisé pour :

* créer le dossier de données si nécessaire ;
* ouvrir la base TinyDB proprement ;
* fermer la base après utilisation ;
* créer des notes de démonstration seulement si la table est vide ;
* récupérer les notes par projet ;
* retourner des données exploitables par la vue Django.

---

## Validation

Commandes utilisées :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
```

Résultat :

* Django ne signale pas d'erreur ;
* les notes sont affichées dans le terminal ;
* la base JSON TinyDB est générée correctement.

---

# Étape 27 — Affichage des notes TinyDB sur la page d'accueil

**Date :** 03/07/2026  
**Statut :** validé

## Objectif

Ne pas garder TinyDB uniquement comme un test terminal.

L'objectif était d'afficher les notes NoSQL directement dans le site afin de prouver l'intégration réelle.

---

## Actions réalisées

* Import du service TinyDB dans `core/views.py`.
* Initialisation des notes de démonstration.
* Récupération des notes du projet Frostia Games.
* Envoi des notes au template `pages/home.html`.
* Ajout d'une section visible sur la page d'accueil.

---

## Fichiers modifiés

```text
core/views.py
templates/pages/home.html
core/services/nosql_notes.py
```

---

## Résultat obtenu

Une section de notes de progression apparaît sur la page d'accueil.

Elle affiche :

* le titre de la note ;
* le contenu ;
* le statut ;
* les tags.

---

## Validation

La page d'accueil affiche correctement les notes issues de TinyDB.

La fonctionnalité est donc démontrable avec les trois piliers :

* extrait du code ;
* explication ;
* capture du rendu final.

---

# Étape 28 — Création d'un compte temporaire de lecture seule

**Date :** 03/07/2026  
**Statut :** validé

## Objectif

Créer un accès limité à l'administration Django pour l'évaluation.

L'objectif était de permettre la consultation des données sans exposer les zones sensibles.

---

## Actions réalisées

* Création d'un groupe de lecture seule.
* Attribution des permissions de consultation uniquement.
* Création d'un utilisateur temporaire.
* Association de l'utilisateur au groupe.
* Vérification des accès depuis l'administration.

---

## Permissions conservées

Le compte peut consulter :

* les créations ;
* les projets jouables.

---

## Permissions non données

Le compte ne doit pas accéder :

* aux utilisateurs ;
* aux groupes ;
* aux permissions sensibles ;
* aux paramètres administrateur ;
* aux fonctions de modification importantes.

---

## Correction réalisée

Une première configuration donnait trop de visibilité dans l'administration.

Les permissions ont été corrigées pour limiter l'accès uniquement aux éléments utiles pour l'évaluation.

---

## Décision de sécurité

Les identifiants réels du compte temporaire ne doivent pas être écrits dans le dossier projet public.

Ils peuvent être transmis séparément uniquement si nécessaire.

---

# Étape 29 — Mise à jour de l'index documentaire

**Date :** 03/07/2026  
**Statut :** validé

## Objectif

Mettre à jour l'index de documentation afin qu'il reflète les ajouts récents.

---

## Fichier mis à jour

```text
doc/00-index-documentation.md
```

---

## Ajouts intégrés

L'index mentionne maintenant :

* la documentation complémentaire de renforcement ;
* le futur fichier `19-renforcement-dossier-projet.md` ;
* les livrables de conception ;
* le SQL natif ;
* le JavaScript dynamique ;
* TinyDB ;
* l'affichage des notes TinyDB ;
* le compte temporaire de lecture seule ;
* la règle des trois piliers ;
* les captures et preuves à préparer.

---

## Validation

L'index correspond mieux à l'état réel du projet.

Il conserve la structure historique du dossier `doc/` sans la casser.

---

# Étape 30 — Mise à jour du journal de bord

**Date :** 03/07/2026  
**Statut :** en cours de validation

## Objectif

Mettre à jour le journal de bord afin qu'il ne s'arrête pas à la première V1.

Le projet a connu plusieurs ajouts et corrections après la première version documentée.

Il était donc nécessaire de conserver une trace de ces éléments.

---

## Éléments à intégrer

Le journal doit maintenant intégrer :

* la branche de renforcement ;
* la documentation complémentaire ;
* les documents de conception ;
* le SQL natif ;
* la documentation JavaScript ;
* la documentation backend ;
* l'intégration TinyDB ;
* les corrections TinyDB ;
* l'affichage des notes sur l'accueil ;
* le compte lecture seule ;
* les corrections de permissions ;
* la mise à jour de l'index ;
* la préparation des preuves.

---

## Validation attendue

Le journal doit devenir la trace complète du projet, depuis la création de la V1 jusqu'au renforcement du dossier.

---

# Étape 31 — Préparation des captures et preuves

**Date :** 03/07/2026  
**Statut :** à finaliser

## Objectif

Préparer les preuves visuelles nécessaires au dossier final.

Le retour formateur indiquait qu'il fallait mieux prouver les compétences avec des éléments concrets.

---

## Règle retenue

Pour chaque compétence importante, il faut préparer trois éléments :

1. une capture du code ou un extrait de code ;
2. une explication du fonctionnement ;
3. une capture du rendu final lorsque la fonctionnalité produit un résultat visible.

---

## Preuves à préparer

Les captures doivent couvrir notamment :

* les modèles Django ;
* les vues Django ;
* le menu JavaScript ;
* le rendu mobile ;
* le SQL natif ;
* le script TinyDB ;
* l'affichage TinyDB sur l'accueil ;
* l'administration Django ;
* le compte temporaire de lecture seule ;
* Render ;
* GitHub ;
* Docker si nécessaire.

---

## Règle de sécurité

Aucune capture ne doit afficher :

* de mot de passe ;
* de clé secrète ;
* de variable d'environnement sensible ;
* d'identifiants privés.

---

# Étape 32 — État actuel après renforcement

**Date :** 03/07/2026  
**Statut :** implantation terminée

## Ce qui fonctionne maintenant

* Le serveur Django local fonctionne.
* `python manage.py check` ne signale pas d'erreur.
* Les pages principales sont accessibles.
* L'administration Django fonctionne.
* Les données SQLite remontent dans les templates.
* Le menu mobile JavaScript fonctionne.
* La conception est documentée.
* Les extraits SQL natifs sont documentés.
* TinyDB est installé.
* TinyDB est testé en terminal.
* Les notes TinyDB sont affichées sur l'accueil.
* Le compte temporaire de lecture seule fonctionne.
* Le dépôt Git est propre après commit.
* Le site reste déployé sur Render.

---

## Ce qui reste à faire

Les prochaines actions ne sont plus de l'implantation lourde.

Il reste à faire :

* relire les documents ;
* mettre à jour les fichiers restants ;
* préparer les captures propres ;
* vérifier les trois piliers pour chaque compétence importante ;
* intégrer les captures dans le dossier Word final ;
* préparer les annexes ;
* exporter le dossier en PDF ;
* faire le commit final de documentation.

---

## Ce qui ne doit plus être ajouté dans Frostia Games V1

Pour éviter d'élargir le périmètre, les éléments suivants restent reportés :

* PostgreSQL ;
* administration personnalisée ;
* upload serveur réel ;
* vrai lecteur de jeu ;
* mini-jeu intégré ;
* système de score ;
* page détail complète ;
* API REST ;
* espace privé complet ;
* Plotly.js ;
* tests automatisés complets ;
* refonte graphique complète.

Le projet est suffisamment renforcé pour répondre au retour formateur.

---

# Bilan complémentaire après renforcement

Le projet Frostia Games dispose maintenant d'une V1 Django fonctionnelle, documentée, déployée et renforcée.

Il contient désormais :

* une interface responsive ;
* un backend Django ;
* une base SQLite ;
* des modèles Django ;
* une administration Django ;
* un affichage dynamique ;
* un menu mobile en JavaScript ;
* Docker ;
* un déploiement Render ;
* un README racine ;
* un fichier de choix techniques ;
* un exemple de variables d'environnement ;
* une documentation SQL ;
* des extraits SQL natifs ;
* une expérimentation NoSQL avec TinyDB ;
* un affichage des notes TinyDB sur la page d'accueil ;
* une documentation de conception ;
* un MCD ;
* un diagramme de cas d'utilisation ;
* un diagramme de séquence ;
* une documentation de sécurité ;
* un compte temporaire de lecture seule ;
* un manuel utilisateur ;
* un changelog ;
* une documentation de tests ;
* une documentation de déploiement ;
* une documentation des limites ;
* une documentation des pistes explorées ;
* un plan de finalisation V1 ;
* une préparation des preuves pour le dossier final.

Le projet reste volontairement limité afin d'éviter une complexité inutile.

L'objectif n'est plus d'ajouter de nouvelles fonctionnalités dans Frostia Games V1.

L'objectif est maintenant de finaliser les documents, préparer les captures, vérifier les preuves et intégrer les éléments dans le dossier projet final.


