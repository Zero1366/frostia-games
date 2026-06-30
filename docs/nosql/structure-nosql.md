# Structure NoSQL — Frostia Games

## Objectif

Cette partie présente l’intégration NoSQL prévue pour le projet **Frostia Games**.

L’objectif n’est pas de remplacer la base relationnelle SQLite, mais d’ajouter une structure complémentaire pour stocker des données plus souples.

La base SQL reste utilisée pour les données principales :

* créations ;
* projets jouables ;
* administration Django ;
* données structurées.

La partie NoSQL est utilisée pour des notes de progression ou des métadonnées variables liées aux projets.

---

## Pourquoi ajouter du NoSQL ?

Certaines données du projet peuvent évoluer de manière plus libre qu’une table relationnelle classique.

Exemples :

* notes de développement ;
* journal de progression ;
* tags variables ;
* remarques libres ;
* étapes de conception ;
* informations temporaires sur un projet.

Ces données n’ont pas toujours besoin d’un schéma relationnel strict.

Le NoSQL est donc utilisé comme complément pour stocker des documents plus flexibles.

---

## Exemple de document NoSQL

```json
{
  "project_code": "frostia-games",
  "title": "Mise en place de la V1",
  "content": "Création du portfolio Django, déploiement Render et structuration des preuves.",
  "tags": ["django", "portfolio", "v1", "render"],
  "status": "done",
  "created_at": "2026-06-30"
}
```

---

## Rôle du document

Ce document représente une note de progression.

Il permet de conserver une trace d’une étape du projet sans modifier la structure SQL principale.

Les champs peuvent varier selon les besoins :

* certaines notes peuvent avoir des tags ;
* certaines notes peuvent avoir un statut ;
* certaines notes peuvent contenir des remarques plus longues ;
* d’autres peuvent seulement contenir un titre et un contenu.

---

## Complémentarité SQL / NoSQL

| Type de données       | Technologie | Justification                  |
| --------------------- | ----------- | ------------------------------ |
| Créations principales | SQLite      | Données structurées et stables |
| Projets jouables      | SQLite      | Données relationnelles simples |
| Notes de progression  | NoSQL       | Données souples et variables   |
| Métadonnées libres    | NoSQL       | Structure flexible             |

---

## Limite volontaire

L’intégration NoSQL reste volontairement limitée.

Le but est de démontrer la complémentarité entre SQL et NoSQL sans transformer la V1 en projet trop complexe.
