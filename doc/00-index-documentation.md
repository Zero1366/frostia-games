# Index de la documentation — Frostia Games

## Objectif

Ce document sert de point d’entrée pour la documentation du projet **Frostia Games**.

Il regroupe les documents techniques, fonctionnels et organisationnels produits pendant la V1.

L’objectif est de conserver une trace claire :

- des choix réalisés ;
- des étapes validées ;
- des fichiers modifiés ;
- des fonctionnalités implantées ;
- des limites volontaires de la V1 ;
- des évolutions prévues ;
- des vérifications réalisées ;
- du déploiement Render ;
- de l’accès d’évaluation en lecture seule ;
- des preuves préparées pour le dossier projet.

Cette documentation permet de montrer que le projet n’a pas été construit au hasard et que la V1 est fonctionnelle, documentée, déployée et défendable.

---

# 1. Rôle de la documentation

La documentation explique :

- pourquoi Django a été retenu ;
- comment le projet est organisé ;
- comment le projet peut être lancé ;
- comment les données sont gérées ;
- comment l’administration Django fonctionne ;
- comment SQLite est utilisée ;
- comment TinyDB est intégré comme expérimentation NoSQL légère ;
- comment les notes TinyDB sont affichées sur la page d’accueil ;
- comment le menu mobile JavaScript fonctionne ;
- comment les extraits SQL natifs sont documentés ;
- comment le compte d’évaluation en lecture seule est configuré ;
- comment le projet est déployé sur Render ;
- comment les données de démonstration sont recréées avec `setup_render_data` ;
- quelles limites sont assumées dans la V1 ;
- quelles évolutions pourront être ajoutées plus tard.

---

# 2. Structure actuelle de la documentation

```text
doc/
├── sql/
│   ├── nosql.md
│   └── schema.sql
│
├── 00-index-documentation.md
├── 01-modernisation-interface.md
├── 02-Journal de bord.md
├── 03-modelisation-backend.md
├── 04-docker-et-lancement.md
├── 05-securite-backend.md
├── 06-manuel-utilisateur.md
├── 07-base-de-donnees.md
├── 08-changelog.md
├── 09-deploiement-render.md
├── 10-bilan-v1-frostia-games.md
├── 11-installation-locale.md
├── 12-architecture.md
├── 13-test-et-vérification.md
├── 14-Capture-et-Preuve.md
├── 15-limites-et-évolutions.md
├── 16-presentation-projet-2.md
├── 17-pistes-explorees-et-non-retenues.md
└── 18-plan-finalisation-v1.md
```

Documentation complémentaire :

```text
docs/
├── backend/
├── conception/
├── frontend/
├── nosql/
├── preuves/
└── sql/
```

---

# 3. Documentation principale `doc/`

## 00 — Index de la documentation

**Fichier :** `doc/00-index-documentation.md`

Ce document sert de point d’entrée pour toute la documentation.

Il présente :

- l’organisation générale ;
- les fichiers disponibles ;
- le rôle de chaque document ;
- l’état actuel de la V1 ;
- les fonctionnalités implantées ;
- les limites assumées ;
- les commandes principales ;
- les documents complémentaires ;
- les preuves à préparer.

---

## 01 — Modernisation de l’interface

**Fichier :** `doc/01-modernisation-interface.md`

Ce document présente le travail réalisé sur l’interface visuelle.

Il explique :

- la direction graphique retenue ;
- les choix de couleurs ;
- l’organisation de la page d’accueil ;
- la sidebar ;
- les cartes de contenu ;
- le responsive desktop et mobile ;
- le menu mobile ;
- les améliorations prévues après stabilisation.

---

## 02 — Journal de bord

**Fichier :** `doc/02-Journal de bord.md`

Ce document consigne les étapes réalisées au fur et à mesure du développement.

Il sert à montrer :

- ce qui a été fait ;
- pourquoi cela a été fait ;
- les fichiers modifiés ;
- les problèmes rencontrés ;
- les décisions prises ;
- les validations effectuées.

Le journal de bord doit rester chronologique et ne pas recopier tous les détails techniques du déploiement Render, car ceux-ci sont déjà centralisés dans `doc/09-deploiement-render.md`.

---

## 03 — Modélisation backend

**Fichier :** `doc/03-modelisation-backend.md`

Ce document présente la modélisation backend du projet.

Il traite notamment :

- les modèles Django ;
- le schéma relationnel simplifié ;
- le rôle de l’ORM Django ;
- les liens entre modèles, vues et templates ;
- les limites de la V1 ;
- les évolutions prévues.

Documents complémentaires associés :

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

---

## 04 — Docker et lancement du projet

**Fichier :** `doc/04-docker-et-lancement.md`

Ce document présente :

- les prérequis ;
- les commandes de lancement local ;
- le lancement avec Docker ;
- le rôle du `Dockerfile` ;
- le rôle de `docker-compose.yml` ;
- le rôle de `.dockerignore` ;
- le rôle de `requirements.txt` ;
- les limites de Docker dans cette V1.

Docker sert ici à tester le projet localement dans un environnement reproductible.

Le déploiement principal est réalisé avec Render.

---

## 05 — Sécurité backend

**Fichier :** `doc/05-securite-backend.md`

Ce document regroupe les choix liés à la sécurité backend.

Il traite notamment :

- le mode `DEBUG` ;
- la clé secrète Django ;
- `ALLOWED_HOSTS`;
- l’utilisation de l’ORM Django ;
- l’absence de SQL brut dans les vues ;
- l’administration Django protégée ;
- l’accès d’évaluation en lecture seule ;
- `EVALUATION_USER_PASSWORD` ;
- la protection CSRF ;
- l’échappement automatique dans les templates ;
- l’absence de vrai upload serveur ;
- la sécurité des captures et des preuves.

---

## 06 — Manuel utilisateur

**Fichier :** `doc/06-manuel-utilisateur.md`

Ce document explique comment utiliser la V1.

Il contient :

- le lancement local ;
- le lancement avec Docker ;
- les pages principales ;
- l’accès à l’administration Django ;
- l’utilisation du compte d’évaluation en lecture seule ;
- les fonctionnalités disponibles ;
- les fonctionnalités non implantées dans la V1 ;
- les vérifications à faire avant une démonstration.

Les identifiants réels ne doivent pas être écrits dans ce document public.

---

## 07 — Base de données

**Fichier :** `doc/07-base-de-donnees.md`

Ce document présente la partie base de données.

Il explique :

- le rôle de SQLite dans la V1 ;
- les modèles Django ;
- les migrations ;
- les tables créées ;
- les extraits SQL natifs ;
- le rôle de l’ORM ;
- le rôle complémentaire de TinyDB ;
- les limites de SQLite sur Render gratuit ;
- l’évolution possible vers PostgreSQL.

Documents associés :

```text
doc/sql/schema.sql
doc/sql/nosql.md
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
docs/nosql/tinydb-integration.md
```

---

## 08 — Changelog

**Fichier :** `doc/08-changelog.md`

Ce document note les changements importants du projet.

Il permet de suivre :

- les ajouts ;
- les corrections ;
- les renforcements ;
- les fichiers concernés ;
- les validations réalisées.

Il doit inclure les derniers éléments importants :

- TinyDB ;
- affichage des notes TinyDB ;
- SQL natif documentaire ;
- compte d’évaluation en lecture seule ;
- déploiement Render ;
- `setup_render_data` ;
- mise à jour des preuves ;
- mise à jour de la documentation finale.

---

## 09 — Déploiement Render

**Fichier :** `doc/09-deploiement-render.md`

Ce document présente le déploiement sur Render.

Il explique :

- l’objectif du déploiement ;
- la plateforme utilisée ;
- la configuration Render ;
- les variables d’environnement ;
- le rôle de `build.sh` ;
- le rôle de Gunicorn ;
- la commande de build ;
- la commande de démarrage ;
- la commande `setup_render_data` ;
- les problèmes rencontrés ;
- les vérifications après déploiement ;
- les limites de l’offre gratuite Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Start Command actuel :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

---

## 10 — Bilan V1 Frostia Games

**Fichier :** `doc/10-bilan-v1-frostia-games.md`

Ce document présente le bilan de la V1.

Il contient :

- l’objectif de la V1 ;
- l’état global du projet ;
- les pourcentages d’avancement estimés ;
- ce qui est terminé ;
- ce qui reste à améliorer ;
- ce qui est volontairement reporté ;
- la conclusion sur l’état actuel du projet.

La V1 est complète dans son périmètre, mais elle ne doit pas être présentée comme une plateforme finale complète.

---

## 11 — Installation locale

**Fichier :** `doc/11-installation-locale.md`

Ce document regroupe les informations liées à l’installation locale.

Il contient :

- la création de l’environnement virtuel ;
- l’activation du `.venv` ;
- l’installation des dépendances ;
- l’installation de Django ;
- l’installation de TinyDB ;
- les commandes de vérification ;
- les problèmes rencontrés ;
- les commandes utiles pour relancer le projet.

---

## 12 — Architecture

**Fichier :** `doc/12-architecture.md`

Ce document présente l’architecture du projet.

Il explique :

- la structure générale ;
- le rôle de `frostia_config` ;
- le rôle des applications Django ;
- le rôle des templates ;
- le rôle des fichiers statiques ;
- le fonctionnement des vues ;
- le fonctionnement de SQLite ;
- le rôle de TinyDB ;
- le rôle du service NoSQL ;
- le rôle de l’administration Django ;
- le fonctionnement du déploiement Render.

Chaîne NoSQL :

```text
TinyDB
→ service Python NoSQL
→ vue Django
→ template de la page d'accueil
→ affichage sur le site
```

---

## 13 — Tests et vérifications

**Fichier :** `doc/13-test-et-vérification.md`

Ce document présente les tests et vérifications réalisés sur la V1.

Il contient :

- les tests du lancement local ;
- les tests des pages principales ;
- les tests de navigation ;
- les tests du responsive ;
- les tests des modèles Django ;
- les tests de l’administration ;
- les tests du compte d’évaluation ;
- les tests Docker ;
- les tests du déploiement Render ;
- les tests TinyDB ;
- les tests d’affichage des notes NoSQL ;
- les vérifications de sécurité minimale.

Commandes importantes :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

---

## 14 — Captures et preuves

**Fichier :** `doc/14-Capture-et-Preuve.md`

Ce document liste les captures d’écran à conserver pour le dossier projet.

Il prévoit notamment :

- captures du site public ;
- captures responsive ;
- captures du menu mobile ;
- captures JavaScript ;
- captures de l’administration Django ;
- captures du compte d’évaluation ;
- captures SQL ;
- captures NoSQL TinyDB ;
- captures Render ;
- captures GitHub ;
- captures Docker ;
- captures de validation technique.

Les preuves sont organisées principalement dans :

```text
docs/preuves/
```

Aucune capture ne doit afficher de mot de passe, de clé secrète ou de valeur sensible.

---

## 15 — Limites et évolutions

**Fichier :** `doc/15-limites-et-évolutions.md`

Ce document présente les limites actuelles de la V1 et les évolutions possibles.

Il explique pourquoi certains éléments sont reportés :

- PostgreSQL ;
- administration personnalisée ;
- upload serveur réel ;
- jeu jouable dans le navigateur ;
- graphiques Plotly.js ;
- espace privé complet ;
- API REST ;
- tests automatisés complets ;
- MongoDB en production.

Il précise aussi que certains éléments ont finalement été ajoutés de manière limitée :

- TinyDB ;
- SQL natif documentaire ;
- compte d’évaluation ;
- `setup_render_data`.

---

## 16 — Présentation du projet 2

**Fichier :** `doc/16-presentation-projet-2.md`

Ce document présente Frostia Games comme proposition de second projet.

Il explique :

- la nature du projet ;
- le positionnement de la V1 ;
- pourquoi le projet peut être proposé comme projet 2 ;
- les fonctionnalités réalisées ;
- les choix techniques ;
- les compétences mises en avant ;
- les limites assumées ;
- les prochaines étapes avant présentation.

---

## 17 — Pistes explorées et non retenues

**Fichier :** `doc/17-pistes-explorees-et-non-retenues.md`

Ce document présente les pistes techniques et fonctionnelles envisagées, mais non intégrées dans la V1.

Il traite notamment :

- C# / ASP.NET Core / Razor ;
- PostgreSQL ;
- MongoDB ;
- administration personnalisée ;
- upload serveur réel ;
- jeu jouable dans le navigateur ;
- Plotly.js ;
- espace privé complet ;
- sauvegardes automatiques ;
- refonte graphique complète ;
- tests automatisés complets ;
- API REST.

Il doit préciser que TinyDB, le compte d’évaluation et le SQL natif documentaire ne sont plus totalement non implantés, car ils ont été ajoutés de manière limitée.

---

## 18 — Plan de finalisation V1

**Fichier :** `doc/18-plan-finalisation-v1.md`

Ce document présente les dernières actions à réaliser avant de considérer la V1 comme terminée.

Il contient :

- la vérification du contenu des pages ;
- la vérification du responsive ;
- la préparation des captures ;
- la vérification du README ;
- la vérification de `CHOIX_TECHNIQUES.md` ;
- la vérification technique finale ;
- la vérification Render ;
- la vérification de l’administration Django ;
- la vérification du compte d’évaluation ;
- la vérification TinyDB ;
- la relecture de la documentation ;
- le commit final.

---

# 4. Documents complémentaires `docs/`

## Conception

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
```

Ces documents permettent de montrer :

- le MCD ;
- les acteurs ;
- les cas d’utilisation ;
- le parcours visiteur ;
- le lien entre navigateur, vues Django, base SQLite et templates.

---

## Backend Django

```text
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

Ces documents présentent :

- les modèles Django ;
- les champs principaux ;
- les vues ;
- les routes ;
- la récupération des données SQLite ;
- la récupération des notes TinyDB ;
- l’envoi des données aux templates.

---

## Frontend et JavaScript

```text
docs/frontend/javascript-menu-mobile.md
```

Ce document explique :

- le rôle de `static/js/menu.js` ;
- l’ouverture et la fermeture du menu mobile ;
- l’utilisation de `querySelector` ;
- l’utilisation de `addEventListener` ;
- l’utilisation de `classList.toggle` ;
- la mise à jour de `aria-expanded`.

---

## SQL natif

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces documents présentent :

- les extraits `CREATE TABLE` ;
- les exemples `INSERT INTO` ;
- le lien entre les modèles Django et les tables SQL ;
- le rôle des migrations ;
- la différence entre ORM Django et SQL natif documentaire.

---

## NoSQL TinyDB

```text
docs/nosql/nosql.md
docs/nosql/structure-nosql.md
docs/nosql/tinydb-integration.md
```

Ces documents présentent :

- pourquoi TinyDB a été retenu ;
- pourquoi l’intégration reste volontairement limitée ;
- le rôle du service Python NoSQL ;
- le rôle du fichier JSON ;
- le rôle du script de démonstration ;
- l’affichage des notes sur la page d’accueil ;
- la différence entre SQLite et TinyDB.

---

## Preuves

```text
docs/preuves/
```

Ce dossier regroupe les captures de fonctionnement.

Organisation recommandée :

```text
docs/preuves/
├── admin/
├── js/
├── nosql/
├── render/
├── sql/
└── test/
```

L’index principal des preuves est :

```text
PREUVES-FONCTIONNEMENT.md
```

---

# 5. Fichiers importants à la racine

```text
README.md
CHOIX_TECHNIQUES.md
PREUVES-FONCTIONNEMENT.md
.env.example
.gitignore
.dockerignore
build.sh
manage.py
requirements.txt
Dockerfile
docker-compose.yml
pyproject.toml
```

## README.md

Présente rapidement :

- le rôle du projet ;
- les technologies utilisées ;
- l’installation locale ;
- le lancement du serveur ;
- le lancement Docker ;
- le déploiement Render ;
- les limites de la V1.

## CHOIX_TECHNIQUES.md

Explique :

- pourquoi Django a été retenu ;
- pourquoi C# / Razor a été envisagé mais reporté ;
- pourquoi SQLite est utilisé dans la V1 ;
- pourquoi TinyDB a été ajouté de manière limitée ;
- pourquoi PostgreSQL est reporté ;
- pourquoi certaines pistes ne doivent pas être ajoutées immédiatement.

## PREUVES-FONCTIONNEMENT.md

Indexe les captures de fonctionnement et les preuves techniques du projet.

## .env.example

Documente les variables d’environnement sans exposer les vraies valeurs :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
EVALUATION_USER_PASSWORD=change-me
```

## build.sh

Utilisé par Render pendant le build.

Il permet notamment :

- d’installer les dépendances ;
- de collecter les fichiers statiques ;
- d’appliquer les migrations ;
- de créer un superutilisateur si les variables sont présentes.

---

# 6. État actuel de la V1

La V1 contient actuellement :

- une structure Django fonctionnelle ;
- trois pages principales ;
- une base SQLite ;
- des modèles Django ;
- des migrations ;
- une administration Django ;
- un compte d’évaluation en lecture seule ;
- un affichage dynamique des données ;
- une interface préparatoire pour les projets jouables ;
- un menu mobile JavaScript ;
- une expérimentation NoSQL avec TinyDB ;
- un affichage des notes TinyDB sur la page d’accueil ;
- un lancement local ;
- un lancement Docker ;
- un déploiement Render ;
- une commande `setup_render_data` ;
- une documentation SQL ;
- une documentation NoSQL ;
- une documentation de modélisation ;
- une documentation frontend ;
- une documentation backend ;
- une documentation de sécurité ;
- une documentation Docker ;
- un manuel utilisateur ;
- un changelog ;
- un bilan V1 ;
- une documentation de déploiement ;
- une documentation des tests ;
- une documentation des limites et évolutions.

---

# 7. Limites assumées

La V1 ne contient pas encore :

- vraie plateforme complète de gestion de projets ;
- PostgreSQL ;
- administration personnalisée ;
- vrai upload serveur ;
- vrai lecteur de jeu ou vidéo ;
- page détail complète pour chaque projet ;
- API REST ;
- système de comptes publics ;
- rôles avancés ;
- graphiques Plotly.js ;
- tests automatisés complets ;
- mini-jeu intégré ;
- système de score ;
- téléchargement public de projet jouable.

Ces limites sont volontaires afin de conserver un projet stable, testable, maintenable et présentable.

---

# 8. Règle de documentation

Une étape du projet est considérée comme terminée uniquement si :

- le code fonctionne ;
- `python manage.py check` ne signale pas d'erreur ;
- les alertes importantes ont été traitées ;
- la fonctionnalité a été testée dans le navigateur ;
- le comportement a été vérifié ;
- la documentation correspondante est mise à jour ;
- les modifications sont sauvegardées avec Git.

---

# 9. Règle des trois piliers pour le dossier projet

Pour chaque compétence importante, le dossier doit présenter :

1. une capture du code ou un extrait de code ;
2. une explication du fonctionnement ;
3. une capture du rendu final lorsque la fonctionnalité produit un résultat visible.

Cette règle concerne notamment :

- le JavaScript dynamique ;
- les vues Django ;
- les modèles Django ;
- le SQL natif ;
- TinyDB ;
- l’administration Django ;
- le compte d’évaluation ;
- le déploiement Render ;
- Docker ;
- GitHub.

---

# 10. Commandes principales

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

## Création d’un administrateur local

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
git push origin main
```

---

# 11. Prochaines actions

Les prochaines actions prévues sont :

1. relire les pages publiques du site ;
2. vérifier le responsive mobile ;
3. préparer les captures ;
4. vérifier le README ;
5. vérifier `CHOIX_TECHNIQUES.md` ;
6. vérifier le site en local ;
7. vérifier le site sur Render ;
8. vérifier l’administration Django ;
9. vérifier le compte d’évaluation en lecture seule ;
10. vérifier l’affichage des notes TinyDB ;
11. vérifier les captures dans `docs/preuves/` ;
12. mettre à jour le dossier final ;
13. intégrer les annexes réelles ;
14. exporter le dossier en PDF si nécessaire ;
15. faire le commit final ;
16. vérifier que le dépôt GitHub est propre.

---

# 12. Conclusion

La documentation de Frostia Games sert à montrer que le projet est construit progressivement, avec une séparation claire entre :

- ce qui est implanté ;
- ce qui est documenté ;
- ce qui est testé ;
- ce qui est déployé ;
- ce qui est volontairement reporté ;
- ce qui pourra être ajouté dans une version future.

L'objectif n'est pas d'empiler les fonctionnalités, mais de présenter une base Django propre, documentée, testée, déployée et évolutive.

La V1 répond désormais aux principaux points de renforcement :

- conception avec MCD, cas d'utilisation et diagramme de séquence ;
- extraits SQL natifs `CREATE TABLE` et `INSERT INTO` ;
- JavaScript dynamique du menu mobile ;
- documentation backend ;
- expérimentation NoSQL TinyDB ;
- affichage NoSQL sur l'accueil ;
- compte d’évaluation en lecture seule ;
- initialisation Render avec `setup_render_data` ;
- organisation des preuves dans `docs/preuves/`.
