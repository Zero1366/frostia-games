# Docker et lancement du projet - Frostia Games

## Objectif du document

Ce document explique comment lancer le projet **Frostia Games** en local et avec Docker.

L'objectif est de fournir une procédure claire permettant de reproduire l'environnement de développement, de tester le projet et de comprendre le rôle des fichiers liés au lancement.

La V1 du projet est prévue pour fonctionner en local. Un déploiement en ligne complet pourra être ajouté plus tard sur une plateforme compatible avec Django.

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
* Docker Compose.

Django est utilisé pour :

* les routes ;
* les vues ;
* les modèles ;
* les migrations ;
* l'administration ;
* les templates.

SQLite est utilisé comme base de données locale pour la V1.

Docker est ajouté afin de rendre le lancement plus reproductible et de montrer que le projet peut fonctionner dans un environnement isolé.

---

# 2. Lancement local avec l'environnement virtuel Python

## 2.1 Se placer à la racine du projet

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
```

---

## 2.2 Activer l'environnement virtuel

Depuis la racine du projet :

```powershell
.\.venv\Scripts\Activate.ps1
```

Si l'environnement virtuel est activé, le terminal affiche généralement :

```text
(.venv)
```

---

## 2.3 Installer les dépendances

Si les dépendances ne sont pas encore installées :

```powershell
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient les dépendances nécessaires au lancement du projet.

Pour la V1, il contient notamment :

```text
Django==6.0.6
```

---

## 2.4 Appliquer les migrations

Avant de lancer le serveur, appliquer les migrations :

```powershell
python manage.py migrate
```

Cette commande crée ou met à jour les tables nécessaires dans la base SQLite.

---

## 2.5 Vérifier le projet Django

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

## 2.6 Lancer le serveur local

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

# 3. Création d'un administrateur Django

Pour accéder à l'administration Django, un superutilisateur doit exister.

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

---

# 4. Lancement avec Docker

## 4.1 Objectif de Docker

Docker permet de lancer le projet dans un environnement isolé.

Cela permet :

* d'éviter les différences entre machines ;
* de lancer le projet sans dépendre directement de l'environnement Python local ;
* de documenter une procédure reproductible ;
* de montrer que le projet peut être préparé pour un déploiement plus sérieux.

Dans la V1, Docker sert surtout à reproduire l'environnement de développement.

Ce n'est pas encore une configuration de production.

---

## 4.2 Fichiers Docker utilisés

Les fichiers utilisés sont :

```text
Dockerfile
docker-compose.yml
.dockerignore
requirements.txt
```

---

# 5. Rôle du fichier Dockerfile

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
* `COPY requirements.txt /app/` : copie le fichier des dépendances.
* `RUN pip install` : installe Django et les dépendances nécessaires.
* `COPY . /app/` : copie le projet dans le conteneur.
* `EXPOSE 8000` : indique le port utilisé.
* `CMD` : lance le serveur Django.

---

# 6. Rôle du fichier docker-compose.yml

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

---

# 7. Rôle du fichier .dockerignore

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
* de garder une image Docker plus propre.

---

# 8. Construire et lancer le projet avec Docker

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

---

# 9. Arrêter Docker

Pour arrêter le serveur Docker :

```powershell
Ctrl + C
```

Pour arrêter et supprimer les conteneurs liés au projet :

```powershell
docker compose down
```

---

# 10. Vérifier Django dans Docker

Une fois le conteneur lancé, il est possible d'exécuter une commande Django dans Docker :

```powershell
docker compose exec web python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

---

# 11. Appliquer les migrations dans Docker

Si nécessaire :

```powershell
docker compose exec web python manage.py migrate
```

Cette commande applique les migrations depuis l'environnement Docker.

---

# 12. Problèmes rencontrés pendant la mise en place Docker

Plusieurs problèmes ont été rencontrés et corrigés :

* Docker Desktop n'était pas lancé ;
* une erreur de syntaxe était présente dans `docker-compose.yml` ;
* le fichier `requirements.txt` avait été mal référencé dans le `Dockerfile` ;
* le serveur Django devait être lancé dans le conteneur avant de tester la page ;
* il fallait reconstruire l'image après correction du fichier Docker.

Ces problèmes ont été corrigés progressivement.

---

# 13. Validation Docker

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

Le lancement Docker est donc considéré comme validé pour la V1.

---

# 14. Limites de la configuration Docker actuelle

La configuration Docker actuelle est adaptée au développement local.

Elle ne correspond pas encore à une configuration de production complète.

Elle ne contient pas encore :

* Gunicorn ;
* Nginx ;
* PostgreSQL ;
* gestion avancée des variables d'environnement ;
* HTTPS ;
* collecte complète des fichiers statiques pour production ;
* serveur de fichiers médias ;
* configuration de sécurité production.

Ces éléments pourront être ajoutés plus tard si le projet est déployé en ligne.

---

# 15. Déploiement futur envisagé

Pour une future mise en ligne, plusieurs pistes pourront être étudiées :

* Railway ;
* Render ;
* Fly.io ;
* serveur VPS ;
* autre plateforme compatible Django.

Une future configuration de production devra prévoir :

* `DEBUG=False` ;
* une vraie valeur pour `SECRET_KEY` stockée hors du code ;
* `ALLOWED_HOSTS` configuré ;
* une base PostgreSQL ;
* un serveur WSGI comme Gunicorn ;
* la gestion des fichiers statiques ;
* la gestion des fichiers médias ;
* HTTPS ;
* une stratégie de sauvegarde.

---

# 16. Commandes récapitulatives

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

## Arrêt Docker

```powershell
docker compose down
```

---

# 17. Conclusion

Le projet Frostia Games peut être lancé de deux manières :

* localement avec l'environnement virtuel Python ;
* avec Docker et Docker Compose.

Le lancement local permet de développer rapidement.

Le lancement Docker permet de reproduire plus facilement l'environnement du projet.

La configuration Docker actuelle est suffisante pour la V1 et pour une démonstration locale, mais elle devra être renforcée avant un vrai déploiement de production.
