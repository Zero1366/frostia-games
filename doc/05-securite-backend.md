# Sécurité backend - Frostia Games

## Objectif du document

Ce document présente les choix de sécurité appliqués ou prévus dans la V1 du projet **Frostia Games**.

L'objectif est de montrer que le backend Django est conçu avec une attention particulière à la sécurité, même si le projet reste une V1 volontairement limitée.

La sécurité du projet repose sur plusieurs principes :

* utiliser les protections intégrées de Django ;
* éviter les requêtes SQL écrites manuellement ;
* protéger l'administration ;
* limiter les fonctionnalités sensibles ;
* ne pas exposer les secrets dans GitHub ;
* documenter les variables d'environnement ;
* distinguer clairement développement local et déploiement en ligne.

---

# 1. Contexte de sécurité

Frostia Games utilise Django pour gérer :

* les routes ;
* les vues ;
* les modèles ;
* l'administration ;
* la base de données ;
* les templates ;
* les fichiers statiques.

Django fournit plusieurs protections intégrées.

La V1 s'appuie sur ces protections tout en limitant volontairement les fonctionnalités sensibles.

L'objectif n'est pas de prétendre que le projet est une plateforme complète de production, mais de montrer que les risques principaux ont été identifiés et que les fonctionnalités sensibles sont encadrées ou reportées.

Le projet est actuellement :

* exécutable en local ;
* exécutable avec Docker ;
* déployé en ligne sur Render ;
* documenté avec un README, un fichier de choix techniques et un exemple de variables d'environnement.

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

Cela réduit le risque d'injection SQL, car Django prépare les requêtes et protège les valeurs utilisées dans les filtres.

---

# 3. Absence de SQL brut dans les vues

Dans la V1, le projet n'utilise pas de requêtes SQL construites manuellement avec des chaînes de caractères.

Exemple de pratique évitée :

```python
cursor.execute("SELECT * FROM creations WHERE slug = '" + slug + "'")
```

Ce type de code est dangereux si une valeur utilisateur est intégrée directement dans la requête.

Le projet utilise plutôt les modèles Django :

```python
Creation.objects.filter(slug=slug)
```

Cette approche permet de garder un code plus sûr, plus lisible et mieux intégré à Django.

---

# 4. Protection contre l'injection SQL

Le risque d'injection SQL est limité par plusieurs choix :

* utilisation des modèles Django ;
* utilisation de l'ORM ;
* absence de SQL brut dans les vues ;
* champs structurés dans les modèles ;
* routes contrôlées par Django ;
* absence de formulaire public manipulant directement la base dans la V1.

La base SQLite est manipulée par Django, pas directement par du SQL écrit dans les pages.

Le fichier `doc/sql/schema.sql` existe uniquement comme document explicatif.

Il ne remplace pas les migrations Django et n'est pas utilisé comme source principale de création des tables dans l'application.

---

# 5. Administration protégée

L'administration Django est accessible via :

```text
/admin/
```

Elle est protégée par le système d'authentification Django.

Seul un utilisateur administrateur peut :

* ajouter une création ;
* modifier une création ;
* ajouter un projet jouable ;
* modifier un projet jouable ;
* rendre un contenu visible ou invisible.

Dans la V1, l'administration sert à gérer les contenus sans modifier directement les templates HTML.

Aucun identifiant administrateur ni mot de passe ne doit être publié dans le dépôt GitHub ou dans la documentation publique.

---

# 6. Compte administrateur

Un compte administrateur existe pour gérer le contenu du projet.

En local, il peut être créé avec :

```powershell
python manage.py createsuperuser
```

Sur Render, la création du superutilisateur peut être automatisée avec le fichier `build.sh` et des variables d'environnement.

Variables utilisées :

```text
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
```

Ces valeurs ne doivent pas être écrites directement dans le code.

Elles doivent rester dans l'environnement local ou dans les variables d'environnement Render.

---

# 7. Validation des mots de passe

Le fichier `settings.py` conserve les validateurs de mots de passe Django.

Ces validateurs permettent notamment :

* la vérification de similarité avec les informations utilisateur ;
* l'imposition d'une longueur minimale ;
* la détection des mots de passe trop communs ;
* le refus des mots de passe uniquement numériques.

Ces règles renforcent la sécurité des comptes administrateurs.

Même pour une V1, il est préférable d'éviter les mots de passe trop simples.

---

# 8. Protection CSRF

Django inclut une protection CSRF pour les formulaires.

La protection CSRF permet de limiter les attaques où un site externe essaie de soumettre une requête à la place d'un utilisateur connecté.

Dans la V1 actuelle, les formulaires publics ne sont pas encore développés.

Cependant, la protection CSRF reste disponible dans la configuration Django pour les évolutions futures.

L'administration Django bénéficie déjà des mécanismes de sécurité fournis par Django.

---

# 9. Échappement automatique dans les templates

Les templates Django échappent automatiquement les variables affichées dans les pages.

Exemple :

```django
{{ creation.title }}
```

Django évite que du code HTML ou JavaScript non souhaité soit exécuté directement dans le navigateur lorsque les variables sont affichées normalement.

Cela réduit le risque d'injection de code dans les pages.

Dans la V1, les données affichées publiquement proviennent principalement des modèles Django `Creation` et `PlayableProject`.

---

# 10. Gestion de la visibilité des contenus

Les modèles utilisent des champs de visibilité :

```python
is_visible = models.BooleanField(default=True)
```

Ces champs permettent de masquer un contenu sans le supprimer de la base.

Les vues utilisent ce type de filtre :

```python
Creation.objects.filter(is_visible=True)
PlayableProject.objects.filter(is_visible=True)
```

Cela permet de contrôler ce qui est réellement affiché sur le site public.

Un contenu peut donc exister dans l'administration sans être visible par les visiteurs.

---

# 11. Upload réel non implanté dans la V1

La page **Projets jouables** contient une interface préparatoire permettant de sélectionner un fichier local.

Cependant, aucun vrai upload serveur n'est implanté dans la V1.

Cela signifie que :

* aucun fichier n'est envoyé au serveur ;
* aucun fichier n'est stocké côté backend ;
* aucun fichier utilisateur n'est exécuté ;
* aucune gestion de média uploadé n'est active ;
* aucun fichier exécutable n'est proposé en téléchargement public.

Ce choix est volontaire.

L'upload de fichiers est une fonctionnalité sensible qui demande des protections supplémentaires.

---

# 12. Risques liés à un futur upload

Si un vrai upload est ajouté plus tard, il faudra prévoir :

* validation des extensions ;
* limitation de la taille des fichiers ;
* stockage dans un dossier sécurisé ;
* renommage des fichiers ;
* contrôle des types MIME ;
* interdiction d'exécuter les fichiers uploadés ;
* séparation entre fichiers publics et fichiers internes ;
* suppression sécurisée ;
* éventuellement scan antivirus ou contrôle externe ;
* règles spécifiques pour les fichiers vidéo, images ou archives.

Pour cette raison, l'upload réel est placé hors périmètre de la V1.

Cela permet d'éviter d'ajouter une fonctionnalité sensible sans sécurité adaptée.

---

# 13. Configuration locale

En développement local, Django peut être lancé avec :

```powershell
python manage.py runserver
```

Le mode développement permet d'afficher des erreurs détaillées afin de faciliter le débogage.

Cependant, ce comportement ne doit pas être utilisé tel quel en production.

En local, il est acceptable d'utiliser une configuration plus permissive, mais les valeurs sensibles ne doivent pas être publiées dans GitHub.

---

# 14. Configuration Render

Le projet est déployé sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Sur Render, les informations sensibles sont stockées dans les variables d'environnement.

Variables principales :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=valeur-secrète
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=adresse-email
DJANGO_SUPERUSER_PASSWORD=mot-de-passe
```

Ces variables ne sont pas publiées dans le dépôt.

Le fichier `.env.example` sert uniquement de modèle.

---

# 15. Mode DEBUG

En production, le mode debug doit être désactivé.

Sur Render, la variable utilisée est :

```text
DJANGO_DEBUG=False
```

Cela permet d'éviter l'affichage d'informations techniques sensibles en cas d'erreur.

Le mode `DEBUG=True` doit rester réservé au développement local.

---

# 16. SECRET_KEY

La clé secrète Django ne doit pas être publiée dans GitHub.

Pour le déploiement, elle est placée dans une variable d'environnement :

```text
DJANGO_SECRET_KEY
```

Dans le code, elle peut être récupérée depuis l'environnement.

Exemple de principe :

```python
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
```

Le fichier `.env.example` indique seulement la variable attendue :

```text
DJANGO_SECRET_KEY=change-me
```

Il ne contient pas la vraie clé.

---

# 17. ALLOWED_HOSTS

Django utilise `ALLOWED_HOSTS` pour limiter les domaines autorisés à servir l'application.

Pour le projet Frostia Games, les hôtes nécessaires peuvent inclure :

```python
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "frostia-games.onrender.com",
]
```

Cette configuration permet d'éviter que l'application réponde à n'importe quel domaine.

Elle est importante pour le déploiement en ligne.

---

# 18. Fichier .env.example

Le fichier `.env.example` permet de documenter les variables nécessaires sans exposer les vraies valeurs.

Exemple :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

Ce fichier peut être partagé sur GitHub.

Il sert de modèle pour comprendre la configuration attendue.

Il ne doit contenir aucune vraie valeur sensible.

---

# 19. Fichier .gitignore

Le fichier `.gitignore` permet d'éviter l'envoi de fichiers sensibles ou inutiles dans GitHub.

Il ignore notamment :

* `.env` ;
* `.env.local` ;
* `.venv/` ;
* `__pycache__/` ;
* `*.pyc` ;
* `db.sqlite3` ;
* `staticfiles/` ;
* `media/` ;
* fichiers temporaires de l'éditeur.

Ce fichier participe à la sécurité du projet, car il évite l'envoi accidentel de secrets ou de fichiers locaux.

Attention : si un fichier était déjà suivi par Git avant d'être ajouté au `.gitignore`, il peut rester suivi. Dans ce cas, il faut vérifier avec `git status`.

---

# 20. Base de données

La V1 utilise SQLite.

SQLite est adapté pour :

* le développement local ;
* les tests ;
* une V1 simple ;
* un projet de démonstration ;
* une base backend légère.

Pour une version plus avancée, PostgreSQL pourra être envisagé.

Cela permettrait notamment :

* une meilleure adaptation à une production durable ;
* une meilleure gestion des accès concurrents ;
* une meilleure séparation entre code applicatif et données ;
* une base distante plus robuste.

Dans la V1 actuelle, SQLite reste un choix volontaire afin de conserver un projet simple et maîtrisable.

---

# 21. Docker et sécurité

Docker est utilisé pour fournir un environnement reproductible.

La configuration actuelle est volontairement simple :

* Python ;
* Django ;
* SQLite ;
* serveur de développement Django.

Elle ne remplace pas une configuration Docker de production complète.

Pour une production Docker avancée, il faudrait ajouter :

* variables d'environnement Docker ;
* serveur applicatif comme Gunicorn ;
* serveur frontal comme Nginx ;
* configuration HTTPS ;
* gestion sécurisée des fichiers statiques et médias ;
* configuration stricte des hôtes autorisés ;
* séparation claire entre développement et production ;
* base PostgreSQL séparée ;
* stratégie de sauvegarde.

Dans la V1 actuelle, Docker sert surtout à tester le projet dans un environnement isolé.

Le déploiement en ligne est réalisé avec Render.

---

# 22. Fichiers statiques et WhiteNoise

Le projet utilise des fichiers statiques pour le CSS, le JavaScript et les images.

En développement local, Django peut servir ces fichiers avec le serveur de développement.

En production sur Render, WhiteNoise permet de servir les fichiers statiques collectés.

La commande suivante est utilisée pendant le build :

```powershell
python manage.py collectstatic --noinput
```

Elle regroupe les fichiers statiques dans le dossier prévu pour la production.

Le dossier `staticfiles/` ne doit pas être modifié manuellement et peut être ignoré par Git.

---

# 23. build.sh et sécurité du déploiement

Le fichier `build.sh` est utilisé par Render pendant la phase de build.

Il contient notamment :

```bash
#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true
```

Ce script permet :

* d'installer les dépendances ;
* de collecter les fichiers statiques ;
* d'appliquer les migrations ;
* de créer un superutilisateur si les variables d'environnement sont présentes.

La création du superutilisateur repose sur les variables d'environnement Render.

Les identifiants ne sont donc pas écrits directement dans le script.

---

# 24. Sécurité non implantée dans la V1

La V1 ne contient pas encore :

* authentification utilisateur publique ;
* rôles avancés ;
* API REST ;
* vrai upload serveur ;
* permissions personnalisées ;
* journalisation avancée ;
* limitation de requêtes ;
* PostgreSQL ;
* tests automatisés de sécurité ;
* compte jury temporaire ;
* administration personnalisée ;
* système de sauvegarde automatique.

Ces éléments ne sont pas oubliés.

Ils sont volontairement placés dans les évolutions futures afin de garder une V1 stable.

---

# 25. Bonnes pratiques appliquées

Les bonnes pratiques actuellement appliquées sont :

* utilisation du framework Django ;
* séparation entre modèles, vues et templates ;
* utilisation de l'ORM ;
* absence de SQL brut ;
* administration protégée ;
* champs de visibilité ;
* validation des champs par les modèles ;
* configuration claire des fichiers statiques ;
* utilisation de variables d'environnement sur Render ;
* fichier `.env.example` sans valeur sensible ;
* fichier `.gitignore` pour exclure les fichiers sensibles ;
* documentation Docker ;
* documentation du schéma SQL ;
* documentation des limites de la V1 ;
* absence de fonctionnalité sensible non maîtrisée.

---

# 26. Évolutions de sécurité prévues

Les évolutions possibles sont :

1. Conserver `SECRET_KEY` uniquement dans les variables d'environnement.
2. Maintenir `DEBUG=False` en production.
3. Vérifier régulièrement `ALLOWED_HOSTS`.
4. Sécuriser un futur système d'upload.
5. Ajouter des permissions plus fines dans l'administration.
6. Mettre en place une base PostgreSQL si le projet évolue.
7. Préparer une configuration de production plus avancée.
8. Ajouter HTTPS via l'hébergeur.
9. Ajouter une journalisation plus complète.
10. Séparer clairement les paramètres de développement et de production.
11. Ajouter des tests automatisés Django.
12. Mettre en place un système de sauvegarde avant modification des contenus.

---

# 27. Lien avec les fichiers racine

La sécurité est aussi documentée par plusieurs fichiers à la racine du projet.

## `README.md`

Le README explique comment lancer le projet, quelles technologies sont utilisées et quelles limites sont assumées dans la V1.

## `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` explique les choix techniques, les technologies envisagées et les limites volontairement conservées.

## `.env.example`

Le fichier `.env.example` documente les variables d'environnement sans exposer les vraies valeurs.

## `.gitignore`

Le fichier `.gitignore` évite d'envoyer les fichiers sensibles ou inutiles dans GitHub.

Ces fichiers renforcent la lisibilité et la sécurité documentaire du projet.

---

# 28. Conclusion

La V1 de Frostia Games utilise les protections de base de Django et limite volontairement les fonctionnalités sensibles.

Le projet applique plusieurs règles importantes :

* données manipulées via l'ORM ;
* administration protégée ;
* pas de SQL brut ;
* pas de vrai upload serveur ;
* templates avec échappement automatique ;
* secrets placés dans les variables d'environnement Render ;
* fichier `.env.example` sans valeurs sensibles ;
* fichier `.gitignore` pour éviter les envois accidentels ;
* déploiement Render avec `DEBUG=False`.

La V1 n'est pas une plateforme de production complète, mais elle est structurée, documentée, déployée et sécurisée de manière cohérente avec son périmètre.

Les protections avancées seront ajoutées plus tard si le projet évolue vers une version plus complète.
