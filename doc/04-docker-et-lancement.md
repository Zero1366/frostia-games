# Docker et lancement du projet - Frostia Games

## Objectif du document

Ce document explique comment lancer le projet **Frostia Games** en local et avec Docker.

L'objectif est de fournir une procédure claire permettant :

* de lancer le projet en environnement local ;
* de reproduire l'environnement de développement avec Docker ;
* de tester le projet ;
* de comprendre le rôle des fichiers liés au lancement ;
* de distinguer le lancement local, le lancement Docker et le déploiement Render.

La V1 du projet peut être lancée localement avec Python, mais aussi avec Docker et Docker Compose.

Le projet est également déployé en ligne sur Render. Docker n'est donc pas utilisé comme solution de production dans cette V1, mais comme outil de développement, de test et de reproductibilité.

---

# 1. Technologies utilisées

Le projet utilise :

* Python ;
* Django ;
* SQLite ;
* HTML ;
* CSS ;
* JavaScript ;
* Docker ;
* Docker Compose ;
* Render pour le déploiement en ligne.

Django est utilisé pour :

* les routes ;
* les vues ;
* les modèles ;
* les migrations ;
* l'administration ;
* les templates.

SQLite est utilisé comme base de données pour la V1.

Docker est ajouté afin de rendre le lancement plus reproductible et de montrer que le projet peut fonctionner dans un environnement isolé.

Render est utilisé pour rendre le projet accessible en ligne.

---

# 2. Différence entre lancement local, Docker et Render

Le projet peut être exécuté de plusieurs manières.

| Méthode         | Rôle                                                       |
| --------------- | ---------------------------------------------------------- |
| Lancement local | Développement rapide avec l'environnement virtuel Python   |
| Docker          | Environnement reproductible et isolé pour tester le projet |
| Render          | Déploiement en ligne de la V1                              |

Docker ne remplace pas Render dans cette V1.

Docker sert surtout à prouver que le projet peut être lancé dans un environnement contrôlé, sans dépendre uniquement de la configuration locale de la machine.

---

# 3. Lancement local avec l'environnement virtuel Python

## 3.1 Se placer à la racine du projet

Depuis le terminal, se placer dans le dossier du projet :

```powershell
cd "D:\Apprentissage\Autre Projet\Frostia Games"
```

La racine du projet doit contenir notamment :

```text
manage.py
Dockerfile
docker-compose.yml
requirements.txt
build.sh
README.md
CHOIX_TECHNIQUES.md
```

---

## 3.2 Activer l'environnement virtuel

Depuis la racine du projet :

```powershell
.\.venv\Scripts\Activate.ps1
```

Si l'environnement virtuel est activé, le terminal affiche généralement :

```text
(.venv)
```

---

## 3.3 Installer les dépendances

Si les dépendances ne sont pas encore installées :

```powershell
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient les dépendances nécessaires au lancement du projet.

Il peut notamment contenir :

```text
Django
gunicorn
whitenoise
```

Django sert au fonctionnement principal du projet.

Gunicorn et WhiteNoise sont utilisés pour le déploiement en ligne sur Render.

---

## 3.4 Appliquer les migrations

Avant de lancer le serveur, appliquer les migrations :

```powershell
python manage.py migrate
```

Cette commande crée ou met à jour les tables nécessaires dans la base SQLite.

---

## 3.5 Vérifier le projet Django

Commande de vérification :

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

Cette commande permet de vérifier que la configuration Django ne contient pas d'erreur bloquante.

---

## 3.6 Lancer le serveur local

Commande :

```powershell
python manage.py runserver
```

Le site est ensuite accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

Pages principales :

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/mes-creations/
http://127.0.0.1:8000/projets-jouables/
```

Administration Django :

```text
http://127.0.0.1:8000/admin/
```

---

# 4. Création d'un administrateur Django local

Pour accéder à l'administration Django en local, un superutilisateur doit exister.

Commande :

```powershell
python manage.py createsuperuser
```

Django demande ensuite :

* un nom d'utilisateur ;
* une adresse e-mail ;
* un mot de passe ;
* une confirmation du mot de passe.

Une fois créé, l'administrateur peut se connecter à :

```text
http://127.0.0.1:8000/admin/
```

En production sur Render, la création du superutilisateur peut être automatisée avec des variables d'environnement et le script `build.sh`.

---

# 5. Lancement avec Docker

## 5.1 Objectif de Docker

Docker permet de lancer le projet dans un environnement isolé.

Cela permet :

* d'éviter les différences entre machines ;
* de lancer le projet sans dépendre directement de l'environnement Python local ;
* de documenter une procédure reproductible ;
* de tester le comportement du projet dans un conteneur ;
* de montrer que le projet peut être préparé pour des environnements plus structurés.

Dans la V1, Docker sert surtout à reproduire l'environnement de développement.

Ce n'est pas la solution de production utilisée pour la mise en ligne actuelle.

---

## 5.2 Fichiers Docker utilisés

Les fichiers utilisés sont :

```text
Dockerfile
docker-compose.yml
.dockerignore
requirements.txt
```

Ces fichiers se trouvent à la racine du projet.

---

# 6. Rôle du fichier Dockerfile

Le fichier `Dockerfile` décrit comment construire l'image Docker du projet.

Il utilise une image Python, installe les dépendances et lance le serveur Django.

Exemple de contenu :

```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Explication

* `FROM python:3.12-slim` : utilise une image Python légère.
* `WORKDIR /app` : définit le dossier de travail dans le conteneur.
* `ENV PYTHONDONTWRITEBYTECODE=1` : évite la création de fichiers `.pyc`.
* `ENV PYTHONUNBUFFERED=1` : améliore l'affichage des logs.
* `COPY requirements.txt /app/` : copie le fichier des dépendances.
* `RUN pip install` : installe Django et les dépendances nécessaires.
* `COPY . /app/` : copie le projet dans le conteneur.
* `EXPOSE 8000` : indique le port utilisé.
* `CMD` : lance le serveur Django.

Cette configuration est adaptée au développement local avec Docker.

---

# 7. Rôle du fichier docker-compose.yml

Le fichier `docker-compose.yml` permet de lancer le service web plus facilement.

Exemple de contenu :

```yaml
services:
  web:
    build: .
    container_name: frostia_games_web
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      DJANGO_DEBUG: "True"
```

## Explication

* `build: .` : construit l'image à partir du `Dockerfile`.
* `container_name` : donne un nom au conteneur.
* `command` : lance le serveur Django.
* `volumes` : synchronise le dossier local avec le conteneur.
* `ports` : rend le site accessible sur le port 8000.
* `environment` : définit une variable d'environnement pour le mode debug.

Le volume `.:/app` permet de modifier le code localement et de voir les changements dans le conteneur.

---

# 8. Rôle du fichier .dockerignore

Le fichier `.dockerignore` indique les fichiers à ne pas copier dans l'image Docker.

Exemple :

```text
.venv
__pycache__
*.pyc
*.pyo
*.pyd
.Python

db.sqlite3
media

.git
.gitignore

.vscode

node_modules
dist
build

.env
.env.local

*.log
```

## Explication

Ce fichier permet :

* d'éviter de copier l'environnement virtuel local ;
* d'éviter de copier les fichiers temporaires ;
* d'éviter de copier les fichiers de cache Python ;
* d'éviter de copier les fichiers sensibles ;
* d'éviter de copier le dossier Git ;
* de garder une image Docker plus propre.

Le fichier `.env` ne doit pas être copié dans l'image Docker car il peut contenir des valeurs sensibles.

---

# 9. Construire et lancer le projet avec Docker

Depuis la racine du projet :

```powershell
docker compose up --build
```

Cette commande :

* construit l'image Docker ;
* installe les dépendances ;
* crée le conteneur ;
* lance le serveur Django ;
* expose le site sur le port 8000.

Le site est ensuite accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

Pages à tester :

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/mes-creations/
http://127.0.0.1:8000/projets-jouables/
http://127.0.0.1:8000/admin/
```

---

# 10. Arrêter Docker

Pour arrêter le serveur Docker depuis le terminal :

```powershell
Ctrl + C
```

Pour arrêter et supprimer les conteneurs liés au projet :

```powershell
docker compose down
```

---

# 11. Vérifier Django dans Docker

Une fois le conteneur lancé, il est possible d'exécuter une commande Django dans Docker :

```powershell
docker compose exec web python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

Cette commande permet de vérifier que Django fonctionne correctement dans le conteneur.

---

# 12. Appliquer les migrations dans Docker

Si nécessaire :

```powershell
docker compose exec web python manage.py migrate
```

Cette commande applique les migrations depuis l'environnement Docker.

---

# 13. Créer un administrateur dans Docker

Si le projet est lancé avec Docker et qu'aucun administrateur n'existe encore :

```powershell
docker compose exec web python manage.py createsuperuser
```

Django demandera ensuite un nom d'utilisateur, une adresse e-mail et un mot de passe.

---

# 14. Problèmes rencontrés pendant la mise en place Docker

Plusieurs problèmes ont été rencontrés et corrigés :

* Docker Desktop n'était pas lancé ;
* une erreur de syntaxe était présente dans `docker-compose.yml` ;
* le fichier `requirements.txt` avait été mal référencé dans le `Dockerfile` ;
* le serveur Django devait être lancé dans le conteneur avant de tester la page ;
* il fallait reconstruire l'image après correction du fichier Docker ;
* certaines commandes devaient être exécutées depuis la racine du projet.

Ces problèmes ont été corrigés progressivement.

---

# 15. Validation Docker

La validation Docker a été faite avec la commande :

```powershell
docker compose up --build
```

Résultat obtenu :

* l'image est construite ;
* les dépendances sont installées ;
* le conteneur est lancé ;
* le serveur Django démarre ;
* le site est accessible sur `http://127.0.0.1:8000/`.

La validation Django peut ensuite être faite avec :

```powershell
docker compose exec web python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

Le lancement Docker est donc considéré comme validé pour la V1.

---

# 16. Limites de la configuration Docker actuelle

La configuration Docker actuelle est adaptée au développement local.

Elle ne correspond pas à une configuration Docker de production complète.

Elle ne contient pas encore :

* Nginx ;
* PostgreSQL dans un conteneur séparé ;
* gestion avancée des variables d'environnement Docker ;
* HTTPS ;
* serveur de fichiers médias ;
* orchestration avancée ;
* système de sauvegarde ;
* configuration Docker dédiée à la production.

Ces éléments sont volontairement reportés.

Dans cette V1, le déploiement en ligne est réalisé avec Render, sans utiliser Docker comme mode de production principal.

---

# 17. Déploiement Render

Le projet est déployé en ligne sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Render utilise une configuration différente de Docker.

Commande de build Render :

```bash
bash build.sh
```

Commande de démarrage Render :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Le fichier `build.sh` permet notamment :

* d'installer les dépendances ;
* de collecter les fichiers statiques ;
* d'appliquer les migrations ;
* de créer un superutilisateur si les variables d'environnement sont présentes.

Docker reste utile pour le développement local, mais Render est la solution retenue pour la mise en ligne actuelle.

---

# 18. Rôle du fichier build.sh

Le fichier `build.sh` est utilisé par Render pendant le déploiement.

Exemple de contenu :

```bash
#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true
```

## Explication

* `pip install -r requirements.txt` : installe les dépendances.
* `collectstatic` : collecte les fichiers statiques pour la production.
* `migrate` : applique les migrations.
* `createsuperuser --noinput || true` : tente de créer un superutilisateur automatiquement sans bloquer le déploiement si l'utilisateur existe déjà.

Ce fichier ne remplace pas Docker.

Il sert uniquement à préparer l'application lors du déploiement Render.

---

# 19. Variables d'environnement importantes

Le projet utilise des variables d'environnement pour éviter d'écrire les secrets directement dans le code.

Exemple documenté dans `.env.example` :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Ces variables sont configurées dans Render pour la production.

Le fichier `.env.example` sert uniquement de modèle.

Les vraies valeurs ne doivent pas être publiées sur GitHub.

---

# 20. Commandes récapitulatives

## Lancement local

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py check
python manage.py runserver
```

## Lancement Docker

```powershell
docker compose up --build
```

## Vérification Django dans Docker

```powershell
docker compose exec web python manage.py check
```

## Migrations dans Docker

```powershell
docker compose exec web python manage.py migrate
```

## Création d'un administrateur dans Docker

```powershell
docker compose exec web python manage.py createsuperuser
```

## Arrêt Docker

```powershell
docker compose down
```

## Commandes Git utiles

```powershell
git status
git add .
git commit -m "Update Docker documentation"
git push
```

---

# 21. Bilan

Le projet Frostia Games peut être lancé de trois manières selon le besoin :

* localement avec l'environnement virtuel Python ;
* avec Docker et Docker Compose ;
* en ligne via Render.

Le lancement local permet de développer rapidement.

Le lancement Docker permet de reproduire plus facilement l'environnement du projet.

Le déploiement Render permet de rendre la V1 accessible en ligne.

La configuration Docker actuelle est suffisante pour la V1 et pour une démonstration locale.

Elle n'est pas destinée à être une configuration Docker de production complète.

Les éléments avancés comme Nginx, PostgreSQL, HTTPS, serveur média ou orchestration Docker sont volontairement reportés afin de conserver une V1 stable, documentée et présentable.
