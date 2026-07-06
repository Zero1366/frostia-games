# Présentation du projet 2 - Frostia Games

## Objectif du document

Ce document présente le projet **Frostia Games** comme proposition de second projet.

L'objectif est d'expliquer clairement la nature du projet, son périmètre, les choix techniques réalisés, les fonctionnalités présentes dans la V1, les preuves de fonctionnement disponibles, ainsi que les limites volontairement assumées.

Ce document sert de base pour présenter le projet de manière claire, structurée et défendable.

---

## Liens du projet

* Site en ligne : https://frostia-games.onrender.com
* Interface d'administration Django : https://frostia-games.onrender.com/admin/
* Dépôt GitHub : https://github.com/Zero1366/frostia-games
* Preuves de fonctionnement : `PREUVES-FONCTIONNEMENT.md`
* Dossier des preuves : `Preuve De Fonctionnement/`

L'accès à l'administration Django n'est pas public.

Un accès d'évaluation en lecture seule peut être fourni au jury ou à l'examinateur si nécessaire.

Les identifiants ne sont pas indiqués dans ce document et doivent être transmis séparément.

---

## Présentation générale

**Frostia Games** est un portfolio développé avec Django.

Le projet a pour objectif de présenter des créations vidéoludiques actuelles et futures dans une interface web simple, moderne, documentée et évolutive.

Il ne s'agit pas d'un simple site statique.

Le projet repose sur une structure Django avec :

* une architecture backend ;
* une base de données SQLite ;
* une administration Django ;
* des modèles de données ;
* un affichage dynamique ;
* un menu mobile JavaScript ;
* des extraits SQL natifs documentés ;
* une démonstration NoSQL légère avec JSON / TinyDB ;
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
* l'utilisation d'une base de données relationnelle ;
* l'utilisation de l'administration Django ;
* la mise en place d'un accès d'évaluation en lecture seule ;
* la documentation d'extraits SQL natifs ;
* la démonstration d'une logique NoSQL légère ;
* la documentation technique ;
* le déploiement en ligne avec Render ;
* le suivi de version avec GitHub ;
* la création de preuves de fonctionnement ;
* la réflexion sur les limites et les évolutions.

Ce projet permet donc de montrer une autre facette du développement web, plus orientée backend Django, documentation, base de données et mise en production.

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
* accès d'évaluation en lecture seule ;
* base SQLite ;
* affichage dynamique de certaines données ;
* extraits SQL natifs documentés ;
* structure NoSQL légère avec documents JSON ;
* script Python de lecture des notes NoSQL ;
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

| Page | Rôle |
| ---- | ---- |
| Accueil | Présenter le portfolio Frostia Games |
| Mes créations | Présenter les créations et projets en cours |
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

## Base de données SQL

La V1 utilise SQLite.

La base de données permet de gérer certains contenus du projet, notamment les créations et les projets jouables à venir.

SQLite est suffisant pour cette première version, car le projet reste un portfolio simple.

Les modèles principaux sont :

* `Creation` ;
* `PlayableProject`.

Les extraits SQL natifs sont documentés dans :

```text
Docs/sql/
```

Fichiers concernés :

```text
Docs/sql/create_tables_creations.sql
Docs/sql/create_tables_playable.sql
Docs/sql/exemples_insert.sql
Docs/sql/sql-natif.md
```

Ces fichiers permettent de montrer :

* les tables SQL générées à partir des modèles Django ;
* des exemples `CREATE TABLE` ;
* des exemples `INSERT INTO` ;
* le lien entre Django ORM et SQL natif.

Une migration vers PostgreSQL pourra être envisagée plus tard si le projet évolue vers une version plus avancée.

---

## Partie NoSQL légère

Une partie NoSQL légère a été ajoutée afin de démontrer une logique documentaire.

Elle ne remplace pas SQLite.

Elle repose sur une structure JSON compatible avec une logique TinyDB.

Fichiers concernés :

```text
Docs/nosql/
```

Exemples :

```text
Docs/nosql/project_notes.json
Docs/nosql/read_project_notes.py
Docs/nosql/nosql.md
Docs/nosql/structure-nosql.md
Docs/nosql/tinydb-integration.md
```

Cette partie permet de montrer :

* une structure documentaire JSON ;
* des notes de progression ;
* une lecture Python des documents ;
* une séparation entre données structurées SQL et données plus souples NoSQL ;
* une évolution possible vers une solution NoSQL plus avancée si le besoin devient réel.

La solution actuelle reste volontairement légère et non critique.

---

## Administration Django

L'administration Django est fonctionnelle.

Lien :

```text
https://frostia-games.onrender.com/admin/
```

Elle permet de gérer les données du projet depuis l'interface `/admin/`.

L'accès administrateur complet reste privé.

Aucun identifiant ni mot de passe n'est publié dans le dépôt GitHub ou dans la documentation publique.

---

## Accès d'évaluation en lecture seule

Un accès d'évaluation en lecture seule peut être fourni au jury ou à l'examinateur si nécessaire.

Cet accès permet de consulter l'administration Django sans disposer des droits d'ajout, de modification ou de suppression.

Configuration prévue :

| Élément | Valeur |
| ------- | ------ |
| Groupe | `Evaluation lecture seule` |
| Utilisateur | `evaluation_temp` |
| Droits | Consultation uniquement |
| Superutilisateur | Non |
| Ajout | Non |
| Modification | Non |
| Suppression | Non |

Les droits sont limités aux permissions de type `view`.

Les identifiants doivent être transmis séparément si l'accès est demandé.

Cette approche permet de fournir un accès de vérification sans ouvrir l'administration complète du projet.

---

## Déploiement

Le projet est déployé sur Render.

URL de production :

```text
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

Le projet est hébergé avec une offre gratuite Render.

Cette offre peut entraîner une mise en veille du service après une période d'inactivité.

Ce comportement est lié à l'hébergement et ne constitue pas une erreur du projet.

---

## Dépôt GitHub

Le code source du projet est disponible sur GitHub.

Lien du dépôt :

```text
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

```text
PREUVES-FONCTIONNEMENT.md
```

Dossier de captures :

```text
Preuve De Fonctionnement/
```

Les preuves sont classées par catégorie :

```text
Preuve De Fonctionnement/
├── Docker/
├── Figma/
├── Github/
├── Render/
├── SiteWeb_FrostiaGame/
│   ├── Admin/
│   ├── Desktop/
│   └── Mobile/
└── Sql/
```

Des preuves complémentaires peuvent aussi être ajoutées :

```text
Preuve De Fonctionnement/NoSQL/
Preuve De Fonctionnement/Tests/
Preuve De Fonctionnement/Code/
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
* l'affichage mobile responsive ;
* la structure SQL ;
* les extraits SQL natifs ;
* la partie NoSQL légère ;
* les tests de vérification.

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

Documentation complémentaire :

```text
Docs/backend/
Docs/conception/
Docs/frontend/
Docs/nosql/
Docs/sql/
```

Cette documentation montre les choix réalisés, les problèmes rencontrés, les solutions appliquées et les évolutions possibles.

---

## Conception

La partie conception a été renforcée afin de mieux montrer la réflexion menée avant et pendant le développement.

Documents concernés :

```text
Docs/conception/mcd.md
Docs/conception/cas-utilisation.md
Docs/conception/diagramme-sequence.md
```

Ces documents permettent de présenter :

* le modèle conceptuel de données ;
* les cas d'utilisation principaux ;
* un diagramme de séquence ;
* le lien entre utilisateur, navigateur, vues Django, base SQL et rendu final.

---

## JavaScript dynamique

Le menu mobile JavaScript est documenté dans :

```text
Docs/frontend/javascript-menu-mobile.md
```

Cette documentation permet de montrer :

* le rôle du JavaScript dans l'interface ;
* le fonctionnement du menu responsive ;
* l'interaction entre bouton, navigation et classes CSS ;
* l'intérêt du JavaScript dans le rendu mobile.

---

## Choix techniques

Les choix techniques principaux sont :

| Élément | Choix |
| ------- | ----- |
| Framework | Django |
| Langage | Python |
| Base de données principale | SQLite |
| ORM | Django ORM |
| NoSQL léger | JSON structuré compatible TinyDB |
| Interface | Templates Django, HTML, CSS, JavaScript |
| Déploiement | Render |
| Serveur production | Gunicorn |
| Fichiers statiques | WhiteNoise |
| Versioning | Git et GitHub |
| Documentation | Markdown |
| Conteneurisation | Docker |

Ces choix permettent de garder un projet simple, stable et compréhensible.

---

## Limites assumées

Certaines fonctionnalités ne sont pas intégrées dans la V1.

Éléments reportés :

* PostgreSQL ;
* interface admin personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* graphiques Plotly.js ;
* statistiques avancées ;
* espace privé complet ;
* tests automatisés complets ;
* MongoDB en production.

L'accès d'évaluation en lecture seule n'est pas une plateforme utilisateur complète.

Il sert uniquement à permettre une consultation encadrée de l'administration Django si nécessaire.

Ces éléments ne sont pas oubliés.

Ils sont volontairement reportés afin de conserver une V1 stable et maîtrisable.

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
* utilisation d'une base de données SQL ;
* documentation d'extraits SQL natifs ;
* démonstration NoSQL légère ;
* configuration de l'administration Django ;
* sécurisation d'un accès d'évaluation en lecture seule ;
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

| Partie | État |
| ------ | ---- |
| Projet Django | Fonctionnel |
| Pages publiques | Fonctionnelles |
| Backend | Fonctionnel pour V1 |
| Base SQLite | Fonctionnelle |
| SQL natif | Documenté |
| NoSQL léger | Documenté et démontré par JSON / script Python |
| Admin Django | Fonctionnel |
| Accès évaluation lecture seule | Préparé / disponible si demandé |
| Déploiement Render | Fonctionnel |
| Dépôt GitHub | Disponible |
| Documentation | Avancée |
| Preuves de fonctionnement | Réalisées et rangées |
| Responsive | Fonctionnel mais améliorable |
| Sécurité minimale | Correcte pour V1 |

---

## Vérifications réalisées

Plusieurs vérifications ont été effectuées ou sont prévues avant la fermeture de la V1 :

* lancement local du projet ;
* vérification des pages publiques ;
* vérification de l'administration Django ;
* vérification de l'accès lecture seule ;
* vérification Docker ;
* vérification Render ;
* vérification du site en ligne ;
* vérification des variables d'environnement masquées ;
* vérification du dépôt GitHub ;
* vérification de la partie SQL ;
* vérification de la partie NoSQL ;
* vérification du statut Git final.

Commande importante :

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues
```

---

## Prochaines étapes avant présentation

Avant de présenter officiellement ce projet comme projet 2, il reste principalement à faire :

* relire les textes ;
* vérifier les captures dans le dossier final ;
* vérifier que les liens sont accessibles ;
* préparer la présentation orale ;
* expliquer clairement le périmètre de la V1 ;
* insister sur les choix volontairement limités ;
* transmettre séparément les identifiants d'évaluation si un accès est demandé.

Les fonctionnalités principales, les preuves, le déploiement et le dépôt GitHub sont déjà en place.

---

## Positionnement du projet

Frostia Games doit être présenté comme une V1 maîtrisée.

Il ne faut pas le présenter comme une plateforme finale complète.

Formulation correcte :

```text
Frostia Games est une première version fonctionnelle d'un portfolio Django destiné à présenter mes projets vidéoludiques. Le projet est déployé en ligne, versionné sur GitHub, documenté et conçu pour évoluer progressivement.
```

Formulation à éviter :

```text
Frostia Games est une plateforme complète de gestion de projets de jeux vidéo.
```

La deuxième formulation serait trop ambitieuse par rapport à l'état réel de la V1.

---

## Conclusion

Frostia Games peut être proposé comme second projet car il possède une base technique réelle, un backend Django, une administration, une base de données, une démonstration SQL / NoSQL, un déploiement en ligne, un dépôt GitHub et une documentation complète.

Le projet reste volontairement limité, mais il est stable, cohérent et défendable.

Il montre une capacité à créer un projet web complet dans son périmètre, à le documenter, à le déployer, à le versionner et à préparer ses futures évolutions sans élargir trop vite le périmètre.

L'accès d'évaluation en lecture seule permet aussi de consulter l'administration Django sans exposer de droits de modification.

