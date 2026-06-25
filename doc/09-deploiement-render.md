# Journal de déploiement Render - Frostia Games

## Objectif

Déployer le projet Django **Frostia Games** sur Render afin d'obtenir une version accessible en ligne.

Ce déploiement permet de vérifier que le projet fonctionne hors de l'environnement local, avec une URL publique, une configuration serveur, les fichiers statiques, les migrations et l'accès à l'administration Django.

## Plateforme utilisée

* Hébergeur : Render
* Type de service : Web Service
* Environnement : Python 3
* Branche déployée : main
* Région : Frankfurt
* URL de production : https://frostia-games.onrender.com

## Structure du projet

Le projet Django possède une structure simple avec le fichier `manage.py` placé à la racine du dépôt GitHub.

Éléments importants du projet :

```txt
frostia-games/
├── frostia_config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── playable/
├── static/
├── staticfiles/
├── templates/
├── build.sh
├── manage.py
├── requirements.txt
└── db.sqlite3
```

Le dossier `frostia_config` contient la configuration principale du projet Django.

Le fichier `wsgi.py` est utilisé par Gunicorn pour lancer l'application Django en production.

## Configuration Render

Le champ **Root Directory** a été laissé vide, car le fichier `manage.py` se trouve directement à la racine du projet.

### Root Directory

```txt
vide
```

### Build Command

```bash
bash build.sh
```

### Start Command

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

## Explication du Start Command

La commande suivante permet de lancer le projet Django avec Gunicorn :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Explication :

* `gunicorn` lance le serveur Python utilisé en production.
* `frostia_config.wsgi:application` indique à Gunicorn où se trouve l'application Django.
* `--bind 0.0.0.0:$PORT` indique au serveur d'écouter sur le port fourni automatiquement par Render.

Cette configuration est importante car Render fournit lui-même le port à utiliser via la variable `$PORT`.

## Variables d'environnement Render

Les variables d'environnement ont été ajoutées dans Render, dans la section **Environment Variables**.

Les valeurs secrètes ne doivent pas être écrites directement dans la documentation du projet.

| Variable                    | Rôle                                     |
| --------------------------- | ---------------------------------------- |
| `DJANGO_DEBUG`              | Active ou désactive le mode debug Django |
| `DJANGO_SECRET_KEY`         | Clé secrète utilisée par Django          |
| `DJANGO_SUPERUSER_USERNAME` | Nom du compte administrateur Django      |
| `DJANGO_SUPERUSER_EMAIL`    | Adresse email du compte administrateur   |
| `DJANGO_SUPERUSER_PASSWORD` | Mot de passe du compte administrateur    |

Configuration utilisée :

```txt
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=valeur masquée pour sécurité
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=valeur masquée ou email personnel
DJANGO_SUPERUSER_PASSWORD=valeur masquée pour sécurité
```

Les variables sensibles comme `DJANGO_SECRET_KEY` et `DJANGO_SUPERUSER_PASSWORD` ne doivent jamais être publiées dans GitHub.

## Script de build

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

## Rôle du script de build

Le script effectue plusieurs actions automatiquement :

1. Installation des dépendances Python.
2. Collecte des fichiers statiques.
3. Application des migrations Django.
4. Tentative de création d'un superutilisateur.

La ligne suivante permet d'éviter que le déploiement échoue si le superutilisateur existe déjà :

```bash
python manage.py createsuperuser --noinput || true
```

## Dépendances nécessaires

Le fichier `requirements.txt` doit contenir les dépendances nécessaires au fonctionnement du projet Django sur Render.

Dépendances importantes :

```txt
Django
gunicorn
whitenoise
```

* `Django` permet de faire fonctionner le projet.
* `gunicorn` permet de lancer le projet en production.
* `whitenoise` permet de servir les fichiers statiques plus simplement en production.

## Problèmes rencontrés

### Confusion entre variables d'environnement et commandes Render

Une confusion a eu lieu entre la section **Environment Variables** et les commandes de déploiement.

Correction effectuée :

* Les variables Django doivent rester dans **Environment Variables**.
* La commande `bash build.sh` doit être placée dans **Build Command**.
* La commande Gunicorn doit être placée dans **Start Command**.

### Erreur locale avec PowerShell

Une erreur est apparue en local sous PowerShell avec la commande :

```bash
bash build.sh
```

Erreur rencontrée :

```txt
failed: No such file or directory
```

Cette erreur venait de l'environnement Windows local, car PowerShell ne gère pas Bash comme un environnement Linux standard.

Sur Render, cette commande fonctionne car le service tourne dans un environnement Linux.

## Résultat du déploiement

Le déploiement Render a réussi.

Message observé dans les logs Render :

```txt
Your service is live
```

Render indique également que l'application écoute correctement sur le port fourni :

```txt
Listening at: http://0.0.0.0:10000
```

Le site est accessible publiquement à l'adresse suivante :

```txt
https://frostia-games.onrender.com
```

## Vérifications effectuées

Les vérifications suivantes ont été réalisées après le déploiement :

* Page d'accueil accessible.
* CSS chargé correctement.
* Navigation fonctionnelle.
* Interface `/admin/` accessible.
* Connexion à l'administration Django fonctionnelle.
* Déploiement Render actif.
* Service indiqué comme live dans les logs Render.

## Limite de l'offre gratuite Render

Le service utilise une instance gratuite Render.

Render peut mettre le service en veille après une période d'inactivité.

Conséquence :

* Le premier chargement peut être plus lent.
* Le site peut mettre plusieurs secondes à se réveiller.
* Ce comportement n'est pas une erreur du projet Django.

## Commandes Git utilisées

Après création ou modification de ce fichier de documentation, les commandes Git suivantes peuvent être utilisées :

```bash
git add .
git commit -m "Add Render deployment journal"
git push
```

## État final

Le projet Django **Frostia Games** est maintenant déployé sur Render.

Le site fonctionne en ligne, l'administration Django est accessible, et la configuration Render est opérationnelle.

Cette étape valide une première mise en production fonctionnelle du projet.
