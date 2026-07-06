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
* du déploiement en ligne ;
* des preuves préparées pour le dossier projet.

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
* comment la base SQLite est utilisée ;
* comment le JavaScript dynamique du menu mobile fonctionne ;
* comment les extraits SQL natifs sont documentés ;
* comment une expérimentation NoSQL légère a été intégrée avec TinyDB ;
* comment les notes TinyDB sont affichées sur la page d'accueil ;
* comment un compte temporaire de lecture seule peut être utilisé pour l'évaluation ;
* comment le projet est déployé sur Render ;
* quelles limites sont assumées dans la V1 ;
* quelles évolutions pourront être ajoutées plus tard.

Cette documentation sert aussi de support pour présenter le projet comme une V1 stable, documentée, testée, déployée et évolutive.

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
├─ 18-plan-finalisation-v1.md
└─ 19-renforcement-dossier-projet.md
```

---

## Documentation complémentaire de renforcement

En complément de la documentation principale présente dans le dossier `doc/`, plusieurs documents techniques complémentaires ont été ajoutés afin de renforcer le dossier projet après le retour formateur.

Ces documents complémentaires concernent notamment :

* la conception avec MCD, diagramme de cas d'utilisation et diagramme de séquence ;
* les extraits SQL natifs avec `CREATE TABLE` et `INSERT INTO` ;
* la documentation du JavaScript dynamique du menu mobile ;
* l'intégration NoSQL légère avec TinyDB ;
* l'affichage des notes TinyDB sur la page d'accueil ;
* la documentation des vues, routes et modèles Django ;
* la préparation des captures et preuves pour les annexes.

Le fichier `doc/19-renforcement-dossier-projet.md` sert de synthèse pour relier ces documents complémentaires à la documentation principale.

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
* les règles de validation ;
* les documents complémentaires ajoutés pour renforcer le dossier projet ;
* les preuves à préparer pour les annexes.

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
* le menu mobile ;
* l'affichage des notes de progression sur l'accueil ;
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

Il doit aussi intégrer les étapes récentes :

* ajout des livrables de conception ;
* ajout des extraits SQL natifs ;
* ajout de la documentation JavaScript ;
* ajout de TinyDB ;
* affichage des notes TinyDB sur la page d'accueil ;
* création du compte temporaire de lecture seule ;
* préparation des preuves et captures pour le dossier projet.

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

Documents complémentaires associés :

* document de MCD ;
* document de cas d'utilisation ;
* document de diagramme de séquence ;
* documentation des modèles Django ;
* documentation des vues et routes.

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

Il sert également de preuve technique pour le dossier projet, notamment avec les captures prévues :

* fichier `Dockerfile` ;
* fichier `docker-compose.yml` ;
* commande `docker compose up --build` ;
* vérification avec `python manage.py check` dans le conteneur.

---

# 05 - Sécurité backend

**Fichier :** `05-securite-backend.md`

Ce document regroupe les choix liés à la sécurité backend.

Il traite notamment :

* le mode `DEBUG` ;
* la clé secrète Django ;
* `ALLOWED_HOSTS` ;
* l'utilisation de l'ORM Django ;
* l'absence de SQL brut non contrôlé dans les vues ;
* la protection contre les injections SQL ;
* l'administration Django protégée ;
* le compte temporaire de lecture seule pour l'évaluation ;
* la protection CSRF ;
* l'échappement automatique dans les templates ;
* les fichiers médias ;
* l'absence de vrai upload serveur dans la V1 ;
* l'absence de téléchargement public d'exécutable ou de fichier ZIP ;
* les protections prévues pour une future version plus avancée.

Ce document permet de montrer que la sécurité est prise en compte, même si la V1 reste volontairement limitée.

Le compte temporaire de lecture seule permet de donner un accès limité à l'administration sans exposer les comptes utilisateurs, les groupes ou les réglages sensibles.

Les identifiants réels de ce compte ne doivent pas être écrits directement dans le dossier projet public.

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
* l'utilisation du compte temporaire de lecture seule ;
* les fonctionnalités disponibles ;
* les fonctionnalités non implantées dans la V1 ;
* les vérifications à faire avant une démonstration.

Ce document sert de manuel d'utilisation pour relancer, tester et présenter le projet.

Il doit rappeler que les identifiants réels du compte temporaire ne doivent pas être écrits directement dans le dossier projet public.

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
* les extraits SQL natifs ;
* les exemples `CREATE TABLE` ;
* les exemples `INSERT INTO` ;
* ce qui est stocké en base ;
* ce qui n'est pas stocké en base ;
* le rôle de l'administration Django ;
* le rôle de l'ORM ;
* le rôle complémentaire de TinyDB ;
* les évolutions possibles vers PostgreSQL.

Documents associés :

* `doc/sql/schema.sql`
* `doc/sql/nosql.md`

Documents complémentaires associés :

* fichier SQL natif pour la table des créations ;
* fichier SQL natif pour la table des projets jouables ;
* fichier d'exemples `INSERT INTO` ;
* documentation SQL native ;
* documentation TinyDB.

Le fichier `schema.sql` contient un équivalent SQL documentaire avec des instructions `CREATE TABLE` et des exemples `INSERT INTO`.

Les fichiers SQL complémentaires contiennent des extraits SQL natifs issus des migrations Django.

Le fichier d'exemples `INSERT INTO` contient des exemples d'insertion de données.

La partie NoSQL ne remplace pas SQLite. Elle sert à montrer une expérimentation complémentaire avec TinyDB pour stocker et afficher des notes de progression liées au projet.

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
* ajout des extraits SQL natifs ;
* ajout de la documentation backend ;
* ajout de la documentation de conception ;
* ajout de la documentation JavaScript ;
* ajout de TinyDB ;
* ajout de l'affichage des notes TinyDB sur l'accueil ;
* ajout du compte temporaire de lecture seule ;
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

Les captures Render devront être préparées sans afficher de secret, de mot de passe ou de variable sensible.

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

Le bilan doit maintenant préciser que les éléments suivants sont terminés :

* conception avec MCD, cas d'utilisation et diagramme de séquence ;
* JavaScript dynamique du menu mobile ;
* SQL natif avec `CREATE TABLE` et `INSERT INTO` ;
* expérimentation NoSQL TinyDB ;
* affichage des notes TinyDB sur la page d'accueil ;
* compte temporaire de lecture seule ;
* préparation des preuves pour les annexes.

---

# 11 - Installation locale

**Fichier :** `11-installation-locale.md`

Ce document regroupe les informations liées à l'installation locale du projet.

Il contient :

* la création de l'environnement virtuel ;
* l'activation du `.venv` ;
* l'installation des dépendances ;
* l'installation de Django ;
* l'installation de TinyDB ;
* la création du projet Django ;
* les premières commandes de vérification ;
* les problèmes rencontrés lors de l'installation ;
* les commandes utiles pour relancer le projet.

Ce fichier remplace l'ancien fichier `installation-django.md`.

Il sert de trace technique sur la mise en place initiale du socle Django.

TinyDB fait maintenant partie des dépendances du projet et doit être présent dans `requirements.txt`.

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
* le rôle de TinyDB pour les notes de progression ;
* le rôle du service NoSQL ;
* le rôle de l'administration Django ;
* le fonctionnement du déploiement ;
* les limites actuelles de l'architecture ;
* les évolutions possibles.

Ce document permet de comprendre comment les différentes parties du projet fonctionnent ensemble.

La chaîne NoSQL ajoutée est la suivante :

```text
TinyDB
→ service Python NoSQL
→ vue Django
→ template de la page d'accueil
→ affichage sur le site
```

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
* les tests du compte temporaire de lecture seule ;
* les tests Docker ;
* les tests du déploiement Render ;
* les tests des variables d'environnement ;
* les tests TinyDB ;
* les tests d'affichage des notes NoSQL sur l'accueil ;
* les vérifications de sécurité minimale ;
* les problèmes rencontrés pendant les tests.

Ce fichier montre que la V1 n'a pas seulement été développée, mais aussi vérifiée.

Commandes importantes à conserver comme preuve :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

---

# 14 - Captures et preuves

**Fichier :** `14-Capture-et Preuve.md`

Ce document liste les captures d'écran à conserver pour le dossier projet.

Il prévoit notamment :

* les captures du site public ;
* les captures responsive ;
* les captures du menu mobile ;
* les captures du JavaScript dynamique ;
* les captures de l'administration Django ;
* les captures du compte temporaire de lecture seule ;
* les captures SQL ;
* les captures NoSQL TinyDB ;
* les captures Render ;
* les captures GitHub ;
* les captures Docker ;
* les captures du code ;
* les captures de validation technique ;
* les captures de documentation.

Ce document sert de checklist pour préparer les preuves visuelles du projet.

Il rappelle aussi qu'aucune capture ne doit afficher de mot de passe, de clé secrète ou de valeur sensible.

Les captures doivent respecter la règle des trois piliers :

* capture du code ou extrait de code ;
* explication du fonctionnement ;
* capture du rendu final lorsque la fonctionnalité produit un résultat visible.

---

# 15 - Limites et évolutions

**Fichier :** `15-limites-et-évolutions.md`

Ce document présente les limites actuelles de la V1 et les évolutions possibles.

Il explique notamment pourquoi certaines fonctionnalités ne sont pas encore intégrées :

* PostgreSQL ;
* administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* graphiques Plotly.js ;
* espace privé complet ;
* tests automatisés complets ;
* API REST ;
* système de comptes publics ;
* rôles avancés ;
* vraie plateforme complète de gestion de projets.

Ce document montre que les limites du projet ne sont pas des oublis, mais des choix de périmètre.

Certaines fonctionnalités envisagées au départ comme reportées ont finalement été intégrées de manière limitée et contrôlée :

* un compte temporaire de lecture seule pour l'évaluation ;
* une expérimentation NoSQL avec TinyDB ;
* un affichage des notes TinyDB sur la page d'accueil ;
* des extraits SQL natifs pour le dossier projet.

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

Il doit mettre en avant les compétences suivantes :

* conception ;
* développement Django ;
* modèles et vues ;
* base de données SQLite ;
* SQL natif documentaire ;
* JavaScript dynamique ;
* NoSQL TinyDB ;
* sécurité minimale ;
* Docker ;
* déploiement Render ;
* GitHub ;
* documentation technique.

---

# 17 - Pistes explorées et non retenues

**Fichier :** `17-pistes-explorees-et-non-retenues.md`

Ce document présente les pistes techniques et fonctionnelles envisagées, mais non intégrées dans la V1.

Il traite notamment :

* C# / ASP.NET Core / Razor ;
* Django ;
* PostgreSQL ;
* administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* Plotly.js ;
* espace privé complet ;
* sauvegardes automatiques ;
* refonte graphique complète ;
* tests automatisés complets ;
* gestion complète des médias ;
* API REST ;
* système de comptes publics.

Ce document montre que plusieurs pistes ont été explorées, puis reportées pour éviter de transformer la V1 en projet trop complexe.

Le compte temporaire de lecture seule et TinyDB ne doivent plus être présentés comme totalement non implantés : ils ont été ajoutés de manière limitée et contrôlée.

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
* la préparation des maquettes Figma si nécessaire ;
* la vérification technique finale ;
* la vérification Render ;
* la vérification de l'administration Django ;
* la vérification du compte temporaire de lecture seule ;
* la vérification TinyDB ;
* la vérification de l'affichage des notes NoSQL ;
* la relecture de la documentation ;
* le commit final ;
* le déploiement final Render.

Ce fichier sert de checklist de fin de V1.

---

# 19 - Renforcement du dossier projet

**Fichier :** `19-renforcement-dossier-projet.md`

Ce document sert de synthèse pour les ajouts réalisés après le retour formateur.

Il présente les éléments ajoutés pour renforcer le dossier projet :

* MCD ;
* diagramme de cas d'utilisation ;
* diagramme de séquence ;
* extraits SQL natifs `CREATE TABLE` ;
* exemples SQL `INSERT INTO` ;
* JavaScript dynamique du menu mobile ;
* documentation des modèles Django ;
* documentation des vues et routes ;
* expérimentation NoSQL TinyDB ;
* affichage des notes TinyDB sur l'accueil ;
* compte temporaire de lecture seule ;
* liste des captures et preuves à préparer.

Ce fichier permet de relier la documentation principale aux documents complémentaires créés pour répondre aux attendus du dossier projet.

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

Ce document présentait initialement la réflexion autour d'une future intégration NoSQL.

La V1 contient maintenant une expérimentation NoSQL légère avec TinyDB.

Ce choix reste volontairement limité afin de conserver une V1 stable, simple et maîtrisable.

Le document peut maintenant expliquer :

* pourquoi NoSQL n'était pas prévu au départ ;
* pourquoi TinyDB a été choisi pour une intégration légère ;
* dans quels cas NoSQL peut devenir utile ;
* un exemple de document NoSQL possible ;
* les différences entre la base SQL actuelle et la base NoSQL documentaire ;
* la roadmap possible pour intégrer MongoDB ou une autre solution NoSQL dans une version plus avancée.

---

# Documents complémentaires de renforcement

Les documents complémentaires ajoutés après le retour formateur permettent de renforcer la présentation du projet dans le dossier final.

Ils concernent principalement :

* la conception ;
* le SQL natif ;
* le JavaScript dynamique ;
* le NoSQL TinyDB ;
* le backend Django ;
* les preuves et captures.

Ces documents ne remplacent pas la documentation principale. Ils servent à compléter les preuves attendues pour le dossier projet.

---

## Conception

Les documents de conception présentent :

* le MCD ;
* le diagramme de cas d'utilisation ;
* le diagramme de séquence.

Ils permettent de montrer que le projet ne repose pas uniquement sur du code, mais aussi sur une réflexion préalable.

---

## Backend Django

Les documents backend présentent :

* les modèles Django ;
* les vues ;
* les routes ;
* la récupération des données SQLite ;
* la récupération des notes TinyDB ;
* l'envoi des données aux templates.

Ils permettent de mieux expliquer la partie développement du projet.

---

## Frontend et JavaScript

Le document frontend présente le JavaScript dynamique du menu mobile.

Il explique notamment :

* le rôle du fichier `static/js/menu.js` ;
* le chargement du script dans `base.html` ;
* l'utilisation de `data-menu-button` ;
* l'utilisation de `data-sidebar` ;
* l'utilisation de `querySelector` ;
* l'utilisation de `addEventListener` ;
* l'ouverture et la fermeture du menu avec `classList.toggle` ;
* la mise à jour de `aria-expanded` ;
* la fermeture du menu lors du clic sur un lien.

Ce document permet de mieux valoriser le JavaScript dynamique dans le dossier projet.

---

## SQL natif

Les documents SQL complémentaires présentent :

* les extraits `CREATE TABLE` ;
* les exemples `INSERT INTO` ;
* le lien entre les modèles Django et les tables SQL ;
* le rôle des migrations ;
* la différence entre ORM Django et SQL natif documentaire.

Ces documents répondent à la demande de mieux valoriser les compétences SQL.

---

## NoSQL TinyDB

La documentation NoSQL présente l'intégration légère réalisée avec TinyDB.

Elle explique :

* pourquoi TinyDB a été retenu ;
* pourquoi cette intégration reste volontairement limitée ;
* le rôle du service Python NoSQL ;
* le rôle du fichier JSON généré par TinyDB ;
* le rôle du script de démonstration terminal ;
* la lecture des notes de progression ;
* l'affichage des notes sur la page d'accueil ;
* la différence entre SQLite et TinyDB ;
* les limites de cette expérimentation.

Cette intégration ne remplace pas SQLite.

SQLite reste la base principale du projet Django. TinyDB sert uniquement de base NoSQL documentaire pour suivre des notes de progression liées au projet.

---

# Fichiers NoSQL implantés dans le projet

## `core/services/nosql_notes.py`

Ce fichier contient le service Python utilisé pour interagir avec TinyDB.

Il contient notamment :

* la création du chemin vers la base NoSQL ;
* l'ouverture de la base TinyDB ;
* la création des notes de démonstration ;
* la lecture de toutes les notes ;
* la recherche de notes par projet.

Ce service est utilisé par la vue d'accueil pour transmettre les notes au template.

---

## `data/nosql/project_notes_db.json`

Ce fichier est la base NoSQL générée par TinyDB.

Il contient les notes de progression du projet Frostia Games.

---

## `scripts/demo_tinydb_notes.py`

Ce script permet de tester la lecture TinyDB depuis le terminal.

Commande de test :

```powershell
python -m scripts.demo_tinydb_notes
```

Ce script affiche les notes de progression dans le terminal et sert de preuve technique.

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
* pourquoi SQLite est utilisé dans la V1 ;
* pourquoi TinyDB a été ajouté de manière limitée ;
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

## `requirements.txt`

Le fichier `requirements.txt` liste les dépendances Python nécessaires au projet.

Il contient notamment :

* Django ;
* Gunicorn ;
* WhiteNoise ;
* TinyDB.

TinyDB est utilisé pour l'expérimentation NoSQL légère.

---

# État actuel de la V1

La V1 de Frostia Games contient actuellement :

* une structure Django fonctionnelle ;
* trois pages principales ;
* une base SQLite ;
* des modèles Django ;
* des migrations ;
* une administration Django ;
* un compte temporaire de lecture seule pour l'évaluation ;
* un affichage dynamique des données ;
* une interface préparatoire pour les projets jouables ;
* un menu mobile en JavaScript ;
* une expérimentation NoSQL avec TinyDB ;
* un affichage des notes TinyDB sur la page d'accueil ;
* un lancement local ;
* un lancement Docker ;
* un déploiement Render ;
* une documentation SQL ;
* une documentation NoSQL ;
* une documentation de modélisation ;
* une documentation frontend ;
* une documentation backend ;
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
* un compte temporaire de lecture seule ;
* l'affichage des créations depuis la base ;
* l'affichage des projets jouables depuis la base ;
* l'affichage des notes TinyDB sur l'accueil ;
* une interface préparatoire de sélection de fichier ;
* Docker ;
* un déploiement Render ;
* une documentation technique complète.

---

# Limites assumées et éléments reportés

La V1 ne contient pas encore :

* de vraie plateforme complète de gestion de projets ;
* de PostgreSQL ;
* d'administration personnalisée ;
* de vrai upload serveur ;
* de vrai lecteur de jeu ou de vidéo ;
* de page détail complète pour chaque projet ;
* d'API REST ;
* de système de comptes publics ;
* de rôles avancés ;
* de graphiques Plotly.js ;
* de tests automatisés complets ;
* de mini-jeu intégré ;
* de système de score ;
* de téléchargement public de projet jouable.

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

# Règle des trois piliers pour le dossier projet

Pour chaque compétence importante, le dossier doit présenter :

1. une capture du code ou un extrait de code ;
2. une explication du fonctionnement ;
3. une capture du rendu final lorsque la fonctionnalité produit un résultat visible.

Cette règle concerne notamment :

* le JavaScript dynamique ;
* les vues Django ;
* les modèles Django ;
* le SQL natif ;
* TinyDB ;
* l'administration Django ;
* le déploiement Render ;
* Docker ;
* GitHub.

---

# Commandes principales

## Lancement local

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

## Installation des dépendances

```powershell
python -m pip install -r requirements.txt
```

## Vérification Django

```powershell
python manage.py check
```

## Test TinyDB

```powershell
python -m scripts.demo_tinydb_notes
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
6. Vérifier le site en local.
7. Vérifier le site sur Render.
8. Vérifier l'administration Django.
9. Vérifier le compte temporaire de lecture seule.
10. Vérifier l'affichage des notes TinyDB sur l'accueil.
11. Faire les captures des preuves.
12. Mettre à jour le dossier Word final.
13. Intégrer les annexes réelles.
14. Exporter le dossier en PDF.
15. Faire le commit final.
16. Vérifier que le dépôt GitHub est propre.

---

# Conclusion

La documentation de Frostia Games sert à montrer que le projet est construit progressivement, avec une séparation claire entre :

* ce qui est implanté ;
* ce qui est documenté ;
* ce qui est testé ;
* ce qui est déployé ;
* ce qui est volontairement reporté ;
* ce qui pourra être ajouté dans une version future.

L'objectif n'est pas d'empiler les fonctionnalités, mais de présenter une base Django propre, documentée, testée, déployée et évolutive.

La V1 de Frostia Games répond désormais aux principaux points de renforcement demandés :

* conception avec MCD, cas d'utilisation et diagramme de séquence ;
* extraits SQL natifs `CREATE TABLE` et `INSERT INTO` ;
* JavaScript dynamique du menu mobile ;
* documentation backend ;
* expérimentation NoSQL TinyDB ;
* affichage NoSQL sur l'accueil ;
* compte temporaire de lecture seule ;
* organisation des preuves à intégrer dans le dossier projet.