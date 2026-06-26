# Installation locale - Frostia Games

## Objectif du document

Ce document explique comment installer, configurer et lancer le projet **Frostia Games** en environnement local.

Il sert à garder une procédure claire pour :

* récupérer le projet ;
* installer les dépendances ;
* activer l’environnement virtuel Python ;
* appliquer les migrations Django ;
* lancer le serveur local ;
* accéder aux pages principales ;
* accéder à l’administration Django ;
* vérifier que le projet fonctionne correctement.

Ce document concerne principalement le lancement local du projet.

Le projet dispose aussi d’un lancement avec Docker et d’un déploiement en ligne sur Render, documentés dans d’autres fichiers.

---

# 1. Présentation rapide du projet

**Frostia Games** est un portfolio développé avec Django.

La V1 du projet contient :

* une page d’accueil ;
* une page **Mes créations** ;
* une page **Projets jouables** ;
* une administration Django ;
* une base SQLite ;
* des modèles Django ;
* des templates HTML ;
* des fichiers CSS et JavaScript ;
* une documentation technique ;
* un déploiement Render.

L’installation locale permet de tester le projet sur la machine de développement avant de le publier ou de le présenter.

---

# 2. Prérequis

Avant de lancer le projet, les outils suivants doivent être installés :

* Python ;
* pip ;
* Git ;
* Visual Studio Code ou un autre éditeur ;
* PowerShell sous Windows ;
* Docker Desktop, uniquement si le lancement Docker est utilisé.

Pour le lancement local classique, Docker n’est pas obligatoire.

---

# 3. Se placer dans le dossier du projet

Depuis PowerShell, se placer à la racine du projet.

Exemple :

```powershell
cd "D:\Apprentissage\Autre Projet\Frostia Games"
```

La racine du projet doit contenir notamment :

```text
manage.py
requirements.txt
README.md
CHOIX_TECHNIQUES.md
Dockerfile
docker-compose.yml
build.sh
```

Le fichier `manage.py` doit être présent à la racine.

C’est lui qui permet de lancer les commandes Django.

---

# 4. Structure attendue du projet

La structure générale du projet est la suivante :

```text
frostia-games/
├── frostia_config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
├── creations/
├── playable/
├── templates/
│   ├── base.html
│   └── pages/
│       ├── home.html
│       ├── creation.html
│       └── projet_jouable.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── doc/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── build.sh
├── README.md
├── CHOIX_TECHNIQUES.md
├── .env.example
└── .gitignore
```

Cette organisation permet de séparer :

* la configuration Django ;
* les applications ;
* les templates ;
* les fichiers statiques ;
* la documentation ;
* les fichiers de lancement ;
* les fichiers de déploiement.

---

# 5. Créer ou utiliser l’environnement virtuel

Le projet utilise un environnement virtuel Python nommé :

```text
.venv
```

## 5.1 Créer l’environnement virtuel

Si l’environnement virtuel n’existe pas encore :

```powershell
python -m venv .venv
```

Cette commande crée un dossier `.venv` à la racine du projet.

---

## 5.2 Activer l’environnement virtuel

Sous Windows avec PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Lorsque l’environnement virtuel est activé, le terminal affiche généralement :

```text
(.venv)
```

Cela signifie que les commandes Python et pip utilisent l’environnement du projet.

---

## 5.3 Problème possible avec PowerShell

Si PowerShell bloque l’activation de l’environnement virtuel, il peut afficher une erreur liée à la politique d’exécution.

Dans ce cas, la commande suivante peut être utilisée pour la session actuelle :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Puis relancer :

```powershell
.\.venv\Scripts\Activate.ps1
```

Cette modification s’applique uniquement à la session PowerShell en cours.

---

# 6. Installer les dépendances

Une fois l’environnement virtuel activé, installer les dépendances du projet :

```powershell
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient les bibliothèques nécessaires au fonctionnement du projet.

Il peut contenir notamment :

```text
Django
gunicorn
whitenoise
```

Rôle des principales dépendances :

| Dépendance | Rôle                                         |
| ---------- | -------------------------------------------- |
| Django     | Framework principal du projet                |
| Gunicorn   | Serveur utilisé pour le déploiement Render   |
| WhiteNoise | Gestion des fichiers statiques en production |

Même si Gunicorn et WhiteNoise sont surtout utiles pour Render, ils restent présents dans les dépendances du projet afin que l’environnement soit complet.

---

# 7. Vérifier l’installation Django

Après l’installation des dépendances, vérifier que Django fonctionne :

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

Cette commande permet de vérifier que la configuration Django ne contient pas d’erreur bloquante.

Elle doit être utilisée régulièrement après une modification importante.

---

# 8. Appliquer les migrations

La base de données locale utilise SQLite.

Avant de lancer le serveur, appliquer les migrations :

```powershell
python manage.py migrate
```

Cette commande crée ou met à jour les tables nécessaires dans la base locale.

Les migrations concernent notamment :

* les tables internes de Django ;
* le modèle `Creation` ;
* le modèle `PlayableProject` ;
* les tables nécessaires à l’administration Django.

---

# 9. Créer un administrateur local

Pour accéder à l’administration Django en local, un superutilisateur doit exister.

Commande :

```powershell
python manage.py createsuperuser
```

Django demande ensuite :

* un nom d’utilisateur ;
* une adresse e-mail ;
* un mot de passe ;
* une confirmation du mot de passe.

Après création, l’administrateur peut se connecter à l’adresse :

```text
http://127.0.0.1:8000/admin/
```

Les identifiants administrateur ne doivent pas être publiés dans GitHub ou dans la documentation publique.

---

# 10. Lancer le serveur local

Pour lancer le serveur Django local :

```powershell
python manage.py runserver
```

Le site devient accessible à l’adresse :

```text
http://127.0.0.1:8000/
```

Le terminal doit rester ouvert pendant que le serveur fonctionne.

Pour arrêter le serveur :

```text
Ctrl + C
```

---

# 11. Pages à tester en local

Après le lancement du serveur, tester les pages suivantes :

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/mes-creations/
http://127.0.0.1:8000/projets-jouables/
http://127.0.0.1:8000/admin/
```

## Page d’accueil

Adresse :

```text
http://127.0.0.1:8000/
```

Cette page présente le portfolio Frostia Games et les sections principales.

## Page Mes créations

Adresse :

```text
http://127.0.0.1:8000/mes-creations/
```

Cette page affiche les créations visibles enregistrées dans la base.

## Page Projets jouables

Adresse :

```text
http://127.0.0.1:8000/projets-jouables/
```

Cette page affiche les futurs projets jouables enregistrés dans la base.

Elle contient aussi une interface préparatoire de sélection de fichier local.

## Administration Django

Adresse :

```text
http://127.0.0.1:8000/admin/
```

Cette interface permet d’ajouter ou modifier les contenus dynamiques du site.

---

# 12. Ajouter des données depuis l’administration

Une fois connecté à l’administration Django, il est possible de gérer les contenus du site.

## 12.1 Ajouter une création

Dans l’administration :

1. Aller dans **Créations**.
2. Cliquer sur **Ajouter une création**.
3. Remplir les champs.
4. Cocher la visibilité si le contenu doit apparaître sur le site.
5. Enregistrer.

Exemple :

```text
Titre : KryonCore
Identifiant URL : kryoncore
Lettre alphabétique : K
Nom de code : KryonCore
Type de projet : Jeu vidéo PC
Statut : En préparation
Visible sur le site : Oui
```

La création peut ensuite apparaître sur la page **Mes créations**.

---

## 12.2 Ajouter un projet jouable

Dans l’administration :

1. Aller dans **Projets jouables**.
2. Cliquer sur **Ajouter un projet jouable**.
3. Remplir les champs.
4. Définir le statut et le message de disponibilité.
5. Cocher la visibilité si le contenu doit apparaître sur le site.
6. Enregistrer.

Exemple :

```text
Titre : Prototype jouable à venir
Identifiant URL : prototype-jouable-a-venir
Statut : Non disponible
Type prévu : Démonstration / teaser
Disponible : Non
Visible sur le site : Oui
```

Le projet peut ensuite apparaître sur la page **Projets jouables**.

---

# 13. Vérifier les données dynamiques

Les données affichées dans les pages publiques proviennent de la base SQLite.

Exemples de récupération dans les vues Django :

```python
Creation.objects.filter(is_visible=True)
```

```python
PlayableProject.objects.filter(is_visible=True)
```

Cela signifie qu’un contenu peut exister dans l’administration mais ne pas apparaître sur le site si son champ de visibilité est désactivé.

À vérifier :

* les créations visibles apparaissent sur la page **Mes créations** ;
* les projets jouables visibles apparaissent sur la page **Projets jouables** ;
* les contenus masqués ne s’affichent pas côté public.

---

# 14. Variables d’environnement locales

Le fichier `.env.example` sert de modèle pour documenter les variables attendues.

Exemple :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Ce fichier ne doit contenir aucune vraie valeur sensible.

Pour le développement local, les vraies valeurs peuvent être définies selon la configuration du projet.

Les variables sensibles ne doivent pas être envoyées dans GitHub.

Le fichier `.gitignore` doit donc ignorer :

```text
.env
.env.local
```

---

# 15. Fichier `.gitignore`

Le fichier `.gitignore` permet d’éviter l’envoi de fichiers inutiles ou sensibles.

Il peut ignorer notamment :

```text
.venv/
__pycache__/
*.pyc
db.sqlite3
staticfiles/
media/

.env
.env.local

.vscode/
.DS_Store
Thumbs.db
```

Rôle principal :

* ne pas envoyer l’environnement virtuel ;
* ne pas envoyer les caches Python ;
* ne pas envoyer les fichiers locaux sensibles ;
* ne pas envoyer les fichiers générés ;
* protéger les variables d’environnement.

Attention : si un fichier était déjà suivi par Git avant son ajout dans `.gitignore`, il peut rester suivi.

Il faut vérifier avec :

```powershell
git status
```

---

# 16. Lancement local avec Docker

Le projet peut aussi être lancé localement avec Docker Compose.

Commande :

```powershell
docker compose up --build
```

Le site est ensuite accessible à l’adresse :

```text
http://127.0.0.1:8000/
```

Commandes utiles dans Docker :

```powershell
docker compose exec web python manage.py check
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Arrêter Docker :

```powershell
docker compose down
```

Le lancement Docker est détaillé dans le fichier :

```text
04-docker-et-lancement.md
```

---

# 17. Différence avec le déploiement Render

Le lancement local sert à développer et tester le projet sur la machine.

Le déploiement Render sert à rendre le projet accessible en ligne.

URL de production :

```text
https://frostia-games.onrender.com
```

Render utilise :

```bash
bash build.sh
```

comme commande de build, puis :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

comme commande de démarrage.

Le déploiement Render est détaillé dans le fichier :

```text
09-deploiement-render.md
```

---

# 18. Fichiers importants à la racine

Plusieurs fichiers situés à la racine du projet sont importants pour l’installation ou la compréhension du projet.

## `README.md`

Présente rapidement :

* le projet ;
* les technologies utilisées ;
* l’installation locale ;
* le lancement Docker ;
* le déploiement Render ;
* les limites de la V1.

## `CHOIX_TECHNIQUES.md`

Explique :

* les choix techniques ;
* pourquoi Django a été retenu ;
* pourquoi certaines pistes ont été reportées ;
* pourquoi le périmètre est volontairement limité.

## `.env.example`

Documente les variables d’environnement nécessaires sans exposer les vraies valeurs sensibles.

## `requirements.txt`

Liste les dépendances Python du projet.

## `build.sh`

Script utilisé par Render pendant le déploiement.

## `Dockerfile` et `docker-compose.yml`

Permettent de lancer le projet avec Docker.

---

# 19. Vérifications avant démonstration locale

Avant une démonstration, effectuer les vérifications suivantes.

## 19.1 Vérifier Django

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

---

## 19.2 Lancer le serveur

```powershell
python manage.py runserver
```

---

## 19.3 Tester les pages

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/mes-creations/
http://127.0.0.1:8000/projets-jouables/
http://127.0.0.1:8000/admin/
```

---

## 19.4 Vérifier les contenus

Vérifier que :

* la page d’accueil se charge ;
* le CSS est appliqué ;
* la navigation fonctionne ;
* la page **Mes créations** affiche les contenus visibles ;
* la page **Projets jouables** affiche les contenus visibles ;
* l’administration Django est accessible ;
* aucune erreur serveur n’apparaît.

---

# 20. Problèmes possibles

## 20.1 L’environnement virtuel ne s’active pas

Solution possible :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
```

---

## 20.2 Django n’est pas reconnu

Vérifier que l’environnement virtuel est activé.

Puis réinstaller les dépendances :

```powershell
pip install -r requirements.txt
```

---

## 20.3 Les tables n’existent pas

Appliquer les migrations :

```powershell
python manage.py migrate
```

---

## 20.4 L’administration n’est pas accessible

Vérifier que le serveur est lancé.

Puis créer un superutilisateur si nécessaire :

```powershell
python manage.py createsuperuser
```

---

## 20.5 Les styles CSS ne s’affichent pas

Vérifier :

* que le dossier `static/` existe ;
* que `static/css/main.css` existe ;
* que les fichiers statiques sont bien configurés dans `settings.py` ;
* que le serveur a été relancé après modification.

---

## 20.6 Le port 8000 est déjà utilisé

Lancer Django sur un autre port :

```powershell
python manage.py runserver 8001
```

Puis ouvrir :

```text
http://127.0.0.1:8001/
```

---

# 21. Commandes récapitulatives

## Installation locale complète

```powershell
cd "D:\Apprentissage\Autre Projet\Frostia Games"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py check
python manage.py runserver
```

---

## Relancer le projet plus tard

```powershell
cd "D:\Apprentissage\Autre Projet\Frostia Games"
.\.venv\Scripts\Activate.ps1
python manage.py check
python manage.py runserver
```

---

## Créer un administrateur

```powershell
python manage.py createsuperuser
```

---

## Lancement Docker

```powershell
docker compose up --build
```

---

## Git après modification

```powershell
git status
git add .
git commit -m "Update local installation documentation"
git push
```

---

# 22. Conclusion

L’installation locale de Frostia Games permet de lancer et tester le projet Django sur une machine de développement.

Le projet peut être utilisé :

* en local avec l’environnement virtuel Python ;
* avec Docker ;
* en ligne via Render.

Pour la V1, l’installation locale est suffisante pour tester les pages, l’administration Django, les modèles, la base SQLite et l’affichage dynamique.

Le projet reste volontairement simple afin de conserver une base stable, documentée et maintenable.
