# Modélisation backend — Frostia Games

## Objectif du document

Ce document présente la modélisation backend de la V1 du projet **Frostia Games**.

Il décrit :

- les entités utilisées dans la base de données ;
- le rôle des modèles Django ;
- le schéma relationnel simplifié ;
- le MCD simplifié ;
- les cas d'utilisation principaux ;
- les diagrammes de séquence ;
- le rôle de l'ORM Django ;
- le rôle du SQL natif documentaire ;
- le rôle de TinyDB ;
- le rôle du compte d’évaluation en lecture seule ;
- le rôle de `setup_render_data` sur Render ;
- les limites de la V1 ;
- les évolutions prévues.

L'objectif est de montrer que le backend du projet repose sur une structure claire, même si la V1 reste volontairement simple.

---

# 1. Contexte backend

Frostia Games est un portfolio développé avec **Django**.

La V1 utilise :

- Django pour les routes, les vues, les modèles et l'administration ;
- SQLite pour les données principales ;
- l'ORM Django pour manipuler les données SQL ;
- TinyDB pour une expérimentation NoSQL légère ;
- un service Python pour lire les notes TinyDB ;
- un compte d’évaluation en lecture seule ;
- une commande `setup_render_data` pour recréer les données Render ;
- Render pour le déploiement en ligne ;
- Gunicorn pour lancer l'application Django en production ;
- WhiteNoise pour les fichiers statiques en production.

Les deux contenus principaux stockés en SQLite sont :

- les créations ;
- les futurs projets jouables.

TinyDB est utilisé en complément pour stocker des notes de progression sous forme documentaire JSON.

Le backend reste volontairement limité afin de conserver une V1 stable, lisible, maintenable et défendable.

---

# 2. Modèles Django utilisés

## 2.1 Modèle `Creation`

Le modèle `Creation` représente une création ou un projet présenté dans la page **Mes créations**.

Il permet d'enregistrer :

- le titre du projet ;
- son identifiant URL ;
- sa lettre de classement alphabétique ;
- son nom de code ;
- son type ;
- son statut ;
- sa description courte ;
- sa visibilité sur le site ;
- ses dates de création et de modification.

Ce modèle permet d'afficher dynamiquement les créations enregistrées dans l'administration Django.

---

## 2.2 Modèle `PlayableProject`

Le modèle `PlayableProject` représente un futur contenu jouable, une vidéo, un teaser ou un prototype prévu dans la page **Projets jouables**.

Il permet d'enregistrer :

- le titre du contenu ;
- son identifiant URL ;
- son statut ;
- le type de contenu prévu ;
- une description courte ;
- un message de disponibilité ;
- son état de disponibilité ;
- sa visibilité sur le site ;
- ses dates de création et de modification.

Ce modèle prépare une évolution future sans annoncer une fonctionnalité qui n'est pas encore disponible dans la V1.

---

## 2.3 Données NoSQL TinyDB

TinyDB ne remplace pas les modèles Django.

Il sert uniquement à stocker des notes de progression liées au projet Frostia Games.

Les notes NoSQL peuvent contenir :

- un code projet ;
- un titre ;
- un contenu ;
- une liste de tags ;
- un statut ;
- une date de création.

Ces données ne sont pas gérées par l'administration Django.

Elles sont lues par un service Python dédié, puis affichées sur la page d'accueil.

---

# 3. Schéma relationnel simplifié

## Table `creations_creation`

| Champ | Type logique | Rôle |
| ----- | ------------ | ---- |
| `id` | Integer | Identifiant unique |
| `title` | Texte court | Titre de la création |
| `slug` | Texte court unique | Identifiant URL |
| `alphabet_letter` | Texte court | Lettre de classement |
| `code_name` | Texte court | Nom de code du projet |
| `project_type` | Texte court | Type de projet |
| `status` | Texte court | Statut de développement |
| `short_description` | Texte long | Description courte |
| `is_visible` | Booléen | Affichage ou non sur le site |
| `created_at` | Date / heure | Date de création |
| `updated_at` | Date / heure | Dernière modification |

## Table `playable_playableproject`

| Champ | Type logique | Rôle |
| ----- | ------------ | ---- |
| `id` | Integer | Identifiant unique |
| `title` | Texte court | Titre du projet jouable |
| `slug` | Texte court unique | Identifiant URL |
| `status` | Texte court | Statut du contenu |
| `content_type` | Texte court | Type de contenu prévu |
| `short_description` | Texte long | Description courte |
| `availability_message` | Texte long | Message de disponibilité |
| `is_available` | Booléen | Indique si le contenu est disponible |
| `is_visible` | Booléen | Affichage ou non sur le site |
| `created_at` | Date / heure | Date de création |
| `updated_at` | Date / heure | Dernière modification |

## Structure documentaire TinyDB

| Champ | Type logique | Rôle |
| ----- | ------------ | ---- |
| `project_code` | Texte court | Code du projet concerné |
| `title` | Texte court | Titre de la note |
| `content` | Texte long | Contenu de la note |
| `tags` | Liste de textes | Tags associés à la note |
| `status` | Texte court | Statut de la note |
| `created_at` | Texte / date | Date de création de la note |

TinyDB permet de montrer la différence entre une base SQL structurée avec tables et une base NoSQL documentaire avec objets JSON.

---

# 4. MCD simplifié

Dans la V1, les deux entités SQL principales sont indépendantes.

```text
+----------------------+
|       CREATION       |
+----------------------+
| id                   |
| title                |
| slug                 |
| alphabet_letter      |
| code_name            |
| project_type         |
| status               |
| short_description    |
| is_visible           |
| created_at           |
| updated_at           |
+----------------------+


+---------------------------+
|     PLAYABLE_PROJECT      |
+---------------------------+
| id                        |
| title                     |
| slug                      |
| status                    |
| content_type              |
| short_description         |
| availability_message      |
| is_available              |
| is_visible                |
| created_at                |
| updated_at                |
+---------------------------+
```

Dans cette V1, il n'existe pas encore de relation directe entre ces deux entités.

Ce choix permet de conserver un backend simple, stable et adapté au périmètre actuel.

Une future version pourra ajouter des relations entre :

- créations ;
- médias ;
- fiches détaillées ;
- versions jouables ;
- captures ;
- liens externes ;
- journaux de développement.

Document complémentaire :

```text
docs/conception/mcd.md
```

---

# 5. Cas d'utilisation

## Acteurs

```text
Visiteur
Administrateur
Évaluateur en lecture seule
```

## Visiteur

Le visiteur peut :

- consulter la page d'accueil ;
- consulter la page **Mes créations** ;
- consulter les créations visibles ;
- consulter la page **Projets jouables** ;
- voir l'état de disponibilité d'un futur projet jouable ;
- sélectionner un fichier local dans l'interface préparatoire ;
- voir les notes de progression affichées sur l'accueil.

Le visiteur n'a pas de compte utilisateur dans cette V1.

Il n'a pas accès à l'administration Django.

## Administrateur

L'administrateur peut :

- se connecter à l'administration Django ;
- ajouter une création ;
- modifier une création ;
- masquer ou afficher une création ;
- ajouter un futur projet jouable ;
- modifier un projet jouable ;
- gérer les groupes et utilisateurs si le compte est superutilisateur.

Aucun identifiant administrateur n'est publié dans GitHub ou dans la documentation publique.

## Évaluateur en lecture seule

Le compte d’évaluation permet uniquement de consulter certaines données dans l'administration Django.

Il peut voir :

- les créations ;
- les projets jouables.

Il ne doit pas permettre :

- l’ajout ;
- la modification ;
- la suppression ;
- l’accès aux utilisateurs ;
- l’accès aux groupes ;
- l’accès aux permissions sensibles ;
- l’accès aux secrets du projet.

---

# 6. Diagramme de cas d'utilisation simplifié

```text
                       +----------------------+
                       |    Frostia Games     |
                       +----------------------+

        +-----------+                         +------------------+
        | Visiteur  |                         | Administrateur   |
        +-----------+                         +------------------+
             |                                          |
             | consulter l'accueil                      |
             | consulter les créations                  |
             | consulter les projets jouables           |
             | consulter les notes de progression       |
             | sélectionner un fichier local            |
                                                        |
                                                        | se connecter à l'admin
                                                        | ajouter une création
                                                        | modifier une création
                                                        | ajouter un projet jouable
                                                        | modifier un projet jouable

        +------------------------------+
        | Évaluateur en lecture seule  |
        +------------------------------+
             |
             | se connecter à l'administration
             | consulter les créations
             | consulter les projets jouables
             | sans modifier les utilisateurs
```

Document complémentaire :

```text
docs/conception/cas-utilisation.md
```

---

# 7. Diagramme de séquence — consultation des créations

```text
Visiteur
   |
   | 1. Demande la page /mes-creations/
   v
Navigateur
   |
   | 2. Envoie une requête HTTP GET
   v
Vue Django : creations()
   |
   | 3. Demande les créations visibles
   v
Modèle Django : Creation
   |
   | 4. Requête via ORM Django
   v
Base SQLite
   |
   | 5. Retourne les créations visibles
   v
Vue Django : creations()
   |
   | 6. Envoie les données au template
   v
Template : creation.html
   |
   | 7. Génère la page HTML
   v
Navigateur
   |
   | 8. Affiche la page au visiteur
```

La vue Django récupère uniquement les créations dont le champ `is_visible` est actif.

La récupération des données passe par l'ORM Django.

---

# 8. Diagramme de séquence — ajout d'une création via l'administration

```text
Administrateur
   |
   | 1. Accède à /admin/
   v
Admin Django
   |
   | 2. Demande une authentification
   v
Administrateur
   |
   | 3. Saisit ses identifiants
   v
Admin Django
   |
   | 4. Vérifie les identifiants
   v
Système d'authentification Django
   |
   | 5. Autorise l'accès à l'administration
   v
Admin Django
   |
   | 6. L'administrateur remplit le formulaire Creation
   v
Modèle Django : Creation
   |
   | 7. Validation des champs du modèle
   v
ORM Django
   |
   | 8. Génère la requête SQL
   v
Base SQLite
   |
   | 9. Enregistre la nouvelle création
   v
Admin Django
   |
   | 10. Affiche la création dans la liste admin
```

L'ORM Django traduit l'opération en requête SQL sans écrire manuellement du SQL dans le code applicatif.

---

# 9. Diagramme de séquence — consultation des projets jouables

```text
Visiteur
   |
   | 1. Demande la page /projets-jouables/
   v
Navigateur
   |
   | 2. Envoie une requête HTTP GET
   v
Vue Django : projets_jouables()
   |
   | 3. Demande les projets jouables visibles
   v
Modèle Django : PlayableProject
   |
   | 4. Requête via ORM Django
   v
Base SQLite
   |
   | 5. Retourne les projets jouables visibles
   v
Vue Django : projets_jouables()
   |
   | 6. Envoie les données au template
   v
Template : projet_jouable.html
   |
   | 7. Génère la page HTML
   v
Navigateur
   |
   | 8. Affiche la page au visiteur
```

Dans la V1, l'interface de sélection de fichier est seulement préparatoire.

Aucun fichier n'est envoyé ni enregistré sur le serveur.

---

# 10. Diagramme de séquence — affichage des notes TinyDB

```text
Visiteur
   |
   | 1. Demande la page /
   v
Navigateur
   |
   | 2. Envoie une requête HTTP GET
   v
Vue Django : home()
   |
   | 3. Initialise ou vérifie les notes TinyDB
   v
Service Python : nosql_notes.py
   |
   | 4. Ouvre la base TinyDB
   v
Base NoSQL : project_notes_db.json
   |
   | 5. Retourne les notes du projet Frostia Games
   v
Service Python : nosql_notes.py
   |
   | 6. Renvoie les notes à la vue Django
   v
Vue Django : home()
   |
   | 7. Envoie les notes au template
   v
Template : home.html
   |
   | 8. Génère la section Notes de progression
   v
Navigateur
   |
   | 9. Affiche les notes au visiteur
```

Cela permet de démontrer une utilisation NoSQL légère sans remplacer la base SQLite principale.

---

# 11. Diagramme de séquence — accès en lecture seule à l'administration

```text
Évaluateur
   |
   | 1. Accède à /admin/
   v
Admin Django
   |
   | 2. Demande une authentification
   v
Évaluateur
   |
   | 3. Saisit les identifiants d'évaluation
   v
Système d'authentification Django
   |
   | 4. Vérifie le compte et le groupe
   v
Permissions Django
   |
   | 5. Autorise uniquement la consultation prévue
   v
Admin Django
   |
   | 6. Affiche seulement les modèles autorisés
```

Le compte d’évaluation est actif et membre de l'équipe, mais il n'est pas superutilisateur.

Il possède uniquement les droits de consultation nécessaires.

---

# 12. Diagramme de séquence — initialisation Render

```text
Render
   |
   | 1. Démarre le service
   v
Start Command
   |
   | 2. python manage.py migrate --noinput
   v
Migrations Django
   |
   | 3. Base SQLite préparée
   v
Start Command
   |
   | 4. python manage.py setup_render_data
   v
Commande Django personnalisée
   |
   | 5. Crée ou met à jour les données de démonstration
   | 6. Crée ou met à jour le groupe Evaluation lecture seule
   | 7. Crée ou met à jour le compte evaluation_temp
   | 8. Applique les permissions de lecture seule
   v
Start Command
   |
   | 9. gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
   v
Application Django en ligne
```

Start Command actuel :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Le mot de passe du compte d’évaluation est fourni par :

```text
EVALUATION_USER_PASSWORD
```

---

# 13. Rôle de l'ORM Django

L'ORM Django permet de manipuler les données à travers des classes Python.

Exemple :

```python
Creation.objects.filter(is_visible=True).order_by(
    "alphabet_letter",
    "title",
)
```

Avantages :

- code plus lisible ;
- meilleure intégration avec Django ;
- réduction du risque d'injection SQL ;
- compatibilité avec les migrations ;
- manipulation des données sous forme d'objets Python ;
- migration future vers PostgreSQL plus simple.

---

# 14. Sécurité liée à la base de données

La V1 utilise plusieurs mécanismes de sécurité fournis par Django :

- utilisation de l'ORM au lieu de requêtes SQL brutes dans les vues ;
- administration protégée par authentification ;
- compte d’évaluation limité en lecture seule ;
- protection CSRF disponible pour les formulaires ;
- échappement automatique des variables dans les templates ;
- validation des champs par les modèles Django ;
- absence de vrai upload serveur dans la V1 ;
- séparation des secrets dans les variables d'environnement ;
- fichier `.env.example` pour documenter les variables sans exposer les vraies valeurs.

Les extraits SQL natifs sont présents dans la documentation pour expliquer la structure de la base, pas pour contourner l'ORM Django.

---

# 15. SQL documentaire

Le fichier suivant contient un équivalent SQL simplifié des tables utilisées :

```text
doc/sql/schema.sql
```

Fichiers complémentaires :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers permettent de montrer :

- les structures SQL générées pour les tables principales ;
- des exemples d'insertion avec `INSERT INTO` ;
- le lien entre modèles Django et tables SQL ;
- la différence entre ORM Django et SQL natif documentaire.

Dans le projet réel, la création des tables est gérée par les migrations Django.

---

# 16. NoSQL avec TinyDB

TinyDB est utilisé pour stocker des notes de progression du projet dans un fichier JSON.

Fichiers principaux :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

Le service `core/services/nosql_notes.py` permet de :

- créer le dossier de stockage si nécessaire ;
- ouvrir la base TinyDB ;
- créer des notes de démonstration ;
- lister les notes ;
- rechercher les notes liées au projet Frostia Games ;
- fermer proprement la base après utilisation.

Commande de test :

```powershell
python -m scripts.demo_tinydb_notes
```

TinyDB n'est pas utilisé pour remplacer SQLite.

Il n'est pas utilisé pour gérer les créations ou les projets jouables.

---

# 17. JavaScript dynamique lié à l'interface

Le JavaScript principal du projet concerne le menu mobile.

Le fichier concerné est :

```text
static/js/menu.js
```

Le script est chargé dans :

```text
templates/partials/base.html
```

Il permet :

- d'ouvrir le menu mobile ;
- de fermer le menu mobile ;
- de modifier l'attribut `aria-expanded` ;
- de fermer la navigation après un clic sur un lien.

Documentation complémentaire :

```text
docs/frontend/javascript-menu-mobile.md
```

---

# 18. Lien avec le déploiement Render

URL de production :

```text
https://frostia-games.onrender.com
```

Build Command Render :

```bash
bash build.sh
```

Start Command Render :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Variables importantes :

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
EVALUATION_USER_PASSWORD
```

---

# 19. Limites de la V1

La V1 ne contient pas encore :

- vraie page détail projet ;
- vrai upload serveur ;
- vrai lecteur vidéo ;
- API REST ;
- système de comptes publics ;
- rôles publics avancés ;
- PostgreSQL ;
- administration personnalisée ;
- graphiques Plotly.js ;
- tests automatisés complets ;
- mini-jeu intégré ;
- système de score ;
- téléchargement public de projet jouable.

Ces limites sont volontaires.

Certains éléments initialement reportés ont été intégrés de manière limitée et contrôlée :

- expérimentation NoSQL légère avec TinyDB ;
- affichage des notes TinyDB sur l'accueil ;
- compte d’évaluation en lecture seule ;
- extraits SQL natifs documentaires ;
- initialisation automatique Render avec `setup_render_data`.

---

# 20. Évolutions prévues

Les évolutions possibles du backend sont :

- ajouter des fiches détaillées pour les créations ;
- relier les projets jouables à une création ;
- ajouter une table de médias ;
- ajouter une table de versions ;
- ajouter une gestion plus avancée des statuts ;
- ajouter un vrai système d'upload sécurisé ;
- migrer vers PostgreSQL si le projet devient plus complet ;
- créer une administration personnalisée ;
- envisager MongoDB pour les contenus très variables ;
- ajouter des tests automatisés Django ;
- ajouter un système de sauvegarde automatique avant modification ;
- ajouter un système de rôles plus avancé si un espace privé est créé.

Ces évolutions sont reportées afin de protéger le périmètre de la V1.

---

# 21. Documents complémentaires

## Conception

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
```

## Backend

```text
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

## SQL

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

## NoSQL

```text
docs/nosql/tinydb-integration.md
```

## Frontend

```text
docs/frontend/javascript-menu-mobile.md
```

## Preuves

```text
docs/preuves/
PREUVES-FONCTIONNEMENT.md
```

---

# 22. Règle des trois piliers

Pour chaque compétence importante, le dossier final doit montrer :

1. une capture du code ou un extrait de code ;
2. une explication du fonctionnement ;
3. une capture du rendu final quand la fonctionnalité produit un résultat visible.

Cette règle concerne notamment :

- les modèles Django ;
- les vues Django ;
- l'administration Django ;
- le compte d’évaluation en lecture seule ;
- le SQL natif ;
- TinyDB ;
- l'affichage des notes TinyDB ;
- le JavaScript dynamique ;
- Docker ;
- Render ;
- GitHub.

---

# 23. Captures et preuves à préparer

Pour le dossier final, les captures utiles sont :

- modèles Django ;
- vues Django ;
- routes ;
- administration Django ;
- compte d’évaluation en lecture seule ;
- fichiers SQL natifs ;
- service TinyDB ;
- script TinyDB ;
- affichage des notes TinyDB sur l'accueil ;
- JavaScript du menu mobile ;
- commande `python manage.py check` ;
- commande `python -m scripts.demo_tinydb_notes` ;
- logs Render avec `setup_render_data`.

Aucune capture ne doit afficher :

- mot de passe ;
- clé secrète ;
- vraie variable d’environnement ;
- identifiant administrateur complet ;
- information sensible inutile.

---

# 24. Conclusion

La V1 de Frostia Games possède un backend simple mais fonctionnel.

Elle montre :

- une structure Django claire ;
- deux modèles reliés à une base SQLite ;
- une administration fonctionnelle ;
- un compte d’évaluation en lecture seule ;
- des migrations ;
- un affichage dynamique dans les templates ;
- une séparation entre données, vues et templates ;
- une réflexion sur la sécurité ;
- une documentation SQL ;
- des extraits SQL natifs ;
- une expérimentation NoSQL avec TinyDB ;
- un affichage des notes NoSQL sur l'accueil ;
- une documentation du JavaScript dynamique ;
- un déploiement Render fonctionnel ;
- une initialisation automatique Render avec `setup_render_data` ;
- une documentation des limites et évolutions.

Le backend reste volontairement limité afin d'éviter une complexité inutile.

Il constitue une base stable pour faire évoluer le projet progressivement.

À ce stade, les éléments backend essentiels sont implantés.

La priorité n'est plus d'ajouter de nouvelles fonctionnalités lourdes, mais de préparer les captures, les annexes et l'intégration propre dans le dossier projet final.
