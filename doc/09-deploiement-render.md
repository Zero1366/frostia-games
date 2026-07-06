# Journal de déploiement Render - Frostia Games

## Objectif

Déployer le projet Django **Frostia Games** sur Render afin d'obtenir une version accessible en ligne.

Ce déploiement permet de vérifier que le projet fonctionne hors de l'environnement local, avec :

* une URL publique ;
* une configuration serveur ;
* les fichiers statiques ;
* les migrations Django ;
* l'accès à l'administration Django ;
* l'affichage des pages publiques ;
* l'affichage des données SQLite ;
* l'affichage des notes TinyDB sur l'accueil ;
* une configuration compatible avec le dossier projet.

Ce document garde une trace des réglages utilisés, des problèmes rencontrés, des vérifications réalisées et des limites connues du déploiement.

---

# 1. Plateforme utilisée

* Hébergeur : Render
* Type de service : Web Service
* Environnement : Python 3
* Branche déployée : `main`
* Région : Frankfurt
* URL de production : `https://frostia-games.onrender.com`

Render est utilisé pour rendre la V1 accessible en ligne.

Docker n'est pas utilisé comme méthode de production dans cette V1.

Docker reste utilisé comme outil de lancement local, de test et de reproductibilité.

---

# 2. Structure du projet

Le projet Django possède une structure simple avec le fichier `manage.py` placé à la racine du dépôt GitHub.

Éléments importants du projet :

```text
frostia-games/
├── frostia_config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── views.py
│   └── services/
│       └── nosql_notes.py
├── creations/
├── playable/
├── data/
│   └── nosql/
│       └── project_notes_db.json
├── scripts/
│   ├── __init__.py
│   └── demo_tinydb_notes.py
├── static/
├── staticfiles/
├── templates/
├── doc/
├── docs/
├── build.sh
├── manage.py
├── requirements.txt
└── db.sqlite3
```

Le dossier `frostia_config` contient la configuration principale du projet Django.

Le fichier `wsgi.py` est utilisé par Gunicorn pour lancer l'application Django en production.

Le dossier `core/services/` contient le service Python utilisé pour l'expérimentation NoSQL TinyDB.

Le dossier `data/nosql/` contient la base JSON TinyDB utilisée pour les notes de progression.

Le dossier `scripts/` contient un script de démonstration permettant de tester TinyDB depuis le terminal.

---

# 3. Configuration Render

Le champ **Root Directory** a été laissé vide, car le fichier `manage.py` se trouve directement à la racine du projet.

## Root Directory

```text
vide
```

## Build Command

```bash
bash build.sh
```

## Start Command

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette configuration permet à Render :

* d'installer les dépendances ;
* de collecter les fichiers statiques ;
* d'appliquer les migrations ;
* de lancer l'application Django avec Gunicorn ;
* d'exposer l'application sur le port fourni par Render.

---

# 4. Explication du Start Command

La commande suivante permet de lancer le projet Django avec Gunicorn :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Explication :

* `gunicorn` lance le serveur Python utilisé en production.
* `frostia_config.wsgi:application` indique à Gunicorn où se trouve l'application Django.
* `--bind 0.0.0.0:$PORT` indique au serveur d'écouter sur le port fourni automatiquement par Render.

Cette configuration est importante car Render fournit lui-même le port à utiliser via la variable `$PORT`.

Il ne faut donc pas écrire un port fixe dans la commande de démarrage.

---

# 5. Variables d'environnement Render

Les variables d'environnement ont été ajoutées dans Render, dans la section **Environment Variables**.

Les valeurs secrètes ne doivent pas être écrites directement dans la documentation du projet.

| Variable                    | Rôle                                     |
| --------------------------- | ---------------------------------------- |
| `DJANGO_DEBUG`              | Active ou désactive le mode debug Django |
| `DJANGO_SECRET_KEY`         | Clé secrète utilisée par Django          |
| `DJANGO_SUPERUSER_USERNAME` | Nom du compte administrateur Django      |
| `DJANGO_SUPERUSER_EMAIL`    | Adresse email du compte administrateur   |
| `DJANGO_SUPERUSER_PASSWORD` | Mot de passe du compte administrateur    |

Configuration utilisée dans le principe :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=valeur masquée pour sécurité
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=valeur masquée ou email personnel
DJANGO_SUPERUSER_PASSWORD=valeur masquée pour sécurité
```

Les variables sensibles comme `DJANGO_SECRET_KEY` et `DJANGO_SUPERUSER_PASSWORD` ne doivent jamais être publiées dans GitHub.

Les captures d'écran Render ne doivent pas afficher les vraies valeurs sensibles.

---

# 6. Fichier `.env.example`

Le fichier `.env.example` sert uniquement de modèle.

Il permet de documenter les variables attendues sans exposer les vraies valeurs.

Exemple :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Ce fichier peut être publié dans GitHub car il ne contient pas les vraies valeurs.

Il ne doit pas contenir :

* la vraie clé secrète ;
* le vrai mot de passe administrateur ;
* les identifiants complets du compte temporaire de lecture seule ;
* une information privée inutile.

---

# 7. Script de build

Le fichier `build.sh` est utilisé par Render pendant la phase de construction du projet.

Contenu du fichier :

```bash
#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true
```

---

# 8. Rôle du script de build

Le script effectue plusieurs actions automatiquement :

1. Installation des dépendances Python.
2. Collecte des fichiers statiques.
3. Application des migrations Django.
4. Tentative de création d'un superutilisateur.

La ligne suivante permet d'éviter que le déploiement échoue si le superutilisateur existe déjà :

```bash
python manage.py createsuperuser --noinput || true
```

Le script ne doit pas contenir directement d'identifiant, de mot de passe ou de clé secrète.

Les valeurs sensibles doivent rester dans les variables d'environnement Render.

---

# 9. Dépendances nécessaires

Le fichier `requirements.txt` doit contenir les dépendances nécessaires au fonctionnement du projet Django sur Render.

Dépendances importantes :

```text
Django
gunicorn
whitenoise
tinydb
```

Rôle des dépendances :

* `Django` permet de faire fonctionner le projet.
* `gunicorn` permet de lancer le projet en production.
* `whitenoise` permet de servir les fichiers statiques plus simplement en production.
* `tinydb` permet de faire fonctionner l'expérimentation NoSQL légère.

TinyDB est nécessaire depuis l'ajout des notes de progression affichées sur la page d'accueil.

---

# 10. Fichiers statiques

Le projet utilise des fichiers statiques pour :

* le CSS ;
* le JavaScript ;
* les images ;
* les éléments d'interface.

Pendant le déploiement, la commande suivante est exécutée :

```bash
python manage.py collectstatic --noinput
```

Cette commande collecte les fichiers statiques dans le dossier prévu pour la production.

WhiteNoise permet ensuite de servir ces fichiers statiques sur Render.

Les fichiers concernés sont notamment :

```text
static/css/main.css
static/js/menu.js
static/images/
```

Le fichier JavaScript `static/js/menu.js` est utilisé pour le menu mobile.

---

# 11. Base SQLite et migrations

La V1 utilise SQLite comme base principale.

Les migrations sont appliquées pendant le build Render avec :

```bash
python manage.py migrate
```

Cette commande crée ou met à jour les tables nécessaires.

Tables principales :

```text
creations_creation
playable_playableproject
```

Ces tables correspondent aux modèles Django :

* `Creation` ;
* `PlayableProject`.

La base SQLite reste adaptée à la V1, car le projet reste un portfolio simple avec un volume de données limité.

Pour une version plus avancée, PostgreSQL pourra être envisagé.

---

# 12. TinyDB sur Render

Le projet utilise aussi TinyDB pour une expérimentation NoSQL légère.

TinyDB sert à stocker et afficher des notes de progression liées au projet Frostia Games.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
templates/pages/home.html
```

Chaîne technique :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

TinyDB ne remplace pas SQLite.

SQLite reste la base principale.

TinyDB sert seulement à démontrer une logique NoSQL simple dans le cadre du dossier projet.

---

# 13. Limite de TinyDB sur Render

TinyDB utilise un fichier JSON.

Sur Render, l'environnement d'exécution gratuit n'est pas conçu comme un stockage de données durable avancé.

Dans cette V1, ce n'est pas un problème majeur, car TinyDB sert uniquement à afficher des notes de démonstration.

Il ne doit pas être utilisé pour stocker :

* des mots de passe ;
* des clés secrètes ;
* des données personnelles sensibles ;
* des données utilisateur importantes ;
* des informations critiques.

Si le projet évolue vers une vraie persistance NoSQL, une solution plus adaptée comme MongoDB pourra être envisagée.

---

# 14. Administration Django en ligne

L'administration Django est accessible en ligne à l'adresse :

```text
https://frostia-games.onrender.com/admin/
```

Elle permet de gérer :

* les créations ;
* les projets jouables.

L'accès administrateur complet doit rester privé.

Aucun identifiant administrateur ne doit être publié dans :

* GitHub ;
* les fichiers Markdown ;
* les captures ;
* le dossier projet public.

---

# 15. Compte temporaire de lecture seule

Un compte temporaire de lecture seule peut être utilisé pour l'évaluation.

Ce compte permet de consulter certaines données dans l'administration Django sans donner un accès complet.

Il peut voir :

* les créations ;
* les projets jouables.

Il ne doit pas voir :

* les utilisateurs ;
* les groupes ;
* les permissions sensibles ;
* les variables d'environnement ;
* les secrets du projet.

Les identifiants réels de ce compte ne doivent pas être écrits dans la documentation publique.

Ils peuvent être transmis séparément uniquement si nécessaire.

---

# 16. Problèmes rencontrés

## Confusion entre variables d'environnement et commandes Render

Une confusion a eu lieu entre la section **Environment Variables** et les commandes de déploiement.

Correction effectuée :

* Les variables Django doivent rester dans **Environment Variables**.
* La commande `bash build.sh` doit être placée dans **Build Command**.
* La commande Gunicorn doit être placée dans **Start Command**.

---

## Erreur locale avec PowerShell

Une erreur est apparue en local sous PowerShell avec la commande :

```bash
bash build.sh
```

Erreur rencontrée :

```text
failed: No such file or directory
```

Cette erreur venait de l'environnement Windows local, car PowerShell ne gère pas Bash comme un environnement Linux standard.

Sur Render, cette commande fonctionne car le service tourne dans un environnement Linux.

---

## Différence entre Docker et Render

Docker et Render n'ont pas le même rôle dans le projet.

Docker sert à tester le projet dans un environnement local reproductible.

Render sert à publier le site en ligne.

Dans cette V1, Docker n'est pas utilisé comme solution de production.

---

# 17. Résultat du déploiement

Le déploiement Render a réussi.

Message observé dans les logs Render :

```text
Your service is live
```

Render indique également que l'application écoute correctement sur le port fourni :

```text
Listening at: http://0.0.0.0:10000
```

Le site est accessible publiquement à l'adresse suivante :

```text
https://frostia-games.onrender.com
```

---

# 18. Vérifications effectuées

Les vérifications suivantes ont été réalisées après le déploiement :

* Page d'accueil accessible.
* CSS chargé correctement.
* Navigation fonctionnelle.
* Menu mobile fonctionnel.
* Interface `/admin/` accessible.
* Connexion à l'administration Django fonctionnelle.
* Données SQLite visibles sur les pages publiques.
* Page **Mes créations** accessible.
* Page **Projets jouables** accessible.
* Notes TinyDB visibles sur l'accueil.
* Déploiement Render actif.
* Service indiqué comme live dans les logs Render.

---

# 19. Vérifications techniques utiles

Avant ou après un déploiement, les commandes locales suivantes peuvent être utilisées :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

Résultats attendus :

```text
System check identified no issues
```

et :

```text
nothing to commit, working tree clean
```

Ces commandes permettent de vérifier :

* la configuration Django ;
* le fonctionnement de TinyDB ;
* l'état du dépôt Git.

---

# 20. Limite de l'offre gratuite Render

Le service utilise une instance gratuite Render.

Render peut mettre le service en veille après une période d'inactivité.

Conséquence :

* le premier chargement peut être plus lent ;
* le site peut mettre plusieurs secondes à se réveiller ;
* ce comportement n'est pas une erreur du projet Django.

Cette limite doit être connue lors d'une démonstration.

Si le site met du temps à répondre au premier chargement, il faut attendre le réveil du service.

---

# 21. Sécurité du déploiement

Les règles suivantes doivent être respectées :

* ne pas publier les vraies variables d'environnement ;
* ne pas publier la vraie clé secrète Django ;
* ne pas publier le mot de passe administrateur ;
* ne pas publier les identifiants du compte temporaire ;
* ne pas afficher les secrets dans les captures ;
* garder `DJANGO_DEBUG=False` en production ;
* vérifier que `ALLOWED_HOSTS` contient bien le domaine Render ;
* utiliser `.env.example` uniquement comme modèle.

Ces règles permettent de conserver une V1 présentable sans exposer d'informations sensibles.

---

# 22. Captures et preuves à préparer

Pour le dossier projet, les captures suivantes peuvent être utiles :

* page du service Render actif ;
* URL de production ;
* logs indiquant que le service est live ;
* Build Command ;
* Start Command ;
* variables d'environnement masquées ;
* fichier `build.sh` ;
* fichier `requirements.txt` ;
* site en ligne ;
* page d'accueil avec notes TinyDB ;
* page **Mes créations** ;
* page **Projets jouables** ;
* administration Django ;
* compte temporaire de lecture seule ;
* terminal avec `python manage.py check` ;
* terminal avec `python -m scripts.demo_tinydb_notes`.

Aucune capture ne doit afficher :

* mot de passe ;
* clé secrète ;
* vraie valeur de variable sensible ;
* identifiant privé inutile ;
* information personnelle inutile.

---

# 23. Commandes Git utilisées

Après création ou modification de ce fichier de documentation, les commandes Git suivantes peuvent être utilisées :

```bash
git add .
git commit -m "Update Render deployment journal"
git push
```

Avant le commit, vérifier l'état du dépôt avec :

```bash
git status
```

---

# 24. État final

Le projet Django **Frostia Games** est déployé sur Render.

Le site fonctionne en ligne.

L'administration Django est accessible.

La configuration Render est opérationnelle.

Les fichiers statiques sont chargés.

Les migrations Django sont appliquées.

La page d'accueil peut afficher les notes TinyDB.

Le compte temporaire de lecture seule peut être utilisé pour une consultation limitée de l'administration.

Cette étape valide une première mise en production fonctionnelle du projet.

La V1 reste volontairement limitée afin de rester stable, documentée, testable et présentable.

---

# 25. Conclusion

Le déploiement Render permet de montrer que Frostia Games fonctionne hors de l'environnement local.

La V1 est accessible en ligne, documentée et vérifiable.

Le projet utilise :

* Django ;
* SQLite ;
* TinyDB ;
* Gunicorn ;
* WhiteNoise ;
* Render ;
* des variables d'environnement ;
* un script de build.

Le déploiement ne transforme pas le projet en plateforme de production complète.

Il permet de présenter une V1 fonctionnelle, déployée et cohérente avec le périmètre du dossier projet.

La priorité après cette étape est de préparer les captures, les preuves et les annexes du dossier final.


