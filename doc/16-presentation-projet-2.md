# Présentation du projet 2 - Frostia Games

## Objectif du document

Ce document présente le projet **Frostia Games** comme proposition de second projet.

L'objectif est d'expliquer clairement la nature du projet, son périmètre, les choix techniques réalisés, les fonctionnalités présentes dans la V1, les limites assumées et les évolutions possibles.

Ce document sert de base pour présenter le projet de manière claire, structurée et défendable.

---

## Présentation générale

**Frostia Games** est un portfolio développé avec **Django**.

Le projet a pour objectif de présenter des créations vidéoludiques actuelles et futures dans une interface web simple, moderne, documentée et évolutive.

Il ne s'agit pas d'un simple site statique. Le projet repose sur une vraie structure Django comprenant :

* une architecture backend ;
* une base de données SQLite ;
* une administration Django ;
* des modèles de données ;
* des templates HTML ;
* des fichiers statiques ;
* un déploiement en ligne ;
* une documentation technique complète.

---

## Positionnement du projet

Frostia Games doit être présenté comme une **V1 fonctionnelle et maîtrisée**.

Le projet ne doit pas être présenté comme une plateforme finale complète.

Formulation correcte :

```txt
Frostia Games est une première version fonctionnelle d'un portfolio Django destiné à présenter mes projets vidéoludiques. Le projet est déployé en ligne, documenté et conçu pour évoluer progressivement.
```

Formulation à éviter :

```txt
Frostia Games est une plateforme complète de gestion de projets de jeux vidéo.
```

La deuxième formulation serait trop ambitieuse par rapport au périmètre réel de la V1.

---

## Pourquoi ce projet peut être proposé comme projet 2

Frostia Games peut être proposé comme second projet car il présente un travail différent et complémentaire du premier dossier projet.

Le projet met en avant :

* la création d'un projet Django ;
* l'organisation d'une architecture web ;
* la gestion de pages publiques ;
* la mise en place d'un backend simple ;
* l'utilisation d'une base de données ;
* l'utilisation de l'administration Django ;
* l'affichage dynamique de contenus ;
* la documentation technique ;
* le déploiement en ligne avec Render ;
* la réflexion sur les limites et les évolutions.

Ce projet montre une autre facette du développement web, plus orientée backend Django, structuration, documentation et mise en production.

---

## Objectif de la V1

L'objectif de la V1 n'est pas de créer une plateforme complète.

L'objectif est de produire une première version :

* fonctionnelle ;
* stable ;
* documentée ;
* déployée ;
* consultable en ligne ;
* évolutive ;
* défendable dans un dossier projet.

Cette V1 sert de fondation pour présenter des projets vidéoludiques et préparer de futures améliorations.

---

## Fonctionnalités réalisées

La V1 contient les fonctionnalités suivantes :

* page d'accueil ;
* page de présentation des créations ;
* page des projets jouables à venir ;
* navigation principale ;
* menu responsive ;
* interface publique ;
* modèles Django ;
* administration Django ;
* base SQLite ;
* affichage dynamique de certaines données ;
* déploiement Render ;
* documentation de déploiement ;
* documentation d'architecture ;
* documentation de tests ;
* documentation des limites et évolutions.

---

## Pages principales

Le site contient trois pages publiques principales.

| Page                     | Rôle                                                            |
| ------------------------ | --------------------------------------------------------------- |
| Accueil                  | Présenter le portfolio Frostia Games                            |
| Mes créations            | Présenter les créations et projets en cours                     |
| Projets jouables à venir | Présenter les futurs projets jouables ou démonstrations prévues |

Ces pages permettent de présenter le projet de manière claire sans surcharger la V1.

---

## Backend Django

Le projet utilise Django comme framework principal.

Django permet de structurer le projet autour :

* des routes ;
* des vues ;
* des templates ;
* des modèles ;
* des migrations ;
* de l'administration ;
* de la base de données ;
* des fichiers statiques.

Le backend reste volontairement simple pour cette V1, mais il montre déjà une organisation réelle et exploitable.

---

## Base de données

La V1 utilise SQLite.

La base de données permet de gérer certains contenus du projet, notamment les créations et les projets jouables à venir.

SQLite est suffisant pour cette première version, car le projet reste un portfolio simple.

Une migration vers PostgreSQL pourra être envisagée plus tard si le projet évolue vers une version plus avancée.

---

## Administration Django

L'administration Django est fonctionnelle.

Elle permet de gérer les données du projet depuis l'interface `/admin/`.

L'accès administrateur reste privé.

Aucun identifiant ni mot de passe n'est publié dans le dépôt GitHub ou dans la documentation publique.

Un compte temporaire pour le jury pourra être créé plus tard uniquement si le projet est validé comme second projet ou si un accès direct est demandé.

---

## Déploiement

Le projet est déployé sur Render.

URL de production :

```txt
https://frostia-games.onrender.com
```

La configuration Render utilise :

```bash
bash build.sh
```

comme commande de build, puis :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

comme commande de démarrage.

Le déploiement permet de montrer que le projet fonctionne en dehors de l'environnement local.

---

## Documentation produite

Le projet dispose d'une documentation technique organisée.

Documents principaux :

* index de documentation ;
* journal de bord ;
* modernisation de l'interface ;
* modélisation backend ;
* Docker et lancement ;
* sécurité backend ;
* manuel utilisateur ;
* base de données ;
* changelog ;
* déploiement Render ;
* bilan V1 ;
* installation locale ;
* architecture ;
* tests et vérifications ;
* captures et preuves ;
* limites et évolutions ;
* présentation du projet 2 ;
* pistes explorées et non retenues ;
* plan de finalisation V1.

Cette documentation montre les choix réalisés, les problèmes rencontrés, les solutions appliquées et les évolutions possibles.

---

## Choix techniques

Les choix techniques principaux sont :

| Élément            | Choix                                   |
| ------------------ | --------------------------------------- |
| Framework          | Django                                  |
| Langage            | Python                                  |
| Base de données    | SQLite                                  |
| Interface          | Templates Django, HTML, CSS, JavaScript |
| Déploiement        | Render                                  |
| Serveur production | Gunicorn                                |
| Fichiers statiques | WhiteNoise                              |
| Versioning         | Git et GitHub                           |
| Documentation      | Markdown                                |

Ces choix permettent de garder un projet simple, stable et compréhensible.

---

## Compétences mises en avant

Le projet permet de montrer plusieurs compétences :

* création d'un projet Django ;
* organisation d'une structure web ;
* gestion des routes ;
* création de vues ;
* utilisation de templates ;
* création de modèles ;
* utilisation de migrations ;
* gestion de l'administration Django ;
* utilisation d'une base SQLite ;
* configuration des fichiers statiques ;
* déploiement avec Render ;
* utilisation de variables d'environnement ;
* documentation technique ;
* cadrage du périmètre ;
* gestion des limites et évolutions.

---

## Limites assumées

Certaines fonctionnalités ne sont pas intégrées dans la V1.

Éléments reportés :

* PostgreSQL ;
* compte jury temporaire ;
* interface admin personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* graphiques Plotly.js ;
* statistiques avancées ;
* espace privé complet ;
* tests automatisés complets.

Ces éléments ne sont pas oubliés. Ils sont volontairement reportés afin de conserver une V1 stable et maîtrisable.

---

## Pourquoi ne pas avoir tout ajouté maintenant

Ajouter trop de fonctionnalités dans cette V1 aurait augmenté les risques :

* perte de stabilité ;
* complexité excessive ;
* dette technique ;
* documentation difficile à maintenir ;
* projet trop long à terminer ;
* fonctionnalités commencées mais non finalisées ;
* risque de transformer le projet en usine à gaz.

Le choix a donc été de privilégier une V1 propre, testable, documentée et déployée.

---

## État actuel

État actuel de la V1 :

| Partie             | État                         |
| ------------------ | ---------------------------- |
| Projet Django      | Fonctionnel                  |
| Pages publiques    | Fonctionnelles               |
| Backend            | Fonctionnel pour V1          |
| Base SQLite        | Fonctionnelle                |
| Admin Django       | Fonctionnel                  |
| Déploiement Render | Fonctionnel                  |
| Documentation      | Avancée                      |
| Responsive         | Fonctionnel mais améliorable |
| Sécurité minimale  | Correcte pour V1             |

---

## Prochaines étapes avant présentation

Avant de présenter officiellement ce projet comme projet 2, il reste à finaliser :

* les captures d'écran ;
* la vérification finale du README à la racine ;
* les maquettes Figma si nécessaires ;
* la relecture des textes ;
* la vérification mobile ;
* le dossier projet final ;
* le commit final propre.

---

## Valeur du projet

Frostia Games montre une démarche complète :

```txt
conception
développement
tests
documentation
déploiement
bilan
évolutions prévues
```

Le projet montre aussi une capacité à limiter le périmètre pour éviter d'ajouter trop de fonctionnalités en même temps.

Cette démarche est importante, car un projet réussi n'est pas seulement un projet avec beaucoup d'idées. C'est aussi un projet stable, compréhensible, terminé et présentable.

---

## Conclusion

Frostia Games peut être proposé comme second projet car il possède une base technique réelle, un backend Django, une administration, une base de données, un déploiement en ligne et une documentation complète.

Le projet reste volontairement limité, mais il est stable, cohérent et défendable.

Il montre une capacité à créer un projet web complet dans son périmètre, à le documenter, à le déployer et à préparer ses futures évolutions sans élargir trop vite le périmètre.
