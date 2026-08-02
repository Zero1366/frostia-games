# Tests et vérifications — Frostia Games

## Objectif du document

Ce document présente les tests et vérifications réalisés sur le projet **Frostia Games**.

L'objectif est de montrer que la V1 a été contrôlée à plusieurs niveaux :

- fonctionnement local ;
- fonctionnement avec Django ;
- fonctionnement de l'interface publique ;
- fonctionnement de l'administration ;
- affichage des données SQLite ;
- affichage des notes TinyDB ;
- responsive ;
- menu mobile JavaScript ;
- déploiement Render ;
- sécurité minimale ;
- accès d’évaluation en lecture seule ;
- absence d'erreurs bloquantes.

Ce document ne présente pas une campagne complète de tests automatisés.

Il s'agit d'une documentation de vérification fonctionnelle adaptée à une V1.

---

# 1. Périmètre des tests

Les tests et vérifications concernent principalement :

- les pages publiques du site ;
- la navigation ;
- l'affichage responsive ;
- les modèles Django ;
- l'administration Django ;
- le compte d’évaluation en lecture seule ;
- la base SQLite ;
- TinyDB ;
- les fichiers SQL natifs documentaires ;
- le lancement local ;
- le lancement avec Docker ;
- le déploiement Render ;
- les fichiers statiques ;
- les variables d'environnement ;
- la sécurité minimale ;
- les preuves à préparer pour le dossier final.

Les tests automatisés avancés sont reportés à une version future.

---

# 2. Environnement de test local

Les premiers tests ont été réalisés en local avec l'environnement suivant :

| Élément | Valeur |
| ------- | ------ |
| Système | Windows |
| Éditeur | Visual Studio Code |
| Terminal | PowerShell |
| Langage | Python |
| Framework | Django |
| Base de données SQL | SQLite |
| Base NoSQL légère | TinyDB |
| Environnement virtuel | `.venv` |

---

# 3. Commandes de vérification principales

Commandes principales :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

Résultat attendu pour Django :

```text
System check identified no issues
```

Résultat attendu pour TinyDB :

```text
Preuve NoSQL TinyDB — Frostia Games
```

Résultat attendu pour Git en fin de travail :

```text
nothing to commit, working tree clean
```

Ces commandes permettent de vérifier :

- l'absence d'erreur de configuration Django ;
- le fonctionnement de TinyDB ;
- l'état du dépôt Git avant le commit final.

---

# 4. Test du serveur local

Le serveur local peut être lancé avec :

```powershell
python manage.py runserver
```

Adresse locale habituelle :

```text
http://127.0.0.1:8000/
```

ou :

```text
http://localhost:8000/
```

Vérifications à effectuer :

- le serveur démarre correctement ;
- aucune erreur bloquante n'apparaît dans le terminal ;
- la page d'accueil est accessible ;
- les autres pages principales sont accessibles ;
- les fichiers CSS sont chargés ;
- le JavaScript du menu fonctionne ;
- les données SQLite s'affichent ;
- les notes TinyDB s'affichent sur l'accueil.

Résultat attendu :

```text
Serveur local fonctionnel.
```

---

# 5. Pages testées

| Page | URL locale | URL Render | Statut |
| ---- | ---------- | ---------- | ------ |
| Accueil | `/` | `https://frostia-games.onrender.com` | Fonctionnelle |
| Mes créations | `/mes-creations/` | `https://frostia-games.onrender.com/mes-creations/` | Fonctionnelle |
| Projets jouables | `/projets-jouables/` | `https://frostia-games.onrender.com/projets-jouables/` | Fonctionnelle |
| Administration Django | `/admin/` | `https://frostia-games.onrender.com/admin/` | Fonctionnelle |

---

# 6. Test de la page d'accueil

La page d'accueil a été vérifiée afin de confirmer que le site présente correctement le projet Frostia Games.

Vérifications réalisées :

- le titre principal s'affiche ;
- le contenu de présentation est visible ;
- la navigation est présente ;
- le design général est cohérent ;
- le CSS est chargé ;
- les notes de progression TinyDB sont visibles si elles sont prévues ;
- la page ne présente pas d'erreur visible.

Résultat attendu :

```text
Page d'accueil fonctionnelle.
```

---

# 7. Test de l'affichage TinyDB sur l'accueil

La page d'accueil affiche des notes de progression issues de TinyDB.

Chaîne technique vérifiée :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
templates/pages/home.html
```

Vérifications réalisées :

- le service TinyDB est importé dans la vue ;
- les notes sont initialisées si nécessaire ;
- les notes sont recherchées avec le code projet ;
- les notes sont transmises au template ;
- les notes sont visibles sur la page d'accueil ;
- aucune donnée sensible n'est stockée dans le fichier JSON.

Commande de vérification :

```powershell
python -m scripts.demo_tinydb_notes
```

Résultat attendu :

```text
Affichage TinyDB fonctionnel pour la V1.
```

---

# 8. Test de la page Mes créations

La page **Mes créations** a été testée afin de vérifier l'affichage des créations du portfolio.

Vérifications réalisées :

- la page est accessible ;
- les créations enregistrées sont affichées ;
- les données remontent depuis la base SQLite ;
- les données sont filtrées avec `is_visible=True` ;
- les cartes de présentation sont visibles ;
- le contenu reste lisible ;
- la page ne provoque pas d'erreur Django.

Résultat attendu :

```text
Page Mes créations fonctionnelle.
```

---

# 9. Test de la page Projets jouables

La page **Projets jouables** a été testée afin de vérifier l'affichage de l'interface préparatoire.

Vérifications réalisées :

- la page est accessible ;
- les projets enregistrés sont affichés ;
- les données remontent depuis la base SQLite ;
- les données sont filtrées avec `is_visible=True` ;
- le bouton de lecture affiche un comportement prévu ;
- le bouton de sélection de fichier local fonctionne ;
- le message d'upload non implanté est visible ;
- aucun vrai upload serveur n'est effectué.

Résultat attendu :

```text
Page Projets jouables fonctionnelle pour la V1.
```

---

# 10. Test de la navigation

La navigation principale a été testée sur les différentes pages.

Vérifications réalisées :

- les liens du menu fonctionnent ;
- les pages se chargent correctement ;
- aucun lien principal ne mène vers une erreur ;
- l'état actif du menu est visible ;
- la navigation reste compréhensible.

Résultat attendu :

```text
Navigation fonctionnelle.
```

---

# 11. Test du responsive

Le responsive a été vérifié afin de contrôler l'affichage sur différents formats d'écran.

Vérifications réalisées :

- l'interface reste lisible sur écran large ;
- les cartes ne débordent pas ;
- le menu mobile fonctionne ;
- les textes restent lisibles ;
- aucun scroll horizontal important n'a été constaté ;
- les blocs principaux restent accessibles.

Résultat attendu :

```text
Responsive fonctionnel pour une V1, avec améliorations possibles.
```

Limite :

```text
Le responsive peut encore être amélioré visuellement dans une prochaine version.
```

---

# 12. Test des fichiers statiques

Les fichiers statiques ont été testés en local et après déploiement.

Fichiers concernés :

```text
static/css/main.css
static/js/menu.js
static/images/
```

Vérifications réalisées :

- le fichier CSS est chargé ;
- les styles s'appliquent correctement ;
- le JavaScript du menu fonctionne ;
- les images prévues peuvent être utilisées ;
- la commande `collectstatic` fonctionne.

Commande utilisée par le build :

```powershell
python manage.py collectstatic --noinput
```

Résultat attendu :

```text
Fichiers statiques correctement collectés et servis.
```

---

# 13. Test de la base SQLite

La V1 utilise SQLite comme base principale.

Fichier local concerné :

```text
db.sqlite3
```

Vérifications réalisées :

- les migrations s'appliquent correctement ;
- les données peuvent être ajoutées depuis l'administration Django ;
- les données sont conservées localement ;
- les données sont affichées dans les templates ;
- les modèles `Creation` et `PlayableProject` fonctionnent.

Commandes utilisées :

```powershell
python manage.py makemigrations
python manage.py migrate
```

Résultat attendu :

```text
Base SQLite fonctionnelle pour la V1.
```

Limite importante :

```text
SQLite est adaptée à la V1, mais sur Render gratuit elle ne doit pas être considérée comme une persistance durable avancée.
```

---

# 14. Test de TinyDB

TinyDB est utilisé comme expérimentation NoSQL légère.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

Commande utilisée :

```powershell
python -m scripts.demo_tinydb_notes
```

Vérifications réalisées :

- TinyDB est installé ;
- le service NoSQL fonctionne ;
- le dossier `data/nosql/` peut être créé ;
- la base JSON peut être ouverte ;
- les notes de démonstration peuvent être créées ;
- les notes liées à Frostia Games peuvent être retrouvées ;
- les notes sont affichées dans le terminal ;
- aucune donnée sensible n'est stockée.

Résultat attendu :

```text
TinyDB fonctionnel pour la V1 renforcée.
```

---

# 15. Test des modèles Django

Modèles concernés :

```text
Creation
PlayableProject
```

Vérifications réalisées :

- les modèles sont reconnus par Django ;
- les migrations sont générées ;
- les migrations sont appliquées ;
- les objets peuvent être créés depuis l'administration ;
- les objets peuvent être affichés côté site.

Résultat attendu :

```text
Modèles Django fonctionnels.
```

---

# 16. Test du SQL natif documentaire

Des fichiers SQL natifs ont été ajoutés pour renforcer le dossier projet.

Fichiers concernés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Vérifications réalisées :

- les fichiers existent ;
- les tables documentées correspondent aux modèles Django ;
- les exemples `INSERT INTO` sont cohérents avec les champs ;
- la documentation explique que le SQL natif est documentaire ;
- les migrations Django restent la source réelle de création des tables.

Résultat attendu :

```text
SQL natif documentaire cohérent avec le projet.
```

---

# 17. Test de l'administration Django

Adresse locale :

```text
http://127.0.0.1:8000/admin/
```

Adresse Render :

```text
https://frostia-games.onrender.com/admin/
```

Vérifications réalisées :

- la page de connexion s'affiche ;
- le compte administrateur fonctionne ;
- les modèles enregistrés apparaissent ;
- il est possible d'ajouter des données ;
- il est possible de modifier des données ;
- les données ajoutées apparaissent côté site.

Résultat attendu :

```text
Administration Django fonctionnelle.
```

---

# 18. Test du compte administrateur

Un compte administrateur privé a été utilisé pour vérifier l'accès complet à l'interface Django.

Vérifications réalisées :

- connexion possible ;
- accès à l'administration Django ;
- accès aux modèles enregistrés ;
- modification des contenus possible ;
- aucun identifiant publié dans la documentation publique.

Résultat attendu :

```text
Compte administrateur fonctionnel.
```

Les identifiants ne sont pas inscrits dans le dépôt GitHub ni dans la documentation publique.

---

# 19. Test du compte d’évaluation en lecture seule

Un compte d’évaluation en lecture seule a été testé pour vérifier l'accès limité à l'administration Django.

Objectif :

```text
Permettre une consultation limitée sans donner les droits complets d'un administrateur.
```

Vérifications réalisées :

- le compte peut se connecter à l'administration ;
- le compte n'est pas superutilisateur ;
- le compte appartient au groupe `Evaluation lecture seule` ;
- le compte peut consulter les créations ;
- le compte peut consulter les projets jouables ;
- le compte ne peut pas ajouter de contenu ;
- le compte ne peut pas modifier de contenu ;
- le compte ne peut pas supprimer de contenu ;
- le compte ne doit pas accéder aux utilisateurs, groupes et permissions sensibles.

Résultat attendu :

```text
Compte d’évaluation en lecture seule fonctionnel.
```

Les identifiants réels ne doivent pas être écrits dans le dossier projet public.

---

# 20. Test Docker

Le projet peut être testé avec Docker.

Commande utilisée :

```powershell
docker compose up --build
```

Adresse locale habituelle :

```text
http://localhost:8000/
```

Vérifications réalisées :

- l'image Docker se construit ;
- le conteneur démarre ;
- le serveur Django se lance ;
- le site est accessible depuis le navigateur ;
- l'environnement Docker permet de relancer le projet plus facilement.

Résultat attendu :

```text
Lancement Docker fonctionnel.
```

---

# 21. Test Django dans Docker

Commande utilisée :

```powershell
docker compose exec web python manage.py check
```

Résultat attendu :

```text
System check identified no issues
```

Résultat :

```text
Vérification Django fonctionnelle dans Docker.
```

---

# 22. Test TinyDB dans Docker

Commande possible :

```powershell
docker compose exec web python -m scripts.demo_tinydb_notes
```

Cette commande permet de vérifier que TinyDB fonctionne aussi dans l'environnement Docker.

Vérifications attendues :

- TinyDB est installé dans le conteneur ;
- le script est accessible ;
- les notes peuvent être lues ou créées ;
- aucune erreur liée au module `tinydb` n'apparaît.

Résultat attendu :

```text
TinyDB fonctionnel dans Docker.
```

---

# 23. Test du déploiement Render

Le projet est déployé sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Vérifications réalisées :

- le service Render démarre ;
- le build s'exécute correctement ;
- les dépendances sont installées ;
- les fichiers statiques sont collectés ;
- les migrations sont appliquées ;
- Gunicorn lance l'application Django ;
- le site est accessible en ligne ;
- l'administration Django est accessible ;
- la page d'accueil peut afficher les notes TinyDB ;
- les données de démonstration sont recréées avec `setup_render_data`.

Message attendu dans les logs Render :

```text
Your service is live
```

Résultat attendu :

```text
Déploiement Render réussi.
```

---

# 24. Test du Build Command Render

Commande utilisée sur Render :

```bash
bash build.sh
```

Vérifications réalisées :

- installation des dépendances ;
- installation de TinyDB via `requirements.txt` ;
- collecte des fichiers statiques ;
- application des migrations ;
- tentative de création du superutilisateur ;
- absence d'erreur bloquante pendant le build.

Résultat attendu :

```text
Build Command fonctionnel.
```

---

# 25. Test du Start Command Render

Start Command actuel :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Vérifications réalisées :

- les migrations sont appliquées ;
- `setup_render_data` recrée les données nécessaires ;
- le compte d’évaluation est configuré ;
- Gunicorn démarre ;
- Django est lancé via `wsgi.py` ;
- Render détecte correctement le port ;
- le site devient accessible.

Résultat attendu :

```text
Start Command fonctionnel.
```

Logs attendus :

```text
Données initiales créées.
Accès d'évaluation configuré.
Utilisateur : evaluation_temp
Droits : lecture seule
Staff : oui
Superutilisateur : non
Le site devient accessible en ligne.
```

---

# 26. Test des variables d'environnement

Variables utilisées :

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
EVALUATION_USER_PASSWORD
```

Vérifications réalisées :

- les variables sont présentes dans Render ;
- les valeurs sensibles ne sont pas publiées ;
- la clé secrète Django n'est pas écrite directement dans le code ;
- le compte administrateur peut être créé automatiquement ;
- le mot de passe du compte d’évaluation est fourni par Render ;
- le mode debug peut être désactivé en production.

Résultat attendu :

```text
Variables d'environnement opérationnelles.
```

---

# 27. Vérification de la sécurité minimale

Vérifications réalisées :

- `DEBUG` désactivé sur Render ;
- `DJANGO_SECRET_KEY` stockée dans Render ;
- aucun mot de passe publié dans GitHub ;
- aucun identifiant administrateur écrit dans la documentation publique ;
- accès admin conservé privé ;
- compte d’évaluation créé et limité ;
- mot de passe du compte d’évaluation stocké dans `EVALUATION_USER_PASSWORD` ;
- aucune donnée sensible dans TinyDB ;
- SQL brut non utilisé dans les vues ;
- captures à préparer sans secret visible.

Résultat attendu :

```text
Sécurité minimale correcte pour une V1.
```

---

# 28. Problèmes rencontrés pendant les tests

## Erreurs PowerShell avec `bash build.sh`

La commande suivante peut poser problème en local sous PowerShell :

```powershell
bash build.sh
```

Cause :

```text
PowerShell Windows ne correspond pas forcément à l'environnement Linux utilisé par Render.
```

Correction :

```text
La commande est utilisée sur Render, qui fonctionne avec un environnement Linux.
```

---

## Fausses alertes Pylance

VS Code / Pylance pouvait signaler certaines alertes liées au typage Django.

Correction :

- passage du mode strict au mode basic ;
- conservation de `python manage.py check` comme validation Django principale ;
- ajout de commentaires `type: ignore` si nécessaire.

---

## Confusion entre Flask et Django

Une commande de démarrage non adaptée avait été envisagée :

```bash
gunicorn app:app
```

Correction Django :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

---

## Ancien Start Command Render insuffisant

Ancienne commande :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Limite :

```text
Elle lançait Django, mais ne recréait pas les données de démonstration ni le compte d’évaluation après redémarrage.
```

Correction :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

---

# 29. Tests non réalisés dans la V1

Certains tests ne sont pas encore réalisés dans cette V1.

Tests reportés :

- tests unitaires automatisés complets ;
- tests d'intégration avancés ;
- tests de charge ;
- tests de sécurité poussés ;
- tests d'upload serveur ;
- tests PostgreSQL ;
- tests d'un espace privé personnalisé ;
- tests de statistiques ou graphiques.

Ces tests sont reportés car les fonctionnalités associées ne font pas partie du périmètre immédiat de la V1.

---

# 30. Tableau récapitulatif des tests

| Élément testé | Résultat |
| ------------- | -------- |
| Lancement local Django | Validé |
| `python manage.py check` | Validé |
| Page d'accueil | Validé |
| Notes TinyDB sur l'accueil | Validé |
| Page Mes créations | Validé |
| Page Projets jouables | Validé |
| Navigation | Validé |
| Responsive | Fonctionnel pour V1 |
| CSS | Validé |
| JavaScript menu | Validé |
| Modèles Django | Validé |
| Migrations | Validé |
| Base SQLite | Validé pour V1 |
| SQL natif documentaire | Validé |
| TinyDB | Validé |
| Administration Django | Validé |
| Compte administrateur | Validé |
| Compte d’évaluation lecture seule | Validé |
| Docker | Validé |
| Déploiement Render | Validé |
| `setup_render_data` | Validé |
| Fichiers statiques en production | Validé |
| Variables d'environnement | Validé |
| Sécurité minimale | Validé pour V1 |

---

# 31. Captures et preuves à préparer

Pour le dossier projet, les preuves suivantes peuvent être préparées :

- terminal avec `python manage.py check` ;
- terminal avec `python -m scripts.demo_tinydb_notes` ;
- page d'accueil ;
- notes TinyDB sur l'accueil ;
- page Mes créations ;
- page Projets jouables ;
- menu mobile ouvert ;
- administration Django ;
- compte d’évaluation en lecture seule ;
- modèles Django ;
- fichier `core/views.py` ;
- fichier `core/services/nosql_notes.py` ;
- fichier `scripts/demo_tinydb_notes.py` ;
- fichier `setup_render_data.py` ;
- fichiers SQL natifs ;
- fichier `static/js/menu.js` ;
- Docker lancé ;
- Render actif ;
- logs Render avec `setup_render_data` ;
- variables Render masquées ;
- GitHub ;
- `git status` propre.

Aucune capture ne doit afficher :

- mot de passe ;
- clé secrète ;
- vraie valeur de variable sensible ;
- identifiant privé inutile ;
- information personnelle inutile.

---

# 32. Bilan

Les tests réalisés montrent que la V1 de **Frostia Games** est fonctionnelle.

Le site peut être lancé en local, lancé avec Docker et consulté en ligne via Render.

Les pages principales fonctionnent, les données Django sont affichées, l'administration est accessible et le déploiement est opérationnel.

La V1 renforcée contient également :

- une expérimentation TinyDB fonctionnelle ;
- des notes NoSQL affichées sur l'accueil ;
- un compte d’évaluation en lecture seule ;
- des fichiers SQL natifs documentaires ;
- une initialisation automatique Render avec `setup_render_data`.

La V1 reste volontairement limitée, mais elle est stable, testée et présentable dans son périmètre actuel.

À ce stade, la priorité n'est plus d'ajouter de nouvelles fonctionnalités lourdes, mais de finaliser les captures, les preuves et le dossier projet final.
