````md
# NoSQL - Frostia Games

## Objectif

Cette section présente la réflexion autour d'une future intégration NoSQL dans le projet Frostia Games.

Dans la V1 actuelle, aucune base NoSQL n'est implantée. Le projet utilise Django avec SQLite afin de conserver une architecture simple, stable et maîtrisable.

Le NoSQL est identifié comme une évolution possible, notamment pour stocker des contenus plus souples liés aux projets de jeux vidéo.

---

## Pourquoi le NoSQL n'est pas implanté dans la V1

La V1 de Frostia Games a pour objectif principal de mettre en place un socle Django fonctionnel :

- pages principales ;
- base SQLite ;
- modèles Django ;
- migrations ;
- administration Django ;
- affichage dynamique des données ;
- lancement local ;
- lancement avec Docker.

L'ajout d'une base NoSQL dès cette version aurait augmenté la complexité du projet sans apporter de bénéfice immédiat au fonctionnement actuel du site.

Le choix retenu est donc de stabiliser d'abord le socle relationnel avec SQLite, puis de prévoir une évolution NoSQL lorsque les besoins seront plus clairs.

---

## Besoins possibles pour une future base NoSQL

Une base NoSQL pourrait être utile plus tard pour stocker des données moins structurées, par exemple :

- fiches détaillées de projets ;
- sections variables selon les jeux ;
- historiques de développement ;
- notes de conception ;
- journaux de mise à jour ;
- blocs de contenu personnalisés ;
- métadonnées de médias ;
- informations évolutives sur les prototypes.

Ces données peuvent varier fortement d'un projet à l'autre. Une structure NoSQL permettrait donc plus de souplesse qu'une table SQL classique.

---

## Exemple de document NoSQL possible

Exemple théorique d'un document MongoDB pour une future fiche projet :

```json
{
  "slug": "kryoncore",
  "title": "KryonCore",
  "status": "En préparation",
  "type": "Jeu vidéo PC",
  "sections": [
    {
      "title": "Présentation",
      "content": "KryonCore est un projet de jeu vidéo servant de base à des recherches techniques et créatives."
    },
    {
      "title": "Gameplay",
      "content": "Le gameplay sera documenté lorsque la direction du projet sera stabilisée."
    },
    {
      "title": "État du développement",
      "content": "Le projet est actuellement en phase préparatoire."
    }
  ],
  "media": {
    "poster": null,
    "trailer": null,
    "screenshots": []
  },
  "updated_at": "2026-06-24"
}
````

---

## Différence entre SQL et NoSQL dans le projet

### SQL actuel

La base SQLite sert à stocker les données principales du site :

* créations ;
* projets jouables ;
* statuts ;
* visibilité ;
* dates de création et de modification.

Ces données sont structurées et correspondent bien à des tables relationnelles.

### NoSQL prévu

Une future base NoSQL pourrait servir à stocker des contenus plus flexibles :

* fiches longues ;
* blocs de contenu variables ;
* notes de conception ;
* médias associés ;
* historiques de projet.

---

## Choix retenu pour la V1

Pour cette V1, le choix technique est le suivant :

* SQLite est utilisé pour la base de données principale ;
* Django ORM est utilisé pour manipuler les données ;
* aucune base NoSQL n'est encore connectée ;
* l'intégration NoSQL est placée dans la roadmap du projet.

Ce choix permet de garder une V1 stable, testable et maintenable.

---

## Roadmap NoSQL

Une future version pourrait intégrer MongoDB ou une autre solution NoSQL pour gérer les fiches détaillées des projets.

Étapes possibles :

1. Identifier les contenus réellement variables.
2. Définir une structure de document.
3. Choisir une solution NoSQL adaptée.
4. Connecter Django à cette base.
5. Tester la récupération des données.
6. Afficher les fiches détaillées dynamiquement.
7. Sécuriser les accès et les données.

---

## Conclusion

Le NoSQL n'est pas implanté dans la V1 de Frostia Games, mais son usage est identifié et documenté.

La V1 privilégie une base SQL simple avec SQLite afin de valider le fonctionnement du backend Django. Le NoSQL est prévu comme une évolution future pour gérer des contenus plus souples et plus détaillés liés aux projets de jeux vidéo.

```
```
