# NoSQL - Frostia Games

## Objectif

Cette section présente la réflexion autour d'une future intégration NoSQL dans le projet **Frostia Games**.

Dans la V1 actuelle, aucune base NoSQL n'est implantée. Le projet utilise Django avec SQLite afin de conserver une architecture simple, stable et maîtrisable.

Le NoSQL est identifié comme une évolution possible, notamment pour stocker des contenus plus souples liés aux projets de jeux vidéo.

---

## Pourquoi le NoSQL n'est pas implanté dans la V1

La V1 de Frostia Games a pour objectif principal de mettre en place un socle Django fonctionnel :

* pages principales ;
* base SQLite ;
* modèles Django ;
* migrations ;
* administration Django ;
* affichage dynamique des données ;
* lancement local ;
* lancement avec Docker ;
* déploiement en ligne sur Render.

L'ajout d'une base NoSQL dès cette version aurait augmenté la complexité du projet sans apporter de bénéfice immédiat au fonctionnement actuel du site.

Le choix retenu est donc de stabiliser d'abord le socle relationnel avec SQLite, puis de prévoir une évolution NoSQL lorsque les besoins seront plus clairs.

---

## Besoins possibles pour une future base NoSQL

Une base NoSQL pourrait être utile plus tard pour stocker des données moins structurées, par exemple :

* fiches détaillées de projets ;
* sections variables selon les jeux ;
* historiques de développement ;
* notes de conception ;
* journaux de mise à jour ;
* blocs de contenu personnalisés ;
* métadonnées de médias ;
* informations évolutives sur les prototypes.

Ces données peuvent varier fortement d'un projet à l'autre.

Une structure NoSQL permettrait donc plus de souplesse qu'une table SQL classique.

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
```

---

## Différence entre SQL et NoSQL dans le projet

## SQL actuel

La base SQLite sert à stocker les données principales du site :

* créations ;
* projets jouables ;
* statuts ;
* visibilité ;
* dates de création et de modification.

Ces données sont structurées et correspondent bien à des tables relationnelles.

---

## NoSQL prévu

Une future base NoSQL pourrait servir à stocker des contenus plus flexibles :

* fiches longues ;
* blocs de contenu variables ;
* notes de conception ;
* médias associés ;
* historiques de projet.

Le NoSQL ne remplacerait pas forcément toute la base relationnelle.

Il pourrait être utilisé en complément de SQLite ou PostgreSQL pour certains contenus plus libres.

---

## Choix retenu pour la V1

Pour cette V1, le choix technique est le suivant :

* SQLite est utilisé pour la base de données principale ;
* Django ORM est utilisé pour manipuler les données ;
* aucune base NoSQL n'est encore connectée ;
* l'intégration NoSQL est placée dans la roadmap du projet.

Ce choix permet de garder une V1 stable, testable et maintenable.

---

## Pourquoi ne pas ajouter NoSQL artificiellement

Ajouter une technologie uniquement pour montrer qu'elle existe ne serait pas pertinent.

Dans la V1 actuelle, les données principales sont encore simples et structurées.

Elles sont donc adaptées à une base relationnelle.

Ajouter NoSQL maintenant aurait créé :

* une configuration supplémentaire ;
* une dépendance technique en plus ;
* une documentation plus longue ;
* des tests supplémentaires ;
* une architecture plus complexe ;
* un risque de confusion entre SQL et NoSQL.

Le choix le plus raisonnable est donc de documenter cette possibilité sans l'intégrer trop tôt.

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
8. Documenter la nouvelle architecture.

---

## Exemple d'utilisation future

Dans une version plus avancée, le projet pourrait utiliser :

* PostgreSQL pour les données structurées ;
* MongoDB pour les fiches longues et variables ;
* Django pour l'administration et l'affichage ;
* un système de sauvegarde pour éviter la perte de contenu.

Exemple de séparation possible :

| Type de donnée             | Solution possible |
| -------------------------- | ----------------- |
| Utilisateurs               | PostgreSQL        |
| Créations principales      | PostgreSQL        |
| Projets jouables           | PostgreSQL        |
| Fiches longues de projets  | MongoDB           |
| Notes de conception        | MongoDB           |
| Blocs de contenu variables | MongoDB           |
| Métadonnées flexibles      | MongoDB           |

Cette organisation n'est pas nécessaire dans la V1, mais elle reste envisageable si le projet devient plus complet.

---

## Limites de cette évolution

Une future intégration NoSQL devra être étudiée avec prudence.

Elle ne devra pas être ajoutée uniquement pour complexifier le projet.

Avant d'intégrer NoSQL, il faudra vérifier :

* si le besoin est réel ;
* si les données sont vraiment variables ;
* si une base SQL ne suffit plus ;
* si l'ajout reste maintenable ;
* si la sécurité est maîtrisée ;
* si la documentation peut rester claire ;
* si le projet ne devient pas trop lourd.

Si le besoin n'est pas confirmé, l'idée pourra être reportée ou abandonnée.

---

## Conclusion

Le NoSQL n'est pas implanté dans la V1 de Frostia Games, mais son usage est identifié et documenté.

La V1 privilégie une base SQL simple avec SQLite afin de valider le fonctionnement du backend Django.

Le NoSQL est prévu comme une évolution future possible pour gérer des contenus plus souples et plus détaillés liés aux projets de jeux vidéo.

Ce choix permet de conserver une V1 stable, claire et défendable, tout en préparant une évolution technique plus avancée si le besoin devient réel.
