# Index de la documentation - Frostia Games

## Objectif

Ce dossier regroupe la documentation technique, fonctionnelle et organisationnelle du projet **Frostia Games**.

L'objectif de cette documentation est de conserver une trace claire :

* des choix réalisés ;
* des étapes validées ;
* des fichiers modifiés ;
* des fonctionnalités implantées ;
* des limites volontaires de la V1 ;
* des évolutions prévues.

Chaque partie importante du projet doit être documentée afin que le projet reste compréhensible, maintenable et présentable.

---

# 00 - Index de la documentation

**Fichier :** `00-index-documentation.md`

Ce document sert de point d'entrée pour toute la documentation du projet.

Il présente :

* l'organisation générale de la documentation ;
* les fichiers disponibles ;
* le rôle de chaque document ;
* les règles de validation d'une étape ;
* l'état actuel de la V1 ;
* les limites volontaires du projet ;
* les prochaines actions.

---

# 01 - Modernisation de l'interface

**Fichier :** `01-modernisation-interface.md`

Ce document présente le travail réalisé sur l'interface visuelle du site.

Il doit expliquer :

* la direction graphique retenue ;
* les choix de couleurs ;
* l'organisation de la page d'accueil ;
* la sidebar ;
* les cartes de contenu ;
* le responsive desktop et mobile ;
* les retouches visuelles prévues après stabilisation du backend.

Ce document permet de garder une trace des choix UI/UX sans mélanger la partie visuelle avec le backend.

---

# 02 - Journal de bord

**Fichier :** `02-journal-de-bord.md`

Ce document consigne les étapes réalisées au fur et à mesure du développement.

Il doit indiquer pour chaque étape :

* ce qui a été fait ;
* pourquoi cela a été fait ;
* quels fichiers ont été modifiés ;
* comment vérifier que cela fonctionne ;
* les problèmes rencontrés ;
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

Ce fichier répond directement aux attendus liés à la modélisation, notamment le MCD, les cas d'utilisation et les diagrammes de séquence.

---

# 04 - Docker et lancement du projet

**Fichier :** `04-docker-et-lancement.md`

Ce document présente les informations liées au lancement local, au lancement avec Docker et au futur déploiement du projet.

Il contient :

* les prérequis ;
* les commandes de lancement local ;
* les commandes de lancement avec Docker ;
* le rôle du `Dockerfile` ;
* le rôle de `docker-compose.yml` ;
* le rôle de `.dockerignore` ;
* le rôle de `requirements.txt` ;
* les commandes de vérification ;
* les limites de la configuration actuelle ;
* les pistes de déploiement futur.

Ce document permet de démontrer que le projet peut être lancé dans un environnement reproductible.

---

# 05 - Sécurité backend

**Fichier :** `05-securite-backend.md`

Ce document regroupe les choix liés à la sécurité backend.

Il traite :

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
* les futurs uploads internes ;
* l'absence de vrai upload serveur dans la V1 ;
* l'absence de téléchargement public d'exécutable ou de fichier ZIP ;
* les protections prévues pour une future mise en production.

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

Le fichier `schema.sql` contient un équivalent SQL documentaire avec des instructions `CREATE TABLE` et `INSERT INTO`.

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
* nettoyage des alertes inutiles dans VS Code.

---

# 09 - Installation Django

**Fichier :** `installation-django.md`

Ce document regroupe les informations liées à l'installation initiale de Django et à la mise en place du projet.

Il peut contenir :

* les commandes d'installation ;
* la création de l'environnement virtuel ;
* l'installation des dépendances ;
* la création du projet Django ;
* les premières commandes de vérification ;
* les problèmes rencontrés lors de l'installation.

Ce fichier sert de trace technique sur la mise en place initiale du socle Django.

---

# 10 - SQL documentaire

## Fichier `doc/sql/schema.sql`

Ce fichier présente l'équivalent SQL simplifié des tables utilisées par Django.

Il contient :

* la table `creations_creation` ;
* la table `playable_playableproject` ;
* des instructions `CREATE TABLE` ;
* des exemples `INSERT INTO` ;
* des commentaires sur le rôle des tables.

Dans le projet réel, les tables sont créées par les migrations Django. Le fichier SQL sert à documenter la structure de la base pour le dossier projet.

---

# 11 - Réflexion NoSQL

## Fichier `doc/sql/nosql.md`

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

# Structure actuelle de documentation

```text
doc/
├─ sql/
│  ├─ nosql.md
│  └─ schema.sql
├─ 00-index-documentation.md
├─ 01-modernisation-interface.md
├─ 02-journal-de-bord.md
├─ 03-modelisation-backend.md
├─ 04-docker-et-lancement.md
├─ 05-securite-backend.md
├─ 06-manuel-utilisateur.md
├─ 07-base-de-donnees.md
├─ 08-changelog.md
└─ installation-django.md
```

---

# État actuel de la V1

La V1 de Frostia Games contient actuellement :

* une structure Django fonctionnelle ;
* trois pages principales ;
* une base SQLite ;
* deux modèles Django ;
* des migrations ;
* une administration Django ;
* un affichage dynamique des données ;
* une interface préparatoire pour les projets jouables ;
* un lancement local ;
* un lancement Docker ;
* une documentation SQL ;
* une réflexion NoSQL ;
* une documentation de modélisation ;
* une documentation de sécurité ;
* une documentation Docker ;
* un manuel utilisateur ;
* un changelog.

---

# Fonctionnalités implantées

La V1 contient :

* la page d'accueil ;
* la page Mes créations ;
* la page Projets jouables ;
* une navigation responsive ;
* un menu mobile ;
* une base SQLite ;
* le modèle `Creation` ;
* le modèle `PlayableProject` ;
* l'administration Django ;
* l'affichage des créations depuis la base ;
* l'affichage des projets jouables depuis la base ;
* une interface préparatoire de sélection de fichier ;
* Docker ;
* des fichiers de documentation.

---

# Fonctionnalités préparées mais non implantées

Certaines fonctionnalités sont préparées mais non finalisées :

* fiche détaillée de projet ;
* vrai upload serveur ;
* vrai lecteur vidéo ;
* contenus jouables intégrés ;
* base NoSQL ;
* hébergement Django en ligne ;
* configuration de production ;
* PostgreSQL.

Ces fonctionnalités sont volontairement placées en roadmap afin d'éviter d'élargir trop vite le périmètre du projet.

---

# Limites assumées de la V1

La V1 ne contient pas encore :

* de vrai upload serveur ;
* de vrai lecteur vidéo ;
* de page détail complète pour chaque projet ;
* d'API REST ;
* de système de comptes publics ;
* de rôles avancés ;
* de base NoSQL connectée ;
* de base PostgreSQL ;
* de déploiement de production complet.

Ces limites sont volontaires afin de conserver un projet stable, testable et maintenable.

---

# Règle de documentation

Une étape du projet est considérée comme terminée uniquement si :

* le code fonctionne ;
* `python manage.py check` ne signale pas d'erreur ;
* Ruff ne signale pas d'erreur importante ;
* les alertes de typage inutiles ont été corrigées ou neutralisées proprement ;
* la fonctionnalité a été testée dans le navigateur ;
* la documentation correspondante est mise à jour.

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

## Création d'un administrateur

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

---

# Prochaines actions

Les prochaines actions prévues sont :

1. Vérifier la cohérence finale de la documentation.
2. Nettoyer les derniers textes temporaires dans l'administration.
3. Préparer les captures d'écran.
4. Préparer les extraits de code à intégrer au dossier.
5. Moderniser légèrement l'interface si nécessaire.
6. Préparer la présentation du projet.
7. Prévoir un futur hébergement compatible Django.

---

# Conclusion

La documentation de Frostia Games sert à montrer que le projet est construit progressivement, avec une séparation claire entre :

* ce qui est implanté ;
* ce qui est préparé ;
* ce qui est volontairement reporté ;
* ce qui sera ajouté dans une version future.

L'objectif n'est pas d'empiler les fonctionnalités, mais de présenter une base Django propre, documentée et évolutive.
