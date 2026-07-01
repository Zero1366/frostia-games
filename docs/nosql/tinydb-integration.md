# Intégration NoSQL TinyDB — Frostia Games

## Objectif du document

Ce document présente l’intégration NoSQL ajoutée au projet **Frostia Games**.

L’objectif n’est pas de remplacer la base relationnelle SQLite, mais d’ajouter une solution NoSQL ciblée pour stocker des données plus souples.

La V1 conserve donc deux approches complémentaires :

* SQLite pour les données principales et structurées du site ;
* TinyDB pour des notes de progression et des métadonnées variables.

---

## Pourquoi TinyDB ?

TinyDB est une base de données NoSQL légère qui stocke les données sous forme de documents JSON.

Elle est adaptée à cette V1 car elle permet de démontrer une logique NoSQL sans ajouter une infrastructure lourde comme MongoDB.

Ce choix permet de garder un périmètre simple, stable et maîtrisable.

---

## Rôle du NoSQL dans Frostia Games

Dans Frostia Games, TinyDB est utilisé pour stocker des notes de progression liées au projet.

Ces notes peuvent contenir des informations variables :

* titre ;
* contenu ;
* statut ;
* tags ;
* date ;
* code du projet.

Ces données sont plus souples que les données principales stockées dans SQLite.

---

## Complémentarité SQL / NoSQL

| Données                | Technologie         | Justification                            |
| ---------------------- | ------------------- | ---------------------------------------- |
| Créations du portfolio | SQLite / Django ORM | Données structurées et stables           |
| Projets jouables       | SQLite / Django ORM | Données principales du site              |
| Notes de progression   | TinyDB              | Données souples au format document       |
| Métadonnées variables  | TinyDB              | Champs pouvant évoluer selon les besoins |

---

## Fichiers concernés

| Fichier                            | Rôle                                                                |
| ---------------------------------- | ------------------------------------------------------------------- |
| `core/services/nosql_notes.py`     | Service Python permettant de créer, lire et filtrer les notes NoSQL |
| `data/nosql/project_notes_db.json` | Base documentaire TinyDB contenant les notes                        |
| `scripts/demo_tinydb_notes.py`     | Script de démonstration permettant de tester la lecture NoSQL       |
| `requirements.txt`                 | Ajout de la dépendance `tinydb`                                     |

---

## Fonctionnement

Le service `nosql_notes.py` contient plusieurs fonctions :

| Fonction                  | Rôle                                           |
| ------------------------- | ---------------------------------------------- |
| `get_notes_db()`          | Ouvre ou crée la base TinyDB                   |
| `seed_project_notes()`    | Ajoute des notes d’exemple si la base est vide |
| `list_project_notes()`    | Récupère toutes les notes                      |
| `find_notes_by_project()` | Recherche les notes liées à un projet précis   |

Le script `demo_tinydb_notes.py` utilise ces fonctions pour charger les notes liées au projet `frostia-games` et les afficher dans le terminal.

---

## Commande de test

La preuve de fonctionnement est obtenue avec la commande suivante :

```bash
python -m scripts.demo_tinydb_notes
```

Cette commande affiche dans le terminal les notes stockées dans TinyDB.

---

## Preuve obtenue

Le test affiche les informations suivantes :

* titre de la note ;
* statut ;
* tags ;
* contenu.

Cela montre que les données NoSQL sont bien stockées, lues et exploitées par un script Python du projet.

---

## Intérêt pour le dossier projet

Cette intégration permet de montrer une utilisation réelle du NoSQL dans Frostia Games.

Elle répond au besoin de démontrer la compétence liée aux composants d’accès aux données SQL et NoSQL, tout en conservant un périmètre raisonnable.

SQLite reste utilisé pour les données principales du site, tandis que TinyDB sert à stocker des données plus flexibles.

Cette séparation permet de montrer la complémentarité entre une base relationnelle et une base documentaire.
