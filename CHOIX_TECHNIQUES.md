# Choix techniques et pistes explorées - Frostia Games

## Objectif du document

Ce document présente les choix techniques réalisés pour le projet **Frostia Games**.

L'objectif est d'expliquer pourquoi certaines technologies ont été envisagées au départ, pourquoi elles n'ont pas été retenues pour la V1, et pourquoi le choix final s'est porté sur **Python avec Django**.

Ce document permet aussi de montrer que les décisions techniques n'ont pas été prises au hasard. Plusieurs pistes ont été explorées, comparées, puis certaines ont été volontairement reportées afin de conserver un projet stable, livrable et documenté.

---

## Principe général

Au début du projet, plusieurs pistes techniques ont été envisagées.

L'objectif n'était pas seulement de choisir une technologie rapidement, mais de réfléchir à ce qui était le plus adapté au périmètre de la V1.

Les critères principaux étaient :

* stabilité du projet ;
* temps de développement raisonnable ;
* lisibilité du code ;
* facilité de documentation ;
* facilité de déploiement ;
* possibilité d'évolution future ;
* limitation du risque de complexité excessive ;
* capacité à terminer une version présentable.

Le projet devait rester maîtrisable. L'objectif n'était pas de construire une plateforme trop complexe dès la première version.

---

## Piste initiale : C# et Razor

Au départ, une piste envisagée était de développer le projet avec une technologie liée à **C#**, comme ASP.NET Core avec Razor.

Cette piste était intéressante car C# est un langage que j'apprécie particulièrement.

C# offre plusieurs avantages :

* un typage fort ;
* une structure rigoureuse ;
* une bonne lisibilité ;
* une organisation claire du code ;
* un bon équilibre entre propreté et puissance ;
* une meilleure prévention de certaines erreurs grâce au compilateur.

C# reste mon langage préféré, notamment parce qu'il impose davantage de rigueur qu'un langage plus permissif.

---

## Pourquoi C# / Razor n'a pas été retenu pour la V1

Même si C# était une piste intéressante, ce choix aurait augmenté le risque de complexité pour cette première version.

Le projet avait besoin d'être :

* rapide à mettre en place ;
* facile à documenter ;
* simple à déployer ;
* stable ;
* terminé dans un délai raisonnable.

Partir sur C# / Razor aurait pu demander plus de préparation, plus de configuration et plus de temps pour obtenir une V1 réellement présentable.

Le risque principal était de transformer le projet en **usine à gaz**, c'est-à-dire un projet trop ambitieux, trop lourd ou trop difficile à stabiliser pour une première version.

La décision a donc été de ne pas suivre cette piste immédiatement.

C# reste une piste importante pour de futurs projets, mais il n'était pas le choix le plus adapté pour cette V1.

---

## Choix final : Python et Django

Le choix final s'est porté sur **Python avec Django**.

Django a été choisi car il permet de construire rapidement une application web structurée avec :

* un système de routes ;
* des vues ;
* des templates ;
* des modèles ;
* une base de données ;
* des migrations ;
* une administration intégrée ;
* une organisation claire du projet.

Django permet d'obtenir rapidement une base fonctionnelle, tout en conservant une architecture compréhensible.

Pour une V1 de portfolio avec backend, administration et déploiement, Django était un choix adapté.

---

## Avantages de Django pour cette V1

Django a été retenu pour plusieurs raisons :

* mise en place rapide ;
* architecture déjà organisée ;
* administration intégrée ;
* base SQLite facile à utiliser ;
* système de templates simple ;
* documentation abondante ;
* déploiement possible sur Render ;
* bonne séparation entre configuration, vues, modèles et templates.

Ces avantages ont permis de concentrer le travail sur la construction d'une V1 fonctionnelle, plutôt que sur une configuration trop lourde.

---

## Limite de Python

Python reste un langage très permissif.

Cela signifie qu'il laisse plus de liberté au développeur, mais qu'il peut aussi laisser passer certaines erreurs plus facilement qu'un langage fortement typé comme C#.

Cette permissivité peut créer des risques :

* erreurs détectées tardivement ;
* variables mal nommées ;
* types moins explicites ;
* dépendance plus forte aux tests et aux vérifications ;
* fausses alertes possibles dans l'éditeur ;
* besoin de discipline supplémentaire.

Ce point a été pris en compte dans le projet.

---

## Garde-fous ajoutés

Pour compenser la permissivité de Python, plusieurs garde-fous ont été mis en place.

L'objectif était de réduire les erreurs et de rendre le projet plus stable.

Garde-fous utilisés :

* documentation régulière ;
* journal de bord ;
* changelog ;
* vérification avec `python manage.py check` ;
* environnement virtuel `.venv` ;
* structure Django claire ;
* séparation des templates, fichiers statiques et vues ;
* utilisation de migrations Django ;
* administration Django contrôlée ;
* variables d'environnement pour les données sensibles ;
* déploiement Render documenté ;
* tests manuels des pages ;
* vérification de l'administration ;
* vérification du responsive ;
* fichiers Markdown pour suivre les choix et limites.

Ces garde-fous permettent d'encadrer le projet malgré la souplesse de Python.

---

## Pourquoi ce choix est cohérent

Le choix de Django est cohérent avec l'objectif de la V1.

Le but n'était pas de faire le projet le plus complexe possible, mais de construire une première version :

* fonctionnelle ;
* stable ;
* déployée ;
* documentée ;
* compréhensible ;
* évolutive.

Django a permis d'atteindre cet objectif plus rapidement.

C# reste une technologie importante pour de futurs projets, mais Django était plus adapté au besoin immédiat du projet Frostia Games.

---

## Pistes explorées

Plusieurs pistes ont été envisagées ou discutées pendant le projet :

* C# / ASP.NET Core / Razor ;
* PostgreSQL ;
* compte jury temporaire ;
* administration personnalisée ;
* upload serveur réel ;
* espace privé complet ;
* graphiques avec Plotly.js ;
* intégration future de projets jouables ;
* système de médias plus avancé ;
* sauvegardes automatiques.

Ces pistes ne sont pas oubliées.

Elles sont simplement reportées, car elles ne sont pas indispensables à la V1.

---

## Pourquoi toutes les pistes ne sont pas intégrées immédiatement

Toutes les pistes ne peuvent pas être intégrées dès la première version.

Un bon projet doit aussi savoir dire non ou reporter certaines fonctionnalités.

Ajouter trop de choses trop tôt peut créer :

* du scope creep ;
* de la dette technique ;
* des bugs supplémentaires ;
* une documentation trop lourde ;
* un projet instable ;
* une perte de temps ;
* une architecture difficile à maintenir.

La V1 doit rester une base propre, pas une version finale complète.

---

## Position retenue

La position retenue est la suivante :

```txt
Toutes les pistes intéressantes sont identifiées, mais seules les fonctionnalités nécessaires à une V1 stable sont intégrées.
```

Cela permet de garder une vision long terme sans dégrader la qualité de la première version.

---

## Conclusion

Le projet Frostia Games a été pensé avec plusieurs pistes techniques possibles.

C# et Razor étaient des options intéressantes, notamment pour leur rigueur et leur structure. Cependant, pour cette V1, Django a été retenu car il permettait d'obtenir plus rapidement une base fonctionnelle, documentée et déployée.

Python étant plus permissif, des garde-fous ont été ajoutés pour limiter les erreurs et mieux structurer le projet.

Le choix final n'est donc pas un abandon des autres technologies, mais une décision de périmètre.

L'objectif était de produire une V1 stable, présentable et évolutive, sans transformer le projet en usine à gaz.
