# Choix techniques et pistes explorées - Frostia Games

## Objectif du document

Ce document présente les choix techniques réalisés pour le projet **Frostia Games**.

L'objectif est d'expliquer pourquoi certaines technologies ont été envisagées au départ, pourquoi elles n'ont pas été retenues pour la V1, et pourquoi le choix final s'est porté sur **Python avec Django**.

Ce document permet aussi de montrer que les décisions techniques n'ont pas été prises au hasard.

Plusieurs pistes ont été explorées, comparées, puis certaines ont été volontairement retenues, reportées, simplifiées ou abandonnées afin de conserver un projet stable, livrable, documenté et déployé.

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
* capacité à terminer une version présentable ;
* capacité à maintenir le projet après la V1.

Le projet devait rester maîtrisable.

L'objectif n'était pas de construire une plateforme trop complexe dès la première version, mais d'obtenir une base claire, fonctionnelle, documentée et évolutive.

---

## Piste initiale : C# et Razor

Au départ, une piste envisagée était de développer le projet avec une technologie liée à **C#**, comme **ASP.NET Core** avec **Razor**.

Cette piste était intéressante car C# est une technologie structurée, rigoureuse et adaptée à des projets applicatifs plus fortement typés.

C# offre plusieurs avantages :

* typage fort ;
* structure rigoureuse ;
* bonne lisibilité ;
* organisation claire du code ;
* bon équilibre entre propreté et puissance ;
* meilleure prévention de certaines erreurs grâce au compilateur ;
* architecture adaptée à des projets plus complexes.

C# reste une technologie intéressante pour de futurs projets, notamment pour sa rigueur, son typage fort et son intérêt dans le développement applicatif ou jeu vidéo.

---

## Pourquoi C# / Razor n'a pas été retenu pour la V1

Même si C# était une piste intéressante, ce choix aurait augmenté le risque de complexité pour cette première version.

Le projet avait besoin d'être :

* rapide à mettre en place ;
* facile à documenter ;
* simple à déployer ;
* stable ;
* terminé dans un délai raisonnable ;
* compatible avec une phase de finalisation courte.

Partir sur C# / Razor aurait pu demander plus de préparation, plus de configuration et plus de temps pour obtenir une V1 réellement présentable.

Le risque principal était de transformer le projet en **usine à gaz**, c'est-à-dire un projet trop ambitieux, trop lourd ou trop difficile à stabiliser pour une première version.

La décision a donc été de ne pas suivre cette piste immédiatement.

C# reste une piste possible pour de futurs projets, mais il n'était pas le choix le plus adapté au périmètre court de la V1 de Frostia Games.

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
* une organisation claire du projet ;
* une gestion des fichiers statiques ;
* une structure adaptée à la documentation.

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
* bonne séparation entre configuration, vues, modèles et templates ;
* possibilité de faire évoluer le projet progressivement.

Ces avantages ont permis de concentrer le travail sur la construction d'une V1 fonctionnelle, plutôt que sur une configuration trop lourde.

Django a également permis de mettre en place rapidement une administration utilisable, sans devoir créer immédiatement une interface privée personnalisée.

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

Le choix de Python n'a donc pas été fait sans garde-fous.

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
* fichier `.env.example` pour documenter la configuration sans exposer les secrets ;
* déploiement Render documenté ;
* tests manuels des pages ;
* vérification de l'administration ;
* vérification du responsive ;
* fichiers Markdown pour suivre les choix, limites et évolutions.

Ces garde-fous permettent d'encadrer le projet malgré la souplesse de Python.

---

## Choix de SQLite pour la V1

Pour la V1, la base de données retenue est **SQLite**.

SQLite est intégrée facilement avec Django et suffit pour un portfolio simple.

Elle permet de stocker les données nécessaires au projet sans ajouter une configuration trop lourde.

SQLite est utilisée pour :

* les créations ;
* les futurs projets jouables ;
* les statuts ;
* les données de visibilité ;
* les dates de création et de modification ;
* les tables internes de Django.

Ce choix est cohérent avec une V1, car le projet ne contient pas encore beaucoup de données ni plusieurs utilisateurs publics.

---

## Pourquoi PostgreSQL n'est pas utilisé dans la V1

PostgreSQL a été envisagé comme évolution future.

C'est une solution plus robuste pour une production durable, mais elle n'était pas indispensable pour cette première version.

L'intégrer dès maintenant aurait demandé :

* une configuration supplémentaire ;
* une base distante ;
* plus de variables d'environnement ;
* des tests de connexion ;
* une documentation supplémentaire ;
* une gestion plus avancée du déploiement.

Pour cette V1, SQLite permet de conserver un projet simple, stable et maîtrisable.

PostgreSQL reste une évolution possible si le projet devient plus avancé.

---

## Choix de Render pour le déploiement

Le projet est déployé en ligne avec **Render**.

Render a été choisi car il permet de déployer une application Django depuis un dépôt GitHub avec une configuration raisonnablement simple.

Le déploiement utilise :

```bash
bash build.sh
```

comme commande de build, puis :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

comme commande de démarrage.

Ce choix permet de montrer que le projet n'est pas seulement fonctionnel en local, mais également accessible en ligne.

URL de production :

```txt
https://frostia-games.onrender.com
```

---

## Choix de Gunicorn

**Gunicorn** est utilisé comme serveur d'application pour lancer Django en production sur Render.

Django possède un serveur de développement avec :

```bash
python manage.py runserver
```

Mais ce serveur n'est pas prévu pour la production.

Gunicorn permet de lancer l'application Django avec le fichier WSGI :

```txt
frostia_config.wsgi:application
```

Ce choix est cohérent avec un déploiement Django en ligne.

---

## Choix de WhiteNoise

**WhiteNoise** est utilisé pour servir les fichiers statiques en production.

Dans un projet Django, les fichiers CSS, JavaScript et images doivent être collectés avec :

```bash
python manage.py collectstatic --noinput
```

WhiteNoise permet ensuite de rendre ces fichiers accessibles correctement en production.

Il est utilisé pour gérer :

* le CSS ;
* le JavaScript ;
* les images ;
* les fichiers statiques collectés.

Ce choix simplifie le déploiement sur Render sans ajouter un serveur spécialisé comme Nginx dans la V1.

---

## Choix de Docker

Docker a été intégré au projet afin de permettre un lancement plus reproductible.

Il permet de tester le projet dans un environnement conteneurisé avec :

```powershell
docker compose up --build
```

Dans la V1, Docker sert surtout à :

* documenter une méthode de lancement alternative ;
* montrer que le projet peut être exécuté dans un environnement isolé ;
* faciliter la reproduction du projet ;
* préparer une architecture plus professionnelle pour la suite.

Docker n'est pas utilisé comme méthode principale de déploiement en production.

Le déploiement principal est réalisé avec Render.

---

## Choix de Git et GitHub

Le projet utilise **Git** pour le versioning et **GitHub** pour l'hébergement du dépôt.

Git permet de conserver un historique du projet, de sauvegarder les étapes importantes et de vérifier l'état du dépôt.

Commandes utilisées :

```powershell
git status
git add .
git commit -m "Message du commit"
git push
```

GitHub permet de connecter le projet à Render pour le déploiement.

Ce choix permet aussi de montrer que le projet est suivi, versionné et sauvegardé proprement.

---

## Choix du fichier `.env.example`

Le projet utilise un fichier `.env.example` pour documenter les variables d'environnement nécessaires.

Ce fichier ne contient pas les vraies valeurs sensibles.

Il sert uniquement d'exemple.

Exemple de variables documentées :

```txt
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Les vraies valeurs sont définies dans Render ou dans l'environnement local.

Ce choix permet de documenter la configuration sans exposer :

* la clé secrète Django ;
* le mot de passe administrateur ;
* les informations sensibles ;
* les identifiants privés.

---

## Pourquoi ce choix est cohérent

Le choix de Django est cohérent avec l'objectif de la V1.

Le but n'était pas de faire le projet le plus complexe possible, mais de construire une première version :

* fonctionnelle ;
* stable ;
* déployée ;
* documentée ;
* compréhensible ;
* évolutive ;
* défendable devant un évaluateur.

Django a permis d'atteindre cet objectif plus rapidement.

C# reste une technologie intéressante pour de futurs projets, mais Django était plus adapté au besoin immédiat du projet Frostia Games.

---

## Pistes explorées

Plusieurs pistes ont été envisagées ou discutées pendant le projet :

* C# / ASP.NET Core / Razor ;
* PostgreSQL ;
* NoSQL / MongoDB ;
* compte jury temporaire ;
* administration personnalisée ;
* upload serveur réel ;
* espace privé complet ;
* graphiques avec Plotly.js ;
* intégration future de projets jouables ;
* système de médias plus avancé ;
* sauvegardes automatiques ;
* tests automatisés complets.

Ces pistes ne sont pas oubliées.

Elles sont reportées, simplifiées ou éventuellement abandonnées lorsqu'elles ne servent pas directement la stabilisation de la V1.

---

## Pourquoi toutes les pistes ne sont pas intégrées immédiatement

Toutes les pistes ne peuvent pas être intégrées dès la première version.

Un bon projet doit aussi savoir dire non, reporter ou abandonner certaines fonctionnalités.

Ajouter trop de choses trop tôt peut créer :

* du scope creep ;
* de la dette technique ;
* des bugs supplémentaires ;
* une documentation trop lourde ;
* un projet instable ;
* une perte de temps ;
* une architecture difficile à maintenir ;
* un risque de transformer le projet en usine à gaz.

La V1 doit rester une base propre, pas une version finale complète.

---

## Position retenue

La position retenue est la suivante :

```txt
Toutes les pistes intéressantes sont identifiées, mais seules les fonctionnalités nécessaires à une V1 stable sont intégrées.
```

Cela permet de garder une vision long terme sans dégrader la qualité de la première version.

Certaines idées resteront dans la roadmap.

D'autres pourront être abandonnées si elles n'apportent pas assez de valeur ou si elles fragilisent la V1.

---

## Tableau récapitulatif des choix

| Élément              | Choix V1            | Raison                                              |
| -------------------- | ------------------- | --------------------------------------------------- |
| Langage principal    | Python              | Rapide à mettre en place pour la V1                 |
| Framework web        | Django              | Structure complète, admin intégrée, ORM             |
| Base de données      | SQLite              | Simple et suffisante pour une V1                    |
| Base future possible | PostgreSQL          | Plus robuste pour une version avancée               |
| NoSQL                | Non intégré         | Besoin encore trop flou pour la V1                  |
| Serveur production   | Gunicorn            | Adapté au déploiement Django                        |
| Fichiers statiques   | WhiteNoise          | Gestion simple des fichiers statiques en production |
| Déploiement          | Render              | Déploiement en ligne depuis GitHub                  |
| Versioning           | Git / GitHub        | Suivi, sauvegarde et connexion à Render             |
| Conteneurisation     | Docker              | Lancement reproductible et documentation technique  |
| Admin                | Admin Django native | Suffisante pour la V1                               |
| Upload serveur       | Non intégré         | Fonction sensible et trop risquée pour la V1        |
| Compte jury          | Non créé            | À faire seulement si demandé                        |
| Graphiques Plotly    | Non intégrés        | Pas indispensable pour stabiliser la V1             |

---

## Conclusion

Le projet Frostia Games a été pensé avec plusieurs pistes techniques possibles.

C# et Razor étaient des options intéressantes, notamment pour leur rigueur et leur structure.

Cependant, pour cette V1, Django a été retenu car il permettait d'obtenir plus rapidement une base fonctionnelle, documentée et déployée.

Python étant plus permissif, des garde-fous ont été ajoutés pour limiter les erreurs et mieux structurer le projet.

Les choix techniques complémentaires renforcent cette logique :

* SQLite pour une base simple ;
* Render pour le déploiement ;
* Gunicorn pour lancer Django en production ;
* WhiteNoise pour gérer les fichiers statiques ;
* Docker pour un lancement reproductible ;
* Git et GitHub pour le versioning ;
* `.env.example` pour documenter la configuration sans exposer les secrets.

Le choix final n'est donc pas un abandon systématique des autres technologies.

C'est une décision de périmètre.

L'objectif était de produire une V1 stable, présentable et évolutive, sans transformer le projet en usine à gaz.

Les pistes non intégrées sont documentées afin de montrer qu'elles ont été réfléchies, mais qu'elles ne devaient pas toutes être ajoutées immédiatement.
