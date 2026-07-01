# Modèles Django — Frostia Games

## Objectif du document

Ce document présente les modèles Django utilisés dans le projet **Frostia Games**.

L’objectif est de montrer comment les données principales du site sont structurées côté back-end.

Le projet utilise **Django ORM** afin de définir les modèles en Python, puis de générer les tables correspondantes dans la base de données SQLite.

---

## Modèles principaux

Deux modèles principaux sont utilisés dans la V1 du projet.

| Modèle            | Rôle                                                                        |
| ----------------- | --------------------------------------------------------------------------- |
| `Creation`        | Représente une création ou un projet présenté dans la page “Mes créations”. |
| `PlayableProject` | Représente un projet jouable ou une démonstration prévue.                   |

---

## Modèle Creation

Le modèle `Creation` permet de stocker les informations liées aux créations présentées dans le portfolio.

Il contient notamment :

* un titre ;
* un slug ;
* une lettre de classement alphabétique ;
* un nom de code ;
* un type de projet ;
* un état d’avancement ;
* une description courte ;
* un indicateur de visibilité ;
* une date de création ;
* une date de modification.

Ce modèle sert à organiser les créations visibles dans la page **Mes créations**.

---

## Rôle du modèle Creation

Le modèle `Creation` permet de structurer les contenus présentés dans le portfolio.

Chaque création peut être affichée ou masquée grâce au champ `is_visible`.

Cela permet de préparer des contenus depuis l’administration Django sans forcément les rendre visibles immédiatement sur le site public.

---

## Modèle PlayableProject

Le modèle `PlayableProject` permet de stocker les informations liées aux projets jouables ou aux futures démonstrations.

Il contient notamment :

* un titre ;
* un slug ;
* un état ;
* un type de contenu ;
* une description courte ;
* un message de disponibilité ;
* un indicateur de disponibilité ;
* un indicateur de visibilité ;
* une date de création ;
* une date de modification.

Ce modèle sert à présenter les projets jouables prévus dans la V1 du site.

---

## Rôle du modèle PlayableProject

Le modèle `PlayableProject` permet de séparer les créations générales des projets réellement jouables ou prévus comme démonstrations.

Cette séparation rend l’organisation du projet plus claire :

* les créations présentent les projets, l’univers ou les idées du portfolio ;
* les projets jouables présentent les démonstrations disponibles ou prévues.

---

## Utilisation de Django ORM

Django ORM permet de manipuler les données à partir de classes Python.

Les modèles définis dans `models.py` sont utilisés par Django pour :

* créer les migrations ;
* générer les tables SQL ;
* gérer les données depuis l’administration Django ;
* récupérer les contenus dans les vues ;
* afficher les contenus dans les templates.

---

## Lien avec la base SQL

Les modèles Django sont liés aux tables SQL générées par les migrations.

| Modèle Django     | Table SQL générée          |
| ----------------- | -------------------------- |
| `Creation`        | `creations_creation`       |
| `PlayableProject` | `playable_playableproject` |

Les fichiers SQL générés sont présents dans :

```txt
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
```

---

## Preuves à intégrer dans le dossier

Pour cette partie, les preuves à intégrer dans le dossier projet sont :

| Élément                          | Preuve                                      |
| -------------------------------- | ------------------------------------------- |
| Code du modèle `Creation`        | Capture du fichier `models.py`              |
| Code du modèle `PlayableProject` | Capture du fichier `models.py`              |
| Table SQL générée                | Extrait `CREATE TABLE` correspondant        |
| Administration Django            | Capture des modèles visibles dans `/admin/` |
| Rendu final                      | Capture de la page utilisant les données    |

---

## Intérêt pour le projet

Les modèles Django constituent la base du back-end du projet.

Ils permettent de structurer les données, de les administrer et de les afficher dans les pages publiques du site.

Cette partie montre le lien entre :

* le code Python ;
* la base de données SQLite ;
* l’administration Django ;
* les vues ;
* les templates ;
* le rendu final côté utilisateur.
