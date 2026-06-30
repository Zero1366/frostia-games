# SQL natif — Frostia Games

## Objectif du document

Ce document présente des extraits SQL natifs liés au projet **Frostia Games**.

L’objectif est de montrer la structure réelle des tables générées par Django, ainsi que des exemples d’insertion de données avec des requêtes `INSERT INTO`.

Le projet utilise SQLite comme base relationnelle principale pour la V1.

---

## Tables principales

Deux tables principales sont utilisées pour les contenus du site :

| Table                      | Rôle                                                          |
| -------------------------- | ------------------------------------------------------------- |
| `creations_creation`       | Stocke les créations présentées dans la page “Mes créations”. |
| `playable_playableproject` | Stocke les projets jouables ou démonstrations prévues.        |

---

## Génération des tables

Les scripts SQL de création des tables ont été générés avec la commande Django suivante :

```bash
python manage.py sqlmigrate creations 0001
python manage.py sqlmigrate playable 0001
```

Ces commandes permettent d’obtenir le SQL réellement produit par Django à partir des migrations du projet.

Les fichiers générés sont stockés dans :

```txt
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
```

---

## Exemple : table creations_creation

La table `creations_creation` contient les informations nécessaires pour présenter une création dans le portfolio.

Elle contient notamment :

* un identifiant unique ;
* un titre ;
* un slug ;
* une lettre de classement alphabétique ;
* un nom de code ;
* un type de projet ;
* un état d’avancement ;
* une description courte ;
* un indicateur de visibilité ;
* les dates de création et de modification.

Cette table permet d’alimenter la page “Mes créations”.

---

## Exemple : table playable_playableproject

La table `playable_playableproject` contient les informations liées aux projets jouables ou aux futures démonstrations.

Elle contient notamment :

* un identifiant unique ;
* un titre ;
* un slug ;
* un état ;
* un type de contenu ;
* une description courte ;
* un message de disponibilité ;
* un indicateur de disponibilité ;
* un indicateur de visibilité ;
* les dates de création et de modification.

Cette table permet de présenter les projets jouables prévus dans la V1 du site.

---

## Exemples INSERT INTO

Des exemples d’insertion SQL native sont présents dans le fichier suivant :

```txt
docs/sql/exemples_insert.sql
```

Ces exemples montrent comment ajouter manuellement une création et un projet jouable dans les tables principales.

---

## Intérêt pour le dossier projet

Ces extraits SQL permettent de montrer que le projet ne repose pas uniquement sur l’ORM Django.

Ils permettent aussi de démontrer la structure relationnelle utilisée par l’application :

* création des tables ;
* typage des champs ;
* contraintes principales ;
* exemples d’insertion de données.

Cette partie valorise les compétences liées à la base de données relationnelle et au SQL natif.
