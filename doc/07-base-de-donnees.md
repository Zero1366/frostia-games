# Base de données - Frostia Games

## Objectif du document

Ce document présente la partie base de données du projet **Frostia Games**.

Il explique :

* le choix de SQLite pour la V1 ;
* le rôle des modèles Django ;
* les tables utilisées ;
* le fonctionnement des migrations ;
* le rôle de l’ORM Django ;
* les données stockées ;
* les données non stockées ;
* le fichier SQL documentaire ;
* les extraits SQL natifs ajoutés pour le dossier projet ;
* l’expérimentation NoSQL avec TinyDB ;
* le lien avec l’administration Django ;
* le compte temporaire de lecture seule ;
* le lien avec le déploiement Render ;
* les limites actuelles ;
* les évolutions possibles vers PostgreSQL ou une solution NoSQL plus avancée.

L’objectif est de montrer que la V1 possède une base de données simple, fonctionnelle et cohérente avec le périmètre du projet.

Ce document a été mis à jour après le renforcement du dossier projet afin d’intégrer :

* TinyDB ;
* les notes de progression NoSQL ;
* les extraits SQL natifs ;
* les exemples `INSERT INTO` ;
* le compte temporaire de lecture seule ;
* les preuves à préparer pour le dossier final.

---

# 1. Contexte

Frostia Games est un portfolio développé avec **Django**.

Dans la V1, la base de données sert à rendre certaines parties du site dynamiques.

Les données ne sont plus uniquement écrites directement dans les fichiers HTML.

Une partie du contenu peut maintenant être ajoutée, modifiée ou masquée depuis l’administration Django.

La base SQLite est utilisée pour gérer :

* les créations ;
* les futurs projets jouables.

Une expérimentation NoSQL légère avec TinyDB a également été ajoutée.

TinyDB sert à stocker et afficher des notes de progression liées au projet.

Ce choix permet de montrer que le projet possède :

* un vrai backend Django ;
* une base SQL principale ;
* une expérimentation NoSQL complémentaire ;
* une documentation SQL native ;
* une séparation claire entre données principales et données documentaires.

Le périmètre reste volontairement limité afin de conserver une V1 stable et maîtrisable.

---

# 2. Choix de SQLite pour la V1

La V1 utilise SQLite comme base principale.

SQLite est adapté pour cette première version car :

* il est intégré facilement avec Django ;
* il ne demande pas de serveur de base de données séparé ;
* il permet de tester rapidement les modèles ;
* il simplifie le lancement local ;
* il fonctionne bien pour une V1 de portfolio ;
* il permet de valider le fonctionnement du backend avant d’ajouter une infrastructure plus complexe.

Le fichier de base de données est :

```text
db.sqlite3
```

Ce choix est volontaire.

L’objectif de la V1 est de stabiliser le backend Django avant d’ajouter une base plus robuste comme PostgreSQL.

---

# 3. SQLite et limites assumées

SQLite est suffisant pour :

* un projet local ;
* une démonstration ;
* une V1 simple ;
* un portfolio avec peu de données ;
* une première validation du backend Django.

Cependant, SQLite n’est pas le choix idéal pour une version plus avancée avec beaucoup de données, plusieurs utilisateurs ou des besoins de production durable.

Dans cette V1, ce choix reste cohérent car le projet ne contient pas encore :

* de comptes utilisateurs publics ;
* de commentaires ;
* de nombreux médias ;
* d’upload serveur réel ;
* de système de rôles publics avancés ;
* de forte charge d’utilisation.

Pour une version plus complète, une migration vers PostgreSQL pourra être envisagée.

---

# 4. Évolution possible vers PostgreSQL

PostgreSQL n’est pas utilisé dans la V1.

Il pourra être envisagé plus tard si le projet évolue vers :

* une mise en production plus robuste ;
* un volume de données plus important ;
* une gestion plus avancée des contenus ;
* des relations plus nombreuses entre projets, médias et versions ;
* une conservation plus durable des données en ligne ;
* une configuration backend plus complète.

PostgreSQL serait plus adapté pour une version avancée du projet.

Dans la V1, SQLite permet de garder un projet simple, stable et maintenable.

---

# 5. Applications Django concernées

Deux applications Django utilisent actuellement la base de données SQLite :

```text
creations
playable
```

## Application `creations`

Cette application gère les créations affichées dans la page **Mes créations**.

Modèle principal :

```text
Creation
```

## Application `playable`

Cette application gère les futurs contenus jouables, vidéos, teasers ou prototypes affichés dans la page **Projets jouables**.

Modèle principal :

```text
PlayableProject
```

Ces deux applications permettent de séparer les responsabilités du projet.

---

# 6. Modèle `Creation`

Le modèle `Creation` sert à stocker les projets ou créations présentés dans le portfolio.

Il contient les champs suivants :

| Champ               | Rôle                                            |
| ------------------- | ----------------------------------------------- |
| `id`                | Identifiant unique généré automatiquement       |
| `title`             | Titre de la création                            |
| `slug`              | Identifiant URL unique                          |
| `alphabet_letter`   | Lettre utilisée pour le classement alphabétique |
| `code_name`         | Nom de code ou nom interne du projet            |
| `project_type`      | Type de projet                                  |
| `status`            | Statut de développement                         |
| `short_description` | Description courte affichée sur le site         |
| `is_visible`        | Indique si la création est visible sur le site  |
| `created_at`        | Date de création de l’entrée                    |
| `updated_at`        | Date de dernière modification                   |

Ce modèle permet d’ajouter ou modifier une création depuis l’administration Django sans modifier directement le template HTML.

---

# 7. Modèle `PlayableProject`

Le modèle `PlayableProject` sert à stocker les informations liées aux futurs contenus jouables.

Il contient les champs suivants :

| Champ                  | Rôle                                        |
| ---------------------- | ------------------------------------------- |
| `id`                   | Identifiant unique généré automatiquement   |
| `title`                | Titre du futur projet jouable               |
| `slug`                 | Identifiant URL unique                      |
| `status`               | Statut du contenu                           |
| `content_type`         | Type de contenu prévu                       |
| `short_description`    | Description courte                          |
| `availability_message` | Message indiquant l’état de disponibilité   |
| `is_available`         | Indique si le contenu est disponible        |
| `is_visible`           | Indique si l’entrée est visible sur le site |
| `created_at`           | Date de création de l’entrée                |
| `updated_at`           | Date de dernière modification               |

Ce modèle permet de préparer la section **Projets jouables** sans annoncer une fonctionnalité qui n’est pas encore réellement disponible.

---

# 8. Tables créées

Avec Django, les modèles sont transformés en tables SQL via les migrations.

Les deux tables principales sont :

```text
creations_creation
playable_playableproject
```

## Table `creations_creation`

Cette table stocke les créations du portfolio.

Elle correspond au modèle Django :

```text
Creation
```

## Table `playable_playableproject`

Cette table stocke les futurs projets jouables ou contenus prévus.

Elle correspond au modèle Django :

```text
PlayableProject
```

Dans la V1, ces deux tables sont indépendantes.

Aucune relation directe n’est encore créée entre une création et un projet jouable.

Ce choix permet de garder une base simple et adaptée au périmètre actuel.

---

# 9. Migrations Django

Django utilise les migrations pour créer et faire évoluer la base de données.

Les migrations permettent de garder une trace des changements apportés aux modèles.

Commandes utilisées :

```powershell
python manage.py makemigrations
python manage.py migrate
```

La commande :

```powershell
python manage.py makemigrations
```

prépare les fichiers de migration à partir des modèles Django.

La commande :

```powershell
python manage.py migrate
```

applique les migrations à la base de données SQLite.

Les migrations évitent de créer ou modifier les tables à la main.

TinyDB ne dépend pas des migrations Django, car il fonctionne avec un fichier JSON.

---

# 10. ORM Django

Le projet utilise l’ORM Django pour manipuler les données SQL.

Exemple dans les vues :

```python
Creation.objects.filter(is_visible=True).order_by(
    "alphabet_letter",
    "title",
)
```

Autre exemple :

```python
PlayableProject.objects.filter(is_visible=True).order_by(
    "title",
)
```

L’ORM permet de récupérer les données sous forme d’objets Python sans écrire directement de requêtes SQL dans les vues.

Cela rend le code plus lisible et limite les risques d’erreurs ou d’injection SQL.

L’ORM permet aussi de garder une logique Django cohérente avec les modèles, les migrations et l’administration.

---

# 11. Données visibles sur le site

Les données affichées publiquement sont filtrées avec le champ :

```text
is_visible
```

Exemple :

```python
Creation.objects.filter(is_visible=True)
```

Cela permet de conserver une donnée en base tout en la masquant temporairement du site.

Le même principe est utilisé pour les projets jouables :

```python
PlayableProject.objects.filter(is_visible=True)
```

Ce fonctionnement permet de gérer la visibilité des contenus depuis l’administration Django.

Les notes TinyDB affichées sur l’accueil sont également préparées côté backend avant d’être transmises au template.

---

# 12. Données actuellement stockées dans SQLite

Dans la V1, SQLite stocke principalement :

* les créations ;
* les futurs projets jouables ;
* les statuts ;
* les descriptions courtes ;
* les messages de disponibilité ;
* les informations de visibilité ;
* les dates de création ;
* les dates de modification.

Exemple de création :

```text
KryonCore
```

Exemple de projet jouable :

```text
Prototype jouable à venir
```

Ces données peuvent être modifiées depuis l’administration Django.

---

# 13. Données actuellement stockées avec TinyDB

TinyDB stocke des notes de progression liées au projet.

Ces notes sont des documents JSON.

Elles peuvent contenir :

* un code projet ;
* un titre ;
* un contenu ;
* une liste de tags ;
* un statut ;
* une date de création.

Fichier concerné :

```text
data/nosql/project_notes_db.json
```

Ces données sont utilisées pour afficher une section de notes sur la page d’accueil.

TinyDB ne remplace pas SQLite.

Il sert uniquement à démontrer une logique NoSQL légère et documentaire.

---

# 14. Données non stockées dans la V1

La V1 ne stocke pas encore :

* les fichiers uploadés ;
* les vidéos ;
* les images de projets ;
* les exécutables ;
* les fichiers ZIP ;
* les comptes utilisateurs publics ;
* les commentaires ;
* les logs avancés ;
* les fiches détaillées complètes ;
* les versions de jeux ;
* les médias associés aux projets ;
* les sauvegardes automatiques de contenu.

Ces éléments pourront être ajoutés plus tard si le projet évolue.

Ils ne sont pas ajoutés maintenant afin de conserver une base simple et maîtrisable.

---

# 15. Interface d’administration

La base SQLite est alimentée principalement via l’administration Django.

Adresse locale :

```text
http://127.0.0.1:8000/admin/
```

Adresse en ligne :

```text
https://frostia-games.onrender.com/admin/
```

L’administration permet de gérer :

* les créations ;
* les projets jouables.

Elle permet notamment :

* d’ajouter une entrée ;
* de modifier une entrée ;
* de masquer une entrée ;
* de contrôler les contenus visibles sur le site.

L’accès à l’administration reste privé.

Aucun identifiant administrateur ni mot de passe ne doit être publié dans GitHub ou dans la documentation publique.

---

# 16. Compte temporaire de lecture seule

Un compte temporaire de lecture seule peut être utilisé pour l’évaluation.

Ce compte ne remplace pas l’administrateur.

Il sert uniquement à permettre une consultation limitée de l’administration Django.

Le compte temporaire peut voir :

* les créations ;
* les projets jouables.

Il ne doit pas voir :

* les utilisateurs ;
* les groupes ;
* les permissions sensibles ;
* les réglages internes ;
* les secrets du projet.

Ce compte permet de montrer la partie administration sans donner un accès complet au backend.

Les identifiants réels ne doivent pas être écrits dans la documentation publique.

---

# 17. Lien avec le déploiement Render

Le projet est déployé en ligne sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Pendant le déploiement, Render exécute le fichier :

```text
build.sh
```

Ce fichier permet notamment :

* d’installer les dépendances ;
* de collecter les fichiers statiques ;
* d’appliquer les migrations ;
* de créer un superutilisateur si les variables d’environnement sont présentes.

Commande importante du script :

```powershell
python manage.py migrate
```

Cette commande applique les migrations nécessaires à la base SQLite.

Pour une V1, ce fonctionnement est suffisant pour montrer que le projet peut être lancé et déployé.

Pour une version plus durable ou plus avancée, PostgreSQL pourra être envisagé.

TinyDB est installé via `requirements.txt`.

Il peut donc être chargé par l’application tant que la dépendance est bien installée.

---

# 18. Variables d’environnement liées au backend

Le projet utilise des variables d’environnement pour éviter d’écrire les informations sensibles directement dans le code.

Exemple documenté dans `.env.example` :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Ces variables servent notamment à :

* configurer le mode debug ;
* stocker la clé secrète Django ;
* créer un superutilisateur ;
* éviter de publier les vraies valeurs sensibles.

Le fichier `.env.example` est seulement un modèle.

Les vraies valeurs doivent rester dans l’environnement local ou dans les variables Render.

Les identifiants du compte temporaire de lecture seule ne doivent pas non plus être écrits dans ce fichier.

---

# 19. Fichier `.gitignore` et base SQLite

Le fichier `.gitignore` permet d’éviter l’envoi de certains fichiers dans GitHub.

Il peut notamment ignorer :

```text
db.sqlite3
staticfiles/
media/
.env
.env.local
```

L’objectif est d’éviter d’envoyer :

* la base locale ;
* les fichiers générés ;
* les fichiers médias ;
* les secrets ;
* les données sensibles.

Attention : si `db.sqlite3` a déjà été suivi par Git avant l’ajout au `.gitignore`, il peut rester suivi.

Dans ce cas, il faut vérifier avec :

```powershell
git status
```

Le choix de suivre ou non `db.sqlite3` doit être cohérent avec le fonctionnement du projet et les données nécessaires à la démonstration.

---

# 20. Fichier `.gitignore` et TinyDB

Le fichier TinyDB est :

```text
data/nosql/project_notes_db.json
```

Il peut être conservé dans le projet uniquement s’il contient des données de démonstration non sensibles.

Il ne doit jamais contenir :

* mot de passe ;
* clé secrète ;
* identifiant administrateur ;
* variable d’environnement ;
* information personnelle sensible ;
* jeton d’accès.

Dans cette V1, TinyDB sert à stocker des notes de progression documentaires.

Il reste donc acceptable si le contenu est contrôlé et non sensible.

---

# 21. Schéma SQL documentaire

Un fichier SQL documentaire a été ajouté :

```text
doc/sql/schema.sql
```

Ce fichier contient :

* l’équivalent SQL simplifié des tables ;
* des instructions `CREATE TABLE` ;
* des exemples `INSERT INTO` ;
* des commentaires expliquant le rôle des tables.

Dans le fonctionnement réel du projet, les tables sont créées par Django grâce aux migrations.

Le fichier SQL sert à documenter la structure de la base et à répondre aux attendus du dossier projet.

Il ne remplace pas les migrations Django.

---

# 22. Extraits SQL natifs complémentaires

Après le retour formateur, des fichiers SQL complémentaires ont été ajoutés afin de mieux valoriser la partie SQL native.

Fichiers concernés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers permettent de présenter :

* la structure SQL de la table des créations ;
* la structure SQL de la table des projets jouables ;
* des exemples `INSERT INTO` ;
* le lien entre modèles Django et tables SQL ;
* la différence entre SQL natif documentaire et ORM Django.

Ces fichiers ne remplacent pas les migrations.

Ils servent à expliquer la base dans le dossier projet.

---

# 23. Exemple de structure SQL

Exemple simplifié de table pour les créations :

```sql
CREATE TABLE creations_creation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(120) NOT NULL,
    slug VARCHAR(140) NOT NULL UNIQUE,
    alphabet_letter VARCHAR(1) NOT NULL,
    code_name VARCHAR(120) NOT NULL,
    project_type VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL,
    short_description TEXT NOT NULL,
    is_visible BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
```

Exemple simplifié de table pour les projets jouables :

```sql
CREATE TABLE playable_playableproject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(120) NOT NULL,
    slug VARCHAR(140) NOT NULL UNIQUE,
    status VARCHAR(100) NOT NULL,
    content_type VARCHAR(100) NOT NULL,
    short_description TEXT NOT NULL,
    availability_message TEXT NOT NULL,
    is_available BOOLEAN NOT NULL DEFAULT 0,
    is_visible BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
```

Ces exemples servent uniquement à expliquer la structure logique de la base.

---

# 24. Exemple d’insertion SQL

Un fichier complémentaire contient des exemples d’insertion :

```text
docs/sql/exemples_insert.sql
```

Exemple logique :

```sql
INSERT INTO creations_creation (
    title,
    slug,
    alphabet_letter,
    code_name,
    project_type,
    status,
    short_description,
    is_visible,
    created_at,
    updated_at
)
VALUES (
    'Frostia Games',
    'frostia-games',
    'F',
    'FROSTIA',
    'Portfolio Django',
    'V1 en développement',
    'Portfolio Django permettant de présenter des projets vidéoludiques.',
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
```

Ces exemples permettent de montrer la compréhension du SQL natif, même si le projet réel utilise principalement les migrations et l’ORM Django.

---

# 25. NoSQL avec TinyDB

Un fichier de réflexion NoSQL existe :

```text
doc/sql/nosql.md
```

La V1 contient maintenant une expérimentation NoSQL légère avec TinyDB.

Ce choix a été ajouté de manière contrôlée afin de répondre au besoin de montrer une compétence NoSQL sans transformer l’architecture du projet.

TinyDB est utilisé pour stocker des notes de progression dans un fichier JSON.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

---

# 26. Rôle de TinyDB

TinyDB sert à démontrer une base documentaire NoSQL.

Il permet de stocker des objets JSON plutôt que des lignes dans une table SQL.

Dans Frostia Games, TinyDB est utilisé pour des notes de progression liées au projet.

Exemple de structure logique :

```json
{
  "project_code": "frostia-games",
  "title": "Renforcement du dossier projet",
  "content": "Ajout de la conception, du SQL natif, du JavaScript documenté et de la partie NoSQL.",
  "tags": ["dossier-projet", "conception", "sql", "nosql"],
  "status": "in_progress",
  "created_at": "2026-06-30"
}
```

Ce format est plus souple qu’une table SQL pour de petites notes documentaires.

---

# 27. Fonctionnement TinyDB dans le projet

La chaîne technique est la suivante :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

Le service Python gère :

* l’ouverture de la base TinyDB ;
* la création des notes de démonstration ;
* la lecture des notes ;
* la recherche par code projet ;
* la fermeture de la base après utilisation.

Le script de démonstration permet de tester TinyDB :

```powershell
python -m scripts.demo_tinydb_notes
```

Cette commande sert de preuve technique pour le dossier projet.

---

# 28. Différence entre SQLite et TinyDB

| Élément | SQLite | TinyDB |
| ------- | ------ | ------ |
| Type | Base SQL relationnelle légère | Base NoSQL documentaire légère |
| Format | Tables | Documents JSON |
| Usage dans le projet | Données principales | Notes de progression |
| Gestion Django | Modèles, ORM, migrations | Service Python séparé |
| Administration Django | Oui | Non |
| Rôle V1 | Base principale | Expérimentation complémentaire |

SQLite reste la base principale du projet.

TinyDB sert uniquement de complément documentaire.

---

# 29. Sécurité liée à la base de données

La sécurité de la base repose principalement sur :

* l’utilisation de l’ORM Django ;
* l’absence de requêtes SQL brutes dans les vues ;
* la validation des champs par les modèles ;
* l’administration protégée par authentification ;
* le compte temporaire de lecture seule ;
* l’échappement automatique dans les templates ;
* le filtrage des contenus visibles ;
* la séparation des secrets avec les variables d’environnement ;
* l’absence de vrai upload serveur dans la V1 ;
* l’absence de données sensibles dans TinyDB.

Le projet ne construit pas de requêtes SQL en concaténant du texte utilisateur.

Cela limite les risques d’injection SQL.

TinyDB ne doit pas contenir de secrets ou d’informations sensibles.

---

# 30. Limites de la V1

La V1 ne contient pas encore :

* de relations complexes entre les tables ;
* de table média ;
* de table version ;
* de table utilisateur personnalisée ;
* de base PostgreSQL ;
* de vrai système d’upload ;
* de stockage de fichiers en base ;
* d’administration personnalisée ;
* de sauvegarde automatique avant modification ;
* de système de restauration des contenus ;
* de base NoSQL avancée comme MongoDB.

Ces limites sont volontaires.

L’objectif est de garder une base claire, testable et stable.

Certains éléments initialement reportés ont finalement été intégrés de manière limitée et contrôlée :

* compte temporaire de lecture seule ;
* TinyDB ;
* affichage des notes TinyDB ;
* extraits SQL natifs documentaires.

---

# 31. Évolutions prévues

Les évolutions possibles sont :

1. Ajouter une table de fiches détaillées.
2. Ajouter une table de médias.
3. Ajouter une table de versions.
4. Relier un projet jouable à une création.
5. Ajouter PostgreSQL pour une version plus avancée.
6. Étudier MongoDB pour les contenus très variables.
7. Ajouter un système d’upload sécurisé.
8. Ajouter des permissions plus fines dans l’administration.
9. Ajouter un système de sauvegarde automatique avant modification.
10. Ajouter un système de restauration des contenus.
11. Ajouter des tests automatisés sur les modèles Django.
12. Ajouter des tests sur les services NoSQL si cette partie évolue.

Ces évolutions sont reportées afin d’éviter d’élargir trop vite le périmètre de la V1.

---

# 32. Lien avec les fichiers racine

La partie base de données est aussi documentée par plusieurs fichiers à la racine du projet.

## `README.md`

Le fichier `README.md` présente :

* le projet ;
* les technologies utilisées ;
* l’installation locale ;
* le lancement Docker ;
* le déploiement Render ;
* les limites de la V1 ;
* les évolutions prévues.

## `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` explique notamment :

* pourquoi SQLite est conservé dans la V1 ;
* pourquoi PostgreSQL est reporté ;
* pourquoi TinyDB est utilisé de manière limitée ;
* pourquoi certaines fonctionnalités sont limitées pour éviter une complexité excessive.

## `.env.example`

Le fichier `.env.example` documente les variables d’environnement nécessaires sans exposer les vraies valeurs sensibles.

## `requirements.txt`

Le fichier `requirements.txt` contient les dépendances utilisées, dont TinyDB.

Ces fichiers complètent la documentation du dossier `doc`.

---

# 33. Captures et preuves à préparer

Pour le dossier projet, les preuves suivantes peuvent être préparées :

* capture des modèles `Creation` et `PlayableProject` ;
* capture de l’administration Django ;
* capture du compte temporaire de lecture seule ;
* capture des tables ou migrations ;
* capture du fichier `doc/sql/schema.sql` ;
* capture des fichiers SQL natifs dans `docs/sql/`;
* capture du fichier `docs/sql/exemples_insert.sql` ;
* capture du service `core/services/nosql_notes.py` ;
* capture du script `scripts/demo_tinydb_notes.py` ;
* capture du terminal avec `python -m scripts.demo_tinydb_notes` ;
* capture des notes TinyDB affichées sur la page d’accueil.

Aucune capture ne doit afficher :

* mot de passe ;
* clé secrète ;
* variable sensible ;
* identifiant administrateur complet ;
* information privée inutile.

---

# 34. Conclusion

La base de données de Frostia Games est simple mais fonctionnelle.

Elle permet déjà :

* de stocker des créations ;
* de stocker des futurs projets jouables ;
* d’administrer les contenus depuis Django ;
* d’afficher les données dynamiquement dans les templates ;
* de masquer ou afficher certains contenus ;
* de documenter la structure SQL du projet ;
* de présenter des extraits SQL natifs ;
* de tester une expérimentation NoSQL avec TinyDB ;
* d’afficher des notes TinyDB sur la page d’accueil ;
* de préparer une évolution future vers PostgreSQL ou une solution NoSQL plus avancée.

Le choix de SQLite est adapté à la V1.

TinyDB est utilisé comme complément limité et contrôlé.

Le projet dispose donc d’une base de données cohérente avec son périmètre : simple, lisible, testable, documentée et suffisante pour une première version.

À ce stade, la priorité n’est plus d’ajouter une nouvelle base ou de complexifier l’architecture.

La priorité est de préparer les captures, les preuves et l’intégration propre dans le dossier projet final.
