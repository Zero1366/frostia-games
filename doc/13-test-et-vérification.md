# Tests et vérifications - Frostia Games

## Objectif du document

Ce document présente les tests et vérifications réalisés sur le projet **Frostia Games**.

L'objectif est de montrer que la V1 a été contrôlée à plusieurs niveaux :

* fonctionnement local ;
* fonctionnement avec Django ;
* fonctionnement de l'interface publique ;
* fonctionnement de l'administration ;
* affichage des données SQLite ;
* affichage des notes TinyDB ;
* responsive ;
* menu mobile JavaScript ;
* déploiement Render ;
* sécurité minimale ;
* compte temporaire de lecture seule ;
* absence d'erreurs bloquantes.

Ce document ne présente pas une campagne de tests automatisés complète. Il s'agit d'une documentation de vérification fonctionnelle adaptée à une V1.

Ce document a été mis à jour après le renforcement du dossier projet afin d'intégrer :

* TinyDB ;
* le script `python -m scripts.demo_tinydb_notes` ;
* l'affichage des notes NoSQL sur l'accueil ;
* le compte temporaire de lecture seule ;
* les fichiers SQL natifs documentaires ;
* les preuves à préparer pour le dossier final.

---

## Périmètre des tests

Les tests réalisés concernent principalement :

* les pages publiques du site ;
* la navigation ;
* l'affichage responsive ;
* les modèles Django ;
* l'administration Django ;
* le compte temporaire de lecture seule ;
* la base SQLite ;
* TinyDB ;
* les fichiers SQL natifs documentaires ;
* le lancement local ;
* le lancement avec Docker ;
* le déploiement Render ;
* les fichiers statiques ;
* les variables d'environnement.

Les tests automatisés avancés sont reportés à une version future.

---

## Environnement de test local

Les premiers tests ont été réalisés en local avec l'environnement suivant :

| Élément               | Valeur             |
| --------------------- | ------------------ |
| Système               | Windows            |
| Éditeur               | Visual Studio Code |
| Terminal              | PowerShell         |
| Langage               | Python             |
| Framework             | Django             |
| Base de données SQL   | SQLite             |
| Base NoSQL légère     | TinyDB             |
| Environnement virtuel | `.venv`            |

---

## Commandes de vérification Django

Les commandes principales utilisées pour vérifier le projet sont :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

La commande Django attendue est :

```powershell
python manage.py check
```

Résultat attendu :

```txt
System check identified no issues (0 silenced).
```

La commande TinyDB attendue est :

```powershell
python -m scripts.demo_tinydb_notes
```

Résultat attendu :

```txt
Preuve NoSQL TinyDB — Frostia Games
```

Ces commandes permettent de vérifier que Django ne détecte pas d'erreur de configuration majeure, que TinyDB fonctionne et que le dépôt Git peut être contrôlé avant un commit final.

---

## Test du serveur local

Le serveur local a été lancé avec la commande :

```powershell
python manage.py runserver
```

Adresse utilisée :

```txt
https://frostia-games.onrender.com/
```

Vérifications effectuées :

* le serveur démarre correctement ;
* aucune erreur bloquante n'apparaît dans le terminal ;
* la page d'accueil est accessible ;
* les autres pages principales sont accessibles ;
* les fichiers CSS sont chargés ;
* le JavaScript du menu fonctionne ;
* les données SQLite s'affichent ;
* les notes TinyDB s'affichent sur l'accueil.

---

## Pages testées

Les pages principales du projet ont été testées.

| Page                  | URL locale           | Statut        |
| --------------------- | -------------------- | ------------- |
| Accueil               | `/`                  | Fonctionnelle |
| Mes créations         | `/mes-creations/`    | Fonctionnelle |
| Projets jouables      | `/projets-jouables/` | Fonctionnelle |
| Administration Django | `/admin/`            | Fonctionnelle |

---

## Test de la page d'accueil

La page d'accueil a été vérifiée afin de confirmer que le site présente correctement le projet Frostia Games.

Vérifications réalisées :

* le titre principal s'affiche ;
* le contenu de présentation est visible ;
* la navigation est présente ;
* le design général est cohérent ;
* le CSS est chargé ;
* les notes de progression TinyDB sont visibles ;
* la page ne présente pas d'erreur visible.

Résultat :

```txt
Page d'accueil fonctionnelle.
```

---

## Test de l'affichage TinyDB sur l'accueil

La page d'accueil affiche des notes de progression issues de TinyDB.

Chaîne technique vérifiée :

```txt
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

Fichiers concernés :

```txt
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
templates/pages/home.html
```

Vérifications réalisées :

* le service TinyDB est importé dans la vue ;
* les notes sont initialisées si nécessaire ;
* les notes sont recherchées avec le code projet ;
* les notes sont transmises au template ;
* les notes sont visibles sur la page d'accueil ;
* aucune donnée sensible n'est stockée dans le fichier JSON.

Commande de vérification :

```powershell
python -m scripts.demo_tinydb_notes
```

Résultat :

```txt
Affichage TinyDB fonctionnel pour la V1.
```

---

## Test de la page Mes créations

La page **Mes créations** a été testée afin de vérifier l'affichage des créations du portfolio.

Vérifications réalisées :

* la page est accessible ;
* les créations enregistrées sont affichées ;
* les données remontent depuis la base SQLite ;
* les données sont filtrées avec `is_visible=True` ;
* les cartes de présentation sont visibles ;
* le contenu reste lisible ;
* la page ne provoque pas d'erreur Django.

Résultat :

```txt
Page Mes créations fonctionnelle.
```

---

## Test de la page Projets jouables

La page **Projets jouables** a été testée afin de vérifier l'affichage de l'interface préparatoire.

Vérifications réalisées :

* la page est accessible ;
* les projets enregistrés sont affichés ;
* les données remontent depuis la base SQLite ;
* les données sont filtrées avec `is_visible=True` ;
* le bouton de lecture affiche un comportement prévu ;
* le bouton de sélection de fichier local fonctionne ;
* le message d'upload non implanté est visible ;
* aucun vrai upload serveur n'est effectué.

Résultat :

```txt
Page Projets jouables fonctionnelle pour la V1.
```

---

## Test de la navigation

La navigation principale a été testée sur les différentes pages.

Vérifications réalisées :

* les liens du menu fonctionnent ;
* les pages se chargent correctement ;
* aucun lien principal ne mène vers une erreur ;
* l'état actif du menu est visible ;
* la navigation reste compréhensible.

Résultat :

```txt
Navigation fonctionnelle.
```

---

## Test du responsive

Le responsive a été vérifié afin de contrôler l'affichage sur différents formats d'écran.

Vérifications réalisées :

* l'interface reste lisible sur écran large ;
* les cartes ne débordent pas ;
* le menu mobile fonctionne ;
* les textes restent lisibles ;
* aucun scroll horizontal important n'a été constaté ;
* les blocs principaux restent accessibles.

Résultat :

```txt
Responsive fonctionnel pour une V1, avec améliorations possibles.
```

Limite constatée :

```txt
Le responsive peut encore être amélioré visuellement dans une prochaine version.
```

---

## Test des fichiers statiques

Les fichiers statiques ont été testés en local et après déploiement.

Fichiers concernés :

```txt
static/css/main.css
static/js/menu.js
static/images/
```

Vérifications réalisées :

* le fichier CSS est chargé ;
* les styles s'appliquent correctement ;
* le JavaScript du menu fonctionne ;
* les images prévues peuvent être utilisées ;
* la commande `collectstatic` fonctionne.

Commande utilisée :

```powershell
python manage.py collectstatic --noinput
```

Résultat :

```txt
Fichiers statiques correctement collectés.
```

---

## Test de la base de données SQLite

La V1 utilise SQLite.

Fichier concerné :

```txt
db.sqlite3
```

Vérifications réalisées :

* les migrations s'appliquent correctement ;
* les données peuvent être ajoutées depuis l'administration Django ;
* les données sont conservées localement ;
* les données sont affichées dans les templates ;
* les modèles `Creation` et `PlayableProject` fonctionnent.

Commandes utilisées :

```powershell
python manage.py makemigrations
python manage.py migrate
```

Résultat :

```txt
Base SQLite fonctionnelle pour la V1.
```

---

## Test de TinyDB

TinyDB est utilisé comme expérimentation NoSQL légère.

Fichiers concernés :

```txt
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

* TinyDB est installé ;
* le service NoSQL fonctionne ;
* le dossier `data/nosql/` peut être créé ;
* la base JSON peut être ouverte ;
* les notes de démonstration peuvent être créées ;
* les notes liées à Frostia Games peuvent être retrouvées ;
* les notes sont affichées dans le terminal ;
* aucune donnée sensible n'est stockée.

Résultat :

```txt
TinyDB fonctionnel pour la V1 renforcée.
```

---

## Test des modèles Django

Les modèles Django principaux ont été vérifiés.

Modèles concernés :

* `Creation` ;
* `PlayableProject`.

Vérifications réalisées :

* les modèles sont reconnus par Django ;
* les migrations sont générées ;
* les migrations sont appliquées ;
* les objets peuvent être créés depuis l'administration ;
* les objets peuvent être affichés côté site.

Résultat :

```txt
Modèles Django fonctionnels.
```

---

## Test du SQL natif documentaire

Des fichiers SQL natifs ont été ajoutés pour renforcer le dossier projet.

Fichiers concernés :

```txt
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Vérifications réalisées :

* les fichiers existent ;
* les tables documentées correspondent aux modèles Django ;
* les exemples `INSERT INTO` sont cohérents avec les champs ;
* la documentation explique que le SQL natif est documentaire ;
* les migrations Django restent la source réelle de création des tables.

Résultat :

```txt
SQL natif documentaire cohérent avec le projet.
```

---

## Test de l'administration Django

L'administration Django a été testée en local puis en ligne.

Adresse locale :

```txt
https://frostia-games.onrender.com/admin/
```

Adresse en ligne :

```txt
https://frostia-games.onrender.com/admin/
```

Vérifications réalisées :

* la page de connexion s'affiche ;
* le compte administrateur fonctionne ;
* les modèles enregistrés apparaissent ;
* il est possible d'ajouter des données ;
* il est possible de modifier des données ;
* les données ajoutées apparaissent côté site.

Résultat :

```txt
Administration Django fonctionnelle.
```

---

## Test du compte administrateur

Un compte administrateur privé a été utilisé pour vérifier l'accès à l'interface Django.

Vérifications réalisées :

* connexion possible ;
* accès à l'admin Django ;
* accès aux modèles enregistrés ;
* modification des contenus possible ;
* aucun identifiant publié dans la documentation.

Résultat :

```txt
Compte administrateur fonctionnel.
```

Pour des raisons de sécurité, les identifiants ne sont pas inscrits dans le dépôt GitHub ni dans la documentation publique.

---

## Test du compte temporaire de lecture seule

Un compte temporaire de lecture seule a été testé pour vérifier l'accès limité à l'administration Django.

Objectif :

```txt
Permettre une consultation limitée sans donner les droits complets d'un administrateur.
```

Vérifications réalisées :

* le compte peut se connecter à l'administration ;
* le compte n'est pas superutilisateur ;
* le compte appartient au groupe de lecture seule ;
* le compte peut consulter les créations ;
* le compte peut consulter les projets jouables ;
* le compte ne doit pas modifier les utilisateurs ;
* le compte ne doit pas modifier les groupes ;
* le compte ne doit pas accéder aux permissions sensibles.

Résultat :

```txt
Compte temporaire de lecture seule fonctionnel.
```

Les identifiants réels ne doivent pas être écrits dans le dossier projet public.

---

## Test Docker

Le projet a également été testé avec Docker.

Commande utilisée :

```powershell
docker compose up --build
```

Vérifications réalisées :

* l'image Docker se construit ;
* le conteneur démarre ;
* le serveur Django se lance ;
* le site est accessible depuis le navigateur ;
* l'environnement Docker permet de relancer le projet plus facilement.

Adresse utilisée :

```txt
https://frostia-games.onrender.com/
```

Résultat :

```txt
Lancement Docker fonctionnel.
```

---

## Test Django dans Docker

Commande utilisée :

```powershell
docker compose exec web python manage.py check
```

Résultat attendu :

```txt
System check identified no issues (0 silenced).
```

Résultat :

```txt
Vérification Django fonctionnelle dans Docker.
```

---

## Test TinyDB dans Docker

Commande possible :

```powershell
docker compose exec web python -m scripts.demo_tinydb_notes
```

Cette commande permet de vérifier que TinyDB fonctionne aussi dans l'environnement Docker.

Vérifications attendues :

* TinyDB est installé dans le conteneur ;
* le script est accessible ;
* les notes peuvent être lues ou créées ;
* aucune erreur liée au module `tinydb` n'apparaît.

Résultat attendu :

```txt
TinyDB fonctionnel dans Docker.
```

---

## Test du déploiement Render

Le projet a été déployé sur Render.

URL de production :

```txt
https://frostia-games.onrender.com
```

Vérifications réalisées :

* le service Render démarre ;
* le build s'exécute correctement ;
* les dépendances sont installées ;
* les fichiers statiques sont collectés ;
* les migrations sont appliquées ;
* Gunicorn lance l'application Django ;
* le site est accessible en ligne ;
* l'administration Django est accessible ;
* la page d'accueil peut afficher les notes TinyDB.

Message observé dans les logs Render :

```txt
Your service is live
```

Résultat :

```txt
Déploiement Render réussi.
```

---

## Test du Build Command Render

Commande utilisée sur Render :

```bash
bash build.sh
```

Vérifications réalisées :

* installation des dépendances ;
* installation de TinyDB via `requirements.txt` ;
* collecte des fichiers statiques ;
* application des migrations ;
* tentative de création du superutilisateur ;
* absence d'erreur bloquante pendant le build.

Résultat :

```txt
Build Command fonctionnel.
```

---

## Test du Start Command Render

Commande utilisée sur Render :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Vérifications réalisées :

* Gunicorn démarre ;
* Django est lancé via `wsgi.py` ;
* Render détecte correctement le port ;
* le site devient accessible.

Résultat :

```txt
Start Command fonctionnel.
```

---

## Test des variables d'environnement

Les variables d'environnement Render ont été vérifiées.

Variables utilisées :

```txt
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
```

Vérifications réalisées :

* les variables sont présentes dans Render ;
* les valeurs sensibles ne sont pas publiées ;
* la clé secrète Django n'est pas écrite directement dans le code ;
* le compte administrateur peut être créé automatiquement ;
* le mode debug peut être désactivé en production.

Résultat :

```txt
Variables d'environnement opérationnelles.
```

---

## Vérification de la sécurité minimale

Vérifications réalisées :

* `DEBUG` désactivé sur Render ;
* `DJANGO_SECRET_KEY` stockée dans Render ;
* aucun mot de passe publié dans GitHub ;
* aucun identifiant administrateur écrit dans la documentation ;
* accès admin conservé privé ;
* compte temporaire de lecture seule créé et limité ;
* aucune donnée sensible dans TinyDB ;
* SQL brut non utilisé dans les vues.

Résultat :

```txt
Sécurité minimale correcte pour une V1.
```

---

## Problèmes rencontrés pendant les tests

Plusieurs problèmes ont été rencontrés pendant les tests et la stabilisation du projet.

### Erreurs PowerShell

La commande suivante a posé problème en local :

```powershell
bash build.sh
```

Cause :

```txt
PowerShell Windows ne correspond pas à un environnement Linux standard.
```

Correction :

```txt
La commande est utilisée sur Render, qui fonctionne avec un environnement Linux.
```

---

### Fausses alertes Pylance

VS Code / Pylance signalait certaines erreurs liées au typage Django.

Ces alertes concernaient notamment :

* `CharField` ;
* `SlugField` ;
* `BooleanField` ;
* `ModelAdmin`.

Correction :

* passage du mode strict au mode basic ;
* conservation de `python manage.py check` comme validation Django principale ;
* ajout de commentaires `type: ignore` lorsque nécessaire.

---

### Confusion entre Flask et Django

Une commande de démarrage non adaptée avait été envisagée :

```bash
gunicorn app:app
```

Correction :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande est adaptée à la structure Django du projet.

---

### Confusion entre commandes Render et variables d'environnement

Une confusion a eu lieu entre les variables d'environnement et les commandes de déploiement.

Correction :

* les variables Django restent dans **Environment Variables** ;
* `bash build.sh` doit être placé dans **Build Command** ;
* la commande Gunicorn doit être placée dans **Start Command**.

---

## Tests non réalisés dans la V1

Certains tests ne sont pas encore réalisés dans cette V1.

Tests reportés :

* tests unitaires automatisés complets ;
* tests d'intégration avancés ;
* tests de charge ;
* tests de sécurité poussés ;
* tests d'upload serveur ;
* tests PostgreSQL ;
* tests d'un espace privé personnalisé ;
* tests de statistiques ou graphiques.

Ces tests sont reportés car les fonctionnalités associées ne font pas partie du périmètre immédiat de la V1.

---

## Tableau récapitulatif des tests

| Élément testé                     | Résultat            |
| --------------------------------- | ------------------- |
| Lancement local Django            | Validé              |
| Commande `python manage.py check` | Validé              |
| Page d'accueil                    | Validé              |
| Notes TinyDB sur l'accueil        | Validé              |
| Page Mes créations                | Validé              |
| Page Projets jouables             | Validé              |
| Navigation                        | Validé              |
| Responsive                        | Fonctionnel pour V1 |
| CSS                               | Validé              |
| JavaScript menu                   | Validé              |
| Modèles Django                    | Validé              |
| Migrations                        | Validé              |
| Base SQLite                       | Validé              |
| SQL natif documentaire            | Validé              |
| TinyDB                            | Validé              |
| Administration Django             | Validé              |
| Compte administrateur             | Validé              |
| Compte temporaire de lecture seule | Validé             |
| Docker                            | Validé              |
| Déploiement Render                | Validé              |
| Fichiers statiques en production  | Validé              |
| Variables d'environnement         | Validé              |
| Sécurité minimale                 | Validé pour V1      |

---

---

## Captures et preuves à préparer

Pour le dossier projet, les preuves suivantes peuvent être préparées :

* terminal avec `python manage.py check` ;
* terminal avec `python -m scripts.demo_tinydb_notes` ;
* page d'accueil ;
* notes TinyDB sur l'accueil ;
* page Mes créations ;
* page Projets jouables ;
* menu mobile ouvert ;
* administration Django ;
* compte temporaire de lecture seule ;
* modèles Django ;
* fichier `core/views.py` ;
* fichier `core/services/nosql_notes.py` ;
* fichier `scripts/demo_tinydb_notes.py` ;
* fichiers SQL natifs ;
* fichier `static/js/menu.js` ;
* Docker lancé ;
* Render actif ;
* variables Render masquées ;
* GitHub ;
* `git status` propre.

Aucune capture ne doit afficher :

* mot de passe ;
* clé secrète ;
* vraie valeur de variable sensible ;
* identifiant privé inutile ;
* information personnelle inutile.

---

## Bilan

Les tests réalisés montrent que la V1 de **Frostia Games** est fonctionnelle.

Le site peut être lancé en local, lancé avec Docker et consulté en ligne via Render.

Les pages principales fonctionnent, les données Django sont affichées, l'administration est accessible et le déploiement est opérationnel.

La V1 renforcée contient également une expérimentation TinyDB fonctionnelle, des notes NoSQL affichées sur l'accueil, un compte temporaire de lecture seule et des fichiers SQL natifs documentaires.

La V1 reste volontairement limitée, mais elle est stable, testée et présentable dans son périmètre actuel.

À ce stade, la priorité n'est plus d'ajouter de nouvelles fonctionnalités lourdes, mais de finaliser les captures, les preuves et le dossier projet final.


