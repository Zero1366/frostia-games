# Index de la documentation - Frostia Games

## Objectif

Ce dossier regroupe la documentation technique, fonctionnelle et organisationnelle du projet **Frostia Games**.

L'objectif de cette documentation est de conserver une trace claire :

* des choix réalisés ;
* des étapes validées ;
* des fichiers modifiés ;
* des fonctionnalités implantées ;
* des limites volontaires de la V1 ;
* des évolutions prévues ;
* des pistes explorées mais non retenues ;
* des vérifications réalisées ;
* du déploiement en ligne.

Chaque partie importante du projet est documentée afin que le projet reste compréhensible, maintenable et présentable.

---

## Rôle de cette documentation

La documentation permet de montrer que le projet n'a pas été construit au hasard.

Elle explique :

* pourquoi Django a été retenu ;
* comment le projet est organisé ;
* comment le projet peut être lancé ;
* comment les données sont gérées ;
* comment l'administration Django fonctionne ;
* comment le projet est déployé sur Render ;
* quelles limites sont assumées dans la V1 ;
* quelles évolutions pourront être ajoutées plus tard.

Cette documentation sert aussi de support pour présenter le projet comme une V1 stable, documentée et évolutive.

---

## Structure actuelle de la documentation

```text
doc/
├─ sql/
│  ├─ nosql.md
│  └─ schema.sql
│
├─ 00-index-documentation.md
├─ 01-modernisation-interface.md
├─ 02-journal-de-bord.md
├─ 03-modelisation-backend.md
├─ 04-docker-et-lancement.md
├─ 05-securite-backend.md
├─ 06-manuel-utilisateur.md
├─ 07-base-de-donnees.md
├─ 08-changelog.md
├─ 09-deploiement-render.md
├─ 10-bilan-v1-frostia-games.md
├─ 11-installation-locale.md
├─ 12-architecture.md
├─ 13-test-et-vérification.md
├─ 14-Capture-et Preuve.md
├─ 15-limites-et-évolutions.md
├─ 16-presentation-projet-2.md
├─ 17-pistes-explorees-et-non-retenues.md
└─ 18-plan-finalisation-v1.md
```

---

# 00 - Index de la documentation

**Fichier :** `00-index-documentation.md`

Ce document sert de point d'entrée pour toute la documentation du projet.

Il présente :

* l'organisation générale de la documentation ;
* les fichiers disponibles ;
* le rôle de chaque document ;
* l'état actuel de la V1 ;
* les fonctionnalités implantées ;
* les limites assumées ;
* les évolutions prévues ;
* les commandes principales ;
* les règles de validation.

---

# 01 - Modernisation de l'interface

**Fichier :** `01-modernisation-interface.md`

Ce document présente le travail réalisé sur l'interface visuelle du site.

Il explique notamment :

* la direction graphique retenue ;
* les choix de couleurs ;
* l'organisation de la page d'accueil ;
* la sidebar ;
* les cartes de contenu ;
* le responsive desktop et mobile ;
* les améliorations visuelles prévues après stabilisation de la V1.

Ce document permet de garder une trace des choix UI/UX sans mélanger la partie visuelle avec la partie backend.

---

# 02 - Journal de bord

**Fichier :** `02-journal-de-bord.md`

Ce document consigne les étapes réalisées au fur et à mesure du développement.

Il indique pour chaque étape :

* ce qui a été fait ;
* pourquoi cela a été fait ;
* quels fichiers ont été modifiés ;
* comment vérifier que cela fonctionne ;
* les problèmes rencontrés ;
* les décisions prises ;
* les prochaines actions.

Le journal de bord permet de montrer que le projet a été construit progressivement, avec une trace claire des décisions prises.

---

# 03 - Modélisation backend

**Fichier :** `03-modelisation-backend.md`

Ce document présente la modélisation backend du projet.

Il contient :

* les modèles Django ;
* le schéma relationnel simplifié ;
* le MCD simplifié ;
* les cas d'utilisation ;
* les diagrammes de séquence ;
* le rôle de l'ORM Django ;
* les limites de la V1 ;
* les évolutions prévues.

Ce fichier répond aux attendus liés à la modélisation, notamment le MCD, les cas d'utilisation et les diagrammes de séquence.

---

# 04 - Docker et lancement du projet

**Fichier :** `04-docker-et-lancement.md`

Ce document présente les informations liées au lancement local et au lancement avec Docker.

Il contient :

* les prérequis ;
* les commandes de lancement local ;
* les commandes de lancement avec Docker ;
* le rôle du `Dockerfile` ;
* le rôle de `docker-compose.yml` ;
* le rôle de `.dockerignore` ;
* le rôle de `requirements.txt` ;
* les commandes de vérification ;
* les limites de la configuration actuelle.

Ce document permet de démontrer que le projet peut être lancé dans un environnement reproductible.

---

# 05 - Sécurité backend

**Fichier :** `05-securite-backend.md`

Ce document regroupe les choix liés à la sécurité backend.

Il traite notamment :

* le mode `DEBUG` ;
* la clé secrète Django ;
* `ALLOWED_HOSTS` ;
* l'utilisation de l'ORM Django ;
* l'absence de SQL brut dans les vues ;
* la protection contre les injections SQL ;
* l'administration Django protégée ;
* la protection CSRF ;
* l'échappement automatique dans les templates ;
* les fichiers médias ;
* l'absence de vrai upload serveur dans la V1 ;
* l'absence de téléchargement public d'exécutable ou de fichier ZIP ;
* les protections prévues pour une future version plus avancée.

Ce document permet de montrer que la sécurité est prise en compte, même si la V1 reste volontairement limitée.

---

# 06 - Manuel utilisateur

**Fichier :** `06-manuel-utilisateur.md`

Ce document explique comment utiliser la V1 du projet.

Il contient :

* le lancement local ;
* le lancement avec Docker ;
* les pages principales ;
* l'accès à l'administration Django ;
* l'ajout d'une création ;
* l'ajout d'un projet jouable ;
* les fonctionnalités disponibles ;
* les fonctionnalités non implantées dans la V1 ;
* les vérifications à faire avant une démonstration.

Ce document sert de manuel d'utilisation pour relancer, tester et présenter le projet.

---

# 07 - Base de données

**Fichier :** `07-base-de-donnees.md`

Ce document présente la partie base de données du projet.

Il explique :

* le rôle de SQLite dans la V1 ;
* les modèles Django ;
* les migrations ;
* les tables créées ;
* le schéma logique de la base ;
* ce qui est stocké en base ;
* ce qui n'est pas stocké en base ;
* le rôle de l'administration Django ;
* le rôle de l'ORM ;
* les évolutions possibles vers PostgreSQL.

Documents associés :

* `doc/sql/schema.sql`
* `doc/sql/nosql.md`

Le fichier `schema.sql` contient un équivalent SQL documentaire avec des instructions `CREATE TABLE` et des exemples `INSERT INTO`.

Le fichier `nosql.md` présente la réflexion autour d'une future intégration NoSQL, sans l'implanter artificiellement dans la V1.

---

# 08 - Changelog

**Fichier :** `08-changelog.md`

Ce document sert à noter les changements importants du projet.

Il contient :

* les étapes importantes du développement ;
* le résumé de chaque modification ;
* les fichiers concernés ;
* les vérifications effectuées ;
* le statut de validation.

Il permet de garder une trace claire de l'évolution du projet, notamment :

* création du projet Django ;
* ajout des pages principales ;
* ajout des modèles ;
* ajout de l'administration Django ;
* connexion des vues à la base SQLite ;
* ajout de Docker ;
* ajout du schéma SQL ;
* ajout de la documentation backend ;
* nettoyage des alertes inutiles dans VS Code ;
* ajout du déploiement Render ;
* ajout de la documentation finale de V1.

---

# 09 - Déploiement Render

**Fichier :** `09-deploiement-render.md`

Ce document présente le déploiement du projet sur Render.

Il explique :

* l'objectif du déploiement ;
* la plateforme utilisée ;
* la configuration Render ;
* les variables d'environnement ;
* le rôle de `build.sh` ;
* le rôle de Gunicorn ;
* la commande de build ;
* la commande de démarrage ;
* les problèmes rencontrés ;
* les vérifications après déploiement ;
* les limites de l'offre gratuite Render.

Le projet est déployé en ligne à l'adresse :

```text
https://frostia-games.onrender.com
```

Ce document prouve que le projet fonctionne en dehors de l'environnement local.

---

# 10 - Bilan V1 Frostia Games

**Fichier :** `10-bilan-v1-frostia-games.md`

Ce document présente le bilan de la V1.

Il contient :

* l'objectif de la V1 ;
* l'état global du projet ;
* les pourcentages d'avancement estimés ;
* ce qui est terminé ;
* ce qui reste à améliorer ;
* ce qui est volontairement reporté ;
* la conclusion sur l'état actuel du projet.

Ce fichier permet de montrer que la V1 est évaluée de manière réaliste, sans la présenter comme une version finale complète.

---

# 11 - Installation locale

**Fichier :** `11-installation-locale.md`

Ce document regroupe les informations liées à l'installation locale du projet.

Il contient :

* la création de l'environnement virtuel ;
* l'activation du `.venv` ;
* l'installation des dépendances ;
* la création du projet Django ;
* les premières commandes de vérification ;
* les problèmes rencontrés lors de l'installation ;
* les commandes utiles pour relancer le projet.

Ce fichier remplace l'ancien fichier `installation-django.md`.

Il sert de trace technique sur la mise en place initiale du socle Django.

---

# 12 - Architecture

**Fichier :** `12-architecture.md`

Ce document présente l'architecture du projet.

Il explique :

* la structure générale du projet ;
* le rôle du dossier `frostia_config` ;
* le rôle des applications Django ;
* le rôle des templates ;
* le rôle des fichiers statiques ;
* le fonctionnement des vues ;
* le fonctionnement de la base SQLite ;
* le rôle de l'administration Django ;
* le fonctionnement du déploiement ;
* les limites actuelles de l'architecture ;
* les évolutions possibles.

Ce document permet de comprendre comment les différentes parties du projet fonctionnent ensemble.

---

# 13 - Tests et vérifications

**Fichier :** `13-test-et-vérification.md`

Ce document présente les tests et vérifications réalisés sur la V1.

Il contient :

* les tests du lancement local ;
* les tests des pages principales ;
* les tests de navigation ;
* les tests du responsive ;
* les tests des modèles Django ;
* les tests de l'administration ;
* les tests Docker ;
* les tests du déploiement Render ;
* les tests des variables d'environnement ;
* les vérifications de sécurité minimale ;
* les problèmes rencontrés pendant les tests.

Ce fichier montre que la V1 n'a pas seulement été développée, mais aussi vérifiée.

---

# 14 - Captures et preuves

**Fichier :** `14-Capture-et Preuve.md`

Ce document liste les captures d'écran à conserver pour le dossier projet.

Il prévoit notamment :

* les captures du site public ;
* les captures responsive ;
* les captures de l'administration Django ;
* les captures Render ;
* les captures du code ;
* les captures de validation technique ;
* les captures de documentation.

Ce document sert de checklist pour préparer les preuves visuelles du projet.

Il rappelle aussi qu'aucune capture ne doit afficher de mot de passe, de clé secrète ou de valeur sensible.

---

# 15 - Limites et évolutions

**Fichier :** `15-limites-et-évolutions.md`

Ce document présente les limites actuelles de la V1 et les évolutions possibles.

Il explique notamment pourquoi certaines fonctionnalités ne sont pas encore intégrées :

* PostgreSQL ;
* compte jury temporaire ;
* administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* graphiques Plotly.js ;
* espace privé complet ;
* tests automatisés complets.

Ce document montre que les limites du projet ne sont pas des oublis, mais des choix de périmètre.

---

# 16 - Présentation du projet 2

**Fichier :** `16-presentation-projet-2.md`

Ce document présente Frostia Games comme proposition de second projet.

Il explique :

* la nature du projet ;
* le positionnement de la V1 ;
* pourquoi le projet peut être proposé comme projet 2 ;
* les fonctionnalités réalisées ;
* les choix techniques ;
* les compétences mises en avant ;
* les limites assumées ;
* les prochaines étapes avant présentation.

Ce document sert de base pour défendre le projet dans un dossier ou une présentation.

---

# 17 - Pistes explorées et non retenues

**Fichier :** `17-pistes-explorees-et-non-retenues.md`

Ce document présente les pistes techniques et fonctionnelles envisagées, mais non intégrées dans la V1.

Il traite notamment :

* C# / ASP.NET Core / Razor ;
* Django ;
* PostgreSQL ;
* compte jury temporaire ;
* administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* Plotly.js ;
* espace privé complet ;
* sauvegardes automatiques ;
* refonte graphique complète ;
* tests automatisés complets ;
* gestion complète des médias.

Ce document montre que plusieurs pistes ont été explorées, puis reportées pour éviter de transformer la V1 en projet trop complexe.

---

# 18 - Plan de finalisation V1

**Fichier :** `18-plan-finalisation-v1.md`

Ce document présente les dernières actions à réaliser avant de considérer la V1 comme terminée.

Il contient :

* la vérification du contenu des pages ;
* la vérification du responsive ;
* la préparation des captures ;
* la vérification du README racine ;
* la vérification du fichier `CHOIX_TECHNIQUES.md` ;
* la préparation des maquettes Figma ;
* la vérification technique finale ;
* la vérification Render ;
* la relecture de la documentation ;
* le commit final ;
* le déploiement final Render.

Ce fichier sert de checklist de fin de V1.

---

# Documents SQL associés

## `doc/sql/schema.sql`

Ce fichier présente l'équivalent SQL simplifié des tables utilisées par Django.

Il contient :

* la table `creations_creation` ;
* la table `playable_playableproject` ;
* des instructions `CREATE TABLE` ;
* des exemples `INSERT INTO` ;
* des commentaires sur le rôle des tables.

Dans le projet réel, les tables sont créées par les migrations Django.

Le fichier SQL sert à documenter la structure de la base pour le dossier projet.

---

## `doc/sql/nosql.md`

Ce document présente la réflexion autour d'une future intégration NoSQL.

Dans la V1 actuelle, aucune base NoSQL n'est implantée.

Ce choix est volontaire afin de conserver une V1 stable, simple et maîtrisable.

Le document explique :

* pourquoi NoSQL n'est pas implanté dans la V1 ;
* dans quels cas NoSQL pourrait devenir utile ;
* un exemple de document NoSQL possible ;
* les différences entre la base SQL actuelle et une future base NoSQL ;
* la roadmap possible pour intégrer MongoDB ou une autre solution NoSQL.

---

# Fichiers importants à la racine

La racine du projet contient aussi plusieurs fichiers importants.

```text
frostia-games/
├─ README.md
├─ CHOIX_TECHNIQUES.md
├─ .env.example
├─ .gitignore
├─ .dockerignore
├─ build.sh
├─ manage.py
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ pyproject.toml
└─ db.sqlite3
```

## `README.md`

Le fichier `README.md` présente rapidement le projet.

Il sert de point d'entrée pour une personne qui découvre le dépôt GitHub.

Il doit expliquer :

* le rôle du projet ;
* les technologies utilisées ;
* l'installation locale ;
* le lancement du serveur ;
* le lancement Docker ;
* le déploiement Render ;
* les limites de la V1 ;
* les évolutions prévues.

---

## `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` présente les choix techniques du projet.

Il explique notamment :

* pourquoi Django a été retenu ;
* pourquoi C# / Razor a été envisagé mais reporté ;
* pourquoi certaines pistes sont volontairement repoussées ;
* comment le projet évite de devenir une usine à gaz.

---

## `.env.example`

Le fichier `.env.example` montre les variables d'environnement nécessaires au projet sans afficher les vraies valeurs sensibles.

Variables principales :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Ce fichier permet de comprendre la configuration attendue sans exposer les secrets.

---

## `build.sh`

Le fichier `build.sh` est utilisé par Render pour préparer le projet avant le lancement.

Il permet notamment :

* d'installer les dépendances ;
* de collecter les fichiers statiques ;
* d'appliquer les migrations ;
* de créer un superutilisateur si les variables nécessaires sont présentes.

---

# État actuel de la V1

La V1 de Frostia Games contient actuellement :

* une structure Django fonctionnelle ;
* trois pages principales ;
* une base SQLite ;
* des modèles Django ;
* des migrations ;
* une administration Django ;
* un affichage dynamique des données ;
* une interface préparatoire pour les projets jouables ;
* un lancement local ;
* un lancement Docker ;
* un déploiement Render ;
* une documentation SQL ;
* une réflexion NoSQL ;
* une documentation de modélisation ;
* une documentation de sécurité ;
* une documentation Docker ;
* un manuel utilisateur ;
* un changelog ;
* un bilan V1 ;
* une documentation de déploiement ;
* une documentation des tests ;
* une documentation des limites et évolutions.

---

# Fonctionnalités implantées

La V1 contient :

* la page d'accueil ;
* la page Mes créations ;
* la page Projets jouables ;
* une navigation responsive ;
* un menu mobile ;
* une base SQLite ;
* les modèles Django nécessaires à la V1 ;
* l'administration Django ;
* l'affichage des créations depuis la base ;
* l'affichage des projets jouables depuis la base ;
* une interface préparatoire de sélection de fichier ;
* Docker ;
* un déploiement Render ;
* une documentation technique complète.

---

# Limites assumées et éléments reportés

La V1 ne contient pas encore :

* de vraie plateforme complète de gestion de projets ;
* de PostgreSQL ;
* de compte jury temporaire ;
* d'administration personnalisée ;
* de vrai upload serveur ;
* de vrai lecteur de jeu ou de vidéo ;
* de page détail complète pour chaque projet ;
* d'API REST ;
* de système de comptes publics ;
* de rôles avancés ;
* de base NoSQL connectée ;
* de graphiques Plotly.js ;
* de tests automatisés complets.

Ces limites sont volontaires afin de conserver un projet stable, testable, maintenable et présentable.

---

# Règle de documentation

Une étape du projet est considérée comme terminée uniquement si :

* le code fonctionne ;
* `python manage.py check` ne signale pas d'erreur ;
* les alertes importantes ont été traitées ;
* la fonctionnalité a été testée dans le navigateur ;
* le comportement a été vérifié ;
* la documentation correspondante est mise à jour ;
* les modifications sont sauvegardées avec Git.

L'objectif est d'éviter que le projet évolue sans trace claire.

---

# Commandes principales

## Lancement local

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

## Vérification Django

```powershell
python manage.py check
```

## Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Création d'un administrateur local

```powershell
python manage.py createsuperuser
```

## Lancement Docker

```powershell
docker compose up --build
```

## Vérification dans Docker

```powershell
docker compose exec web python manage.py check
```

## Git

```powershell
git status
git add .
git commit -m "Update documentation"
git push
```

---

# Prochaines actions

Les prochaines actions prévues sont :

1. Relire les pages publiques du site.
2. Vérifier le responsive mobile.
3. Préparer les captures d'écran.
4. Vérifier le README à la racine.
5. Vérifier le fichier `CHOIX_TECHNIQUES.md`.
6. Préparer les maquettes Figma si nécessaire.
7. Vérifier le site en local.
8. Vérifier le site sur Render.
9. Vérifier l'administration Django.
10. Faire le commit final.
11. Vérifier que le dépôt GitHub est propre.

---

# Conclusion

La documentation de Frostia Games sert à montrer que le projet est construit progressivement, avec une séparation claire entre :

* ce qui est implanté ;
* ce qui est documenté ;
* ce qui est testé ;
* ce qui est déployé ;
* ce qui est volontairement reporté ;
* ce qui pourra être ajouté dans une version future.

L'objectif n'est pas d'empiler les fonctionnalités, mais de présenter une base Django propre, documentée, déployée et évolutive.
