# Installation locale - Frostia Games

## Objectif du document

Ce document explique comment installer, configurer et lancer le projet **Frostia Games** en environnement local.

Il sert à garder une procédure claire pour :

* récupérer le projet ;
* installer les dépendances ;
* activer l’environnement virtuel Python ;
* appliquer les migrations Django ;
* tester TinyDB ;
* lancer le serveur local ;
* accéder aux pages principales ;
* accéder à l’administration Django ;
* vérifier que le projet fonctionne correctement ;
* préparer une démonstration locale.

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
* une expérimentation NoSQL avec TinyDB ;
* un affichage des notes TinyDB sur l’accueil ;
* des templates HTML ;
* des fichiers CSS et JavaScript ;
* une documentation technique ;
* une documentation de conception ;
* une documentation SQL ;
* une documentation NoSQL ;
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
│   ├── views.py
│   └── services/
│       └── nosql_notes.py
├── creations/
├── playable/
├── scripts/
│   ├── __init__.py
│   └── demo_tinydb_notes.py
├── data/
│   └── nosql/
│       └── project_notes_db.json
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
├── docs/
│   ├── backend/
│   ├── conception/
│   ├── frontend/
│   ├── nosql/
│   ├── preuves/
│   └── sql/
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
* les services internes ;
* les scripts de test ;
* les données NoSQL ;
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

ou :

```powershell
python -m pip install -r requirements.txt
```

Le fichier `requirements.txt` contient les bibliothèques nécessaires au fonctionnement du projet.

Il peut contenir notamment :

```text
Django
gunicorn
whitenoise
tinydb
```

Rôle des principales dépendances :

| Dépendance | Rôle                                         |
| ---------- | -------------------------------------------- |
| Django     | Framework principal du projet                |
| Gunicorn   | Serveur utilisé pour le déploiement Render   |
| WhiteNoise | Gestion des fichiers statiques en production |
| TinyDB     | Expérimentation NoSQL légère                 |

Même si Gunicorn et WhiteNoise sont surtout utiles pour Render, ils restent présents dans les dépendances du projet afin que l’environnement soit complet.

TinyDB est nécessaire pour tester les notes de progression NoSQL affichées sur la page d’accueil.

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

# 8. Vérifier TinyDB en local

Après l’installation des dépendances, vérifier que TinyDB fonctionne :

```powershell
python -m scripts.demo_tinydb_notes
```

Cette commande permet de vérifier que :

* TinyDB est installé ;
* le service `core/services/nosql_notes.py` fonctionne ;
* le fichier JSON peut être créé ou lu ;
* les notes de progression sont disponibles ;
* l’expérimentation NoSQL est testable depuis le terminal.

Résultat attendu :

```text
Preuve NoSQL TinyDB — Frostia Games
```

Le terminal doit ensuite afficher les notes de progression.

Ce test sert de preuve technique pour la partie NoSQL du dossier projet.

---

# 9. Appliquer les migrations

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

TinyDB ne dépend pas des migrations Django, car il utilise un fichier JSON.

---

# 10. Créer un administrateur local

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
https://frostia-games.onrender.com/admin/
```

Les identifiants administrateur ne doivent pas être publiés dans GitHub ou dans la documentation publique.

---

# 11. Compte temporaire de lecture seule

Un compte temporaire de lecture seule peut être utilisé pour l’évaluation.

Ce compte ne remplace pas le compte administrateur.

Il permet seulement de consulter certaines données dans l’administration Django.

Il peut voir :

* les créations ;
* les projets jouables.

Il ne doit pas voir :

* les utilisateurs ;
* les groupes ;
* les permissions sensibles ;
* les réglages internes ;
* les secrets du projet.

Les identifiants réels de ce compte ne doivent pas être écrits dans la documentation publique.

Ils peuvent être transmis séparément uniquement si nécessaire.

---

# 12. Lancer le serveur local

Pour lancer le serveur Django local :

```powershell
python manage.py runserver
```

Le site devient accessible à l’adresse :

```text
https://frostia-games.onrender.com/
```

Le terminal doit rester ouvert pendant que le serveur fonctionne.

Pour arrêter le serveur :

```text
Ctrl + C
```

---

# 13. Pages à tester en local

Après le lancement du serveur, tester les pages suivantes :

```text
https://frostia-games.onrender.com/
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
https://frostia-games.onrender.com/admin/
```

## Page d’accueil

Adresse :

```text
https://frostia-games.onrender.com/
```

Cette page présente le portfolio Frostia Games et les sections principales.

Elle affiche aussi les notes de progression provenant de TinyDB.

## Page Mes créations

Adresse :

```text
https://frostia-games.onrender.com/mes-creations/
```

Cette page affiche les créations visibles enregistrées dans la base SQLite.

## Page Projets jouables

Adresse :

```text
https://frostia-games.onrender.com/projets-jouables/
```

Cette page affiche les futurs projets jouables enregistrés dans la base SQLite.

Elle contient aussi une interface préparatoire de sélection de fichier local.

## Administration Django

Adresse :

```text
https://frostia-games.onrender.com/admin/
```

Cette interface permet d’ajouter ou modifier les contenus dynamiques du site.

---

# 14. Ajouter des données depuis l’administration

Une fois connecté à l’administration Django, il est possible de gérer les contenus du site.

## 14.1 Ajouter une création

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

## 14.2 Ajouter un projet jouable

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

# 15. Vérifier les données dynamiques SQLite

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

# 16. Vérifier les notes TinyDB

Les notes TinyDB sont affichées sur la page d’accueil.

La chaîne technique est la suivante :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

À vérifier :

* la commande `python -m scripts.demo_tinydb_notes` fonctionne ;
* la page d’accueil se charge ;
* les notes de progression apparaissent ;
* aucune erreur ne s’affiche dans le terminal ;
* le fichier `data/nosql/project_notes_db.json` ne contient pas de données sensibles.

TinyDB sert uniquement d’expérimentation NoSQL légère.

Il ne remplace pas SQLite.

---

# 17. Variables d’environnement locales

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

# 18. Fichier `.gitignore`

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

Le fichier TinyDB `data/nosql/project_notes_db.json` peut être conservé uniquement s’il contient des données de démonstration non sensibles.

---

# 19. Lancement local avec Docker

Le projet peut aussi être lancé localement avec Docker Compose.

Commande :

```powershell
docker compose up --build
```

Le site est ensuite accessible à l’adresse :

```text
https://frostia-games.onrender.com/
```

Commandes utiles dans Docker :

```powershell
docker compose exec web python manage.py check
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python -m scripts.demo_tinydb_notes
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

# 20. Différence avec le déploiement Render

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

# 21. Fichiers importants à la racine

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

Il doit contenir TinyDB depuis l’ajout de la partie NoSQL.

## `build.sh`

Script utilisé par Render pendant le déploiement.

## `Dockerfile` et `docker-compose.yml`

Permettent de lancer le projet avec Docker.

---

# 22. Fichiers complémentaires importants

Plusieurs fichiers complémentaires renforcent le dossier projet.

## Conception

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
```

## SQL

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

## NoSQL

```text
docs/nosql/tinydb-integration.md
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
```

## Frontend

```text
docs/frontend/javascript-menu-mobile.md
static/js/menu.js
```

## Backend

```text
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

Ces fichiers ne sont pas tous nécessaires au lancement local, mais ils sont importants pour comprendre et défendre le projet.

---

# 23. Vérifications avant démonstration locale

Avant une démonstration, effectuer les vérifications suivantes.

## 23.1 Vérifier Django

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

---

## 23.2 Vérifier TinyDB

```powershell
python -m scripts.demo_tinydb_notes
```

Le terminal doit afficher les notes de progression.

---

## 23.3 Lancer le serveur

```powershell
python manage.py runserver
```

---

## 23.4 Tester les pages

```text
https://frostia-games.onrender.com/
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
https://frostia-games.onrender.com/admin/
```

---

## 23.5 Vérifier les contenus

Vérifier que :

* la page d’accueil se charge ;
* les notes TinyDB apparaissent sur l’accueil ;
* le CSS est appliqué ;
* la navigation fonctionne ;
* le menu mobile fonctionne ;
* la page **Mes créations** affiche les contenus visibles ;
* la page **Projets jouables** affiche les contenus visibles ;
* l’administration Django est accessible ;
* le compte temporaire de lecture seule reste limité ;
* aucune erreur serveur n’apparaît.

---

# 24. Problèmes possibles

## 24.1 L’environnement virtuel ne s’active pas

Solution possible :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
```

---

## 24.2 Django n’est pas reconnu

Vérifier que l’environnement virtuel est activé.

Puis réinstaller les dépendances :

```powershell
pip install -r requirements.txt
```

---

## 24.3 TinyDB n’est pas reconnu

Vérifier que les dépendances sont installées.

Commande :

```powershell
pip install -r requirements.txt
```

Puis tester :

```powershell
python -m scripts.demo_tinydb_notes
```

Si l’erreur indique que le module `tinydb` est absent, vérifier que `tinydb` est bien présent dans `requirements.txt`.

---

## 24.4 Le script TinyDB ne se lance pas

Vérifier que les fichiers suivants existent :

```text
scripts/__init__.py
scripts/demo_tinydb_notes.py
core/services/nosql_notes.py
```

Puis relancer :

```powershell
python -m scripts.demo_tinydb_notes
```

La commande doit être lancée depuis la racine du projet.

---

## 24.5 Les tables n’existent pas

Appliquer les migrations :

```powershell
python manage.py migrate
```

---

## 24.6 L’administration n’est pas accessible

Vérifier que le serveur est lancé.

Puis créer un superutilisateur si nécessaire :

```powershell
python manage.py createsuperuser
```

---

## 24.7 Les styles CSS ne s’affichent pas

Vérifier :

* que le dossier `static/` existe ;
* que `static/css/main.css` existe ;
* que les fichiers statiques sont bien configurés dans `settings.py` ;
* que le serveur a été relancé après modification.

---

## 24.8 Le JavaScript du menu mobile ne fonctionne pas

Vérifier :

* que `static/js/menu.js` existe ;
* que `templates/base.html` charge bien le fichier JavaScript ;
* que le script est chargé avec `defer` ;
* que les attributs `data-menu-button` et `data-sidebar` existent dans le template ;
* que le serveur a été relancé ou que la page a été rechargée.

---

## 24.9 Le port 8000 est déjà utilisé

Lancer Django sur un autre port :

```powershell
python manage.py runserver 8001
```

Puis ouvrir :

```text
https://frostia-games.onrender.com/
```

---

# 25. Commandes récapitulatives

## Installation locale complète

```powershell
cd "D:\Apprentissage\Autre Projet\Frostia Games"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py check
python -m scripts.demo_tinydb_notes
python manage.py runserver
```

---

## Relancer le projet plus tard

```powershell
cd "D:\Apprentissage\Autre Projet\Frostia Games"
.\.venv\Scripts\Activate.ps1
python manage.py check
python -m scripts.demo_tinydb_notes
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

## Tests Docker utiles

```powershell
docker compose exec web python manage.py check
docker compose exec web python -m scripts.demo_tinydb_notes
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

# 26. Captures utiles pour le dossier projet

Pour le dossier projet, il peut être utile de préparer des captures de :

* l’environnement virtuel activé ;
* `pip install -r requirements.txt` si nécessaire ;
* `python manage.py check` ;
* `python -m scripts.demo_tinydb_notes` ;
* `python manage.py runserver` ;
* la page d’accueil locale ;
* les notes TinyDB affichées sur l’accueil ;
* la page **Mes créations** ;
* la page **Projets jouables** ;
* l’administration Django ;
* le compte temporaire de lecture seule ;
* le fichier `requirements.txt` ;
* le fichier `core/services/nosql_notes.py` ;
* le fichier `scripts/demo_tinydb_notes.py`.

Aucune capture ne doit afficher :

* mot de passe ;
* clé secrète ;
* vraie variable sensible ;
* identifiant privé inutile ;
* information personnelle inutile.

---

# 27. Conclusion

L’installation locale de Frostia Games permet de lancer et tester le projet Django sur une machine de développement.

Le projet peut être utilisé :

* en local avec l’environnement virtuel Python ;
* avec Docker ;
* en ligne via Render.

Pour la V1, l’installation locale est suffisante pour tester :

* les pages ;
* l’administration Django ;
* les modèles ;
* la base SQLite ;
* l’affichage dynamique ;
* le menu mobile ;
* TinyDB ;
* les notes de progression sur l’accueil.

Le projet reste volontairement simple afin de conserver une base stable, documentée et maintenable.

À ce stade, l’objectif n’est plus d’ajouter de nouvelles fonctionnalités lourdes, mais de finaliser les preuves, les captures et le dossier projet final.



