# Captures et preuves - Frostia Games

## Objectif du document

Ce document liste les captures d'écran et preuves à conserver pour le projet **Frostia Games**.

L'objectif est de montrer que la V1 du projet est fonctionnelle, testée, documentée et déployée en ligne.

Ces captures pourront être utilisées dans le dossier projet, dans une présentation ou comme preuve de validation technique.

---

## Organisation des preuves

Un fichier de preuve sera ajouté afin de regrouper et présenter les captures importantes du projet **Frostia Games**.

Ce fichier de preuve servira à montrer visuellement :

* les captures des maquettes Figma ;
* les captures du site public ;
* les captures responsive ;
* les captures de l'administration Django ;
* les captures du déploiement Render ;
* les captures du code ;
* les captures des commandes de validation ;
* les captures du dépôt GitHub ;
* les captures de la documentation.

Toutes les images utilisées comme preuves seront regroupées dans un répertoire dédié.

Organisation prévue :

```txt
doc/
└── preuves/
    ├── preuves-frostia-games.md
    └── images/
        ├── figma-accueil.png
        ├── figma-mes-creations.png
        ├── figma-projets-jouables.png
        ├── site-accueil-desktop.png
        ├── site-mes-creations.png
        ├── site-projets-jouables.png
        ├── site-accueil-mobile.png
        ├── site-mes-creations-mobile.png
        ├── admin-connexion.png
        ├── admin-tableau-de-bord.png
        ├── admin-creations.png
        ├── admin-projets-jouables.png
        ├── render-service-live.png
        ├── render-build-start-command.png
        ├── django-check.png
        ├── git-status-clean.png
        └── github-depot.png
```

Le fichier `preuves-frostia-games.md` servira à présenter les captures avec un court commentaire pour expliquer ce que chaque image prouve.

Le dossier `images/` contiendra toutes les captures utilisées comme preuves.

Cette organisation permet de faciliter :

* la préparation du dossier projet ;
* la relecture ;
* l'ajout des images dans le dossier final ;
* la vérification des preuves techniques ;
* la présentation du projet à l'évaluateur ;
* la séparation entre la documentation écrite et les fichiers images.

Les captures ne doivent pas contenir d'informations sensibles.

Avant d'ajouter une image dans le dossier de preuves, il faut vérifier que la capture ne montre pas :

* de mot de passe ;
* de clé secrète Django ;
* de valeur `DJANGO_SECRET_KEY` ;
* de valeur `DJANGO_SUPERUSER_PASSWORD` ;
* de variable d'environnement sensible ;
* d'information personnelle inutile ;
* d'identifiants administrateur complets.

---

## Règles de sécurité pour les captures

Avant de prendre une capture d'écran, il faut vérifier qu'aucune information sensible n'est visible.

Ne jamais afficher dans une capture :

* mot de passe ;
* clé secrète Django ;
* valeur de `DJANGO_SECRET_KEY` ;
* valeur de `DJANGO_SUPERUSER_PASSWORD` ;
* jeton privé ;
* clé API ;
* information personnelle inutile ;
* lien privé de déploiement non destiné au public.

Les captures doivent montrer le fonctionnement du projet sans exposer les secrets.

---

## Liste des captures recommandées

Les captures à conserver sont réparties en plusieurs catégories :

* captures des maquettes Figma ;
* captures du site public ;
* captures responsive ;
* captures de l'administration Django ;
* captures Render ;
* captures du code ;
* captures de la documentation ;
* captures de validation technique.

---

# 0. Captures des maquettes Figma

## Capture 00 - Maquettes Figma du projet

### Objectif

Montrer que l'interface du projet a été préparée visuellement avant ou pendant l'intégration.

### Éléments à capturer

* maquette de la page d'accueil ;
* maquette de la page Mes créations ;
* maquette de la page Projets jouables ;
* structure générale prévue ;
* organisation visuelle des pages.

### À montrer sur la capture

* la mise en page prévue ;
* les sections principales ;
* l'organisation des cartes ;
* la logique de navigation ;
* les choix visuels de départ ;
* l'intention graphique du projet.

### Statut

```txt
À capturer
```

---

# 1. Captures du site public

## Capture 01 - Page d'accueil desktop

### Objectif

Montrer que la page d'accueil du site Frostia Games est accessible et correctement affichée.

### Élément à capturer

```txt
https://frostia-games.onrender.com
```

### À montrer sur la capture

* le titre du site ;
* la navigation ;
* le contenu principal ;
* le design général ;
* le rendu desktop ;
* l'URL Render visible si possible.

### Statut

```txt
À capturer
```

---

## Capture 02 - Page Mes créations

### Objectif

Montrer la page dédiée aux créations et futurs projets.

### Élément à capturer

```txt
https://frostia-games.onrender.com/mes-creations/
```

### À montrer sur la capture

* le titre de la page ;
* les cartes ou blocs de créations ;
* les données affichées ;
* la navigation ;
* le style général.

### Statut

```txt
À capturer
```

---

## Capture 03 - Page Projets jouables à venir

### Objectif

Montrer la page prévue pour les futurs projets jouables.

### Élément à capturer

```txt
https://frostia-games.onrender.com/projets-jouables/
```

### À montrer sur la capture

* le titre de la page ;
* la zone préparatoire ;
* le message indiquant que l'upload serveur n'est pas encore implanté ;
* le bouton ou l'interface prévue pour une évolution future ;
* le contenu affiché depuis Django.

### Statut

```txt
À capturer
```

---

# 2. Captures responsive

## Capture 04 - Page d'accueil mobile

### Objectif

Montrer que le site reste consultable sur petit écran.

### Élément à capturer

Page d'accueil en largeur mobile dans l'inspecteur du navigateur.

### À montrer sur la capture

* menu mobile ;
* contenu lisible ;
* absence de débordement important ;
* cartes adaptées ;
* navigation accessible.

### Statut

```txt
À capturer
```

---

## Capture 05 - Page Mes créations mobile

### Objectif

Montrer que la page des créations reste lisible sur mobile.

### À montrer sur la capture

* cartes adaptées ;
* textes lisibles ;
* blocs correctement alignés ;
* pas de scroll horizontal important.

### Statut

```txt
À capturer
```

---

# 3. Captures de l'administration Django

## Capture 06 - Page de connexion admin Django

### Objectif

Montrer que l'administration Django est accessible en ligne.

### Élément à capturer

```txt
https://frostia-games.onrender.com/admin/
```

### À montrer sur la capture

* page de connexion Django ;
* URL `/admin/` ;
* aucun mot de passe visible.

### Statut

```txt
À capturer
```

---

## Capture 07 - Tableau de bord admin Django

### Objectif

Montrer que l'administration Django fonctionne après connexion.

### À montrer sur la capture

* tableau de bord admin ;
* modèles disponibles ;
* interface Django chargée correctement.

### Attention

Ne pas afficher de mot de passe ou de donnée sensible.

### Statut

```txt
À capturer
```

---

## Capture 08 - Modèle Creation dans l'admin

### Objectif

Montrer que les créations peuvent être gérées depuis l'administration Django.

### À montrer sur la capture

* liste des créations ;
* colonnes principales ;
* filtres ou recherche si visibles ;
* interface propre.

### Statut

```txt
À capturer
```

---

## Capture 09 - Modèle PlayableProject dans l'admin

### Objectif

Montrer que les projets jouables à venir sont gérés depuis l'administration Django.

### À montrer sur la capture

* liste des projets jouables ;
* statut des projets ;
* informations principales ;
* interface Django fonctionnelle.

### Statut

```txt
À capturer
```

---

# 4. Captures Render

## Capture 10 - Service Render actif

### Objectif

Montrer que le service Render est bien en ligne.

### À montrer sur la capture

* nom du service ;
* statut actif ;
* URL publique ;
* type de service Web ;
* branche GitHub utilisée.

### Statut

```txt
À capturer
```

---

## Capture 11 - Logs Render avec service live

### Objectif

Montrer que le déploiement a réussi.

### À montrer sur la capture

Message Render :

```txt
Your service is live
```

Si visible, montrer aussi :

```txt
Listening at: http://0.0.0.0:10000
```

### Statut

```txt
À capturer
```

---

## Capture 12 - Build Command et Start Command

### Objectif

Montrer la configuration de déploiement Render.

### À montrer sur la capture

Build Command :

```bash
bash build.sh
```

Start Command :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

### Attention

Ne pas afficher de variables secrètes.

### Statut

```txt
À capturer
```

---

## Capture 13 - Variables d'environnement Render

### Objectif

Montrer que les variables d'environnement sont utilisées sans exposer leurs valeurs.

### À montrer sur la capture

Uniquement les noms des variables :

```txt
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
```

### Attention

Les valeurs doivent être masquées.

### Statut

```txt
À capturer avec prudence
```

---

# 5. Captures du code

## Capture 14 - Structure du projet dans VS Code

### Objectif

Montrer l'organisation générale du projet.

### À montrer sur la capture

* dossier `frostia_config` ;
* dossier `core` ;
* dossier `creations` ;
* dossier `playable` ;
* dossier `templates` ;
* dossier `static` ;
* dossier `doc` ;
* fichier `manage.py` ;
* fichier `requirements.txt` ;
* fichier `build.sh` ;
* fichier `README.md` ;
* fichier `CHOIX_TECHNIQUES.md`.

### Statut

```txt
À capturer
```

---

## Capture 15 - Fichier settings.py

### Objectif

Montrer une partie de la configuration Django.

### À montrer sur la capture

* `INSTALLED_APPS` ;
* configuration des templates ;
* configuration des fichiers statiques ;
* `ALLOWED_HOSTS` si présent ;
* logique des variables d'environnement si visible.

### Attention

Ne pas afficher la vraie clé secrète.

### Statut

```txt
À capturer avec prudence
```

---

## Capture 16 - Fichier models.py

### Objectif

Montrer les modèles Django utilisés dans le projet.

### À montrer sur la capture

* modèle `Creation` ;
* modèle `PlayableProject` ;
* champs principaux ;
* statuts ;
* visibilité ;
* dates.

### Statut

```txt
À capturer
```

---

## Capture 17 - Fichier admin.py

### Objectif

Montrer la configuration de l'administration Django.

### À montrer sur la capture

* `list_display` ;
* `list_filter` ;
* `search_fields` ;
* `prepopulated_fields` ;
* `readonly_fields`.

### Statut

```txt
À capturer
```

---

## Capture 18 - Fichier views.py

### Objectif

Montrer la liaison entre le backend Django et les templates.

### À montrer sur la capture

* vues principales ;
* récupération des données ;
* `render` vers les templates ;
* logique simple et lisible.

### Statut

```txt
À capturer
```

---

## Capture 19 - Fichier build.sh

### Objectif

Montrer le script utilisé par Render pour préparer le projet.

### À montrer sur la capture

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true
```

### Statut

```txt
À capturer
```

---

# 6. Captures de validation technique

## Capture 20 - Commande python manage.py check

### Objectif

Montrer que Django ne détecte pas d'erreur de configuration.

### Commande à lancer

```powershell
python manage.py check
```

### Résultat attendu

```txt
System check identified no issues (0 silenced).
```

### Statut

```txt
À capturer
```

---

## Capture 21 - Commande git status propre

### Objectif

Montrer que le projet est sauvegardé proprement dans Git.

### Commande à lancer

```powershell
git status
```

### Résultat attendu

```txt
nothing to commit, working tree clean
```

### Statut

```txt
À capturer après commit final
```

---

## Capture 22 - Dépôt GitHub

### Objectif

Montrer que le projet est versionné et disponible dans un dépôt GitHub.

### À montrer sur la capture

* nom du dépôt ;
* branche `main` ;
* fichiers principaux ;
* dernier commit visible.

### Statut

```txt
À capturer
```

---

# 7. Captures de documentation

## Capture 23 - Dossier doc

### Objectif

Montrer que le projet est documenté.

### À montrer sur la capture

Fichiers du dossier `doc` :

```txt
00-index-documentation.md
01-modernisation-interface.md
02-journal-de-bord.md
03-modelisation-backend.md
04-docker-et-lancement.md
05-securite-backend.md
06-manuel-utilisateur.md
07-base-de-donnees.md
08-changelog.md
09-deploiement-render.md
10-bilan-v1-frostia-games.md
11-installation-locale.md
12-architecture.md
13-test-et-vérification.md
14-Capture-et Preuve.md
15-limites-et-évolutions.md
16-presentation-projet-2.md
17-pistes-explorees-et-non-retenues.md
18-plan-finalisation-v1.md
```

### Statut

```txt
À capturer
```

---

## Capture 24 - Documentation de déploiement Render

### Objectif

Montrer que le déploiement est documenté.

### À montrer sur la capture

* titre du document ;
* Build Command ;
* Start Command ;
* variables d'environnement ;
* résultat du déploiement ;
* problèmes rencontrés.

### Statut

```txt
À capturer
```

---

## Capture 25 - Bilan V1

### Objectif

Montrer que l'état du projet est évalué avec un bilan clair.

### À montrer sur la capture

* tableau d'avancement ;
* avancement global ;
* limites ;
* évolutions prévues.

### Statut

```txt
À capturer
```

---

## Capture 26 - Fichier de preuve

### Objectif

Montrer que les captures sont organisées dans un fichier de preuve dédié.

### À montrer sur la capture

* fichier `preuves-frostia-games.md` ;
* répertoire `images/` ;
* liste des captures utilisées ;
* organisation claire des preuves.

### Statut

```txt
À capturer après création du fichier de preuve
```

---

# Tableau récapitulatif des captures

| N° | Capture                            | Priorité | Statut                 |
| -: | ---------------------------------- | -------- | ---------------------- |
| 00 | Maquettes Figma                    | Haute    | À faire                |
| 01 | Page d'accueil desktop             | Haute    | À faire                |
| 02 | Page Mes créations                 | Haute    | À faire                |
| 03 | Page Projets jouables              | Haute    | À faire                |
| 04 | Page d'accueil mobile              | Haute    | À faire                |
| 05 | Page Mes créations mobile          | Moyenne  | À faire                |
| 06 | Connexion admin Django             | Haute    | À faire                |
| 07 | Tableau de bord admin Django       | Haute    | À faire                |
| 08 | Modèle Creation admin              | Moyenne  | À faire                |
| 09 | Modèle PlayableProject admin       | Moyenne  | À faire                |
| 10 | Service Render actif               | Haute    | À faire                |
| 11 | Logs Render service live           | Haute    | À faire                |
| 12 | Build Command / Start Command      | Haute    | À faire                |
| 13 | Variables d'environnement masquées | Moyenne  | À faire avec prudence  |
| 14 | Structure du projet VS Code        | Haute    | À faire                |
| 15 | settings.py sans secret            | Moyenne  | À faire avec prudence  |
| 16 | models.py                          | Haute    | À faire                |
| 17 | admin.py                           | Moyenne  | À faire                |
| 18 | views.py                           | Moyenne  | À faire                |
| 19 | build.sh                           | Haute    | À faire                |
| 20 | python manage.py check             | Haute    | À faire                |
| 21 | git status propre                  | Haute    | À faire                |
| 22 | dépôt GitHub                       | Moyenne  | À faire                |
| 23 | dossier doc                        | Haute    | À faire                |
| 24 | documentation Render               | Moyenne  | À faire                |
| 25 | bilan V1                           | Moyenne  | À faire                |
| 26 | fichier de preuve                  | Moyenne  | À faire après création |

---

## Captures prioritaires minimum

Si le temps est limité, les captures indispensables sont :

```txt
00 - Maquettes Figma
01 - Page d'accueil desktop
02 - Page Mes créations
03 - Page Projets jouables
04 - Page d'accueil mobile
06 - Connexion admin Django
07 - Tableau de bord admin Django
10 - Service Render actif
11 - Logs Render service live
12 - Build Command / Start Command
14 - Structure du projet VS Code
20 - python manage.py check
21 - git status propre
23 - dossier doc
```

Ces captures suffisent à prouver que la V1 est fonctionnelle, déployée et documentée.

---

## Captures non nécessaires pour l'instant

Certaines captures ne sont pas indispensables pour la V1 :

* création d'un compte jury temporaire ;
* configuration PostgreSQL ;
* interface d'administration personnalisée ;
* graphiques Plotly ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* espace privé complet.

Ces éléments ne font pas partie du périmètre actuel.

---

## Bilan

Les captures listées dans ce document permettent de préparer une preuve claire du fonctionnement du projet Frostia Games.

Elles montrent :

* les maquettes Figma ;
* l'interface publique ;
* le responsive ;
* l'administration Django ;
* le déploiement Render ;
* la configuration technique ;
* les tests réalisés ;
* la documentation produite ;
* l'organisation des preuves dans un fichier dédié ;
* le regroupement des images dans un répertoire prévu.

Ce document sert de checklist pour préparer le dossier projet et vérifier que la V1 est correctement présentée.
