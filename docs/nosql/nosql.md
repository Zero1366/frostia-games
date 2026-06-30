# NoSQL - Frostia Games

## Objectif du document

Ce document présente la réflexion menée autour d'une future intégration NoSQL dans le projet **Frostia Games**.

Dans la V1 actuelle, aucune base NoSQL n'est implantée. Le projet utilise Django avec une base relationnelle SQLite afin de conserver une architecture simple, stable et maîtrisable.

Le NoSQL est identifié comme une évolution possible du projet, notamment pour stocker des contenus plus souples liés aux projets de jeux vidéo.

Ce document ne présente donc pas une fonctionnalité NoSQL déjà développée, mais une analyse technique préparatoire permettant d'expliquer pourquoi cette technologie n'a pas été ajoutée dans la V1 et dans quels cas elle pourrait devenir pertinente.

---

## Situation actuelle du projet

La V1 de Frostia Games repose sur une architecture Django classique.

Elle comprend :

* des pages publiques ;
* une base SQLite ;
* des modèles Django ;
* des migrations ;
* une administration Django ;
* un affichage dynamique des données ;
* un lancement local ;
* un lancement avec Docker ;
* un déploiement en ligne sur Render ;
* une documentation technique ;
* des preuves de fonctionnement.

Cette version a été volontairement limitée afin de produire un socle stable, testable et défendable.

Le choix principal de la V1 est donc de stabiliser d'abord le fonctionnement SQL avec Django ORM avant d'ajouter une technologie supplémentaire.

---

## Pourquoi le NoSQL n'est pas implanté dans la V1

L'ajout d'une base NoSQL dès la V1 aurait augmenté la complexité du projet sans apporter de bénéfice immédiat au fonctionnement actuel du site.

Les données actuellement utilisées dans Frostia Games sont simples et structurées.

Elles concernent principalement :

* les créations ;
* les projets jouables ;
* les statuts ;
* les informations de visibilité ;
* les dates de création et de modification.

Ces données correspondent bien à une structure relationnelle classique.

Le choix retenu est donc de ne pas ajouter NoSQL artificiellement, mais de documenter cette possibilité comme une évolution future si le projet devient plus riche.

---

## Rôle de la base SQL actuelle

La base SQLite est utilisée comme base relationnelle principale.

Elle permet de stocker les données nécessaires au fonctionnement de la V1.

Les données sont manipulées avec Django ORM, ce qui permet :

* de définir les modèles dans le code Python ;
* de générer les migrations ;
* de créer les tables ;
* de gérer les données depuis l'administration Django ;
* d'afficher les informations dans les templates.

Dans la V1, cette solution est suffisante car les données restent prévisibles et structurées.

---

## Limite de l'approche SQL pour les futures évolutions

Si Frostia Games évolue vers une plateforme plus complète, certains contenus pourraient devenir plus difficiles à modéliser uniquement avec des tables relationnelles.

Par exemple, chaque projet de jeu vidéo pourrait avoir une structure différente :

* certains projets pourraient avoir une section gameplay ;
* d'autres pourraient avoir une section univers ;
* certains pourraient avoir un journal de développement détaillé ;
* certains pourraient contenir des prototypes ;
* certains pourraient contenir des médias ;
* certains pourraient avoir des notes de conception très variables.

Dans ce cas, une base relationnelle classique pourrait demander beaucoup de tables ou de champs optionnels.

Le NoSQL pourrait alors devenir utile pour stocker des documents plus souples.

---

## Besoins possibles pour une future base NoSQL

Une base NoSQL pourrait être utile plus tard pour stocker des données moins structurées.

Exemples de contenus concernés :

* fiches détaillées de projets ;
* sections variables selon les jeux ;
* historiques de développement ;
* notes de conception ;
* journaux de mise à jour ;
* blocs de contenu personnalisés ;
* métadonnées de médias ;
* informations évolutives sur les prototypes ;
* brouillons de description ;
* informations narratives ou créatives.

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
  "tags": [
    "jeu vidéo",
    "prototype",
    "recherche technique"
  ],
  "updated_at": "2026-06-24"
}
```

Ce type de document permettrait de stocker une fiche projet complète sans imposer une structure identique à tous les projets.

---

## Différence entre SQL et NoSQL dans Frostia Games

### SQL actuel

La base SQLite sert à stocker les données principales du site.

Elle est adaptée pour :

* les créations ;
* les projets jouables ;
* les statuts ;
* la visibilité ;
* les dates de création ;
* les dates de modification ;
* les données structurées.

Ces données correspondent bien à des tables relationnelles.

---

### NoSQL envisagé

Une future base NoSQL pourrait servir à stocker des contenus plus flexibles.

Elle serait adaptée pour :

* les fiches longues ;
* les blocs de contenu variables ;
* les notes de conception ;
* les médias associés ;
* les historiques de projet ;
* les informations créatives non uniformes.

Le NoSQL ne remplacerait pas forcément la base relationnelle.

Il pourrait être utilisé en complément de SQLite ou PostgreSQL pour certains contenus plus libres.

---

## Exemple de séparation SQL / NoSQL

Dans une version plus avancée, l'organisation pourrait être la suivante :

| Type de donnée             | Solution possible |
| -------------------------- | ----------------- |
| Utilisateurs               | PostgreSQL        |
| Créations principales      | PostgreSQL        |
| Projets jouables           | PostgreSQL        |
| Statuts                    | PostgreSQL        |
| Visibilité                 | PostgreSQL        |
| Fiches longues de projets  | MongoDB           |
| Notes de conception        | MongoDB           |
| Blocs de contenu variables | MongoDB           |
| Métadonnées flexibles      | MongoDB           |

Cette organisation n'est pas nécessaire dans la V1, mais elle pourrait devenir pertinente si le projet évolue vers une plateforme plus complète.

---

## Exemple de composant d'accès NoSQL envisagé

Dans une future version, un composant spécifique pourrait être créé pour accéder aux documents NoSQL.

Exemple théorique :

```python
class ProjectDocumentRepository:
    def __init__(self, collection):
        self.collection = collection

    def find_by_slug(self, slug):
        return self.collection.find_one({"slug": slug})

    def find_visible_projects(self):
        return self.collection.find({"is_visible": True})

    def update_project_sections(self, slug, sections):
        return self.collection.update_one(
            {"slug": slug},
            {"$set": {"sections": sections}}
        )
```

Ce code n'est pas intégré dans la V1.

Il montre seulement comment un futur composant d'accès aux données NoSQL pourrait être organisé.

---

## Exemple d'utilisation future côté Django

Dans une future version, une vue Django pourrait récupérer une fiche projet détaillée depuis une base NoSQL.

Exemple théorique :

```python
def project_detail(request, slug):
    project = project_document_repository.find_by_slug(slug)

    if project is None:
        raise Http404("Projet introuvable")

    return render(request, "pages/project_detail.html", {
        "project": project
    })
```

Ce type de fonctionnement permettrait d'afficher des fiches longues avec des sections variables.

La base SQL pourrait continuer à stocker les informations principales, tandis que la base NoSQL stockerait les contenus détaillés.

---

## Choix retenu pour la V1

Pour cette V1, le choix technique est le suivant :

* SQLite est utilisé pour la base de données principale ;
* Django ORM est utilisé pour manipuler les données ;
* aucune base NoSQL n'est connectée ;
* l'intégration NoSQL est placée dans la roadmap du projet ;
* la priorité est donnée à la stabilité de la V1.

Ce choix permet de garder une version stable, testable et maintenable.

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
* un risque de confusion entre SQL et NoSQL ;
* une dette technique inutile.

Le choix le plus raisonnable est donc de documenter cette possibilité sans l'intégrer trop tôt.

---

## Roadmap NoSQL

Une future version pourrait intégrer MongoDB ou une autre solution NoSQL pour gérer les fiches détaillées des projets.

Étapes possibles :

1. Identifier les contenus réellement variables.
2. Définir une structure de document.
3. Choisir une solution NoSQL adaptée.
4. Connecter Django à cette base.
5. Créer un composant d'accès aux données NoSQL.
6. Tester la récupération des documents.
7. Afficher les fiches détaillées dynamiquement.
8. Sécuriser les accès et les données.
9. Documenter la nouvelle architecture.
10. Vérifier que l'ajout apporte un bénéfice réel au projet.

---

## Risques d'une intégration NoSQL

Une future intégration NoSQL devra être étudiée avec prudence.

Les principaux risques seraient :

* complexifier inutilement l'architecture ;
* multiplier les sources de données ;
* rendre les sauvegardes plus difficiles ;
* devoir sécuriser une deuxième base ;
* augmenter les tests nécessaires ;
* créer une dépendance technique supplémentaire ;
* rendre le projet moins lisible pour une V1.

Avant d'intégrer NoSQL, il faudra vérifier que le besoin est réel.

---

## Critères avant une future intégration

Avant d'ajouter NoSQL, plusieurs questions devront être posées :

* Les données sont-elles vraiment variables ?
* Une base SQL ne suffit-elle plus ?
* Les fiches projets nécessitent-elles des structures très différentes ?
* L'ajout de NoSQL améliore-t-il réellement le projet ?
* La sécurité est-elle maîtrisée ?
* La documentation reste-t-elle claire ?
* Le projet reste-t-il maintenable ?
* L'intégration ne transforme-t-elle pas le projet en architecture trop lourde ?

Si le besoin n'est pas confirmé, l'idée pourra être reportée ou abandonnée.

---

## Positionnement pour le dossier projet

Pour le dossier projet, il est important de présenter cette partie avec précision.

La V1 de Frostia Games ne doit pas être présentée comme un projet utilisant déjà NoSQL.

La formulation correcte est :

```txt
Le projet utilise actuellement une base relationnelle SQLite. Une évolution NoSQL est documentée pour de futurs besoins de contenus plus flexibles, mais elle n'est pas intégrée dans la V1.
```

La formulation à éviter est :

```txt
Le projet utilise SQL et NoSQL.
```

Cette deuxième formulation serait incorrecte pour l'état actuel de la V1.

---

## Limite par rapport à la compétence NoSQL

Cette section permet de montrer une réflexion technique sur le NoSQL, mais elle ne remplace pas un composant NoSQL réellement développé.

Si le dossier projet final exige une preuve concrète de composant d'accès NoSQL, il faudra soit :

* ajouter une petite intégration NoSQL réelle dans une future version ;
* présenter cette compétence à travers un autre projet ;
* demander au formateur si cette documentation préparatoire est suffisante pour le dépôt d'entraînement.

Pour le dépôt d'entraînement du dossier projet, cette section permet surtout d'obtenir un retour du formateur sur la manière de traiter cette compétence.

---

## Conclusion

Le NoSQL n'est pas implanté dans la V1 de Frostia Games, mais son usage est identifié, cadré et documenté.

La V1 privilégie une base SQL simple avec SQLite afin de valider le fonctionnement du backend Django.

Le NoSQL est prévu comme une évolution future possible pour gérer des contenus plus souples et plus détaillés liés aux projets de jeux vidéo.

Ce choix permet de conserver une V1 stable, claire et défendable, tout en préparant une évolution technique plus avancée si le besoin devient réel.
