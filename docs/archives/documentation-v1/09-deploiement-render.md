# Journal de déploiement Render — Frostia Games

## Objectif du document

Ce document décrit la configuration réelle utilisée pour déployer **Frostia Games** sur Render.

Il sert à expliquer :

- comment le site est lancé en ligne ;
- comment les fichiers statiques et les migrations sont gérés ;
- comment les variables d'environnement sont utilisées ;
- pourquoi une commande d'initialisation automatique a été ajoutée ;
- comment l'accès d'évaluation en lecture seule est recréé sur la version en ligne ;
- quelles limites sont liées à l'utilisation de SQLite et TinyDB sur Render.

Ce fichier complète le journal de bord général. Il ne reprend pas tout l'historique du projet : il se concentre uniquement sur le déploiement et la configuration Render.

---

# 1. Plateforme utilisée

La V1 de Frostia Games est déployée sur Render.

Informations principales :

```text
Hébergeur : Render
Type de service : Web Service
Runtime : Python
Branche déployée : main
URL de production : https://frostia-games.onrender.com
```

Render permet d'obtenir une version accessible en ligne sans dépendre du serveur local de développement.

Docker reste documenté et utilisable comme environnement local de test, mais il n'est pas utilisé comme méthode de production dans cette V1.

---

# 2. Organisation du projet pour Render

Le fichier `manage.py` se trouve à la racine du dépôt.

Render peut donc lancer directement les commandes Django sans définir de dossier racine particulier.

Structure simplifiée utile au déploiement :

```text
frostia-games/
├── frostia_config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── views.py
│   ├── services/
│   │   └── nosql_notes.py
│   └── management/
│       └── commands/
│           └── setup_render_data.py
├── creations/
├── playable/
├── static/
├── templates/
├── build.sh
├── manage.py
└── requirements.txt
```

Le fichier `frostia_config/wsgi.py` est utilisé par Gunicorn pour lancer l'application Django en production.

---

# 3. Configuration Render actuelle

## Root Directory

Le champ **Root Directory** est laissé vide.

```text
Root Directory : vide
```

Cette configuration est correcte car `manage.py` est directement à la racine du projet.

---

## Build Command

La commande de build utilisée par Render est :

```bash
bash build.sh
```

Render exécute donc le fichier `build.sh` pendant la phase de construction.

---

## Start Command

La commande de démarrage utilisée est :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande fait trois choses dans l'ordre :

1. applique les migrations Django ;
2. recrée les données nécessaires à la démonstration ;
3. lance le serveur avec Gunicorn.

Cette configuration a été retenue pour éviter que la base en ligne reste vide après un redémarrage ou un redéploiement.

---

# 4. Rôle du fichier `build.sh`

Le fichier `build.sh` est exécuté par Render au moment du build.

Contenu utilisé :

```bash
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || true
```

Rôle des commandes :

- `pip install -r requirements.txt` installe les dépendances Python ;
- `collectstatic` prépare les fichiers statiques pour la production ;
- `migrate` applique les migrations Django ;
- `createsuperuser --noinput || true` tente de créer le compte administrateur sans faire échouer le déploiement si le compte existe déjà.

Le fichier `build.sh` ne doit pas contenir de mot de passe, de clé secrète ou d'identifiant sensible en clair.

---

# 5. Lancement avec Gunicorn

Render lance Django avec Gunicorn grâce à la partie suivante du Start Command :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Explication :

- `gunicorn` lance le serveur applicatif Python ;
- `frostia_config.wsgi:application` indique le point d'entrée WSGI de Django ;
- `--bind 0.0.0.0:$PORT` indique que le serveur doit écouter sur le port fourni automatiquement par Render.

Il ne faut pas utiliser un port fixe, car Render fournit lui-même la valeur de `$PORT`.

---

# 6. Variables d'environnement Render

Les variables d'environnement sont configurées dans Render, dans la section **Environment**.

Les valeurs sensibles ne sont pas écrites dans le code source.

Variables principales :

| Variable | Rôle |
| --- | --- |
| `DJANGO_DEBUG` | Désactive ou active le mode debug |
| `DJANGO_SECRET_KEY` | Clé secrète Django |
| `DJANGO_SUPERUSER_USERNAME` | Nom du compte administrateur |
| `DJANGO_SUPERUSER_EMAIL` | Email du compte administrateur |
| `DJANGO_SUPERUSER_PASSWORD` | Mot de passe du compte administrateur |
| `EVALUATION_USER_PASSWORD` | Mot de passe du compte d'évaluation en lecture seule |

La variable `EVALUATION_USER_PASSWORD` permet de créer ou mettre à jour le compte d'évaluation sans écrire le mot de passe dans le code source.

Les captures Render ne doivent pas afficher les vraies valeurs des variables sensibles.

---

# 7. Initialisation automatique des données Render

Une difficulté a été rencontrée sur Render : la base SQLite en ligne pouvait se retrouver vide après un redémarrage ou un redéploiement.

Les données créées manuellement depuis l'administration Django n'étaient donc pas une solution fiable pour la démonstration.

Pour corriger ce problème, une commande Django personnalisée a été ajoutée :

```bash
python manage.py setup_render_data
```

Fichier concerné :

```text
core/management/commands/setup_render_data.py
```

Cette commande recrée automatiquement :

- la création principale `Frostia Games` ;
- le projet jouable de démonstration `Prototype jouable à venir` ;
- le groupe `Evaluation lecture seule` ;
- le compte `evaluation_temp` ;
- les permissions de lecture seule nécessaires.

La commande est exécutée dans le Start Command Render, juste avant Gunicorn.

---

# 8. Accès d'évaluation en lecture seule

Le projet prévoit un compte d'évaluation limité.

Ce compte sert à permettre au jury de consulter l'administration Django sans obtenir un accès complet.

Configuration attendue :

```text
Utilisateur : evaluation_temp
Groupe : Evaluation lecture seule
Statut équipe : oui
Superutilisateur : non
```

Permissions accordées :

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

L'objectif est de montrer une logique de sécurité minimale : l'évaluateur peut consulter les données, mais ne peut pas administrer complètement le site.

Les identifiants exacts peuvent être transmis séparément si nécessaire, mais ils ne doivent pas apparaître dans les captures publiques ni dans un dossier public.

---

# 9. Base SQLite sur Render

La V1 utilise SQLite comme base relationnelle principale.

SQLite est suffisante pour une V1 de portfolio simple, mais elle présente une limite importante sur Render : elle ne doit pas être considérée comme une base persistante robuste pour une application de production complète.

Dans ce projet, cette limite est acceptée car :

- le volume de données est très faible ;
- le site sert de démonstration ;
- les données essentielles sont recréées automatiquement par `setup_render_data` ;
- une migration vers PostgreSQL reste prévue comme évolution possible.

Pour une version plus avancée, PostgreSQL serait plus adapté.

---

# 10. TinyDB sur Render

TinyDB est utilisé comme démonstration NoSQL légère.

Il ne remplace pas SQLite.

Il sert à présenter des notes de progression sous forme de documents JSON.

Fichiers concernés :

```text
core/services/nosql_notes.py
data/nosql/project_notes_db.json
scripts/demo_tinydb_notes.py
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

Sur Render, TinyDB ne doit pas être utilisé comme stockage critique.

La partie NoSQL est volontairement limitée à une démonstration documentaire.

---

# 11. Sécurisation de l'affichage des notes NoSQL

Pendant les tests Render, la page d'accueil a pu renvoyer une erreur si la partie TinyDB n'était pas disponible correctement.

Pour éviter qu'une erreur NoSQL fasse tomber la page d'accueil, l'affichage des notes a été sécurisé côté vue Django.

Principe retenu :

- tenter d'initialiser et de lire les notes TinyDB ;
- si TinyDB fonctionne, afficher les notes issues de TinyDB ;
- si TinyDB échoue ou retourne une liste vide, afficher des notes de secours ;
- ne pas bloquer l'affichage de la page d'accueil.

Cette décision permet de conserver une page d'accueil stable même si la démonstration NoSQL rencontre une limite liée à l'environnement Render.

---

# 12. Fichiers statiques

Les fichiers statiques sont collectés avec :

```bash
python manage.py collectstatic --noinput
```

WhiteNoise permet ensuite à Django de servir les fichiers statiques en production.

Fichiers concernés :

```text
static/css/main.css
static/js/menu.js
static/images/
```

Le fichier `static/js/menu.js` est utilisé pour le menu mobile responsive.

---

# 13. Dépendances utilisées

Le fichier `requirements.txt` contient les dépendances nécessaires au fonctionnement du projet sur Render.

Dépendances principales :

```text
Django
gunicorn
whitenoise
tinydb
```

Rôle des dépendances :

- `Django` fournit le framework web ;
- `gunicorn` lance l'application en production ;
- `whitenoise` sert les fichiers statiques ;
- `tinydb` permet la démonstration NoSQL légère.

---

# 14. Problèmes rencontrés pendant le déploiement

## Confusion entre Build Command et Start Command

Une confusion a eu lieu entre les variables d'environnement et les commandes Render.

Correction retenue :

```text
Build Command : bash build.sh
Start Command : python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

---

## Données Render vides

Les données créées manuellement dans l'administration Render pouvaient disparaître.

Correction retenue :

```bash
python manage.py setup_render_data
```

Cette commande est exécutée automatiquement au démarrage.

---

## Erreur 500 sur la page d'accueil

La page d'accueil a pu générer une erreur 500 lorsque la partie TinyDB posait problème sur Render.

Correction retenue :

- sécurisation de la récupération des notes ;
- ajout d'un comportement de secours ;
- maintien de l'affichage de la page même si TinyDB échoue.

---

## Absence de Shell Render

L'offre ou la configuration utilisée ne permettait pas d'utiliser directement un shell Render.

Correction retenue :

- ne pas dépendre du Shell Render ;
- passer par le Start Command ;
- utiliser les variables d'environnement Render.

---

# 15. Vérifications effectuées

Après correction, les éléments suivants ont été vérifiés :

- le service Render démarre ;
- les logs indiquent que `setup_render_data` s'exécute ;
- le site public est accessible ;
- l'administration Django est accessible ;
- la création `Frostia Games` est présente ;
- le projet jouable `Prototype jouable à venir` est présent ;
- le groupe `Evaluation lecture seule` est présent ;
- le compte `evaluation_temp` est présent ;
- le compte d'évaluation peut se connecter ;
- le compte d'évaluation possède uniquement des droits de lecture ;
- le compte n'est pas superutilisateur.

Logs attendus :

```text
Données initiales créées.
Accès d'évaluation configuré.
Utilisateur : evaluation_temp
Droits : lecture seule
Staff : oui
Superutilisateur : non
```

---

# 16. Captures de preuve

Les captures finales doivent montrer la version en ligne Render, et non le serveur local.

Captures utiles :

```text
docs/preuves/admin/capture-admin-evaluation-accueil-render.png
docs/preuves/admin/capture-admin-evaluation-creations-render.png
docs/preuves/admin/capture-admin-evaluation-projets-jouables-render.png
docs/preuves/admin/capture-admin-evaluation-compte-render.png
```

Autres captures utiles :

```text
docs/preuves/render/
docs/preuves/sql/
docs/preuves/nosql/
docs/preuves/test/
```

Aucune capture ne doit afficher :

- un mot de passe ;
- une clé secrète ;
- une valeur complète de variable d'environnement ;
- un token ;
- une information personnelle inutile.

---

# 17. Limites de l'offre Render gratuite

Le service Render utilisé peut se mettre en veille après une période d'inactivité.

Conséquences possibles :

- premier chargement plus lent ;
- délai avant que le site réponde ;
- redémarrage automatique du service ;
- nécessité de recréer certaines données si elles sont liées à SQLite.

La commande `setup_render_data` limite l'impact de ces redémarrages en recréant les données nécessaires à la démonstration.

---

# 18. Limites assumées du déploiement

Ce déploiement ne transforme pas Frostia Games en application de production complète.

Limites assumées :

- SQLite reste une solution simple pour la V1 ;
- TinyDB est utilisé comme démonstration NoSQL légère ;
- Render gratuit peut mettre le service en veille ;
- PostgreSQL n'est pas encore intégré ;
- l'administration Django reste l'administration standard ;
- aucun espace utilisateur public n'est prévu dans cette V1.

Ces limites sont cohérentes avec le périmètre du projet.

---

# 19. Commandes utiles

Commandes locales de vérification :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

Commandes Git après modification documentaire :

```powershell
git status
git add .
git commit -m "Mise a jour documentation deploiement Render"
git push origin main
```

---

# 20. Conclusion

La version Render de Frostia Games est maintenant fonctionnelle et vérifiable.

Le site public est accessible en ligne.

L'administration Django est accessible.

Les données nécessaires à la démonstration sont recréées automatiquement.

Le compte d'évaluation en lecture seule fonctionne sur la version en ligne.

Le déploiement reste volontairement simple, mais il prouve que la V1 peut fonctionner hors de l'environnement local.

Cette configuration est suffisante pour le dossier projet, tout en laissant des pistes d'évolution claires comme PostgreSQL, une persistance plus robuste et une administration plus avancée.
