# Captures et preuves - Frostia Games

## Objectif du document

Ce document liste les captures d'écran et preuves à conserver pour le projet **Frostia Games**.

L'objectif est de montrer que la V1 du projet est fonctionnelle, testée, documentée et déployée en ligne.

Ces captures pourront être utilisées dans le dossier projet, dans une présentation ou comme preuve de validation technique.

Ce document a été mis à jour après le renforcement du dossier projet afin d’intégrer :

* les captures TinyDB ;
* les captures du compte temporaire de lecture seule ;
* les captures SQL natives ;
* les captures JavaScript ;
* les captures des documents de conception ;
* les captures de la documentation complémentaire `docs/` ;
* les captures de validation technique récentes.

---

# 1. Organisation des preuves

Un fichier de preuve peut être ajouté afin de regrouper et présenter les captures importantes du projet **Frostia Games**.

Ce fichier de preuve sert à montrer visuellement :

* les captures des maquettes Figma ;
* les captures du site public ;
* les captures responsive ;
* les captures de l'administration Django ;
* les captures du compte temporaire de lecture seule ;
* les captures du déploiement Render ;
* les captures du code ;
* les captures SQL ;
* les captures NoSQL TinyDB ;
* les captures JavaScript ;
* les captures des commandes de validation ;
* les captures du dépôt GitHub ;
* les captures de la documentation.

Toutes les images utilisées comme preuves doivent être regroupées dans un répertoire dédié.

Organisation prévue :

```text
doc/
└── preuves/
    ├── preuves-frostia-games.md
    └── images/
        ├── figma-accueil.png
        ├── figma-mes-creations.png
        ├── figma-projets-jouables.png
        ├── site-accueil-desktop.png
        ├── site-accueil-notes-tinydb.png
        ├── site-mes-creations.png
        ├── site-projets-jouables.png
        ├── site-accueil-mobile.png
        ├── site-menu-mobile-ouvert.png
        ├── site-mes-creations-mobile.png
        ├── admin-connexion.png
        ├── admin-tableau-de-bord.png
        ├── admin-creations.png
        ├── admin-projets-jouables.png
        ├── admin-compte-lecture-seule.png
        ├── admin-permissions-lecture-seule.png
        ├── render-service-live.png
        ├── render-build-start-command.png
        ├── render-variables-masquees.png
        ├── django-check.png
        ├── tinydb-demo-terminal.png
        ├── git-status-clean.png
        ├── github-depot.png
        ├── code-modeles-django.png
        ├── code-vues-django.png
        ├── code-menu-js.png
        ├── code-tinydb-service.png
        ├── code-tinydb-script.png
        ├── sql-create-tables.png
        ├── sql-insert-exemples.png
        └── docs-structure.png
```

Le fichier `preuves-frostia-games.md` sert à présenter les captures avec un court commentaire pour expliquer ce que chaque image prouve.

Le dossier `images/` contient toutes les captures utilisées comme preuves.

Cette organisation permet de faciliter :

* la préparation du dossier projet ;
* la relecture ;
* l'ajout des images dans le dossier final ;
* la vérification des preuves techniques ;
* la présentation du projet à l'évaluateur ;
* la séparation entre la documentation écrite et les fichiers images.

---

# 2. Règles de sécurité pour les captures

Avant de prendre une capture d'écran, il faut vérifier qu'aucune information sensible n'est visible.

Ne jamais afficher dans une capture :

* mot de passe ;
* clé secrète Django ;
* valeur de `DJANGO_SECRET_KEY` ;
* valeur de `DJANGO_SUPERUSER_PASSWORD` ;
* jeton privé ;
* clé API ;
* vraie valeur de variable d'environnement ;
* identifiants administrateur complets ;
* identifiants complets du compte temporaire ;
* information personnelle inutile ;
* lien privé de déploiement non destiné au public.

Les captures doivent montrer le fonctionnement du projet sans exposer les secrets.

Les identifiants du compte temporaire de lecture seule doivent être transmis séparément uniquement si cela est demandé.

Ils ne doivent pas être présents dans le dossier public.

---

# 3. Règle des trois preuves

Pour chaque élément important, il est recommandé de préparer trois preuves :

1. une capture du code ;
2. une explication courte dans la documentation ;
3. une capture du résultat visible ou de la commande de test.

Exemple pour TinyDB :

| Type de preuve | Exemple |
| -------------- | ------- |
| Code | `core/services/nosql_notes.py` |
| Documentation | `docs/nosql/tinydb-integration.md` |
| Résultat | page d'accueil avec notes ou terminal avec `python -m scripts.demo_tinydb_notes` |

Cette méthode permet de montrer qu'une fonctionnalité n'est pas seulement déclarée, mais aussi codée, expliquée et vérifiée.

---

# 4. Liste des catégories de captures

Les captures à conserver sont réparties en plusieurs catégories :

* captures des maquettes Figma ;
* captures du site public ;
* captures responsive ;
* captures de l'administration Django ;
* captures du compte temporaire de lecture seule ;
* captures Render ;
* captures du code ;
* captures SQL ;
* captures NoSQL TinyDB ;
* captures JavaScript ;
* captures de documentation ;
* captures de validation technique ;
* captures Git et GitHub.

---

# 5. Captures des maquettes Figma

## Capture 00 - Maquettes Figma du projet

### Objectif

Montrer que l'interface du projet a été préparée visuellement avant ou pendant l'intégration.

### Éléments à capturer

* maquette de la page d'accueil ;
* maquette de la page Mes créations ;
* maquette de la page Projets jouables ;
* structure générale prévue ;
* organisation visuelle des pages.

### À montrer sur la capture

* la mise en page prévue ;
* les sections principales ;
* l'organisation des cartes ;
* la logique de navigation ;
* les choix visuels de départ ;
* l'intention graphique du projet.

### Statut

```text
À capturer
```

---

# 6. Captures du site public

## Capture 01 - Page d'accueil desktop

### Objectif

Montrer que la page d'accueil du site Frostia Games est accessible et correctement affichée.

### Élément à capturer

```text
https://frostia-games.onrender.com
```

### À montrer sur la capture

* le titre du site ;
* la navigation ;
* le contenu principal ;
* le design général ;
* le rendu desktop ;
* l'URL Render visible si possible.

### Statut

```text
À capturer
```

---

## Capture 02 - Page d'accueil avec notes TinyDB

### Objectif

Montrer que les notes de progression issues de TinyDB sont affichées sur la page d'accueil.

### Élément à capturer

```text
https://frostia-games.onrender.com
```

### À montrer sur la capture

* section des notes de progression ;
* titres des notes ;
* statuts ;
* tags ;
* intégration visuelle dans la page d'accueil.

### Attention

Ne pas afficher de donnée sensible.

TinyDB doit contenir uniquement des données de démonstration.

### Statut

```text
À capturer
```

---

## Capture 03 - Page Mes créations

### Objectif

Montrer la page dédiée aux créations et futurs projets.

### Élément à capturer

```text
https://frostia-games.onrender.com/mes-creations/
```

### À montrer sur la capture

* le titre de la page ;
* les cartes ou blocs de créations ;
* les données affichées ;
* la navigation ;
* le style général.

### Statut

```text
À capturer
```

---

## Capture 04 - Page Projets jouables à venir

### Objectif

Montrer la page prévue pour les futurs projets jouables.

### Élément à capturer

```text
https://frostia-games.onrender.com/projets-jouables/
```

### À montrer sur la capture

* le titre de la page ;
* la zone préparatoire ;
* le message indiquant que l'upload serveur n'est pas encore implanté ;
* le bouton ou l'interface prévue pour une évolution future ;
* le contenu affiché depuis Django.

### Statut

```text
À capturer
```

---

# 7. Captures responsive

## Capture 05 - Page d'accueil mobile

### Objectif

Montrer que le site reste consultable sur petit écran.

### Élément à capturer

Page d'accueil en largeur mobile dans l'inspecteur du navigateur.

### À montrer sur la capture

* contenu lisible ;
* absence de débordement important ;
* cartes adaptées ;
* navigation accessible ;
* rendu mobile cohérent.

### Statut

```text
À capturer
```

---

## Capture 06 - Menu mobile ouvert

### Objectif

Montrer que le menu mobile JavaScript fonctionne.

### À montrer sur la capture

* bouton de menu ;
* sidebar ouverte ;
* liens de navigation visibles ;
* affichage adapté au mobile.

### Fichiers liés

```text
static/js/menu.js
templates/base.html
static/css/main.css
```

### Statut

```text
À capturer
```

---

## Capture 07 - Page Mes créations mobile

### Objectif

Montrer que la page des créations reste lisible sur mobile.

### À montrer sur la capture

* cartes adaptées ;
* textes lisibles ;
* blocs correctement alignés ;
* pas de scroll horizontal important.

### Statut

```text
À capturer si nécessaire
```

---

# 8. Captures de l'administration Django

## Capture 08 - Page de connexion admin Django

### Objectif

Montrer que l'administration Django est accessible en ligne.

### Élément à capturer

```text
https://frostia-games.onrender.com/admin/
```

### À montrer sur la capture

* page de connexion Django ;
* URL `/admin/` ;
* aucun mot de passe visible.

### Statut

```text
À capturer
```

---

## Capture 09 - Tableau de bord admin Django

### Objectif

Montrer que l'administration Django fonctionne après connexion.

### À montrer sur la capture

* tableau de bord admin ;
* modèles disponibles ;
* interface Django chargée correctement.

### Attention

Ne pas afficher de mot de passe ou de donnée sensible.

### Statut

```text
À capturer
```

---

## Capture 10 - Modèle Creation dans l'admin

### Objectif

Montrer que les créations peuvent être gérées depuis l'administration Django.

### À montrer sur la capture

* liste des créations ;
* colonnes principales ;
* filtres ou recherche si visibles ;
* interface propre.

### Statut

```text
À capturer
```

---

## Capture 11 - Modèle PlayableProject dans l'admin

### Objectif

Montrer que les projets jouables à venir sont gérés depuis l'administration Django.

### À montrer sur la capture

* liste des projets jouables ;
* statut des projets ;
* informations principales ;
* interface Django fonctionnelle.

### Statut

```text
À capturer
```

---

# 9. Captures du compte temporaire de lecture seule

## Capture 12 - Tableau de bord avec compte lecture seule

### Objectif

Montrer que le compte temporaire peut accéder à l'administration avec des droits limités.

### À montrer sur la capture

* tableau de bord admin ;
* seulement les sections autorisées ;
* accès aux créations ;
* accès aux projets jouables.

### Attention

Ne pas afficher les identifiants du compte.

### Statut

```text
À capturer
```

---

## Capture 13 - Permissions limitées du compte lecture seule

### Objectif

Montrer que le compte temporaire n'a pas les droits complets.

### À montrer sur la capture

* absence d'accès aux utilisateurs ;
* absence d'accès aux groupes ;
* absence d'accès aux permissions sensibles ;
* affichage limité aux éléments utiles.

### Attention

Ne pas afficher de mot de passe.

### Statut

```text
À capturer avec prudence
```

---

# 10. Captures Render

## Capture 14 - Service Render actif

### Objectif

Montrer que le service Render est bien en ligne.

### À montrer sur la capture

* nom du service ;
* statut actif ;
* URL publique ;
* type de service Web ;
* branche GitHub utilisée.

### Statut

```text
À capturer
```

---

## Capture 15 - Logs Render avec service live

### Objectif

Montrer que le déploiement a réussi.

### À montrer sur la capture

Message Render :

```text
Your service is live
```

Si visible, montrer aussi :

```text
Listening at: http://0.0.0.0:10000
```

### Statut

```text
À capturer
```

---

## Capture 16 - Build Command et Start Command

### Objectif

Montrer la configuration de déploiement Render.

### À montrer sur la capture

Build Command :

```bash
bash build.sh
```

Start Command :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

### Attention

Ne pas afficher de variables secrètes.

### Statut

```text
À capturer
```

---

## Capture 17 - Variables d'environnement Render masquées

### Objectif

Montrer que les variables d'environnement sont utilisées sans exposer leurs valeurs.

### À montrer sur la capture

Uniquement les noms des variables :

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
```

### Attention

Les valeurs doivent être masquées.

### Statut

```text
À capturer avec prudence
```

---

# 11. Captures du code

## Capture 18 - Structure du projet dans VS Code

### Objectif

Montrer l'organisation générale du projet.

### À montrer sur la capture

* dossier `frostia_config` ;
* dossier `core` ;
* dossier `creations` ;
* dossier `playable` ;
* dossier `scripts` ;
* dossier `data/nosql` ;
* dossier `templates` ;
* dossier `static` ;
* dossier `doc` ;
* dossier `docs` ;
* fichier `manage.py` ;
* fichier `requirements.txt` ;
* fichier `build.sh` ;
* fichier `README.md` ;
* fichier `CHOIX_TECHNIQUES.md`.

### Statut

```text
À capturer
```

---

## Capture 19 - Fichier settings.py

### Objectif

Montrer une partie de la configuration Django.

### À montrer sur la capture

* `INSTALLED_APPS` ;
* configuration des templates ;
* configuration des fichiers statiques ;
* `ALLOWED_HOSTS` si présent ;
* logique des variables d'environnement si visible.

### Attention

Ne pas afficher la vraie clé secrète.

### Statut

```text
À capturer avec prudence
```

---

## Capture 20 - Fichiers models.py

### Objectif

Montrer les modèles Django utilisés dans le projet.

### À montrer sur la capture

* modèle `Creation` ;
* modèle `PlayableProject` ;
* champs principaux ;
* statuts ;
* visibilité ;
* dates.

### Statut

```text
À capturer
```

---

## Capture 21 - Fichiers admin.py

### Objectif

Montrer la configuration de l'administration Django.

### À montrer sur la capture

* `list_display` ;
* `list_filter` ;
* `search_fields` ;
* `prepopulated_fields` ;
* `readonly_fields`.

### Statut

```text
À capturer
```

---

## Capture 22 - Fichier views.py

### Objectif

Montrer la liaison entre le backend Django et les templates.

### À montrer sur la capture

* vues principales ;
* récupération des données SQLite ;
* récupération des notes TinyDB ;
* `render` vers les templates ;
* logique simple et lisible.

### Statut

```text
À capturer
```

---

## Capture 23 - Fichier build.sh

### Objectif

Montrer le script utilisé par Render pour préparer le projet.

### À montrer sur la capture

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true
```

### Statut

```text
À capturer
```

---

# 12. Captures SQL

## Capture 24 - Fichiers SQL natifs

### Objectif

Montrer que le projet possède des fichiers SQL documentaires.

### Fichiers à capturer

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

### À montrer sur la capture

* structure `CREATE TABLE` ;
* exemple `INSERT INTO` ;
* lien entre SQL natif et modèles Django ;
* documentation du rôle du SQL.

### Statut

```text
À capturer
```

---

## Capture 25 - Fichier schema.sql

### Objectif

Montrer le schéma SQL documentaire initial.

### Fichier à capturer

```text
doc/sql/schema.sql
```

### À montrer sur la capture

* tables principales ;
* champs ;
* commentaires ;
* exemples si visibles.

### Statut

```text
À capturer si utile
```

---

# 13. Captures NoSQL TinyDB

## Capture 26 - Service TinyDB

### Objectif

Montrer le code Python utilisé pour gérer TinyDB.

### Fichier à capturer

```text
core/services/nosql_notes.py
```

### À montrer sur la capture

* chemin de la base JSON ;
* ouverture TinyDB ;
* création des notes ;
* recherche par projet ;
* fermeture de la base.

### Statut

```text
À capturer
```

---

## Capture 27 - Script de démonstration TinyDB

### Objectif

Montrer le script utilisé pour tester TinyDB.

### Fichier à capturer

```text
scripts/demo_tinydb_notes.py
```

### À montrer sur la capture

* import du service TinyDB ;
* appel de `seed_project_notes()` ;
* appel de `find_notes_by_project()`;
* affichage des notes dans le terminal.

### Statut

```text
À capturer
```

---

## Capture 28 - Résultat terminal TinyDB

### Objectif

Montrer que TinyDB fonctionne réellement.

### Commande à lancer

```powershell
python -m scripts.demo_tinydb_notes
```

### Résultat attendu

```text
Preuve NoSQL TinyDB — Frostia Games
```

### À montrer sur la capture

* titres des notes ;
* statuts ;
* tags ;
* contenu ;
* absence d'erreur.

### Statut

```text
À capturer
```

---

## Capture 29 - Base JSON TinyDB

### Objectif

Montrer que TinyDB stocke des documents JSON.

### Fichier à capturer

```text
data/nosql/project_notes_db.json
```

### À montrer sur la capture

* documents JSON ;
* champs `project_code`, `title`, `content`, `tags`, `status`, `created_at`.

### Attention

Ne pas afficher de donnée sensible.

### Statut

```text
À capturer si utile
```

---

# 14. Captures JavaScript

## Capture 30 - Fichier menu.js

### Objectif

Montrer que le projet contient du JavaScript dynamique.

### Fichier à capturer

```text
static/js/menu.js
```

### À montrer sur la capture

* `querySelector` ;
* `addEventListener` ;
* `classList.toggle` ;
* `aria-expanded` ;
* fermeture du menu après clic sur un lien.

### Statut

```text
À capturer
```

---

## Capture 31 - Documentation JavaScript

### Objectif

Montrer que le JavaScript est documenté.

### Fichier à capturer

```text
docs/frontend/javascript-menu-mobile.md
```

### À montrer sur la capture

* objectif du fichier ;
* fonctionnement du menu ;
* explication des événements ;
* limites.

### Statut

```text
À capturer si utile
```

---

# 15. Captures de validation technique

## Capture 32 - Commande python manage.py check

### Objectif

Montrer que Django ne détecte pas d'erreur de configuration.

### Commande à lancer

```powershell
python manage.py check
```

### Résultat attendu

```text
System check identified no issues (0 silenced).
```

### Statut

```text
À capturer
```

---

## Capture 33 - Commande git status propre

### Objectif

Montrer que le projet est sauvegardé proprement dans Git.

### Commande à lancer

```powershell
git status
```

### Résultat attendu

```text
nothing to commit, working tree clean
```

### Statut

```text
À capturer après commit final
```

---

## Capture 34 - Dépôt GitHub

### Objectif

Montrer que le projet est versionné et disponible dans un dépôt GitHub.

### À montrer sur la capture

* nom du dépôt ;
* branche `main` ;
* fichiers principaux ;
* dernier commit visible.

### Statut

```text
À capturer
```

---

# 16. Captures de documentation

## Capture 35 - Dossier doc

### Objectif

Montrer que le projet est documenté.

### À montrer sur la capture

Fichiers du dossier `doc` :

```text
00-index-documentation.md
01-modernisation-interface.md
02-journal-de-bord.md
03-modelisation-backend.md
04-docker-et-lancement.md
05-securite-backend.md
06-manuel-utilisateur.md
07-base-de-donnees.md
08-changelog.md
09-deploiement-render.md
10-bilan-v1-frostia-games.md
11-installation-locale.md
12-architecture.md
13-test-et-vérification.md
14-Capture-et Preuve.md
15-limites-et-évolutions.md
16-presentation-projet-2.md
17-pistes-explorees-et-non-retenues.md
18-plan-finalisation-v1.md
19-renforcement-dossier-projet.md
```

### Statut

```text
À capturer
```

---

## Capture 36 - Dossier docs

### Objectif

Montrer la documentation complémentaire ajoutée pendant le renforcement du dossier.

### À montrer sur la capture

```text
docs/backend/
docs/conception/
docs/frontend/
docs/nosql/
docs/preuves/
docs/sql/
```

### Statut

```text
À capturer
```

---

## Capture 37 - Documentation de déploiement Render

### Objectif

Montrer que le déploiement est documenté.

### À montrer sur la capture

* titre du document ;
* Build Command ;
* Start Command ;
* variables d'environnement ;
* résultat du déploiement ;
* problèmes rencontrés.

### Statut

```text
À capturer
```

---

## Capture 38 - Bilan V1

### Objectif

Montrer que l'état du projet est évalué avec un bilan clair.

### À montrer sur la capture

* tableau d'avancement ;
* avancement global ;
* limites ;
* évolutions prévues.

### Statut

```text
À capturer
```

---

## Capture 39 - Fichier de preuve

### Objectif

Montrer que les captures sont organisées dans un fichier de preuve dédié.

### À montrer sur la capture

* fichier `preuves-frostia-games.md` ;
* répertoire `images/` ;
* liste des captures utilisées ;
* organisation claire des preuves.

### Statut

```text
À capturer après création du fichier de preuve
```

---

# 17. Tableau récapitulatif des captures

| N° | Capture                            | Priorité | Statut                 |
| -: | ---------------------------------- | -------- | ---------------------- |
| 00 | Maquettes Figma                    | Haute    | À faire                |
| 01 | Page d'accueil desktop             | Haute    | À faire                |
| 02 | Page d'accueil avec notes TinyDB   | Haute    | À faire                |
| 03 | Page Mes créations                 | Haute    | À faire                |
| 04 | Page Projets jouables              | Haute    | À faire                |
| 05 | Page d'accueil mobile              | Haute    | À faire                |
| 06 | Menu mobile ouvert                 | Haute    | À faire                |
| 07 | Page Mes créations mobile          | Moyenne  | À faire si nécessaire  |
| 08 | Connexion admin Django             | Haute    | À faire                |
| 09 | Tableau de bord admin Django       | Haute    | À faire                |
| 10 | Modèle Creation admin              | Moyenne  | À faire                |
| 11 | Modèle PlayableProject admin       | Moyenne  | À faire                |
| 12 | Admin compte lecture seule         | Haute    | À faire                |
| 13 | Permissions lecture seule          | Haute    | À faire avec prudence  |
| 14 | Service Render actif               | Haute    | À faire                |
| 15 | Logs Render service live           | Haute    | À faire                |
| 16 | Build Command / Start Command      | Haute    | À faire                |
| 17 | Variables d'environnement masquées | Moyenne  | À faire avec prudence  |
| 18 | Structure du projet VS Code        | Haute    | À faire                |
| 19 | settings.py sans secret            | Moyenne  | À faire avec prudence  |
| 20 | models.py                          | Haute    | À faire                |
| 21 | admin.py                           | Moyenne  | À faire                |
| 22 | views.py                           | Moyenne  | À faire                |
| 23 | build.sh                           | Haute    | À faire                |
| 24 | SQL natif                          | Haute    | À faire                |
| 25 | schema.sql                         | Moyenne  | À faire si utile       |
| 26 | Service TinyDB                     | Haute    | À faire                |
| 27 | Script TinyDB                      | Haute    | À faire                |
| 28 | Résultat terminal TinyDB           | Haute    | À faire                |
| 29 | Base JSON TinyDB                   | Moyenne  | À faire si utile       |
| 30 | menu.js                            | Haute    | À faire                |
| 31 | Documentation JavaScript           | Moyenne  | À faire si utile       |
| 32 | python manage.py check             | Haute    | À faire                |
| 33 | git status propre                  | Haute    | À faire                |
| 34 | dépôt GitHub                       | Moyenne  | À faire                |
| 35 | dossier doc                        | Haute    | À faire                |
| 36 | dossier docs                       | Haute    | À faire                |
| 37 | documentation Render               | Moyenne  | À faire                |
| 38 | bilan V1                           | Moyenne  | À faire                |
| 39 | fichier de preuve                  | Moyenne  | À faire après création |

---

# 18. Captures prioritaires minimum

Si le temps est limité, les captures indispensables sont :

```text
00 - Maquettes Figma
01 - Page d'accueil desktop
02 - Page d'accueil avec notes TinyDB
03 - Page Mes créations
04 - Page Projets jouables
05 - Page d'accueil mobile
06 - Menu mobile ouvert
08 - Connexion admin Django
09 - Tableau de bord admin Django
12 - Admin compte lecture seule
14 - Service Render actif
15 - Logs Render service live
16 - Build Command / Start Command
18 - Structure du projet VS Code
24 - SQL natif
26 - Service TinyDB
28 - Résultat terminal TinyDB
30 - menu.js
32 - python manage.py check
33 - git status propre
35 - dossier doc
36 - dossier docs
```

Ces captures suffisent à prouver que la V1 est fonctionnelle, déployée, documentée et renforcée.

---

# 19. Captures non nécessaires pour l'instant

Certaines captures ne sont pas indispensables pour la V1 :

* configuration PostgreSQL ;
* interface d'administration personnalisée ;
* graphiques Plotly ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* espace privé complet ;
* API REST ;
* MongoDB ;
* mini-jeu intégré ;
* système de score.

Ces éléments ne font pas partie du périmètre actuel.

---

# 20. Vérification finale avant intégration au dossier

Avant d’intégrer les captures au dossier, vérifier :

* que chaque image est lisible ;
* que les noms de fichiers sont clairs ;
* que les images sont rangées dans le bon dossier ;
* qu’aucune image ne montre de secret ;
* que les captures techniques correspondent bien à l’état actuel du projet ;
* que les captures Render ne montrent pas les valeurs des variables ;
* que les captures du compte lecture seule ne montrent pas le mot de passe ;
* que les captures TinyDB ne montrent pas de donnée sensible ;
* que les captures GitHub ne montrent pas d’information privée inutile.

---

# 21. Bilan

Les captures listées dans ce document permettent de préparer une preuve claire du fonctionnement du projet Frostia Games.

Elles montrent :

* les maquettes Figma ;
* l'interface publique ;
* le responsive ;
* le menu mobile ;
* l'administration Django ;
* le compte temporaire de lecture seule ;
* le déploiement Render ;
* la configuration technique ;
* le SQL natif ;
* TinyDB ;
* le JavaScript ;
* les tests réalisés ;
* la documentation produite ;
* l'organisation des preuves dans un fichier dédié ;
* le regroupement des images dans un répertoire prévu.

Ce document sert de checklist pour préparer le dossier projet et vérifier que la V1 est correctement présentée.

À ce stade, la priorité est de préparer les captures utiles et d’éviter d’ajouter de nouvelles fonctionnalités lourdes.
