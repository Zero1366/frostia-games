# Sécurité backend — Frostia Games

## Objectif du document

Ce document présente les choix de sécurité appliqués ou prévus dans la V1 du projet **Frostia Games**.

L'objectif est de montrer que le backend Django est conçu avec une attention particulière à la sécurité, même si le projet reste une V1 volontairement limitée.

La sécurité repose sur plusieurs principes :

- utiliser les protections intégrées de Django ;
- manipuler les données avec l'ORM Django ;
- éviter le SQL brut dans les vues ;
- protéger l'administration Django ;
- limiter les droits du compte d'évaluation ;
- ne pas exposer les secrets dans le code source ;
- utiliser les variables d'environnement Render ;
- éviter les captures contenant des mots de passe ou des clés ;
- limiter les fonctionnalités sensibles non maîtrisées ;
- documenter clairement les limites de la V1.

---

# 1. Contexte de sécurité

Frostia Games utilise Django pour gérer :

- les routes ;
- les vues ;
- les modèles ;
- l'administration ;
- la base de données SQLite ;
- les templates ;
- les fichiers statiques ;
- l'intégration NoSQL légère avec TinyDB.

Django fournit plusieurs protections intégrées.

La V1 s'appuie sur ces protections tout en évitant d'ajouter des fonctionnalités sensibles non nécessaires.

Le projet est actuellement :

- exécutable en local ;
- testable avec Docker ;
- déployé en ligne sur Render ;
- documenté avec un README et des fichiers Markdown ;
- renforcé avec une démonstration NoSQL légère ;
- protégé par un accès administrateur ;
- consultable avec un compte d'évaluation en lecture seule.

---

# 2. Utilisation de l'ORM Django

Le projet utilise l'ORM Django pour manipuler les données.

Exemple :

```python
Creation.objects.filter(is_visible=True).order_by(
    "alphabet_letter",
    "title",
)
```

L'ORM permet d'éviter d'écrire directement des requêtes SQL brutes dans les vues.

Cela réduit le risque d'injection SQL, car Django prépare les requêtes et encadre les valeurs utilisées dans les filtres.

Les modèles Django servent de couche intermédiaire entre le code Python et la base SQLite.

---

# 3. Absence de SQL brut dans les vues

Dans la V1, le projet n'utilise pas de requêtes SQL construites manuellement dans les vues.

Exemple de pratique évitée :

```python
cursor.execute("SELECT * FROM creations WHERE slug = '" + slug + "'")
```

Ce type de code est dangereux si une valeur utilisateur est intégrée directement dans la requête.

Le projet utilise plutôt les modèles Django :

```python
Creation.objects.filter(slug=slug)
```

Cette approche est plus sûre, plus lisible et mieux intégrée à Django.

---

# 4. Protection contre l'injection SQL

Le risque d'injection SQL est limité par plusieurs choix :

- utilisation des modèles Django ;
- utilisation de l'ORM ;
- absence de SQL brut dans les vues ;
- champs structurés dans les modèles ;
- routes contrôlées par Django ;
- absence de formulaire public manipulant directement la base dans la V1.

La base SQLite est manipulée par Django, pas directement par des chaînes SQL écrites dans les templates ou dans les vues.

Les fichiers SQL du projet sont documentaires.

Ils servent à expliquer la structure de la base, mais ne remplacent pas les migrations Django.

---

# 5. SQL natif documentaire

Le projet contient des fichiers SQL documentaires.

Ils permettent de montrer la structure de la base et de répondre aux attendus du dossier projet.

Fichiers concernés :

```text
doc/sql/schema.sql
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers présentent :

- des exemples `CREATE TABLE` ;
- des exemples `INSERT INTO` ;
- le lien entre les modèles Django et les tables SQLite ;
- la différence entre l'ORM Django et le SQL natif documentaire.

Ces fichiers ne doivent contenir aucun identifiant, mot de passe, secret ou donnée personnelle sensible.

---

# 6. Administration Django protégée

L'administration Django est accessible via :

```text
https://frostia-games.onrender.com/admin/
```

Elle est protégée par le système d'authentification Django.

Elle permet de gérer :

- les créations ;
- les projets jouables à venir ;
- les comptes autorisés ;
- les groupes et permissions.

L'accès administrateur complet doit rester privé.

Aucun identifiant administrateur ni mot de passe administrateur ne doit être publié dans :

- le code source ;
- le README ;
- les captures ;
- le dossier projet public ;
- les fichiers de documentation publics.

---

# 7. Compte administrateur

Un compte administrateur existe pour gérer le contenu du projet.

Sur Render, le superutilisateur peut être créé à partir de variables d'environnement.

Variables utilisées :

```text
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
```

Ces valeurs ne sont pas écrites directement dans le code.

Elles sont stockées dans les variables d'environnement Render.

Le compte administrateur complet ne doit pas être utilisé comme compte de démonstration pour le jury.

Pour une évaluation, un compte limité en lecture seule est préférable.

---

# 8. Accès d'évaluation en lecture seule

Un compte d'évaluation en lecture seule est prévu pour permettre au jury de consulter l'administration Django sans pouvoir modifier les données.

Configuration :

| Élément | Configuration |
| ------- | ------------- |
| Groupe | `Evaluation lecture seule` |
| Utilisateur | `evaluation_temp` |
| Type de compte | Staff Django |
| Superutilisateur | Non |
| Droits | Lecture seule |
| Ajout | Non |
| Modification | Non |
| Suppression | Non |

Le compte peut consulter uniquement :

- les créations ;
- les projets jouables.

Il ne doit pas permettre :

- d'ajouter des contenus ;
- de modifier des contenus ;
- de supprimer des contenus ;
- de modifier les utilisateurs ;
- de modifier les groupes ;
- de modifier les permissions ;
- de consulter des secrets ;
- d'accéder aux variables d'environnement.

---

# 9. Initialisation automatique de l'accès d'évaluation

Sur Render, la base SQLite peut être réinitialisée lors d'un redémarrage ou d'un redéploiement.

Pour éviter que les données de démonstration disparaissent, une commande Django personnalisée a été ajoutée :

```bash
python manage.py setup_render_data
```

Cette commande recrée automatiquement :

- la création principale **Frostia Games** ;
- le projet jouable de démonstration ;
- le groupe `Evaluation lecture seule` ;
- le compte `evaluation_temp` ;
- les permissions de lecture seule.

Le mot de passe du compte d'évaluation n'est pas stocké directement dans le code source.

Il est fourni par une variable d'environnement Render :

```text
EVALUATION_USER_PASSWORD
```

Cette approche évite de mettre le mot de passe dans `build.sh`, dans `settings.py` ou dans le code Python.

---

# 10. Permissions du compte d'évaluation

Les permissions accordées au compte d'évaluation sont limitées aux permissions `view`.

Permissions utilisées :

```text
Can view Création
Can view Projet jouable
```

Permissions non accordées :

```text
Can add
Can change
Can delete
```

Le compte d'évaluation peut donc consulter les éléments utiles sans pouvoir altérer les données.

---

# 11. Validation des mots de passe

Django conserve ses validateurs de mots de passe.

Ces validateurs permettent notamment :

- de refuser les mots de passe trop courts ;
- de refuser les mots de passe trop communs ;
- de refuser les mots de passe uniquement numériques ;
- de détecter les mots de passe trop proches des informations utilisateur.

Même dans une V1, ces règles permettent d'éviter des comptes trop faibles.

---

# 12. Protection CSRF

Django inclut une protection CSRF pour les formulaires.

Cette protection permet de limiter les attaques où un site externe tente de soumettre une action à la place d'un utilisateur connecté.

Dans la V1 actuelle, les formulaires publics ne sont pas encore développés.

L'administration Django bénéficie déjà des mécanismes de sécurité fournis par Django.

---

# 13. Échappement automatique dans les templates

Les templates Django échappent automatiquement les variables affichées dans les pages.

Exemple :

```django
{{ creation.title }}
```

Django évite que du HTML ou du JavaScript non souhaité soit exécuté directement dans le navigateur lorsque les variables sont affichées normalement.

Cela réduit le risque d'injection de code dans les pages.

Dans la V1, les données affichées publiquement proviennent principalement :

- des modèles Django `Creation` et `PlayableProject` ;
- des notes de progression TinyDB ;
- de contenus contrôlés dans le projet.

Aucun contenu libre saisi par des visiteurs n'est implanté dans cette V1.

---

# 14. Gestion de la visibilité des contenus

Les modèles utilisent des champs de visibilité.

Exemple :

```python
is_visible = models.BooleanField(default=True)
```

Les vues filtrent les contenus visibles :

```python
Creation.objects.filter(is_visible=True)
PlayableProject.objects.filter(is_visible=True)
```

Cela permet de garder un contenu dans l'administration sans forcément l'afficher sur le site public.

---

# 15. Sécurité de TinyDB

TinyDB est utilisé comme expérimentation NoSQL légère.

Il ne remplace pas SQLite.

Il sert uniquement à stocker et afficher des notes de progression liées au projet.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

La base TinyDB ne doit pas contenir :

- mot de passe ;
- clé secrète ;
- jeton d'accès ;
- variable d'environnement ;
- information personnelle sensible ;
- identifiant administrateur ;
- donnée confidentielle.

Les notes TinyDB sont des données documentaires.

Elles servent à démontrer une logique NoSQL simple dans le cadre du dossier projet.

---

# 16. Fonctionnement sécurisé de TinyDB dans la V1

La logique TinyDB est isolée dans un service Python :

```text
core/services/nosql_notes.py
```

Ce service permet :

- de créer le dossier de données si besoin ;
- d'ouvrir la base TinyDB ;
- de créer des notes de démonstration ;
- de lire les notes ;
- de rechercher les notes liées au projet ;
- de fermer la base après utilisation.

Le script suivant permet de tester TinyDB :

```powershell
python -m scripts.demo_tinydb_notes
```

TinyDB reste limité à un rôle documentaire.

Il n'est pas utilisé pour l'authentification, les permissions ou les secrets.

---

# 17. Upload réel non implanté dans la V1

La page **Projets jouables** contient une interface préparatoire.

Cependant, aucun vrai upload serveur n'est implanté dans la V1.

Cela signifie que :

- aucun fichier n'est envoyé au serveur ;
- aucun fichier n'est stocké côté backend ;
- aucun fichier utilisateur n'est exécuté ;
- aucune gestion de média uploadé n'est active ;
- aucun fichier exécutable n'est proposé en téléchargement public.

Ce choix est volontaire.

L'upload de fichiers est une fonctionnalité sensible qui demande des protections spécifiques.

---

# 18. Risques liés à un futur upload

Si un vrai upload est ajouté plus tard, il faudra prévoir :

- validation des extensions ;
- limitation de la taille des fichiers ;
- stockage dans un dossier sécurisé ;
- renommage des fichiers ;
- contrôle des types MIME ;
- interdiction d'exécuter les fichiers uploadés ;
- séparation entre fichiers publics et fichiers internes ;
- suppression sécurisée ;
- éventuellement scan antivirus ou contrôle externe.

Pour cette raison, l'upload réel est hors périmètre de la V1.

---

# 19. Configuration locale

En développement local, Django peut être lancé avec :

```powershell
python manage.py runserver
```

Le mode développement peut afficher des erreurs détaillées pour faciliter le débogage.

Ce comportement ne doit pas être utilisé tel quel en production.

Les vérifications principales en local sont :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
```

La première commande vérifie la configuration Django.

La seconde vérifie l'expérimentation TinyDB.

---

# 20. Configuration Render

Le projet est déployé sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Les informations sensibles sont stockées dans les variables d'environnement Render.

Variables principales :

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
EVALUATION_USER_PASSWORD
```

Les valeurs ne doivent pas être publiées dans le dépôt.

Les captures Render ne doivent pas afficher les vraies valeurs.

---

# 21. Mode DEBUG

En production, le mode debug doit être désactivé.

Sur Render, la variable utilisée est :

```text
DJANGO_DEBUG=False
```

Cela évite l'affichage d'informations techniques sensibles en cas d'erreur.

Le mode `DEBUG=True` doit rester réservé au développement local.

---

# 22. SECRET_KEY

La clé secrète Django ne doit pas être publiée dans GitHub.

Pour le déploiement, elle est placée dans une variable d'environnement :

```text
DJANGO_SECRET_KEY
```

Le fichier `.env.example` indique seulement la variable attendue :

```text
DJANGO_SECRET_KEY=change-me
```

Il ne contient pas la vraie clé.

---

# 23. ALLOWED_HOSTS

Django utilise `ALLOWED_HOSTS` pour limiter les domaines autorisés à servir l'application.

Pour la production Render, le domaine principal est :

```text
frostia-games.onrender.com
```

Des valeurs locales comme `localhost` ou `127.0.0.1` peuvent être conservées pour le développement local.

Cette présence dans `settings.py` n'est pas une fuite de secret.

Elle sert uniquement au fonctionnement en développement.

---

# 24. Fichier .env.example

Le fichier `.env.example` permet de documenter les variables nécessaires sans exposer les vraies valeurs.

Exemple :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
EVALUATION_USER_PASSWORD=change-me
```

Ce fichier peut être partagé car il ne contient pas les vraies valeurs.

Il sert uniquement de modèle.

---

# 25. Fichier .gitignore

Le fichier `.gitignore` permet d'éviter l'envoi de fichiers sensibles ou inutiles.

Il ignore notamment :

- `.env` ;
- `.env.local` ;
- `.venv/` ;
- `__pycache__/` ;
- `*.pyc` ;
- `db.sqlite3` ;
- `staticfiles/` ;
- `media/` ;
- fichiers temporaires de l'éditeur.

Attention : si un fichier était déjà suivi par Git avant d'être ajouté au `.gitignore`, il peut rester suivi.

Il faut alors vérifier avec :

```powershell
git status
```

---

# 26. Base SQLite

La V1 utilise SQLite comme base principale.

SQLite est adapté pour :

- le développement local ;
- les tests ;
- une V1 simple ;
- un projet de démonstration ;
- une base backend légère.

Sur Render gratuit, SQLite ne doit pas être considéré comme une persistance durable avancée.

Pour éviter une base vide après redéploiement, la commande `setup_render_data` recrée les données de démonstration.

Pour une version plus avancée, PostgreSQL pourra être envisagé.

---

# 27. Base NoSQL TinyDB

TinyDB est utilisé en complément de SQLite.

SQLite reste la base principale.

TinyDB sert uniquement à documenter et afficher des notes de progression.

Cette séparation permet de démontrer une compétence NoSQL sans complexifier fortement le backend.

TinyDB ne doit pas être utilisé pour :

- gérer les comptes ;
- gérer les mots de passe ;
- gérer les permissions ;
- stocker des secrets ;
- stocker des informations sensibles ;
- remplacer les modèles Django principaux.

---

# 28. Docker et sécurité

Docker est utilisé pour fournir un environnement local reproductible.

La configuration actuelle est volontairement simple.

Docker sert surtout à tester le projet dans un environnement isolé.

Dans cette V1, le déploiement en ligne est réalisé avec Render.

Pour une production Docker avancée, il faudrait prévoir :

- variables d'environnement Docker ;
- Gunicorn ;
- serveur frontal comme Nginx ;
- configuration HTTPS ;
- gestion sécurisée des fichiers statiques et médias ;
- base PostgreSQL séparée ;
- stratégie de sauvegarde.

---

# 29. Fichiers statiques et WhiteNoise

Le projet utilise des fichiers statiques pour :

- le CSS ;
- le JavaScript ;
- les images.

En production sur Render, WhiteNoise sert les fichiers statiques collectés.

La commande utilisée pendant le build est :

```powershell
python manage.py collectstatic --noinput
```

Le dossier `staticfiles/` ne doit pas être modifié manuellement.

---

# 30. JavaScript dynamique et sécurité

Le projet contient un fichier JavaScript pour le menu mobile :

```text
static/js/menu.js
```

Ce fichier sert à :

- ouvrir le menu mobile ;
- fermer le menu mobile ;
- mettre à jour `aria-expanded` ;
- fermer le menu après un clic sur un lien.

Ce JavaScript :

- ne manipule pas de donnée sensible ;
- ne communique pas avec une API ;
- ne transmet pas de donnée utilisateur au serveur.

Il reste limité à l'interface.

---

# 31. build.sh et sécurité du déploiement

Le fichier `build.sh` est utilisé par Render pendant la phase de build.

Il contient les actions de préparation :

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || true
```

Ce script permet :

- d'installer les dépendances ;
- de collecter les fichiers statiques ;
- d'appliquer les migrations ;
- de créer le superutilisateur si les variables Render sont disponibles.

Aucun secret ne doit être ajouté dans `build.sh`.

Les identifiants doivent rester dans les variables d'environnement Render.

La création du compte d'évaluation est gérée au démarrage par le Start Command Render avec :

```bash
python manage.py setup_render_data
```

---

# 32. Start Command Render sécurisé

Le Start Command actuel applique les migrations, initialise les données nécessaires et lance l'application :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande permet de sécuriser la disponibilité des données de démonstration sur Render.

Elle évite que l'administration se retrouve vide après redémarrage.

---

# 33. Sécurité non implantée dans la V1

La V1 ne contient pas encore :

- authentification utilisateur publique ;
- rôles publics avancés ;
- API REST ;
- vrai upload serveur ;
- permissions personnalisées avancées ;
- journalisation avancée ;
- limitation de requêtes ;
- PostgreSQL ;
- tests automatisés de sécurité ;
- administration personnalisée ;
- système de sauvegarde automatique ;
- scan antivirus pour fichiers uploadés ;
- séparation complète des paramètres de développement et de production.

Ces éléments ne sont pas oubliés.

Ils sont volontairement placés dans les évolutions futures afin de garder une V1 stable.

---

# 34. Bonnes pratiques appliquées

Les bonnes pratiques actuellement appliquées sont :

- utilisation du framework Django ;
- séparation entre modèles, vues et templates ;
- utilisation de l'ORM ;
- absence de SQL brut dans les vues ;
- SQL natif limité à la documentation ;
- administration protégée ;
- compte d'évaluation limité en lecture seule ;
- champs de visibilité ;
- validation des champs par les modèles ;
- configuration claire des fichiers statiques ;
- utilisation de variables d'environnement sur Render ;
- fichier `.env.example` sans valeur sensible ;
- fichier `.gitignore` pour exclure les fichiers sensibles ;
- documentation Docker ;
- documentation SQL ;
- documentation TinyDB ;
- documentation des limites de la V1 ;
- absence de fonctionnalité sensible non maîtrisée.

---

# 35. Évolutions de sécurité prévues

Les évolutions possibles sont :

1. Maintenir `SECRET_KEY` uniquement dans les variables d'environnement.
2. Maintenir `DEBUG=False` en production.
3. Vérifier régulièrement `ALLOWED_HOSTS`.
4. Sécuriser un futur système d'upload.
5. Ajouter des permissions plus fines dans l'administration.
6. Mettre en place PostgreSQL si le projet évolue.
7. Préparer une configuration de production plus avancée.
8. Ajouter une journalisation plus complète.
9. Séparer plus clairement les paramètres de développement et de production.
10. Ajouter des tests automatisés Django.
11. Ajouter des tests automatisés de sécurité.
12. Mettre en place un système de sauvegarde avant modification des contenus.
13. Encadrer plus strictement les données NoSQL si elles deviennent modifiables depuis une interface.

---

# 36. Captures et preuves à préparer

Pour le dossier projet, plusieurs preuves peuvent être préparées.

## Administration

- capture de l'administration Django ;
- capture du compte d'évaluation en lecture seule ;
- capture montrant uniquement les modèles accessibles au compte limité.

## Sécurité des secrets

- capture de `.env.example` sans vraie valeur ;
- capture de `.gitignore` ;
- capture de variables Render avec valeurs masquées.

## ORM et base de données

- extrait de code montrant l'utilisation de l'ORM ;
- capture du modèle `Creation` ;
- capture du modèle `PlayableProject` ;
- capture du SQL documentaire.

## TinyDB

- capture de `core/services/nosql_notes.py` ;
- capture de `scripts/demo_tinydb_notes.py` ;
- capture du terminal avec `python -m scripts.demo_tinydb_notes` ;
- capture de l'affichage des notes TinyDB sur l'accueil.

## Render

- capture du site en ligne ;
- capture de la configuration Render sans secret visible ;
- capture du déploiement actif ;
- capture des logs montrant `setup_render_data`.

Aucune capture ne doit afficher :

- mot de passe ;
- clé secrète ;
- jeton ;
- identifiant sensible ;
- variable contenant une vraie valeur privée.

---

# 37. Conclusion

La V1 de Frostia Games utilise les protections de base de Django et limite volontairement les fonctionnalités sensibles.

Le projet applique plusieurs règles importantes :

- données manipulées via l'ORM ;
- administration protégée ;
- compte d'évaluation en lecture seule ;
- pas de SQL brut dans les vues ;
- SQL natif limité à la documentation ;
- pas de vrai upload serveur ;
- templates avec échappement automatique ;
- secrets placés dans les variables d'environnement Render ;
- fichier `.env.example` sans valeurs sensibles ;
- fichier `.gitignore` pour éviter les envois accidentels ;
- TinyDB limité à des notes non sensibles ;
- Render configuré avec `DEBUG=False` ;
- données initiales Render recréées automatiquement par `setup_render_data`.

La V1 n'est pas une plateforme de production complète, mais elle est structurée, documentée, déployée et sécurisée de manière cohérente avec son périmètre.

Les protections avancées seront ajoutées plus tard si le projet évolue vers une version plus complète.
