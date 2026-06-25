# Tests et vérifications - Frostia Games

## Objectif du document

Ce document présente les tests et vérifications réalisés sur le projet **Frostia Games**.

L'objectif est de montrer que la V1 a été contrôlée à plusieurs niveaux :

* fonctionnement local ;
* fonctionnement avec Django ;
* fonctionnement de l'interface publique ;
* fonctionnement de l'administration ;
* affichage des données ;
* responsive ;
* déploiement Render ;
* sécurité minimale ;
* absence d'erreurs bloquantes.

Ce document ne présente pas une campagne de tests automatisés complète. Il s'agit d'une documentation de vérification fonctionnelle adaptée à une V1.

---

## Périmètre des tests

Les tests réalisés concernent principalement :

* les pages publiques du site ;
* la navigation ;
* l'affichage responsive ;
* les modèles Django ;
* l'administration Django ;
* la base SQLite ;
* le lancement local ;
* le lancement avec Docker ;
* le déploiement Render ;
* les fichiers statiques ;
* les variables d'environnement.

Les tests automatisés avancés sont reportés à une version future.

---

## Environnement de test local

Les premiers tests ont été réalisés en local avec l'environnement suivant :

| Élément               | Valeur             |
| --------------------- | ------------------ |
| Système               | Windows            |
| Éditeur               | Visual Studio Code |
| Terminal              | PowerShell         |
| Langage               | Python             |
| Framework             | Django             |
| Base de données       | SQLite             |
| Environnement virtuel | `.venv`            |

---

## Commandes de vérification Django

La commande principale utilisée pour vérifier la validité du projet Django est :

```powershell
python manage.py check
```

Résultat attendu :

```txt
System check identified no issues (0 silenced).
```

Cette commande permet de vérifier que Django ne détecte pas d'erreur de configuration majeure.

---

## Test du serveur local

Le serveur local a été lancé avec la commande :

```powershell
python manage.py runserver
```

Adresse utilisée :

```txt
http://127.0.0.1:8000/
```

Vérifications effectuées :

* le serveur démarre correctement ;
* aucune erreur bloquante n'apparaît dans le terminal ;
* la page d'accueil est accessible ;
* les autres pages principales sont accessibles ;
* les fichiers CSS sont chargés ;
* le JavaScript du menu fonctionne.

---

## Pages testées

Les pages principales du projet ont été testées.

| Page                  | URL locale           | Statut        |
| --------------------- | -------------------- | ------------- |
| Accueil               | `/`                  | Fonctionnelle |
| Mes créations         | `/mes-creations/`    | Fonctionnelle |
| Projets jouables      | `/projets-jouables/` | Fonctionnelle |
| Administration Django | `/admin/`            | Fonctionnelle |

---

## Test de la page d'accueil

La page d'accueil a été vérifiée afin de confirmer que le site présente correctement le projet Frostia Games.

Vérifications réalisées :

* le titre principal s'affiche ;
* le contenu de présentation est visible ;
* la navigation est présente ;
* le design général est cohérent ;
* le CSS est chargé ;
* la page ne présente pas d'erreur visible.

Résultat :

```txt
Page d'accueil fonctionnelle.
```

---

## Test de la page Mes créations

La page **Mes créations** a été testée afin de vérifier l'affichage des créations du portfolio.

Vérifications réalisées :

* la page est accessible ;
* les créations enregistrées sont affichées ;
* les données remontent depuis la base SQLite ;
* les cartes de présentation sont visibles ;
* le contenu reste lisible ;
* la page ne provoque pas d'erreur Django.

Résultat :

```txt
Page Mes créations fonctionnelle.
```

---

## Test de la page Projets jouables

La page **Projets jouables** a été testée afin de vérifier l'affichage de l'interface préparatoire.

Vérifications réalisées :

* la page est accessible ;
* les projets enregistrés sont affichés ;
* les données remontent depuis la base SQLite ;
* le bouton de lecture affiche un comportement prévu ;
* le bouton de sélection de fichier local fonctionne ;
* le message d'upload non implanté est visible ;
* aucun vrai upload serveur n'est effectué.

Résultat :

```txt
Page Projets jouables fonctionnelle pour la V1.
```

---

## Test de la navigation

La navigation principale a été testée sur les différentes pages.

Vérifications réalisées :

* les liens du menu fonctionnent ;
* les pages se chargent correctement ;
* aucun lien principal ne mène vers une erreur ;
* l'état actif du menu est visible ;
* la navigation reste compréhensible.

Résultat :

```txt
Navigation fonctionnelle.
```

---

## Test du responsive

Le responsive a été vérifié afin de contrôler l'affichage sur différents formats d'écran.

Vérifications réalisées :

* l'interface reste lisible sur écran large ;
* les cartes ne débordent pas ;
* le menu mobile fonctionne ;
* les textes restent lisibles ;
* aucun scroll horizontal important n'a été constaté ;
* les blocs principaux restent accessibles.

Résultat :

```txt
Responsive fonctionnel pour une V1, avec améliorations possibles.
```

Limite constatée :

```txt
Le responsive peut encore être amélioré visuellement dans une prochaine version.
```

---

## Test des fichiers statiques

Les fichiers statiques ont été testés en local et après déploiement.

Fichiers concernés :

```txt
static/css/main.css
static/js/menu.js
static/images/
```

Vérifications réalisées :

* le fichier CSS est chargé ;
* les styles s'appliquent correctement ;
* le JavaScript du menu fonctionne ;
* les images prévues peuvent être utilisées ;
* la commande `collectstatic` fonctionne.

Commande utilisée :

```powershell
python manage.py collectstatic --noinput
```

Résultat :

```txt
Fichiers statiques correctement collectés.
```

---

## Test de la base de données

La V1 utilise SQLite.

Fichier concerné :

```txt
db.sqlite3
```

Vérifications réalisées :

* les migrations s'appliquent correctement ;
* les données peuvent être ajoutées depuis l'administration Django ;
* les données sont conservées localement ;
* les données sont affichées dans les templates ;
* les modèles `Creation` et `PlayableProject` fonctionnent.

Commandes utilisées :

```powershell
python manage.py makemigrations
python manage.py migrate
```

Résultat :

```txt
Base SQLite fonctionnelle pour la V1.
```

---

## Test des modèles Django

Les modèles Django principaux ont été vérifiés.

Modèles concernés :

* `Creation` ;
* `PlayableProject`.

Vérifications réalisées :

* les modèles sont reconnus par Django ;
* les migrations sont générées ;
* les migrations sont appliquées ;
* les objets peuvent être créés depuis l'administration ;
* les objets peuvent être affichés côté site.

Résultat :

```txt
Modèles Django fonctionnels.
```

---

## Test de l'administration Django

L'administration Django a été testée en local puis en ligne.

Adresse locale :

```txt
http://127.0.0.1:8000/admin/
```

Adresse en ligne :

```txt
https://frostia-games.onrender.com/admin/
```

Vérifications réalisées :

* la page de connexion s'affiche ;
* le compte administrateur fonctionne ;
* les modèles enregistrés apparaissent ;
* il est possible d'ajouter des données ;
* il est possible de modifier des données ;
* les données ajoutées apparaissent côté site.

Résultat :

```txt
Administration Django fonctionnelle.
```

---

## Test du compte administrateur

Un compte administrateur privé a été utilisé pour vérifier l'accès à l'interface Django.

Vérifications réalisées :

* connexion possible ;
* accès à l'admin Django ;
* accès aux modèles enregistrés ;
* modification des contenus possible ;
* aucun identifiant publié dans la documentation.

Résultat :

```txt
Compte administrateur fonctionnel.
```

Pour des raisons de sécurité, les identifiants ne sont pas inscrits dans le dépôt GitHub ni dans la documentation publique.

---

## Test Docker

Le projet a également été testé avec Docker.

Commande utilisée :

```powershell
docker compose up --build
```

Vérifications réalisées :

* l'image Docker se construit ;
* le conteneur démarre ;
* le serveur Django se lance ;
* le site est accessible depuis le navigateur ;
* l'environnement Docker permet de relancer le projet plus facilement.

Adresse utilisée :

```txt
http://127.0.0.1:8000/
```

Résultat :

```txt
Lancement Docker fonctionnel.
```

---

## Test du déploiement Render

Le projet a été déployé sur Render.

URL de production :

```txt
https://frostia-games.onrender.com
```

Vérifications réalisées :

* le service Render démarre ;
* le build s'exécute correctement ;
* les dépendances sont installées ;
* les fichiers statiques sont collectés ;
* les migrations sont appliquées ;
* Gunicorn lance l'application Django ;
* le site est accessible en ligne ;
* l'administration Django est accessible.

Message observé dans les logs Render :

```txt
Your service is live
```

Résultat :

```txt
Déploiement Render réussi.
```

---

## Test du Build Command Render

Commande utilisée sur Render :

```bash
bash build.sh
```

Vérifications réalisées :

* installation des dépendances ;
* collecte des fichiers statiques ;
* application des migrations ;
* tentative de création du superutilisateur ;
* absence d'erreur bloquante pendant le build.

Résultat :

```txt
Build Command fonctionnel.
```

---

## Test du Start Command Render

Commande utilisée sur Render :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Vérifications réalisées :

* Gunicorn démarre ;
* Django est lancé via `wsgi.py` ;
* Render détecte correctement le port ;
* le site devient accessible.

Résultat :

```txt
Start Command fonctionnel.
```

---

## Test des variables d'environnement

Les variables d'environnement Render ont été vérifiées.

Variables utilisées :

```txt
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
```

Vérifications réalisées :

* les variables sont présentes dans Render ;
* les valeurs sensibles ne sont pas publiées ;
* la clé secrète Django n'est pas écrite directement dans le code ;
* le compte administrateur peut être créé automatiquement ;
* le mode debug peut être désactivé en production.

Résultat :

```txt
Variables d'environnement opérationnelles.
```

---

## Vérification de la sécurité minimale

Vérifications réalisées :

* `DEBUG` désactivé sur Render ;
* `DJANGO_SECRET_KEY` stockée dans Render ;
* aucun mot de passe publié dans GitHub ;
* aucun identifiant administrateur écrit dans la documentation ;
* accès admin conservé privé ;
* pas de compte jury temporaire créé pour l'instant.

Résultat :

```txt
Sécurité minimale correcte pour une V1.
```

---

## Problèmes rencontrés pendant les tests

Plusieurs problèmes ont été rencontrés pendant les tests et la stabilisation du projet.

### Erreurs PowerShell

La commande suivante a posé problème en local :

```powershell
bash build.sh
```

Cause :

```txt
PowerShell Windows ne correspond pas à un environnement Linux standard.
```

Correction :

```txt
La commande est utilisée sur Render, qui fonctionne avec un environnement Linux.
```

---

### Fausses alertes Pylance

VS Code / Pylance signalait certaines erreurs liées au typage Django.

Ces alertes concernaient notamment :

* `CharField` ;
* `SlugField` ;
* `BooleanField` ;
* `ModelAdmin`.

Correction :

* passage du mode strict au mode basic ;
* conservation de `python manage.py check` comme validation Django principale ;
* ajout de commentaires `type: ignore` lorsque nécessaire.

---

### Confusion entre Flask et Django

Une commande de démarrage non adaptée avait été envisagée :

```bash
gunicorn app:app
```

Correction :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande est adaptée à la structure Django du projet.

---

### Confusion entre commandes Render et variables d'environnement

Une confusion a eu lieu entre les variables d'environnement et les commandes de déploiement.

Correction :

* les variables Django restent dans **Environment Variables** ;
* `bash build.sh` doit être placé dans **Build Command** ;
* la commande Gunicorn doit être placée dans **Start Command**.

---

## Tests non réalisés dans la V1

Certains tests ne sont pas encore réalisés dans cette V1.

Tests reportés :

* tests unitaires automatisés complets ;
* tests d'intégration avancés ;
* tests de charge ;
* tests de sécurité poussés ;
* tests d'upload serveur ;
* tests PostgreSQL ;
* tests de compte jury temporaire ;
* tests d'un espace privé personnalisé ;
* tests de statistiques ou graphiques.

Ces tests sont reportés car les fonctionnalités associées ne font pas partie du périmètre immédiat de la V1.

---

## Tableau récapitulatif des tests

| Élément testé                     | Résultat            |
| --------------------------------- | ------------------- |
| Lancement local Django            | Validé              |
| Commande `python manage.py check` | Validé              |
| Page d'accueil                    | Validé              |
| Page Mes créations                | Validé              |
| Page Projets jouables             | Validé              |
| Navigation                        | Validé              |
| Responsive                        | Fonctionnel pour V1 |
| CSS                               | Validé              |
| JavaScript menu                   | Validé              |
| Modèles Django                    | Validé              |
| Migrations                        | Validé              |
| Base SQLite                       | Validé              |
| Administration Django             | Validé              |
| Compte administrateur             | Validé              |
| Docker                            | Validé              |
| Déploiement Render                | Validé              |
| Fichiers statiques en production  | Validé              |
| Variables d'environnement         | Validé              |
| Sécurité minimale                 | Validé pour V1      |

---

## Bilan

Les tests réalisés montrent que la V1 de **Frostia Games** est fonctionnelle.

Le site peut être lancé en local, lancé avec Docker et consulté en ligne via Render.

Les pages principales fonctionnent, les données Django sont affichées, l'administration est accessible et le déploiement est opérationnel.

La V1 reste volontairement limitée, mais elle est stable, testée et présentable dans son périmètre actuel.
