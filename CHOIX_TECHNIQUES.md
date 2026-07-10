# Choix techniques et pistes explorées — Frostia Games

## Objectif du document

Ce document présente les choix techniques réalisés pour le projet **Frostia Games**.

L'objectif est d'expliquer :

- les technologies envisagées ;
- les technologies retenues ;
- les technologies reportées ;
- les raisons des choix effectués ;
- les limites assumées pour la V1 ;
- les évolutions possibles.

Ce document montre que les décisions techniques n'ont pas été prises au hasard.

Plusieurs pistes ont été explorées, comparées, puis certaines ont été retenues, reportées, simplifiées ou abandonnées afin de conserver un projet stable, livrable, documenté et déployé.

---

# 1. Principe général

Au début du projet, plusieurs pistes techniques ont été envisagées.

L'objectif n'était pas seulement de choisir une technologie rapidement, mais de réfléchir à ce qui était le plus adapté au périmètre de la V1.

Les critères principaux étaient :

- stabilité du projet ;
- temps de développement raisonnable ;
- lisibilité du code ;
- facilité de documentation ;
- facilité de déploiement ;
- possibilité d'évolution future ;
- limitation du risque de complexité excessive ;
- capacité à terminer une version présentable ;
- capacité à maintenir le projet après la V1.

Le projet devait rester maîtrisable.

L'objectif n'était pas de construire une plateforme trop complexe dès la première version, mais d'obtenir une base claire, fonctionnelle, documentée et évolutive.

---

# 2. Piste initiale — C# et Razor

Au départ, une piste envisagée était de développer le projet avec une technologie liée à **C#**, comme **ASP.NET Core** avec **Razor**.

Cette piste était intéressante car C# est une technologie structurée, rigoureuse et adaptée à des projets applicatifs plus fortement typés.

C# offre plusieurs avantages :

- typage fort ;
- structure rigoureuse ;
- bonne lisibilité ;
- organisation claire du code ;
- prévention de certaines erreurs grâce au compilateur ;
- architecture adaptée à des projets plus complexes.

C# reste une technologie intéressante pour de futurs projets, notamment pour sa rigueur, son typage fort et son lien avec des projets applicatifs ou vidéoludiques.

---

# 3. Pourquoi C# / Razor n'a pas été retenu pour la V1

Même si C# était une piste intéressante, ce choix aurait augmenté le risque de complexité pour cette première version.

Le projet avait besoin d'être :

- rapide à mettre en place ;
- facile à documenter ;
- simple à déployer ;
- stable ;
- terminé dans un délai raisonnable ;
- compatible avec une phase de finalisation courte.

Partir sur C# / Razor aurait pu demander plus de préparation, plus de configuration et plus de temps pour obtenir une V1 réellement présentable.

Le risque principal était de transformer le projet en **usine à gaz**, c'est-à-dire un projet trop ambitieux, trop lourd ou trop difficile à stabiliser pour une première version.

La décision a donc été de ne pas suivre cette piste immédiatement.

C# reste une piste possible pour de futurs projets, mais il n'était pas le choix le plus adapté au périmètre court de la V1 de Frostia Games.

---

# 4. Choix final — Python et Django

Le choix final s'est porté sur **Python avec Django**.

Django a été choisi car il permet de construire rapidement une application web structurée avec :

- un système de routes ;
- des vues ;
- des templates ;
- des modèles ;
- une base de données ;
- des migrations ;
- une administration intégrée ;
- une organisation claire du projet ;
- une gestion des fichiers statiques ;
- une structure adaptée à la documentation.

Django permet d'obtenir rapidement une base fonctionnelle, tout en conservant une architecture compréhensible.

Pour une V1 de portfolio avec backend, administration et déploiement, Django était un choix adapté.

---

# 5. Avantages de Django pour cette V1

Django a été retenu pour plusieurs raisons :

- mise en place rapide ;
- architecture déjà organisée ;
- administration intégrée ;
- base SQLite facile à utiliser ;
- système de templates simple ;
- documentation abondante ;
- déploiement possible sur Render ;
- bonne séparation entre configuration, vues, modèles et templates ;
- possibilité de faire évoluer le projet progressivement.

Ces avantages ont permis de concentrer le travail sur la construction d'une V1 fonctionnelle, plutôt que sur une configuration trop lourde.

Django a également permis de mettre en place rapidement une administration utilisable, sans devoir créer immédiatement une interface privée personnalisée.

---

# 6. Limite de Python

Python reste un langage permissif.

Cela signifie qu'il laisse plus de liberté au développeur, mais qu'il peut aussi laisser passer certaines erreurs plus facilement qu'un langage fortement typé comme C#.

Cette permissivité peut créer des risques :

- erreurs détectées tardivement ;
- variables mal nommées ;
- types moins explicites ;
- dépendance plus forte aux tests et aux vérifications ;
- fausses alertes possibles dans l'éditeur ;
- besoin de discipline supplémentaire.

Ce point a été pris en compte dans le projet.

Le choix de Python n'a donc pas été fait sans garde-fous.

---

# 7. Garde-fous ajoutés

Pour compenser la permissivité de Python, plusieurs garde-fous ont été mis en place.

Garde-fous utilisés :

- documentation régulière ;
- journal de bord ;
- changelog ;
- vérification avec `python manage.py check` ;
- environnement virtuel `.venv` ;
- structure Django claire ;
- séparation des templates, fichiers statiques et vues ;
- utilisation de migrations Django ;
- administration Django contrôlée ;
- compte d’évaluation limité en lecture seule ;
- variables d'environnement pour les données sensibles ;
- fichier `.env.example` pour documenter la configuration sans exposer les secrets ;
- déploiement Render documenté ;
- tests manuels des pages ;
- vérification de l'administration ;
- vérification du responsive ;
- fichiers Markdown pour suivre les choix, limites et évolutions.

Ces garde-fous permettent d'encadrer le projet malgré la souplesse de Python.

---

# 8. Choix de SQLite pour la V1

Pour la V1, la base de données retenue est **SQLite**.

SQLite est intégrée facilement avec Django et suffit pour un portfolio simple.

Elle permet de stocker les données nécessaires au projet sans ajouter une configuration trop lourde.

SQLite est utilisée pour :

- les créations ;
- les futurs projets jouables ;
- les statuts ;
- les données de visibilité ;
- les dates de création et de modification ;
- les tables internes de Django.

Ce choix est cohérent avec une V1, car le projet ne contient pas encore beaucoup de données ni plusieurs utilisateurs publics.

---

# 9. Limite de SQLite sur Render

SQLite reste adaptée à la V1, mais elle présente une limite importante sur un hébergement gratuit comme Render.

Sur Render, la base SQLite du service ne doit pas être considérée comme une persistance durable avancée.

Après un redémarrage ou un redéploiement, les données créées manuellement peuvent disparaître ou ne plus être disponibles.

Pour stabiliser la démonstration, une commande Django personnalisée a été ajoutée :

```bash
python manage.py setup_render_data
```

Cette commande recrée automatiquement :

- la création principale Frostia Games ;
- le projet jouable de démonstration ;
- le groupe `Evaluation lecture seule` ;
- le compte d’évaluation ;
- les permissions de lecture seule.

Cette solution est cohérente pour une V1 de démonstration.

Pour une production durable, une base externe comme PostgreSQL serait plus adaptée.

---

# 10. Pourquoi PostgreSQL n'est pas utilisé dans la V1

PostgreSQL a été envisagé comme évolution future.

C'est une solution plus robuste pour une production durable, mais elle n'était pas indispensable pour cette première version.

L'intégrer dès maintenant aurait demandé :

- une configuration supplémentaire ;
- une base distante ;
- plus de variables d'environnement ;
- des tests de connexion ;
- une documentation supplémentaire ;
- une gestion plus avancée du déploiement.

Pour cette V1, SQLite permet de conserver un projet simple, stable et maîtrisable.

PostgreSQL reste une évolution possible si le projet devient plus avancé.

---

# 11. Choix de TinyDB pour la démonstration NoSQL

Une expérimentation NoSQL légère a été ajoutée avec **TinyDB**.

TinyDB permet de stocker des notes de progression dans un fichier JSON.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

TinyDB a été retenu car :

- il est léger ;
- il ne demande pas de serveur externe ;
- il permet de montrer une logique documentaire NoSQL ;
- il reste simple à expliquer ;
- il ne complexifie pas fortement l'architecture.

TinyDB ne remplace pas SQLite.

SQLite reste la base principale du projet.

TinyDB sert uniquement de démonstration NoSQL contrôlée dans le périmètre de la V1.

---

# 12. Pourquoi MongoDB n'est pas utilisé dans la V1

MongoDB a été envisagé comme piste NoSQL plus avancée.

Cependant, l'intégrer dans la V1 aurait ajouté :

- une base externe supplémentaire ;
- une configuration plus lourde ;
- plus de variables d'environnement ;
- une documentation plus importante ;
- des risques de complexité inutile.

Le besoin NoSQL de la V1 est limité.

TinyDB suffit pour démontrer une logique documentaire simple.

MongoDB reste une évolution possible si le projet évolue vers des contenus très variables, des fiches projets plus riches ou des journaux de développement plus complexes.

---

# 13. Choix de Render pour le déploiement

Le projet est déployé en ligne avec **Render**.

Render a été choisi car il permet de déployer une application Django depuis un dépôt GitHub avec une configuration raisonnablement simple.

URL de production :

```text
https://frostia-games.onrender.com
```

Render permet de montrer que le projet n'est pas seulement fonctionnel en local, mais également accessible en ligne.

---

# 14. Configuration Render

Le déploiement utilise la commande de build suivante :

```bash
bash build.sh
```

Le démarrage utilise la commande suivante :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande permet :

1. d'appliquer les migrations Django ;
2. de recréer les données minimales nécessaires à la démonstration ;
3. de recréer le compte d’évaluation en lecture seule ;
4. de lancer l'application Django avec Gunicorn.

Cette configuration correspond à l'état actuel du projet.

---

# 15. Choix de Gunicorn

**Gunicorn** est utilisé comme serveur d'application pour lancer Django en production sur Render.

Django possède un serveur de développement avec :

```bash
python manage.py runserver
```

Mais ce serveur n'est pas prévu pour la production.

Gunicorn permet de lancer l'application Django avec le fichier WSGI :

```text
frostia_config.wsgi:application
```

Ce choix est cohérent avec un déploiement Django en ligne.

---

# 16. Choix de WhiteNoise

**WhiteNoise** est utilisé pour servir les fichiers statiques en production.

Dans un projet Django, les fichiers CSS, JavaScript et images doivent être collectés avec :

```bash
python manage.py collectstatic --noinput
```

WhiteNoise permet ensuite de rendre ces fichiers accessibles correctement en production.

Il est utilisé pour gérer :

- le CSS ;
- le JavaScript ;
- les images ;
- les fichiers statiques collectés.

Ce choix simplifie le déploiement sur Render sans ajouter un serveur spécialisé comme Nginx dans la V1.

---

# 17. Choix de Docker

Docker a été intégré au projet afin de permettre un lancement plus reproductible.

Il permet de tester le projet dans un environnement conteneurisé avec :

```powershell
docker compose up --build
```

Dans la V1, Docker sert surtout à :

- documenter une méthode de lancement alternative ;
- montrer que le projet peut être exécuté dans un environnement isolé ;
- faciliter la reproduction du projet ;
- préparer une architecture plus professionnelle pour la suite.

Docker n'est pas utilisé comme méthode principale de déploiement en production.

Le déploiement principal est réalisé avec Render.

---

# 18. Choix de Git et GitHub

Le projet utilise **Git** pour le versioning et **GitHub** pour l'hébergement du dépôt.

Git permet de conserver un historique du projet, de sauvegarder les étapes importantes et de vérifier l'état du dépôt.

Commandes utilisées :

```powershell
git status
git add .
git commit -m "Message du commit"
git push origin main
```

GitHub permet de connecter le projet à Render pour le déploiement.

Ce choix permet aussi de montrer que le projet est suivi, versionné et sauvegardé proprement.

Le dépôt peut rester privé selon le contexte de remise.

---

# 19. Choix du fichier `.env.example`

Le projet utilise un fichier `.env.example` pour documenter les variables d'environnement nécessaires.

Ce fichier ne contient pas les vraies valeurs sensibles.

Il sert uniquement d'exemple.

Variables documentées :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
EVALUATION_USER_PASSWORD=change-me
```

Les vraies valeurs sont définies dans Render ou dans l'environnement local.

Ce choix permet de documenter la configuration sans exposer :

- la clé secrète Django ;
- le mot de passe administrateur ;
- le mot de passe du compte d’évaluation ;
- les informations sensibles ;
- les identifiants privés.

---

# 20. Choix du compte d’évaluation en lecture seule

Un compte d’évaluation limité a été ajouté pour permettre une consultation encadrée de l’administration Django.

Ce compte est :

- staff ;
- non superutilisateur ;
- limité aux permissions de lecture ;
- limité aux créations et projets jouables.

Il ne permet pas :

- d’ajouter des contenus ;
- de modifier des contenus ;
- de supprimer des contenus ;
- de modifier les utilisateurs ;
- de modifier les groupes ;
- de modifier les permissions.

Ce choix est plus sécurisé que de fournir un compte administrateur complet.

Le mot de passe du compte d’évaluation n’est pas écrit dans le code source.

Il est fourni par la variable Render :

```text
EVALUATION_USER_PASSWORD
```

---

# 21. Pourquoi ce choix global est cohérent

Le choix de Django est cohérent avec l'objectif de la V1.

Le but n'était pas de faire le projet le plus complexe possible, mais de construire une première version :

- fonctionnelle ;
- stable ;
- déployée ;
- documentée ;
- compréhensible ;
- évolutive ;
- défendable devant un évaluateur.

Django a permis d'atteindre cet objectif rapidement.

C# reste une technologie intéressante pour de futurs projets, mais Django était plus adapté au besoin immédiat du projet Frostia Games.

---

# 22. Pistes explorées

Plusieurs pistes ont été envisagées ou discutées pendant le projet :

- C# / ASP.NET Core / Razor ;
- PostgreSQL ;
- MongoDB ;
- administration personnalisée ;
- upload serveur réel ;
- espace privé complet ;
- graphiques avec Plotly.js ;
- intégration future de projets jouables ;
- système de médias plus avancé ;
- sauvegardes automatiques ;
- tests automatisés complets.

Certaines pistes ont finalement été ajoutées de manière limitée :

- TinyDB ;
- SQL natif documentaire ;
- compte d’évaluation en lecture seule ;
- initialisation automatique Render avec `setup_render_data`.

Les autres restent reportées ou pourront être abandonnées si elles n'apportent pas assez de valeur.

---

# 23. Pourquoi toutes les pistes ne sont pas intégrées immédiatement

Toutes les pistes ne peuvent pas être intégrées dès la première version.

Un bon projet doit aussi savoir dire non, reporter ou abandonner certaines fonctionnalités.

Ajouter trop de choses trop tôt peut créer :

- du scope creep ;
- de la dette technique ;
- des bugs supplémentaires ;
- une documentation trop lourde ;
- un projet instable ;
- une perte de temps ;
- une architecture difficile à maintenir ;
- un risque de transformer le projet en usine à gaz.

La V1 doit rester une base propre, pas une version finale complète.

---

# 24. Position retenue

La position retenue est la suivante :

```text
Toutes les pistes intéressantes sont identifiées, mais seules les fonctionnalités nécessaires à une V1 stable sont intégrées.
```

Cela permet de garder une vision long terme sans dégrader la qualité de la première version.

Certaines idées resteront dans la roadmap.

D'autres pourront être abandonnées si elles n'apportent pas assez de valeur ou si elles fragilisent la V1.

---

# 25. Tableau récapitulatif des choix

| Élément | Choix V1 | Raison |
| ------- | -------- | ------ |
| Langage principal | Python | Rapide à mettre en place pour la V1 |
| Framework web | Django | Structure complète, admin intégrée, ORM |
| Base principale | SQLite | Simple et suffisante pour une V1 |
| Base future possible | PostgreSQL | Plus robuste pour une version avancée |
| NoSQL léger | TinyDB | Démonstration documentaire simple |
| NoSQL avancé | MongoDB reporté | Trop lourd pour la V1 |
| Serveur production | Gunicorn | Adapté au déploiement Django |
| Fichiers statiques | WhiteNoise | Gestion simple des fichiers statiques en production |
| Déploiement | Render | Déploiement en ligne depuis GitHub |
| Initialisation Render | `setup_render_data` | Recrée les données de démonstration |
| Versioning | Git / GitHub | Suivi, sauvegarde et connexion à Render |
| Conteneurisation | Docker | Lancement reproductible et documentation technique |
| Admin | Admin Django native | Suffisante pour la V1 |
| Compte évaluation | Lecture seule | Consultation sans droits de modification |
| Upload serveur | Reporté | Fonction sensible et trop risquée pour la V1 |
| Graphiques Plotly | Reportés | Pas indispensable pour stabiliser la V1 |
| Tests automatisés complets | Reportés | Priorité donnée à la stabilisation et aux preuves |

---

# 26. Conclusion

Le projet Frostia Games a été pensé avec plusieurs pistes techniques possibles.

C# et Razor étaient des options intéressantes, notamment pour leur rigueur et leur structure.

Cependant, pour cette V1, Django a été retenu car il permettait d'obtenir plus rapidement une base fonctionnelle, documentée et déployée.

Python étant plus permissif, des garde-fous ont été ajoutés pour limiter les erreurs et mieux structurer le projet.

Les choix techniques complémentaires renforcent cette logique :

- SQLite pour une base simple ;
- TinyDB pour une démonstration NoSQL légère ;
- Render pour le déploiement ;
- `setup_render_data` pour recréer les données nécessaires en ligne ;
- Gunicorn pour lancer Django en production ;
- WhiteNoise pour gérer les fichiers statiques ;
- Docker pour un lancement reproductible ;
- Git et GitHub pour le versioning ;
- `.env.example` pour documenter la configuration sans exposer les secrets ;
- compte d’évaluation en lecture seule pour éviter de partager un compte administrateur complet.

Le choix final n'est donc pas un abandon systématique des autres technologies.

C'est une décision de périmètre.

L'objectif était de produire une V1 stable, présentable et évolutive, sans transformer le projet en usine à gaz.

Les pistes non intégrées sont documentées afin de montrer qu'elles ont été réfléchies, mais qu'elles ne devaient pas toutes être ajoutées immédiatement.
