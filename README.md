# Frostia Games

## Présentation

**Frostia Games** est une V1 de portfolio développé avec **Django**.

Le projet sert à présenter des créations vidéoludiques actuelles et futures dans une interface web simple, responsive, documentée et déployée en ligne.

Cette version n'est pas une plateforme complète de gestion de jeux vidéo. Elle constitue une base fonctionnelle, stable et évolutive.

---

## Liens utiles

- Site en ligne : https://frostia-games.onrender.com
- Administration Django : https://frostia-games.onrender.com/admin/
- Documentation principale : `docs/`
- Index des preuves : `PREUVES-FONCTIONNEMENT.md`
- Dossier des preuves : `Preuve De Fonctionnement/`

L'accès administrateur complet reste privé.

Un compte d'évaluation en lecture seule peut être fourni séparément au jury si nécessaire.

---

## Objectif de la V1

L'objectif de cette V1 est de proposer une première version :

- fonctionnelle ;
- documentée ;
- déployée en ligne ;
- versionnée avec Git ;
- accompagnée de preuves de fonctionnement ;
- limitée volontairement pour rester stable.

Le projet est conçu comme une base pouvant évoluer progressivement.

---

## Fonctionnalités principales

La V1 contient :

- une page d'accueil ;
- une page **Mes créations** ;
- une page **Projets jouables à venir** ;
- une navigation principale ;
- un menu mobile en JavaScript ;
- une interface responsive ;
- deux modèles Django principaux ;
- une administration Django ;
- une base SQLite ;
- des extraits SQL natifs documentés ;
- une démonstration NoSQL légère avec TinyDB ;
- un affichage de notes de progression sur la page d'accueil ;
- un accès d'évaluation en lecture seule ;
- un déploiement Render ;
- une documentation technique complète ;
- des preuves de fonctionnement organisées.

---

## Technologies utilisées

| Élément | Technologie |
| ------- | ----------- |
| Framework backend | Django |
| Langage | Python |
| Base principale | SQLite |
| ORM | Django ORM |
| NoSQL léger | TinyDB / JSON |
| Frontend | HTML, CSS, JavaScript |
| Templates | Django Templates |
| Serveur production | Gunicorn |
| Fichiers statiques | WhiteNoise |
| Déploiement | Render |
| Conteneurisation locale | Docker |
| Versioning | Git / GitHub |
| Documentation | Markdown |

---

## Structure simplifiée du projet

```text
frostia-games/
├── frostia_config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── views.py
│   ├── urls.py
│   ├── services/
│   │   └── nosql_notes.py
│   └── management/
│       └── commands/
│           └── setup_render_data.py
├── creations/
├── playable/
├── data/
│   └── nosql/
├── docs/
│   ├── backend/
│   ├── conception/
│   ├── frontend/
│   ├── nosql/
│   └── sql/
├── Preuve De Fonctionnement/
├── scripts/
├── static/
├── templates/
├── build.sh
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── README.md
└── PREUVES-FONCTIONNEMENT.md
```

---

## Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/Zero1366/frostia-games.git
cd frostia-games
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l'environnement virtuel

Sous Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Appliquer les migrations

```bash
python manage.py migrate
```

### 6. Lancer le serveur local

```bash
python manage.py runserver
```

Le site local est ensuite accessible depuis l'adresse fournie par Django dans le terminal.

---

## Vérification Django

Commande de vérification :

```bash
python manage.py check
```

Résultat attendu :

```text
System check identified no issues
```

---

## Lancement avec Docker

Le projet contient une configuration Docker pour tester le lancement dans un environnement local reproductible.

Commande :

```bash
docker compose up --build
```

Docker est utilisé comme outil de test local.

Dans cette V1, Docker n'est pas utilisé comme solution de production.

---

## Administration Django

L'administration Django est disponible à l'adresse :

```text
https://frostia-games.onrender.com/admin/
```

Elle permet de gérer :

- les créations ;
- les projets jouables à venir.

L'accès administrateur complet reste privé.

Aucun mot de passe administrateur ne doit être publié dans le dépôt ou dans les captures.

---

## Accès d'évaluation en lecture seule

Un compte d'évaluation en lecture seule peut être utilisé pour permettre au jury de consulter l'administration Django sans modifier les données.

Configuration générale :

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

Les identifiants ne sont pas indiqués dans ce README. Ils peuvent être transmis séparément si nécessaire.

---

## Initialisation automatique des données Render

Sur Render, la base SQLite peut être réinitialisée lors d'un redémarrage ou d'un redéploiement.

Pour éviter que la version en ligne se retrouve vide, une commande Django personnalisée a été ajoutée :

```bash
python manage.py setup_render_data
```

Cette commande recrée automatiquement :

- la création principale **Frostia Games** ;
- le projet jouable de démonstration ;
- le groupe `Evaluation lecture seule` ;
- le compte `evaluation_temp` ;
- les droits de lecture seule nécessaires.

Le mot de passe du compte d'évaluation n'est pas stocké directement dans le code source.

Il est fourni par une variable d'environnement Render :

```text
EVALUATION_USER_PASSWORD
```

---

## Déploiement Render

Le site est déployé sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

### Build Command

```bash
bash build.sh
```

### Start Command

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande permet :

1. d'appliquer les migrations ;
2. de recréer les données initiales de démonstration ;
3. de recréer l'accès d'évaluation ;
4. de lancer Django avec Gunicorn.

---

## Variables d'environnement

Les variables sensibles doivent rester dans Render ou dans un fichier `.env` non versionné.

Variables attendues :

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
EVALUATION_USER_PASSWORD
```

Le fichier `.env.example` sert uniquement de modèle.

Il ne doit pas contenir les vraies valeurs sensibles.

---

## SQL

Le projet utilise SQLite comme base relationnelle principale.

Les modèles Django principaux sont :

- `Creation` ;
- `PlayableProject`.

La documentation SQL est disponible dans :

```text
docs/sql/
```

Fichiers principaux :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers expliquent le lien entre les modèles Django, l'ORM et les instructions SQL natives.

---

## NoSQL / TinyDB

Une démonstration NoSQL légère a été ajoutée avec TinyDB.

TinyDB sert à stocker et afficher des notes de progression.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/
```

Commande de test :

```bash
python -m scripts.demo_tinydb_notes
```

TinyDB ne remplace pas SQLite.

Il sert uniquement à démontrer une logique documentaire NoSQL dans le cadre de la V1.

---

## JavaScript

Le projet contient un menu mobile dynamique.

Fichier concerné :

```text
static/js/menu.js
```

Ce JavaScript permet :

- d'ouvrir et fermer le menu mobile ;
- de modifier l'état visuel de la navigation ;
- de gérer l'attribut `aria-expanded` ;
- de refermer le menu après un clic sur un lien.

Documentation associée :

```text
docs/frontend/javascript-menu-mobile.md
```

---

## Documentation

La documentation principale est rangée dans :

```text
docs/
```

La documentation complémentaire de renforcement est rangée dans :

```text
docs/
```

La documentation écrite, les scripts techniques et les captures sont désormais regroupés dans `docs/` selon leur catégorie.

Exemples de documents :

```text
docs/archives/documentation-v1/02-Journal de bord.md
docs/backend/modeles-django.md
docs/conception/mcd.md
docs/frontend/javascript-menu-mobile.md
docs/nosql/tinydb-integration.md
docs/sql/sql-natif.md
```

---

## Preuves de fonctionnement

Les preuves sont indexées dans :

```text
PREUVES-FONCTIONNEMENT.md
```

Les captures et éléments visuels sont centralisés dans :

```text
Preuve De Fonctionnement/
```

Ce répertoire regroupe notamment les preuves liées :

- à la conception et aux diagrammes ;
- aux maquettes Figma ;
- au site public sur ordinateur, tablette et mobile ;
- au JavaScript ;
- au backend Django et à l’administration ;
- au SQL et à TinyDB ;
- à la sécurité ;
- aux tests fonctionnels ;
- à GitHub, Docker et Render ;
- aux difficultés rencontrées et aux corrections appliquées.

Un grand nombre d’images a été conservé afin de ne perdre aucune preuve utile. Certains fichiers peuvent donc sembler proches ou apparaître en plusieurs exemplaires. Ces doublons correspondent parfois à des résolutions, des environnements ou des étapes de vérification différents.

Le dossier principal et les annexes utilisent uniquement les captures les plus lisibles et les plus représentatives. Le répertoire complet sert de banque de preuves pour le dossier projet et le futur dossier professionnel.

Les captures ne doivent pas afficher :

- mot de passe ;
- clé secrète ;
- valeur de variable d’environnement ;
- jeton privé ;
- information personnelle inutile.

---

## Limites assumées de la V1

Certaines fonctionnalités sont volontairement reportées :

- PostgreSQL ;
- interface d'administration personnalisée ;
- upload serveur réel ;
- jeu jouable dans le navigateur ;
- espace privé complet ;
- API REST ;
- graphiques Plotly.js ;
- statistiques avancées ;
- tests automatisés complets ;
- MongoDB en production.

Ces limites sont assumées afin de conserver une V1 stable, documentée et présentable.

---

## État actuel

| Partie | État |
| ------ | ---- |
| Projet Django | Fonctionnel |
| Pages publiques | Fonctionnelles |
| Admin Django | Fonctionnel |
| Base SQLite | Fonctionnelle pour V1 |
| SQL natif | Documenté |
| TinyDB | Intégré comme démonstration NoSQL |
| JavaScript menu mobile | Fonctionnel |
| Render | Fonctionnel |
| Compte évaluation lecture seule | Fonctionnel en ligne |
| Documentation | Avancée |
| Preuves | Centralisées dans `Preuve De Fonctionnement/` |

---

## Positionnement du projet

Formulation correcte :

```text
Frostia Games est une première version fonctionnelle d'un portfolio Django destiné à présenter mes projets vidéoludiques. Le projet est déployé en ligne, versionné avec Git, documenté et conçu pour évoluer progressivement.
```

Formulation à éviter :

```text
Frostia Games est une plateforme complète de gestion de projets de jeux vidéo.
```

La V1 est volontairement limitée pour rester maîtrisable.

---

## Conclusion

Frostia Games est une V1 Django fonctionnelle, déployée, documentée et accompagnée de preuves.

Le projet montre une démarche complète :

- conception ;
- développement ;
- base de données ;
- administration ;
- JavaScript ;
- SQL ;
- NoSQL léger ;
- déploiement ;
- versioning ;
- documentation ;
- preuves de fonctionnement.

Cette version constitue une base stable pour présenter le projet et préparer ses futures évolutions.
