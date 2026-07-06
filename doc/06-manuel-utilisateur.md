# Manuel utilisateur - Frostia Games

## Objectif du document

Ce document explique comment utiliser la V1 du projet **Frostia Games**.

Il présente :

* le lancement du projet en local ;
* le lancement du projet avec Docker ;
* l'accès au site en ligne sur Render ;
* les pages principales ;
* l'accès à l'administration Django ;
* l'accès avec un compte temporaire de lecture seule ;
* l'ajout d'une création ;
* l'ajout d'un projet jouable ;
* l'affichage des notes TinyDB sur l'accueil ;
* les fonctionnalités disponibles ;
* les limites de la V1 ;
* les vérifications à effectuer avant une démonstration ;
* les captures à préparer pour le dossier projet.

L'objectif est de fournir un guide simple pour utiliser, tester et présenter le projet.

Ce document a été mis à jour après le renforcement du dossier projet afin d'intégrer :

* TinyDB ;
* les notes de progression affichées sur l'accueil ;
* le compte temporaire de lecture seule ;
* les nouvelles commandes de vérification ;
* les preuves à préparer pour le dossier final.

---

# 1. Présentation du site

Frostia Games est un portfolio personnel développé avec **Django**.

Il est destiné à présenter des projets de jeux vidéo actuels ou futurs dans une interface web simple, moderne et évolutive.

La V1 contient trois pages principales :

* Accueil ;
* Mes créations ;
* Projets jouables.

Le site utilise Django pour gérer :

* les routes ;
* les vues ;
* les templates ;
* les modèles ;
* l'administration ;
* la base SQLite ;
* l'affichage dynamique de certaines données.

La V1 utilise aussi TinyDB pour une expérimentation NoSQL légère.

TinyDB sert à stocker et afficher des notes de progression liées au projet.

La V1 peut être utilisée :

* en local avec l'environnement virtuel Python ;
* avec Docker et Docker Compose ;
* en ligne via Render.

---

# 2. Accès au site en ligne

Le projet est déployé sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Pages principales en ligne :

```text
https://frostia-games.onrender.com/
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
```

Administration Django en ligne :

```text
https://frostia-games.onrender.com/admin/
```

L'administration est protégée par un compte administrateur.

Un compte temporaire de lecture seule peut aussi être utilisé pour permettre une consultation limitée de certaines parties de l'administration.

Aucun identifiant ni mot de passe ne doit être publié dans le dépôt GitHub ou dans la documentation publique.

---

# 3. Lancer le projet en local

## 3.1 Se placer à la racine du projet

Depuis le terminal, se placer dans le dossier du projet :

```powershell
cd "D:\Apprentissage\Autre Projet\Frostia Games"
```

La racine doit contenir notamment :

```text
manage.py
requirements.txt
README.md
CHOIX_TECHNIQUES.md
Dockerfile
docker-compose.yml
build.sh
```

Elle peut aussi contenir :

```text
core/
creations/
playable/
templates/
static/
data/
scripts/
doc/
docs/
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

ou :

```powershell
python -m pip install -r requirements.txt
```

Le fichier `requirements.txt` contient les dépendances nécessaires au projet, notamment :

* Django ;
* Gunicorn ;
* WhiteNoise ;
* TinyDB.

Django sert au fonctionnement principal du projet.

Gunicorn et WhiteNoise sont utilisés pour le déploiement en ligne sur Render.

TinyDB sert à l'expérimentation NoSQL légère et à l'affichage des notes de progression sur la page d'accueil.

---

## 3.4 Appliquer les migrations

Avant de lancer le serveur, appliquer les migrations :

```powershell
python manage.py migrate
```

Cette commande crée ou met à jour les tables nécessaires dans la base SQLite.

Elle concerne les modèles Django comme :

* `Creation` ;
* `PlayableProject`.

TinyDB ne dépend pas des migrations Django, car il utilise un fichier JSON.

---

## 3.5 Vérifier le projet

Commande de vérification Django :

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

Cette commande permet de vérifier que la configuration Django ne contient pas d'erreur bloquante.

---

## 3.6 Vérifier TinyDB

Commande de vérification TinyDB :

```powershell
python -m scripts.demo_tinydb_notes
```

Cette commande permet de vérifier que :

* TinyDB est bien installé ;
* le service NoSQL fonctionne ;
* les notes de progression sont créées ou lues ;
* le fichier JSON TinyDB est accessible ;
* les données peuvent être affichées dans le terminal.

Cette commande sert aussi de preuve technique pour le dossier projet.

---

## 3.7 Lancer le serveur local

Commande :

```powershell
python manage.py runserver
```

Le site est ensuite accessible à l'adresse :

```text
https://frostia-games.onrender.com/
```

Pages principales locales :

```text
https://frostia-games.onrender.com/
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
```

Administration Django locale :

```text
https://frostia-games.onrender.com/admin/
```

---

## 3.8 Vérifications après lancement local

Après le lancement local, vérifier :

* la page d'accueil ;
* les notes de progression TinyDB sur l'accueil ;
* la page **Mes créations** ;
* la page **Projets jouables** ;
* le menu mobile ;
* l'administration Django ;
* l'affichage des données SQLite ;
* l'absence d'erreur dans le terminal.

---

# 4. Lancer le projet avec Docker

Le projet peut aussi être lancé avec Docker Compose.

Depuis la racine du projet :

```powershell
docker compose up --build
```

Le site est ensuite accessible à l'adresse :

```text
https://frostia-games.onrender.com/
```

Pages principales :

```text
https://frostia-games.onrender.com/
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
```

Administration Django :

```text
https://frostia-games.onrender.com/admin/
```

---

## 4.1 Appliquer les migrations dans Docker

Si nécessaire, les migrations peuvent être lancées dans le conteneur :

```powershell
docker compose exec web python manage.py migrate
```

---

## 4.2 Vérifier Django dans Docker

Commande :

```powershell
docker compose exec web python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

---

## 4.3 Vérifier TinyDB dans Docker

Commande :

```powershell
docker compose exec web python -m scripts.demo_tinydb_notes
```

Cette commande permet de vérifier que l'expérimentation NoSQL fonctionne aussi dans l'environnement Docker.

---

## 4.4 Créer un administrateur dans Docker

Si aucun administrateur n'existe dans l'environnement Docker :

```powershell
docker compose exec web python manage.py createsuperuser
```

Django demandera ensuite :

* un nom d'utilisateur ;
* une adresse e-mail ;
* un mot de passe ;
* une confirmation du mot de passe.

---

## 4.5 Arrêter Docker

Pour arrêter le serveur Docker depuis le terminal :

```powershell
Ctrl + C
```

Pour arrêter et supprimer les conteneurs liés au projet :

```powershell
docker compose down
```

---

# 5. Pages publiques

## 5.1 Page Accueil

Adresse locale :

```text
https://frostia-games.onrender.com/
```

Adresse en ligne :

```text
https://frostia-games.onrender.com/
```

La page d'accueil présente :

* le nom Frostia Games ;
* l'objectif du portfolio ;
* les sections principales ;
* l'état général de la V1 ;
* une introduction au projet ;
* les notes de progression provenant de TinyDB.

Cette page sert de point d'entrée au site.

---

## 5.2 Notes TinyDB sur l'accueil

La page d'accueil affiche maintenant des notes de progression issues de TinyDB.

Ces notes servent à montrer une expérimentation NoSQL légère.

Elles peuvent contenir :

* un titre ;
* un statut ;
* des tags ;
* un contenu descriptif ;
* une date de création.

La chaîne technique est la suivante :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

L'utilisateur n'a rien à saisir dans l'interface publique.

Les notes sont préparées par le service Python NoSQL.

---

## 5.3 Page Mes créations

Adresse locale :

```text
https://frostia-games.onrender.com/mes-creations/
```

Adresse en ligne :

```text
https://frostia-games.onrender.com/mes-creations/
```

Cette page présente les créations enregistrées dans la base de données.

La V1 utilise un lexique alphabétique.

La lettre `K` permet d'afficher le projet KryonCore lorsque celui-ci est enregistré dans l'administration Django et marqué comme visible.

Les créations affichées sont filtrées avec le champ :

```text
is_visible = True
```

Cela permet de masquer une création sans la supprimer de la base.

---

## 5.4 Page Projets jouables

Adresse locale :

```text
https://frostia-games.onrender.com/projets-jouables/
```

Adresse en ligne :

```text
https://frostia-games.onrender.com/projets-jouables/
```

Cette page présente l'espace prévu pour de futurs projets jouables, vidéos, teasers ou prototypes.

Dans la V1, aucun vrai projet jouable n'est encore disponible.

La page contient :

* une zone de lecteur préparatoire ;
* un bouton Lecture affichant un message ;
* un bouton de sélection de fichier local ;
* les informations enregistrées en base pour les futurs projets jouables ;
* un message expliquant que la fonctionnalité réelle est prévue plus tard.

Aucun vrai upload serveur n'est implanté dans cette version.

---

# 6. Accéder à l'administration Django

Adresse locale :

```text
https://frostia-games.onrender.com/admin/
```

Adresse en ligne :

```text
https://frostia-games.onrender.com/admin/
```

L'administration Django permet de gérer les contenus dynamiques du site.

Elle nécessite un compte autorisé.

Pour créer un compte administrateur local si nécessaire :

```powershell
python manage.py createsuperuser
```

Avec Docker :

```powershell
docker compose exec web python manage.py createsuperuser
```

Sur Render, la création du superutilisateur peut être automatisée avec les variables d'environnement et le fichier `build.sh`.

Les identifiants administrateur ne doivent jamais être écrits dans la documentation publique.

---

# 7. Accès avec un compte temporaire de lecture seule

Un compte temporaire de lecture seule peut être utilisé pour l'évaluation.

Ce compte permet de consulter certaines données dans l'administration Django sans donner un accès complet.

Le compte peut voir :

* les créations ;
* les projets jouables.

Le compte ne doit pas voir :

* les utilisateurs ;
* les groupes ;
* les permissions sensibles ;
* les réglages internes ;
* les secrets du projet.

Ce compte est utile pour montrer l'administration Django à un évaluateur sans transmettre un compte superutilisateur.

Les identifiants réels ne doivent pas être écrits dans ce manuel public.

Ils peuvent être transmis séparément uniquement si nécessaire.

---

# 8. Ajouter une création

Depuis l'administration Django :

1. Aller dans la section **Créations**.
2. Cliquer sur **Ajouter une création**.
3. Remplir les champs.
4. Enregistrer.

## Champs principaux

| Champ               | Rôle                                           |
| ------------------- | ---------------------------------------------- |
| Titre               | Nom de la création                             |
| Identifiant URL     | Slug unique utilisé pour identifier le contenu |
| Lettre alphabétique | Lettre utilisée dans le lexique                |
| Nom de code         | Nom interne ou nom du projet                   |
| Type de projet      | Exemple : jeu vidéo PC                         |
| Statut              | État du projet                                 |
| Description courte  | Texte affiché sur le site                      |
| Visible sur le site | Permet d'afficher ou masquer la création       |

## Exemple

```text
Titre : KryonCore
Identifiant URL : kryoncore
Lettre alphabétique : K
Nom de code : KryonCore
Type de projet : Jeu vidéo PC
Statut : En préparation
Visible sur le site : Oui
```

Une fois enregistrée, la création peut apparaître sur la page **Mes créations** si elle est visible.

---

# 9. Modifier une création

Depuis l'administration :

1. Aller dans **Créations**.
2. Cliquer sur la création à modifier.
3. Modifier les champs nécessaires.
4. Enregistrer.

Il est possible de masquer temporairement une création en décochant :

```text
Visible sur le site
```

La création reste en base mais n'apparaît plus sur le site public.

---

# 10. Ajouter un projet jouable

Depuis l'administration Django :

1. Aller dans la section **Projets jouables**.
2. Cliquer sur **Ajouter un projet jouable**.
3. Remplir les champs.
4. Enregistrer.

## Champs principaux

| Champ                    | Rôle                                            |
| ------------------------ | ----------------------------------------------- |
| Titre                    | Nom du futur contenu jouable                    |
| Identifiant URL          | Slug unique                                     |
| Statut                   | État du contenu                                 |
| Type de contenu prévu    | Exemple : démonstration, teaser, prototype      |
| Description courte       | Résumé affiché sur le site                      |
| Message de disponibilité | Message indiquant si le contenu est disponible  |
| Disponible               | Indique si le contenu est réellement disponible |
| Visible sur le site      | Permet d'afficher ou masquer l'entrée           |

## Exemple

```text
Titre : Prototype jouable à venir
Identifiant URL : prototype-jouable-a-venir
Statut : Non disponible
Type prévu : Démonstration / teaser
Disponible : Non
Visible sur le site : Oui
```

Une fois enregistré, le projet peut apparaître sur la page **Projets jouables** si le champ `Visible sur le site` est actif.

---

# 11. Modifier un projet jouable

Depuis l'administration :

1. Aller dans **Projets jouables**.
2. Cliquer sur le projet à modifier.
3. Modifier le statut, le message ou la visibilité.
4. Enregistrer.

Dans la V1, le champ `Disponible` permet uniquement d'indiquer l'état du contenu.

Il ne lance pas encore de vraie démo, vidéo ou version jouable.

---

# 12. Fonctionnement de l'interface préparatoire d'upload

La page **Projets jouables** contient une interface de sélection de fichier.

Cette interface permet :

* de cliquer sur un bouton de sélection ;
* d'ouvrir l'explorateur de fichiers ;
* d'afficher le nom du fichier choisi ;
* d'indiquer clairement que l'upload n'est pas implanté.

Dans la V1 :

* aucun fichier n'est envoyé au serveur ;
* aucun fichier n'est enregistré en base ;
* aucun fichier n'est exécuté ;
* aucune vidéo n'est réellement lue ;
* aucun exécutable n'est proposé au téléchargement.

Cette interface sert uniquement à préparer une future fonctionnalité.

---

# 13. Données dynamiques

Les pages récupèrent les données via les vues Django.

Exemples :

```python
Creation.objects.filter(is_visible=True)
```

```python
PlayableProject.objects.filter(is_visible=True)
```

Les données sont ensuite envoyées aux templates HTML pour être affichées.

Cela permet de modifier certains contenus depuis l'administration sans modifier directement le code HTML.

Les notes TinyDB sont récupérées avec un service Python séparé.

Elles sont ensuite envoyées à la page d'accueil pour être affichées.

---

# 14. Fonctionnalités disponibles dans la V1

La V1 permet :

* de lancer le site en local ;
* de lancer le site avec Docker ;
* de consulter le site en ligne sur Render ;
* de consulter les trois pages principales ;
* d'accéder à l'administration Django ;
* d'utiliser un compte temporaire de lecture seule ;
* d'ajouter une création ;
* de modifier une création ;
* d'ajouter un projet jouable ;
* de modifier un projet jouable ;
* d'afficher des données depuis la base SQLite ;
* d'afficher des notes de progression depuis TinyDB ;
* de masquer ou afficher des contenus ;
* de tester une interface préparatoire pour les projets jouables ;
* de vérifier le projet avec `python manage.py check` ;
* de vérifier TinyDB avec `python -m scripts.demo_tinydb_notes`.

---

# 15. Fonctionnalités non disponibles dans la V1

La V1 ne contient pas encore :

* de vraie page détail projet ;
* de vrai upload serveur ;
* de vrai lecteur vidéo ;
* de jeu jouable dans le navigateur ;
* de système de compte utilisateur public ;
* d'API REST ;
* de rôles publics avancés ;
* de base PostgreSQL ;
* d'administration personnalisée ;
* de graphiques Plotly.js ;
* de tests automatisés complets ;
* de mini-jeu intégré ;
* de système de score ;
* de téléchargement public de projet jouable.

Ces fonctionnalités sont prévues comme évolutions possibles.

Elles ne sont pas ajoutées maintenant afin de conserver une V1 stable, maîtrisable et présentable.

Certains éléments initialement reportés ont finalement été ajoutés de manière limitée et contrôlée :

* compte temporaire de lecture seule ;
* TinyDB ;
* affichage des notes TinyDB ;
* SQL natif documentaire.

---

# 16. Fichiers utiles pour l'utilisateur ou l'évaluateur

Plusieurs fichiers facilitent la compréhension du projet.

## `README.md`

Le fichier `README.md` présente rapidement :

* le rôle du projet ;
* les technologies utilisées ;
* l'installation locale ;
* le lancement Docker ;
* le déploiement Render ;
* les limites de la V1 ;
* les évolutions prévues.

## `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` explique les décisions techniques du projet :

* pourquoi Django a été retenu ;
* pourquoi C# / Razor a été envisagé mais reporté ;
* pourquoi certaines fonctionnalités sont volontairement limitées ;
* pourquoi le projet évite d'élargir trop vite le périmètre.

## `.env.example`

Le fichier `.env.example` montre les variables d'environnement nécessaires sans exposer les vraies valeurs sensibles.

Exemple :

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=change-me
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=change-me
```

## `build.sh`

Le fichier `build.sh` est utilisé par Render pendant le déploiement.

Il permet notamment :

* d'installer les dépendances ;
* de collecter les fichiers statiques ;
* d'appliquer les migrations ;
* de créer un superutilisateur si les variables d'environnement sont présentes.

## `requirements.txt`

Le fichier `requirements.txt` liste les dépendances nécessaires au projet.

Il contient notamment :

* Django ;
* Gunicorn ;
* WhiteNoise ;
* TinyDB.

## `core/services/nosql_notes.py`

Ce fichier contient le service Python utilisé pour lire les notes TinyDB.

## `scripts/demo_tinydb_notes.py`

Ce fichier permet de tester TinyDB depuis le terminal.

---

# 17. Vérifications à faire avant une démonstration

Avant de présenter le projet, vérifier en local :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
```

Puis tester :

```text
https://frostia-games.onrender.com/
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
https://frostia-games.onrender.com/admin/
```

Vérifier aussi le site en ligne :

```text
https://frostia-games.onrender.com/
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
```

Points à vérifier :

* les pages se chargent correctement ;
* le CSS est bien appliqué ;
* la navigation fonctionne ;
* le menu mobile fonctionne ;
* les données SQL apparaissent ;
* les notes TinyDB apparaissent sur l'accueil ;
* la lettre `K` affiche KryonCore si le projet est enregistré et visible ;
* l'administration est accessible ;
* le compte temporaire de lecture seule montre uniquement les sections prévues ;
* la page Projets jouables affiche le message de disponibilité ;
* le bouton de sélection de fichier affiche bien le nom du fichier choisi ;
* aucun vrai upload serveur n'est déclenché ;
* aucune information sensible n'est visible dans les captures.

---

# 18. Conseils pour les captures d'écran

Pour le dossier projet, il est utile de conserver des captures de :

* la page d'accueil ;
* les notes TinyDB sur la page d'accueil ;
* la page **Mes créations** ;
* la page **Projets jouables** ;
* l'administration Django ;
* le compte temporaire de lecture seule ;
* la liste des créations dans l'admin ;
* la liste des projets jouables dans l'admin ;
* le déploiement Render ;
* le terminal avec `python manage.py check` ;
* le terminal avec `python -m scripts.demo_tinydb_notes` ;
* le dépôt GitHub ;
* la documentation du projet ;
* le fichier `requirements.txt` ;
* le service `core/services/nosql_notes.py` ;
* le fichier JavaScript `static/js/menu.js`.

Il ne faut pas capturer :

* les mots de passe ;
* la vraie valeur de `DJANGO_SECRET_KEY` ;
* les variables d'environnement sensibles ;
* les identifiants administrateur complets ;
* les identifiants complets du compte temporaire ;
* les informations privées inutiles.

---

# 19. Règle des trois piliers pour le dossier projet

Pour chaque compétence importante, il faut idéalement préparer :

1. une capture du code ou un extrait de code ;
2. une explication du fonctionnement ;
3. une capture du rendu final si la fonctionnalité produit un résultat visible.

Cette règle concerne notamment :

* les modèles Django ;
* les vues Django ;
* l'administration Django ;
* le compte temporaire de lecture seule ;
* le SQL natif ;
* TinyDB ;
* l'affichage des notes TinyDB ;
* le JavaScript dynamique ;
* Docker ;
* Render ;
* GitHub.

---

# 20. Conclusion

La V1 de Frostia Games permet de présenter un portfolio Django simple, fonctionnel, documenté et déployé.

Le site dispose :

* d'une structure de pages claire ;
* d'un backend Django minimal ;
* d'une base SQLite ;
* d'une expérimentation NoSQL TinyDB ;
* d'un affichage des notes TinyDB sur l'accueil ;
* d'une administration ;
* d'un compte temporaire de lecture seule ;
* d'un lancement local ;
* d'un lancement Docker ;
* d'un déploiement Render ;
* d'une documentation technique ;
* d'un README ;
* d'un fichier de choix techniques ;
* d'un exemple de variables d'environnement.

Le projet reste volontairement limité afin de conserver une base stable, testable, maintenable et présentable.

Les fonctionnalités avancées sont reportées à une version future.

À ce stade, l'objectif principal est de préparer les captures, les preuves et l'intégration propre dans le dossier projet final.


