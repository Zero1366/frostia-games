# Modélisation backend - Frostia Games

## Objectif du document

Ce document présente la modélisation backend de la V1 du projet **Frostia Games**.

Il décrit :

* les entités utilisées dans la base de données ;
* le rôle des modèles Django ;
* le schéma relationnel simplifié ;
* le MCD simplifié ;
* les cas d'utilisation principaux ;
* les diagrammes de séquence ;
* le rôle de l'ORM Django ;
* les limites de la V1 ;
* les évolutions prévues.

L'objectif est de montrer que le backend du projet repose sur une structure claire, même si la V1 reste volontairement simple.

---

# 1. Contexte backend du projet

Frostia Games est un portfolio développé avec **Django**.

La V1 utilise :

* Django pour le routage, les vues, les modèles et l'administration ;
* SQLite pour stocker les données principales ;
* l'ORM Django pour manipuler les données ;
* l'administration Django pour ajouter ou modifier les contenus ;
* des templates Django pour afficher les données dans les pages HTML ;
* Render pour le déploiement en ligne ;
* Gunicorn pour lancer l'application Django en production ;
* WhiteNoise pour la gestion des fichiers statiques en production.

La base de données est utilisée pour rendre certaines parties du site dynamiques.

Actuellement, deux types de contenus sont stockés en base :

* les créations ;
* les futurs projets jouables.

Le backend reste volontairement limité afin de conserver une V1 stable, lisible et maintenable.

---

# 2. Modèles Django utilisés

## 2.1 Modèle `Creation`

Le modèle `Creation` représente une création ou un projet présenté dans la page **Mes créations**.

Il permet d'enregistrer :

* le titre du projet ;
* son identifiant URL ;
* sa lettre de classement alphabétique ;
* son nom de code ;
* son type ;
* son statut ;
* sa description courte ;
* sa visibilité sur le site ;
* ses dates de création et de modification.

Ce modèle permet d'afficher dynamiquement les créations enregistrées dans l'administration Django.

Il évite de devoir modifier directement le HTML pour changer certains contenus affichés dans la page **Mes créations**.

---

## 2.2 Modèle `PlayableProject`

Le modèle `PlayableProject` représente un futur contenu jouable, une vidéo, un teaser ou un prototype prévu dans la page **Projets jouables**.

Il permet d'enregistrer :

* le titre du contenu ;
* son identifiant URL ;
* son statut ;
* le type de contenu prévu ;
* une description courte ;
* un message de disponibilité ;
* son état de disponibilité ;
* sa visibilité sur le site ;
* ses dates de création et de modification.

Ce modèle permet d'afficher clairement qu'un projet jouable est prévu, sans annoncer une fonctionnalité qui n'est pas encore disponible dans la V1.

Il sert donc à préparer une évolution future tout en restant honnête sur les limites actuelles du projet.

---

# 3. Schéma relationnel simplifié

## Table `creations_creation`

| Champ               | Type logique       | Rôle                         |
| ------------------- | ------------------ | ---------------------------- |
| `id`                | Integer            | Identifiant unique           |
| `title`             | Texte court        | Titre de la création         |
| `slug`              | Texte court unique | Identifiant URL              |
| `alphabet_letter`   | Texte court        | Lettre de classement         |
| `code_name`         | Texte court        | Nom de code du projet        |
| `project_type`      | Texte court        | Type de projet               |
| `status`            | Texte court        | Statut de développement      |
| `short_description` | Texte long         | Description courte           |
| `is_visible`        | Booléen            | Affichage ou non sur le site |
| `created_at`        | Date / heure       | Date de création             |
| `updated_at`        | Date / heure       | Dernière modification        |

---

## Table `playable_playableproject`

| Champ                  | Type logique       | Rôle                                 |
| ---------------------- | ------------------ | ------------------------------------ |
| `id`                   | Integer            | Identifiant unique                   |
| `title`                | Texte court        | Titre du projet jouable              |
| `slug`                 | Texte court unique | Identifiant URL                      |
| `status`               | Texte court        | Statut du contenu                    |
| `content_type`         | Texte court        | Type de contenu prévu                |
| `short_description`    | Texte long         | Description courte                   |
| `availability_message` | Texte long         | Message de disponibilité             |
| `is_available`         | Booléen            | Indique si le contenu est disponible |
| `is_visible`           | Booléen            | Affichage ou non sur le site         |
| `created_at`           | Date / heure       | Date de création                     |
| `updated_at`           | Date / heure       | Dernière modification                |

---

# 4. MCD simplifié

Dans la V1, les deux entités sont indépendantes.

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

## Explication

L'entité `CREATION` sert à gérer les projets présentés dans le lexique de la page **Mes créations**.

L'entité `PLAYABLE_PROJECT` sert à gérer les contenus liés à la page **Projets jouables**.

Dans cette V1, il n'existe pas encore de relation directe entre ces deux entités.

Ce choix est volontaire.

Il permet de conserver un backend simple, stable et adapté au périmètre actuel.

Une future version pourra ajouter des relations entre :

* les créations ;
* les médias ;
* les fiches détaillées ;
* les versions jouables ;
* les captures ;
* les liens externes ;
* les journaux de développement.

---

# 5. Cas d'utilisation

## Acteurs

Le projet possède deux acteurs principaux :

```text
- Visiteur
- Administrateur
```

---

## 5.1 Visiteur

Le visiteur peut :

* consulter la page d'accueil ;
* consulter la page **Mes créations** ;
* cliquer sur une lettre du lexique ;
* consulter les créations visibles ;
* consulter la page **Projets jouables** ;
* voir l'état de disponibilité d'un futur projet jouable ;
* sélectionner un fichier local dans l'interface préparatoire ;
* comprendre qu'aucun vrai upload serveur n'est implanté dans la V1.

Le visiteur n'a pas de compte utilisateur dans cette V1.

Il n'a pas accès à l'administration Django.

---

## 5.2 Administrateur

L'administrateur peut :

* se connecter à l'administration Django ;
* ajouter une création ;
* modifier une création ;
* masquer ou afficher une création ;
* ajouter un futur projet jouable ;
* modifier un projet jouable ;
* définir si un projet jouable est disponible ;
* masquer ou afficher un projet jouable.

L'administration Django reste privée.

Aucun identifiant administrateur n'est publié dans GitHub ou dans la documentation publique.

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
             |----------------------------------------->|
             |                                          |
             | consulter les créations                  |
             |----------------------------------------->|
             |                                          |
             | afficher un projet depuis le lexique     |
             |----------------------------------------->|
             |                                          |
             | consulter les projets jouables           |
             |----------------------------------------->|
             |                                          |
             | sélectionner un fichier local            |
             |----------------------------------------->|
             |                                          |
                                                        |
                                                        | se connecter à l'admin
                                                        |---------------------->
                                                        |
                                                        | ajouter une création
                                                        |---------------------->
                                                        |
                                                        | modifier une création
                                                        |---------------------->
                                                        |
                                                        | ajouter un projet jouable
                                                        |---------------------->
                                                        |
                                                        | modifier un projet jouable
                                                        |---------------------->
```

## Explication

Le visiteur interagit uniquement avec les pages publiques du site.

L'administrateur utilise l'administration Django pour gérer les données affichées sur le site.

La V1 ne contient pas encore :

* d'espace utilisateur public ;
* de système de rôles avancé ;
* de compte jury temporaire ;
* de véritable upload serveur ;
* de compte visiteur ;
* d'API REST.

Ces éléments sont reportés afin de conserver une V1 stable.

---

# 7. Diagramme de séquence : consultation des créations

## Objectif

Ce diagramme montre le fonctionnement lorsqu'un visiteur consulte la page **Mes créations**.

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
   v
Visiteur
```

## Explication

La vue Django récupère uniquement les créations dont le champ `is_visible` est actif.

La récupération des données passe par l'ORM Django, ce qui évite d'écrire directement des requêtes SQL brutes dans le code.

---

# 8. Diagramme de séquence : ajout d'une création via l'administration Django

## Objectif

Ce diagramme montre le fonctionnement lorsqu'un administrateur ajoute une création dans l'administration Django.

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
   v
Administrateur
```

## Explication

L'ajout d'une création passe par l'administration Django.

Les champs du modèle définissent les contraintes principales comme :

* la longueur maximale ;
* l'unicité du slug ;
* les champs obligatoires ;
* la visibilité ;
* les dates de création et de modification.

L'ORM Django traduit l'opération en requête SQL sans écrire manuellement du SQL dans le code applicatif.

---

# 9. Diagramme de séquence : consultation des projets jouables

## Objectif

Ce diagramme montre le fonctionnement lorsqu'un visiteur consulte la page **Projets jouables**.

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
   v
Visiteur
```

## Explication

La page **Projets jouables** affiche les données enregistrées dans la base SQLite.

Dans la V1, l'interface de sélection de fichier est seulement préparatoire.

Aucun fichier n'est envoyé ni enregistré sur le serveur.

---

# 10. Rôle de l'ORM Django

L'ORM Django permet de manipuler les données à travers des classes Python.

Exemple :

```python
Creation.objects.filter(is_visible=True).order_by(
    "alphabet_letter",
    "title",
)
```

Cette instruction permet de récupérer les créations visibles sans écrire directement de requête SQL.

L'ORM apporte plusieurs avantages :

* code plus lisible ;
* meilleure intégration avec Django ;
* réduction du risque d'injection SQL ;
* compatibilité avec les migrations ;
* manipulation des données sous forme d'objets Python ;
* possibilité de changer de moteur de base plus tard plus facilement.

Ce dernier point est important, car une migration future vers PostgreSQL pourra être envisagée sans réécrire toute la logique métier.

---

# 11. Sécurité liée à la base de données

La V1 utilise plusieurs mécanismes de sécurité fournis par Django :

* utilisation de l'ORM au lieu de requêtes SQL brutes ;
* administration protégée par authentification ;
* protection CSRF disponible pour les formulaires ;
* échappement automatique des variables dans les templates ;
* validation des champs par les modèles Django ;
* absence de vrai upload serveur dans la V1 ;
* séparation des secrets dans les variables d'environnement ;
* fichier `.env.example` pour documenter les variables sans exposer les vraies valeurs.

Le projet n'utilise pas de requêtes SQL construites manuellement avec des chaînes de caractères.

Cela limite les risques d'injection SQL.

---

# 12. Scripts SQL documentaires

Le fichier suivant contient un équivalent SQL simplifié des tables utilisées :

```text
doc/sql/schema.sql
```

Il contient :

* les instructions `CREATE TABLE` ;
* les exemples `INSERT INTO` ;
* les commentaires expliquant le rôle des tables.

Dans le projet réel, la création des tables est gérée par les migrations Django.

Le fichier SQL est ajouté pour documenter la structure de la base et répondre aux attendus du dossier projet.

Il ne remplace pas les migrations Django.

---

# 13. NoSQL

Le fichier suivant présente la réflexion autour d'une future intégration NoSQL :

```text
doc/sql/nosql.md
```

Dans la V1, aucune base NoSQL n'est implantée.

Le projet utilise SQLite afin de conserver une base simple, stable et adaptée au périmètre actuel.

Une future base NoSQL pourrait servir à stocker des contenus plus flexibles comme :

* fiches détaillées ;
* blocs de contenu variables ;
* notes de conception ;
* historiques de développement ;
* métadonnées de médias.

Ce choix est documenté comme une piste future, mais il n'est pas intégré dans la V1 afin d'éviter une complexité inutile.

---

# 14. Lien avec le déploiement Render

Le backend est maintenant déployé en ligne avec Render.

Le projet utilise :

```text
https://frostia-games.onrender.com
```

Le déploiement permet de vérifier que :

* Django fonctionne hors de l'environnement local ;
* Gunicorn lance correctement l'application ;
* les fichiers statiques sont collectés ;
* les migrations sont appliquées ;
* l'administration Django reste accessible ;
* les variables d'environnement peuvent être utilisées pour les secrets.

La commande de build Render est :

```bash
bash build.sh
```

La commande de démarrage Render est :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

---

# 15. Limites de la V1

La V1 ne contient pas encore :

* de vraie page détail projet ;
* de vrai upload serveur ;
* de vrai lecteur vidéo ;
* d'API REST ;
* de système de comptes publics ;
* de rôles avancés ;
* de base NoSQL connectée ;
* de base PostgreSQL ;
* de compte jury temporaire ;
* d'administration personnalisée ;
* de graphiques Plotly.js ;
* de tests automatisés complets.

Ces limites sont volontaires.

Elles permettent de conserver un projet stable, testable, maintenable et présentable.

Le déploiement Render est fonctionnel, mais une configuration de production plus avancée pourra être envisagée plus tard si le projet évolue.

---

# 16. Évolutions prévues

Les évolutions possibles du backend sont :

* ajouter des fiches détaillées pour les créations ;
* relier les projets jouables à une création ;
* ajouter une table de médias ;
* ajouter une table de versions ;
* ajouter une gestion plus avancée des statuts ;
* ajouter un vrai système d'upload sécurisé ;
* migrer vers PostgreSQL si le projet devient plus complet ;
* créer un compte jury temporaire en lecture seule si un accès direct est demandé ;
* créer une administration personnalisée ;
* envisager une base NoSQL pour les contenus très variables ;
* ajouter des tests automatisés Django ;
* ajouter un système de sauvegarde automatique avant modification.

Ces évolutions sont reportées afin de protéger le périmètre de la V1.

---

# 17. Lien avec les fichiers racine

La modélisation backend est complétée par plusieurs fichiers situés à la racine du projet.

## `README.md`

Le fichier `README.md` permet de présenter rapidement le projet, son installation, son lancement, son déploiement et ses limites.

## `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` explique pourquoi Django a été retenu pour la V1 et pourquoi d'autres pistes, comme C# / Razor, ont été reportées.

## `.env.example`

Le fichier `.env.example` documente les variables d'environnement nécessaires sans exposer les vraies valeurs sensibles.

Ces fichiers permettent de rendre le backend plus compréhensible pour une personne qui découvre le dépôt.

---

# 18. Conclusion

La V1 de Frostia Games possède un backend simple mais fonctionnel.

Elle montre :

* une structure Django claire ;
* deux modèles reliés à une base SQLite ;
* une administration fonctionnelle ;
* des migrations ;
* un affichage dynamique dans les templates ;
* une séparation entre données, vues et templates ;
* une réflexion sur la sécurité ;
* une documentation SQL et NoSQL ;
* un déploiement Render fonctionnel ;
* une documentation des limites et évolutions.

Le backend reste volontairement limité afin d'éviter une complexité inutile.

Il constitue une base stable pour faire évoluer le projet progressivement.
