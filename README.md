# Présentation du projet 2 - Frostia Games

## Objectif du document

Ce document présente le projet **Frostia Games** comme proposition de second projet.

L'objectif est d'expliquer clairement la nature du projet, son périmètre, les choix techniques réalisés, les fonctionnalités présentes dans la V1, les preuves de fonctionnement disponibles, ainsi que les limites volontairement assumées.

Ce document sert de base pour présenter le projet de manière claire, structurée et défendable.

---

## Liens du projet

* Site en ligne : https://frostia-games.onrender.com
* Dépôt GitHub : https://github.com/Zero1366/frostia-games
* Preuves de fonctionnement : `PREUVES-FONCTIONNEMENT.md`

---

## Présentation générale

**Frostia Games** est un portfolio développé avec Django.

Le projet a pour objectif de présenter des créations vidéoludiques actuelles et futures dans une interface web simple, moderne, documentée et évolutive.

Il ne s'agit pas d'un simple site statique. Le projet repose sur une structure Django avec :

* une architecture backend ;
* une base de données SQLite ;
* une administration Django ;
* des modèles de données ;
* un affichage dynamique ;
* un déploiement en ligne ;
* une documentation technique complète ;
* des preuves de fonctionnement organisées.

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
* la documentation technique ;
* le déploiement en ligne avec Render ;
* le suivi de version avec GitHub ;
* la création de preuves de fonctionnement ;
* la réflexion sur les limites et les évolutions.

Ce projet permet donc de montrer une autre facette du développement web, plus orientée backend Django, documentation et mise en production.

---

## Objectif de la V1

L'objectif de la V1 n'est pas de créer une plateforme complète.

L'objectif est de produire une première version :

* fonctionnelle ;
* stable ;
* documentée ;
* déployée ;
* consultable en ligne ;
* versionnée sur GitHub ;
* accompagnée de preuves de fonctionnement ;
* évolutive.

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
* dépôt GitHub public ;
* documentation de déploiement ;
* documentation d'architecture ;
* documentation de tests ;
* documentation des limites et évolutions ;
* preuves de fonctionnement organisées par catégorie.

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
* de la base de données.

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

Le projet est hébergé avec une offre gratuite Render. Cette offre peut entraîner une mise en veille du service après une période d'inactivité. Ce comportement est lié à l'hébergement et ne constitue pas une erreur du projet.

---

## Dépôt GitHub

Le code source du projet est disponible sur GitHub.

Lien du dépôt :

```txt
https://github.com/Zero1366/frostia-games
```

GitHub est utilisé pour :

* sauvegarder le projet ;
* suivre l'historique des modifications ;
* centraliser le code source ;
* conserver les fichiers de documentation ;
* conserver les preuves de fonctionnement ;
* permettre la consultation du projet.

Le dépôt contient notamment :

* le code Django ;
* les templates ;
* les fichiers statiques ;
* la configuration Docker ;
* la configuration Render ;
* les fichiers de documentation ;
* les captures de preuves de fonctionnement.

---

## Preuves de fonctionnement

Le projet contient un dossier de preuves de fonctionnement.

Document principal :

```txt
PREUVES-FONCTIONNEMENT.md
```

Dossier de captures :

```txt
Preuve De Fonctionnement/
```

Les preuves sont classées par catégorie :

```txt
Preuve De Fonctionnement/
├── Docker/
├── Figma/
├── Github/
├── Render/
└── SiteWeb_FrostiaGame/
    ├── Admin/
    ├── Desktop/
    └── Mobile/
```

Ces preuves montrent :

* le fonctionnement Docker ;
* les maquettes Figma ;
* le dépôt GitHub ;
* le déploiement Render ;
* les variables d'environnement masquées ;
* les logs Render ;
* le site en ligne ;
* l'administration Django ;
* l'affichage desktop ;
* l'affichage mobile responsive.

Les captures ne doivent pas afficher de mot de passe, de clé secrète ou de valeur sensible.

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
* preuves de fonctionnement.

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
| Conteneurisation   | Docker                                  |

Ces choix permettent de garder un projet simple, stable et compréhensible.

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

## Valeur du projet

Frostia Games montre plusieurs compétences importantes :

* création d'un projet Django ;
* structuration d'une application web ;
* gestion des templates ;
* utilisation de modèles Django ;
* utilisation d'une base de données ;
* configuration de l'administration Django ;
* déploiement en ligne ;
* gestion des variables d'environnement ;
* utilisation de Git et GitHub ;
* organisation des preuves de fonctionnement ;
* documentation technique ;
* cadrage du périmètre ;
* réflexion sur les évolutions futures.

Le projet montre donc une démarche complète : conception, développement, test, déploiement, versioning et documentation.

---

## État actuel

État actuel de la V1 :

| Partie                    | État                         |
| ------------------------- | ---------------------------- |
| Projet Django             | Fonctionnel                  |
| Pages publiques           | Fonctionnelles               |
| Backend                   | Fonctionnel pour V1          |
| Base SQLite               | Fonctionnelle                |
| Admin Django              | Fonctionnel                  |
| Déploiement Render        | Fonctionnel                  |
| Dépôt GitHub              | Disponible                   |
| Documentation             | Avancée                      |
| Preuves de fonctionnement | Réalisées et rangées         |
| Responsive                | Fonctionnel mais améliorable |
| Sécurité minimale         | Correcte pour V1             |

---

## Vérifications réalisées

Plusieurs vérifications ont été effectuées avant la fermeture de la V1 :

* lancement local du projet ;
* vérification des pages publiques ;
* vérification de l'administration Django ;
* vérification Docker ;
* vérification Render ;
* vérification du site en ligne ;
* vérification des variables d'environnement masquées ;
* vérification du dépôt GitHub ;
* vérification du statut Git final.

Le statut Git final indique que le projet est bien synchronisé avec le dépôt distant et qu'aucune modification locale n'est oubliée.

---

## Prochaines étapes avant présentation

Avant de présenter officiellement ce projet comme projet 2, il reste principalement à faire :

* relire les textes ;
* vérifier les captures dans le dossier final ;
* vérifier que les liens sont accessibles ;
* préparer la présentation orale ;
* expliquer clairement le périmètre de la V1 ;
* insister sur les choix volontairement limités.

Les fonctionnalités principales, les preuves, le déploiement et le dépôt GitHub sont déjà en place.

---

## Positionnement du projet

Frostia Games doit être présenté comme une V1 maîtrisée.

Il ne faut pas le présenter comme une plateforme finale complète.

Formulation correcte :

```txt
Frostia Games est une première version fonctionnelle d'un portfolio Django destiné à présenter mes projets vidéoludiques. Le projet est déployé en ligne, versionné sur GitHub, documenté et conçu pour évoluer progressivement.
```

Formulation à éviter :

```txt
Frostia Games est une plateforme complète de gestion de projets de jeux vidéo.
```

La deuxième formulation serait trop ambitieuse par rapport à l'état réel de la V1.

---

## Conclusion

Frostia Games peut être proposé comme second projet car il possède une base technique réelle, un backend Django, une administration, une base de données, un déploiement en ligne, un dépôt GitHub et une documentation complète.

Le projet reste volontairement limité, mais il est stable, cohérent et défendable.

Il montre une capacité à créer un projet web complet dans son périmètre, à le documenter, à le déployer, à le versionner et à préparer ses futures évolutions sans élargir trop vite le périmètre.
