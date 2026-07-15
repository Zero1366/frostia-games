# Changelog — Frostia Games

## Objectif du document

Ce document regroupe les changements importants réalisés pendant le développement de **Frostia Games**.

Il permet de conserver une trace claire :

- des étapes réalisées ;
- des fichiers modifiés ;
- des fonctionnalités ajoutées ;
- des vérifications effectuées ;
- des choix techniques importants ;
- des éléments volontairement reportés ;
- du déploiement en ligne ;
- des ajouts réalisés après le renforcement du dossier projet ;
- des preuves à préparer pour le dossier final.

Ce changelog ne remplace pas le journal de bord.

Le journal de bord raconte la progression du projet.  
Le changelog liste les changements importants de manière plus synthétique.

---

# 1. Création du projet Django

## Résumé

Mise en place du projet Django servant de base au site Frostia Games.

## Fichiers concernés

```text
manage.py
frostia_config/settings.py
frostia_config/urls.py
frostia_config/wsgi.py
frostia_config/asgi.py
```

## Modifications réalisées

- création du projet Django ;
- configuration de base ;
- mise en place de SQLite ;
- configuration des applications Django de base ;
- vérification du lancement local.

## Validation

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues
```

## Statut

Validé.

---

# 2. Création des applications internes

## Résumé

Création des applications Django internes du projet.

## Applications créées

```text
core
creations
playable
```

## Rôle des applications

| Application | Rôle |
| ----------- | ---- |
| `core` | Pages principales, vues publiques et logique générale |
| `creations` | Modèle des créations du portfolio |
| `playable` | Modèle des projets jouables à venir |

## Statut

Validé.

---

# 3. Création des pages principales

## Résumé

Création des trois pages principales du portfolio.

## Pages créées

- Accueil ;
- Mes créations ;
- Projets jouables.

## Fichiers concernés

```text
templates/partials/base.html
templates/pages/home.html
templates/pages/creation.html
templates/pages/projet_jouable.html
core/views.py
core/urls.py
```

## Validation

Pages testées :

```text
/
 /mes-creations/
 /projets-jouables/
```

## Statut

Validé.

---

# 4. Interface visuelle et responsive

## Résumé

Mise en place de l’interface utilisateur du site.

## Fichiers concernés

```text
static/css/main.css
static/js/menu.js
templates/partials/base.html
templates/pages/home.html
templates/pages/creation.html
templates/pages/projet_jouable.html
doc/01-modernisation-interface.md
```

## Modifications réalisées

- création du thème visuel ;
- ajout de la sidebar ;
- création du responsive mobile ;
- création des cartes de contenu ;
- ajout du menu mobile JavaScript ;
- amélioration progressive de la lisibilité des pages ;
- documentation de la modernisation de l’interface.

## Statut

Validé.

---

# 5. Modèle `Creation`

## Résumé

Ajout du modèle Django dédié aux créations du portfolio.

## Fichiers concernés

```text
creations/models.py
creations/admin.py
creations/apps.py
creations/migrations/
frostia_config/settings.py
```

## Modifications réalisées

- création du modèle `Creation` ;
- ajout des champs du modèle ;
- ajout du champ de visibilité ;
- enregistrement dans l’administration Django ;
- création et application des migrations.

## Validation

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

## Statut

Validé.

---

# 6. Modèle `PlayableProject`

## Résumé

Ajout du modèle Django dédié aux futurs projets jouables.

## Fichiers concernés

```text
playable/models.py
playable/admin.py
playable/apps.py
playable/migrations/
frostia_config/settings.py
```

## Modifications réalisées

- création du modèle `PlayableProject` ;
- ajout des champs du modèle ;
- ajout du champ de visibilité ;
- enregistrement dans l’administration Django ;
- création et application des migrations.

## Statut

Validé.

---

# 7. Connexion des vues à SQLite

## Résumé

Connexion des pages publiques aux modèles Django afin d’afficher les données enregistrées en base SQLite.

## Fichiers concernés

```text
core/views.py
templates/pages/creation.html
templates/pages/projet_jouable.html
```

## Modifications réalisées

- import des modèles `Creation` et `PlayableProject` ;
- récupération des données visibles avec `is_visible=True` ;
- tri des résultats ;
- envoi des données aux templates ;
- affichage dynamique côté site public.

## Validation

Pages testées :

```text
/mes-creations/
/projets-jouables/
```

## Statut

Validé.

---

# 8. Administration Django

## Résumé

Configuration de l’administration Django pour gérer les contenus dynamiques du site.

## Fichiers concernés

```text
creations/admin.py
playable/admin.py
```

## Modifications réalisées

- ajout des modèles dans l’administration ;
- ajout des colonnes visibles ;
- ajout des filtres ;
- ajout de la recherche ;
- ajout de la génération automatique du slug ;
- ajout des dates en lecture seule.

## Statut

Validé.

---

# 9. Interface préparatoire des projets jouables

## Résumé

Préparation de la page **Projets jouables** sans activer de vrai upload serveur.

## Fichiers concernés

```text
templates/pages/projet_jouable.html
static/css/main.css
static/js/menu.js
core/views.py
playable/models.py
```

## Modifications réalisées

- ajout d’une zone de lecteur préparatoire ;
- ajout d’un bouton de lecture fictif ;
- ajout d’une sélection locale de fichier ;
- affichage du nom du fichier sélectionné ;
- message indiquant que l’upload serveur n’est pas implanté ;
- affichage des projets jouables enregistrés en base.

## Limite

Aucun fichier n’est envoyé au serveur.

## Statut

Validé.

---

# 10. Docker

## Résumé

Ajout d’une configuration Docker simple pour tester le projet dans un environnement reproductible.

## Fichiers concernés

```text
Dockerfile
docker-compose.yml
.dockerignore
requirements.txt
doc/04-docker-et-lancement.md
```

## Commande de lancement

```powershell
docker compose up --build
```

## Rôle de Docker dans la V1

Docker sert au test local et à la reproductibilité.

Il n’est pas utilisé comme méthode principale de production.

Le déploiement principal est réalisé avec Render.

## Statut

Validé.

---

# 11. SQL documentaire

## Résumé

Ajout d’une documentation SQL pour présenter la structure de la base.

## Fichiers concernés

```text
doc/sql/schema.sql
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

## Modifications réalisées

- ajout d’exemples `CREATE TABLE` ;
- ajout d’exemples `INSERT INTO` ;
- documentation du lien entre Django ORM, migrations et SQL ;
- distinction entre SQL documentaire et base réelle Django.

## Important

Les tables réelles sont gérées par les migrations Django.

Les fichiers SQL servent de preuve et de documentation.

## Statut

Validé.

---

# 12. Réflexion NoSQL initiale

## Résumé

Ajout d’une première réflexion sur le NoSQL dans les évolutions possibles du projet.

## Fichier concerné

```text
doc/sql/nosql.md
```

## Évolution

Cette réflexion a ensuite été complétée par une intégration réelle et limitée avec TinyDB.

Le NoSQL n’est donc plus seulement théorique dans la V1.

## Statut

Validé, puis complété par TinyDB.

---

# 13. TinyDB

## Résumé

Ajout de TinyDB pour démontrer une logique NoSQL légère.

## Fichiers concernés

```text
requirements.txt
core/services/nosql_notes.py
scripts/__init__.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/nosql.md
docs/nosql/structure-nosql.md
docs/nosql/tinydb-integration.md
```

## Modifications réalisées

- ajout de TinyDB dans les dépendances ;
- création d’un service Python NoSQL ;
- création d’une base JSON TinyDB ;
- création d’un script de démonstration ;
- documentation de l’intégration NoSQL.

## Commande de test

```powershell
python -m scripts.demo_tinydb_notes
```

## Limite

TinyDB ne remplace pas SQLite.

Il sert uniquement de démonstration NoSQL légère.

## Statut

Validé.

---

# 14. Affichage des notes TinyDB sur l’accueil

## Résumé

Connexion des notes TinyDB à la page d’accueil.

## Fichiers concernés

```text
core/views.py
templates/pages/home.html
core/services/nosql_notes.py
data/nosql/project_notes_db.json
```

## Chaîne technique

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

## Validation

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
```

## Statut

Validé.

---

# 15. Documentation complémentaire `docs/`

## Résumé

Création d’un dossier complémentaire de renforcement documentaire.

## Structure

```text
docs/
├── backend/
├── conception/
├── frontend/
├── nosql/
└── sql/

Preuve De Fonctionnement/
└── captures et preuves visuelles du projet
```

## Documents ajoutés

```text
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
docs/frontend/javascript-menu-mobile.md
docs/nosql/nosql.md
docs/nosql/structure-nosql.md
docs/nosql/tinydb-integration.md
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

## Statut

Validé.

---

# 16. JavaScript du menu mobile

## Résumé

Documentation du JavaScript dynamique utilisé pour le menu mobile.

## Fichiers concernés

```text
static/js/menu.js
templates/partials/base.html
docs/frontend/javascript-menu-mobile.md
```

## Modifications réalisées

- documentation du rôle de `menu.js` ;
- explication de `querySelector` ;
- explication de `addEventListener` ;
- explication de `classList.toggle` ;
- explication de `aria-expanded` ;
- préparation des preuves JavaScript.

## Statut

Validé.

---

# 17. Compte d’évaluation en lecture seule

## Résumé

Ajout d’un compte limité pour permettre une consultation de l’administration Django sans donner les droits administrateur complets.

## Éléments concernés

```text
Groupe : Evaluation lecture seule
Utilisateur : evaluation_temp
Permissions : view uniquement
```

## Droits accordés

- consultation des créations ;
- consultation des projets jouables.

## Droits non accordés

- ajout ;
- modification ;
- suppression ;
- gestion des utilisateurs ;
- gestion des groupes ;
- gestion des permissions ;
- accès aux secrets.

## Sécurité

Les identifiants réels ne doivent pas être affichés dans la documentation publique ou dans les captures.

Le mot de passe est géré par variable d’environnement Render.

## Statut

Validé.

---

# 18. Variables d’environnement

## Résumé

Mise en place et documentation des variables d’environnement nécessaires au projet.

## Fichiers concernés

```text
.env.example
frostia_config/settings.py
doc/05-securite-backend.md
doc/09-deploiement-render.md
README.md
```

## Variables principales

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
EVALUATION_USER_PASSWORD
```

## Statut

Validé.

---

# 19. Déploiement Render initial

## Résumé

Mise en ligne de la V1 sur Render.

## URL de production

```text
https://frostia-games.onrender.com
```

## Fichiers concernés

```text
requirements.txt
build.sh
frostia_config/settings.py
frostia_config/wsgi.py
.env.example
doc/09-deploiement-render.md
```

## Build Command

```bash
bash build.sh
```

## Statut

Validé.

---

# 20. Correction du démarrage Render avec `setup_render_data`

## Résumé

Après redéploiement, une difficulté a été identifiée : les données de démonstration et l’accès d’évaluation pouvaient être absents de la base SQLite en ligne.

Pour stabiliser la démonstration Render, une commande Django personnalisée a été ajoutée.

## Fichier concerné

```text
core/management/commands/setup_render_data.py
```

## Rôle de la commande

La commande recrée automatiquement :

- la création principale Frostia Games ;
- le projet jouable de démonstration ;
- le groupe `Evaluation lecture seule` ;
- le compte `evaluation_temp` ;
- les droits de lecture seule.

## Start Command actuel Render

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

## Validation attendue dans les logs Render

```text
Données initiales créées.
Accès d'évaluation configuré.
Utilisateur : evaluation_temp
Droits : lecture seule
Staff : oui
Superutilisateur : non
```

## Statut

Validé.

---

# 21. `build.sh`

## Résumé

Vérification du script utilisé par Render pendant le build.

## Contenu attendu

```bash
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || true
```

## Rôle

- installer les dépendances ;
- collecter les fichiers statiques ;
- appliquer les migrations ;
- créer le superutilisateur si les variables Render sont présentes.

## Important

La création des données de démonstration et du compte d’évaluation est gérée par le Start Command avec `setup_render_data`.

## Statut

Validé.

---

# 22. Mise à jour de la documentation Render

## Résumé

Mise à jour du document de déploiement Render pour correspondre à l’état réel.

## Fichier concerné

```text
doc/09-deploiement-render.md
```

## Modifications réalisées

- correction du Start Command ;
- ajout de `setup_render_data` ;
- ajout de `EVALUATION_USER_PASSWORD` ;
- explication de la limite SQLite sur Render gratuit ;
- ajout des logs de validation ;
- consignes de captures sans secrets.

## Statut

Validé.

---

# 23. Centralisation et mise à jour des preuves

## Résumé

Centralisation des captures et preuves visuelles dans un emplacement unique afin de faciliter leur consultation et leur réutilisation dans le dossier projet et les annexes.

## Éléments concernés

```text
PREUVES-FONCTIONNEMENT.md
doc/14-Capture-et-Preuve.md
Preuve De Fonctionnement/
```

## Organisation retenue

Le dossier `Preuve De Fonctionnement/` devient l’emplacement principal des captures du projet.

Il regroupe notamment les preuves liées :

- à la conception ;
- aux maquettes ;
- au site public ;
- au responsive ;
- à l’administration ;
- au JavaScript ;
- au SQL et au NoSQL ;
- à la sécurité ;
- aux tests ;
- à GitHub ;
- à Docker ;
- à Render.

Les dossiers `doc/` et `docs/` restent consacrés à la documentation écrite, aux documents de conception et aux scripts techniques.

## Présence possible de doublons

Un grand nombre d’images a été ajouté afin de conserver toutes les preuves utiles.

Certains fichiers peuvent donc sembler proches ou apparaître en plusieurs exemplaires. Ces doublons sont conservés lorsqu’ils montrent un format d’écran, une étape de vérification ou un environnement différent, par exemple le fonctionnement local, Docker ou Render.

Le dossier principal utilise uniquement les captures les plus lisibles. Le répertoire complet sert de banque de preuves pour le dossier projet, les annexes et le futur dossier professionnel.

## Règle de sécurité

Aucune capture ne doit afficher :

- mot de passe ;
- clé secrète ;
- vraie valeur de variable d’environnement ;
- token ;
- information sensible inutile.

## Statut

Validé.

---

# 24. Mise à jour de la sécurité backend

## Résumé

Mise à jour de la documentation sécurité pour intégrer l’état actuel.

## Fichier concerné

```text
doc/05-securite-backend.md
```

## Modifications réalisées

- ajout du compte d’évaluation en lecture seule ;
- ajout de `EVALUATION_USER_PASSWORD` ;
- ajout de `setup_render_data` ;
- ajout de la sécurité liée à TinyDB ;
- ajout de la distinction SQL documentaire / ORM Django ;
- ajout des règles de sécurité pour les captures ;
- mise à jour du Start Command Render.

## Statut

Validé.

---

# 25. Mise à jour du README

## Résumé

Correction du README racine afin qu’il serve de vraie page d’entrée du dépôt.

## Fichier concerné

```text
README.md
```

## Modifications réalisées

- présentation du projet ;
- technologies utilisées ;
- installation locale ;
- lancement Docker ;
- administration Django ;
- accès d’évaluation ;
- TinyDB ;
- SQL ;
- déploiement Render ;
- variables d’environnement ;
- limites de la V1.

## Statut

Validé.

---

# 26. Mise à jour de `CHOIX_TECHNIQUES.md`

## Résumé

Correction du fichier de choix techniques pour correspondre à l’état actuel.

## Fichier concerné

```text
CHOIX_TECHNIQUES.md
```

## Modifications réalisées

- correction de l’état du NoSQL ;
- ajout de TinyDB ;
- ajout du compte d’évaluation ;
- ajout de `setup_render_data` ;
- correction du Start Command Render ;
- ajout de `EVALUATION_USER_PASSWORD` ;
- mise à jour du tableau récapitulatif.

## Statut

Validé.

---

# 27. Mise à jour de l’index documentaire

## Résumé

Correction de l’index documentaire pour correspondre à la structure réelle du projet.

## Fichier concerné

```text
doc/00-index-documentation.md
```

## Modifications réalisées

- correction des noms de fichiers ;
- correction de l’organisation `Preuve De Fonctionnement/` ;
- ajout de `setup_render_data` ;
- ajout de `EVALUATION_USER_PASSWORD` ;
- clarification du rôle de `doc/` et `docs/` ;
- suppression des anciennes incohérences.

## Statut

Validé.

---

# 28. Mise à jour du bilan V1

## Résumé

Mise à jour du bilan V1 pour intégrer les corrections finales.

## Fichier concerné

```text
doc/10-bilan-v1-frostia-games.md
```

## Modifications réalisées

- ajout de l’initialisation Render automatique ;
- ajout de l’accès d’évaluation réellement fonctionnel ;
- ajout de `Preuve De Fonctionnement/` ;
- clarification des limites de SQLite sur Render gratuit ;
- mise à jour des éléments terminés.

## Statut

Validé.

---

# 29. Mise à jour des limites et évolutions

## Résumé

Mise à jour du document des limites pour correspondre à l’état réel.

## Fichier concerné

```text
doc/15-limites-et-évolutions.md
```

## Modifications réalisées

- ajout de `setup_render_data` ;
- correction de l’état de TinyDB ;
- correction de l’état du compte d’évaluation ;
- correction de l’organisation des preuves ;
- clarification des limites de SQLite sur Render.

## Statut

Validé.

---

# 30. Mise à jour du plan de finalisation

## Résumé

Mise à jour du plan de finalisation de la V1.

## Fichier concerné

```text
doc/18-plan-finalisation-v1.md
```

## Modifications réalisées

- correction de l’organisation des preuves ;
- ajout de `setup_render_data` ;
- correction du Start Command Render ;
- ajout de la vérification du compte d’évaluation ;
- ajout de la vérification des logs Render.

## Statut

Validé.

---

# 31. Vérifications techniques finales

## Commandes à lancer

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

## Résultats attendus

```text
System check identified no issues
```

```text
Preuve NoSQL TinyDB — Frostia Games
```

```text
nothing to commit, working tree clean
```

## Statut

À vérifier après remplacement final des fichiers.

---

# 32. État actuel de la V1

La V1 contient maintenant :

- pages principales fonctionnelles ;
- backend Django fonctionnel ;
- base SQLite ;
- modèles Django ;
- administration Django ;
- compte d’évaluation en lecture seule ;
- données dynamiques ;
- interface préparatoire de projet jouable ;
- menu mobile JavaScript ;
- Docker ;
- déploiement Render ;
- `setup_render_data` ;
- documentation SQL ;
- SQL natif complémentaire ;
- TinyDB ;
- affichage des notes TinyDB sur l’accueil ;
- documentation NoSQL ;
- documentation de sécurité ;
- manuel utilisateur ;
- changelog ;
- journal de bord ;
- documentation de modernisation ;
- documentation d’architecture ;
- documentation de tests ;
- documentation de déploiement ;
- README racine ;
- fichier de choix techniques ;
- fichier `.env.example` ;
- preuves organisées dans `Preuve De Fonctionnement/`.

## Statut général

V1 fonctionnelle, documentée, déployée et renforcée.

---

# 33. Éléments volontairement reportés

Les éléments suivants sont reportés à une version future :

- PostgreSQL ;
- administration personnalisée ;
- upload serveur réel ;
- jeu jouable dans le navigateur ;
- lecteur vidéo réel ;
- fiches projet détaillées ;
- API REST ;
- comptes utilisateurs publics ;
- rôles publics avancés ;
- base NoSQL avancée comme MongoDB ;
- graphiques Plotly.js ;
- tests automatisés complets ;
- système de sauvegarde automatique ;
- mini-jeu intégré ;
- système de score ;
- téléchargement public de projet jouable.

Ces éléments ne sont pas oubliés.

Ils sont volontairement reportés afin de conserver une V1 stable, maintenable et présentable.

---

# 34. Captures et preuves à préparer

## Code et backend

- modèles Django ;
- vues Django ;
- routes ;
- service TinyDB ;
- script TinyDB ;
- commande `setup_render_data`.

## Base de données

- migrations ;
- SQL natif ;
- exemples `INSERT INTO` ;
- base TinyDB ;
- affichage NoSQL sur l’accueil.

## Interface

- page d’accueil ;
- page Mes créations ;
- page Projets jouables ;
- menu mobile ouvert.

## Administration

- administration Django ;
- modèles visibles ;
- compte d’évaluation en lecture seule ;
- absence de droits d’ajout, modification et suppression avec le compte limité.

## Déploiement

- Render ;
- logs `setup_render_data` ;
- GitHub ;
- commandes de vérification ;
- site en ligne.

Aucune capture ne doit afficher de mot de passe, clé secrète ou variable sensible.

---

# 35. Enrichissement final de la banque de preuves

## Résumé

Ajout d’un volume important de captures complémentaires après la préparation de la partie Frostia Games du dossier projet.

## Modifications réalisées

- regroupement des nouvelles images dans `Preuve De Fonctionnement/` ;
- ajout des preuves utilisées dans les pages du dossier projet ;
- conservation des versions desktop, tablette et mobile ;
- ajout de captures liées à la sécurité, aux tests, au déploiement et aux difficultés rencontrées ;
- préparation des images destinées aux annexes ;
- conservation de certains doublons utiles afin de ne perdre aucune preuve.

## Décision prise

Les doublons ne sont pas considérés comme bloquants dans la banque de preuves. Ils peuvent correspondre à plusieurs résolutions, plusieurs environnements ou plusieurs étapes d’une même vérification.

Une sélection plus courte et plus lisible est utilisée dans le dossier principal. Les autres fichiers restent disponibles comme preuves complémentaires.

## Statut

Validé.

---

# 36. Conclusion

Frostia Games a évolué vers une V1 Django fonctionnelle, documentée, déployée et renforcée.

Le backend reste volontairement simple, mais il est :

- fonctionnel ;
- administrable ;
- relié à SQLite ;
- complété par TinyDB ;
- lançable avec Docker ;
- disponible en ligne via Render ;
- documenté ;
- accompagné de preuves.

Les technologies mises de côté ont été identifiées et expliquées.

Le choix de conserver Django/Python dans cette V1 permet de protéger la stabilité du projet et d’éviter de repartir de zéro.

À ce stade, l’objectif principal est de finaliser les captures, les annexes et le dossier projet final, sans ajouter de nouvelles fonctionnalités lourdes.