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
* des technologies envisagées mais non retenues.

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
* une solution plus proche de mes futurs projets de jeux vidéo ;
* une organisation plus proche d’un environnement applicatif C#.

Ces pistes restent intéressantes pour de futurs projets, car elles correspondent davantage à certaines préférences personnelles en matière de structure, de typage et de lisibilité du code.

---

## Point de vue technique personnel

J’accorde de l’importance à l’élégance d’une technologie.

Par élégance, j’entends :

* une syntaxe claire ;
* une structure logique ;
* un typage rassurant ;
* une séparation propre des responsabilités ;
* une architecture qui évite les solutions trop dispersées ;
* un langage qui aide le développeur à garder un code stable.

De ce point de vue, certaines technologies envisagées me semblaient plus intéressantes que Python, notamment pour leur structure ou leur typage.

Cependant, ce projet devait rester réaliste et terminé dans un délai raisonnable.

---

## Pourquoi ne pas avoir changé de technologie

Même si certaines pistes me paraissaient plus élégantes ou plus proches de mes préférences techniques, elles n’ont pas été retenues pour cette V1.

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

Python reste également lisible, rapide à mettre en place et suffisamment élégant lorsqu’il est utilisé avec méthode, documentation et règles de validation.

---

## Décision retenue

La décision prise est donc la suivante :

* conserver Django pour la V1 ;
* ne pas repartir de zéro avec une nouvelle technologie ;
* documenter les limites du choix technique ;
* reporter les expérimentations C# / ASP.NET / Razor à de futurs projets ;
* privilégier une version fonctionnelle, testable et maintenable ;
* éviter le changement de technologie en cours de route.

Ce choix permet de protéger le projet contre le risque de dérive technique.

---

## Bilan de cette réflexion

Cette réflexion est un point positif du projet.

Elle montre que les technologies mises de côté ne l’ont pas été par oubli, mais par choix de périmètre.

Le projet aurait pu partir vers une technologie plus proche de mes préférences, mais cela aurait augmenté le risque de ne pas terminer correctement la V1.

Le choix final est donc un compromis entre :

* mes préférences techniques ;
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

---

## Résultat obtenu

L’interface est devenue plus propre, plus lisible et plus professionnelle.

La modernisation lourde est volontairement reportée après la stabilisation du backend et de la documentation.

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
http://127.0.0.1:8000/
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

# Étape 11 — État actuel du projet

**Date :** 24/06/2026
**Statut :** en cours de stabilisation finale

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

---

## Ce qu’il reste à faire

* Vérifier la cohérence finale de la documentation.
* Nettoyer les textes temporaires dans l’administration.
* Préparer les captures écran.
* Préparer les extraits de code.
* Moderniser légèrement l’interface si nécessaire.
* Préparer la présentation du projet.
* Prévoir une solution d’hébergement Django en ligne plus tard.

---

# Bilan

Le projet Frostia Games dispose maintenant d’une V1 Django fonctionnelle.

Il contient :

* une interface responsive ;
* un backend Django ;
* une base SQLite ;
* une administration ;
* un affichage dynamique ;
* Docker ;
* une documentation SQL ;
* une réflexion NoSQL ;
* une documentation de sécurité ;
* un manuel utilisateur ;
* un changelog.

Le projet reste volontairement limité afin d’éviter une complexité inutile.

Le choix de ne pas changer de technologie en cours de route est une décision importante du projet.

Même si certaines technologies auraient pu correspondre davantage à mes préférences personnelles, la priorité a été donnée à une V1 terminée, stable, documentée et présentable.

L’objectif est maintenant de stabiliser, documenter et présenter le projet proprement.
