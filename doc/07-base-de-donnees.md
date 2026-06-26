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
* la réflexion NoSQL ;
* le lien avec l’administration Django ;
* le lien avec le déploiement Render ;
* les limites actuelles ;
* les évolutions possibles vers PostgreSQL.

L’objectif est de montrer que la V1 possède une base de données simple, fonctionnelle et cohérente avec le périmètre du projet.

---

# 1. Contexte

Frostia Games est un portfolio développé avec **Django**.

Dans la V1, la base de données sert à rendre certaines parties du site dynamiques.

Les données ne sont plus uniquement écrites directement dans les fichiers HTML.

Une partie du contenu peut maintenant être ajoutée, modifiée ou masquée depuis l’administration Django.

La base est utilisée pour gérer :

* les créations ;
* les futurs projets jouables.

Ce choix permet de montrer que le projet possède un vrai backend Django, même si le périmètre reste volontairement limité.

---

# 2. Choix de SQLite pour la V1

La V1 utilise SQLite.

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
* de système de rôles avancés ;
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

Deux applications Django utilisent actuellement la base de données :

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

---

# 10. ORM Django

Le projet utilise l’ORM Django pour manipuler les données.

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

---

# 12. Données actuellement stockées

Dans la V1, la base stocke principalement :

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

# 13. Données non stockées dans la V1

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

# 14. Interface d’administration

La base est alimentée principalement via l’administration Django.

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

# 15. Lien avec le déploiement Render

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

Cette commande applique les migrations nécessaires à la base.

Pour une V1, ce fonctionnement est suffisant pour montrer que le projet peut être lancé et déployé.

Pour une version plus durable ou plus avancée, PostgreSQL pourra être envisagé.

---

# 16. Variables d’environnement liées au backend

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

---

# 17. Fichier `.gitignore` et base SQLite

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

# 18. Schéma SQL documentaire

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

# 19. Exemple de structure SQL

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

# 20. NoSQL

Un fichier de réflexion NoSQL a été ajouté :

```text
doc/sql/nosql.md
```

Dans la V1, aucune base NoSQL n’est implantée.

Ce choix est volontaire, car l’objectif actuel est de stabiliser le socle Django avec SQLite.

Une future base NoSQL pourrait être utile pour stocker des contenus plus souples :

* fiches détaillées ;
* notes de conception ;
* blocs de contenu variables ;
* historiques de développement ;
* métadonnées de médias ;
* sections différentes selon les projets.

Le NoSQL est donc identifié comme une évolution possible, mais il n’est pas ajouté artificiellement dans la V1.

---

# 21. Sécurité liée à la base de données

La sécurité de la base repose principalement sur :

* l’utilisation de l’ORM Django ;
* l’absence de requêtes SQL brutes dans les vues ;
* la validation des champs par les modèles ;
* l’administration protégée par authentification ;
* l’échappement automatique dans les templates ;
* le filtrage des contenus visibles ;
* la séparation des secrets avec les variables d’environnement ;
* l’absence de vrai upload serveur dans la V1.

Le projet ne construit pas de requêtes SQL en concaténant du texte utilisateur.

Cela limite les risques d’injection SQL.

---

# 22. Limites de la V1

La V1 ne contient pas encore :

* de relations complexes entre les tables ;
* de table média ;
* de table version ;
* de table utilisateur personnalisée ;
* de base PostgreSQL ;
* de base NoSQL connectée ;
* de vrai système d’upload ;
* de stockage de fichiers en base ;
* de compte jury temporaire ;
* d’administration personnalisée ;
* de sauvegarde automatique avant modification ;
* de système de restauration des contenus.

Ces limites sont volontaires.

L’objectif est de garder une base claire, testable et stable.

---

# 23. Évolutions prévues

Les évolutions possibles sont :

1. Ajouter une table de fiches détaillées.
2. Ajouter une table de médias.
3. Ajouter une table de versions.
4. Relier un projet jouable à une création.
5. Ajouter PostgreSQL pour une version plus avancée.
6. Étudier une base NoSQL pour les contenus variables.
7. Ajouter un système d’upload sécurisé.
8. Ajouter des permissions plus fines dans l’administration.
9. Créer un compte jury temporaire si un accès direct est demandé.
10. Ajouter un système de sauvegarde automatique avant modification.
11. Ajouter un système de restauration des contenus.
12. Ajouter des tests automatisés sur les modèles Django.

Ces évolutions sont reportées afin d’éviter d’élargir trop vite le périmètre de la V1.

---

# 24. Lien avec les fichiers racine

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
* pourquoi NoSQL n’est pas implanté artificiellement ;
* pourquoi certaines fonctionnalités sont limitées pour éviter une complexité excessive.

## `.env.example`

Le fichier `.env.example` documente les variables d’environnement nécessaires sans exposer les vraies valeurs sensibles.

Ces fichiers complètent la documentation du dossier `doc`.

---

# 25. Conclusion

La base de données de Frostia Games est simple mais fonctionnelle.

Elle permet déjà :

* de stocker des créations ;
* de stocker des futurs projets jouables ;
* d’administrer les contenus depuis Django ;
* d’afficher les données dynamiquement dans les templates ;
* de masquer ou afficher certains contenus ;
* de documenter la structure SQL du projet ;
* de préparer une évolution future vers PostgreSQL ou NoSQL.

Le choix de SQLite est adapté à la V1.

Il permet de valider le backend Django sans complexifier inutilement l’architecture.

Le projet dispose donc d’une base de données cohérente avec son périmètre : simple, lisible, testable, documentée et suffisante pour une première version.
