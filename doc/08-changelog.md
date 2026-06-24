# Changelog - Frostia Games

## Objectif du document

Ce document regroupe les changements importants réalisés pendant le développement du projet **Frostia Games**.

Il permet de conserver une trace claire :

* des étapes réalisées ;
* des fichiers modifiés ;
* des fonctionnalités ajoutées ;
* des vérifications effectuées ;
* de l’état de validation de chaque étape ;
* des choix techniques importants.

---

# 1. Création du projet Django

## Résumé

Mise en place du projet Django servant de base au site Frostia Games.

## Fichiers concernés

* `manage.py`
* `frostia_config/settings.py`
* `frostia_config/urls.py`
* `frostia_config/wsgi.py`
* `frostia_config/asgi.py`

## Modifications réalisées

* Création du projet Django.
* Configuration de base.
* Mise en place de SQLite.
* Configuration des applications Django de base.
* Vérification du lancement local.

## Validation

Commande utilisée :

`python manage.py check`

Résultat attendu :

`System check identified no issues (0 silenced).`

## Statut

Validé.

---

# 2. Création des pages principales

## Résumé

Création des trois pages principales du portfolio.

## Pages créées

* Accueil ;
* Mes créations ;
* Projets jouables.

## Fichiers concernés

* `templates/base.html`
* `templates/pages/home.html`
* `templates/pages/creation.html`
* `templates/pages/projet_jouable.html`
* `core/views.py`
* `core/urls.py`

## Modifications réalisées

* Mise en place du template commun.
* Ajout de la navigation principale.
* Création des vues Django.
* Création des routes.
* Connexion des templates aux vues.

## Validation

Pages testées :

* `/`
* `/mes-creations/`
* `/projets-jouables/`

## Statut

Validé.

---

# 3. Ajout de l’interface visuelle

## Résumé

Création de l’interface utilisateur du site.

## Fichiers concernés

* `static/css/main.css`
* `static/js/menu.js`
* `templates/base.html`
* `templates/pages/home.html`
* `templates/pages/creation.html`
* `templates/pages/projet_jouable.html`

## Modifications réalisées

* Mise en place du thème visuel.
* Création de la sidebar.
* Création du responsive mobile.
* Création des cartes de contenu.
* Ajout du menu mobile.
* Ajout d’une interface préparatoire pour les projets jouables.

## Validation

Tests effectués :

* affichage desktop ;
* affichage mobile ;
* navigation entre les pages ;
* ouverture du menu mobile ;
* lisibilité générale de l’interface.

## Statut

Validé.

---

# 4. Création de l’application `creations`

## Résumé

Ajout d’une application Django dédiée aux créations du portfolio.

## Fichiers concernés

* `creations/models.py`
* `creations/admin.py`
* `creations/apps.py`
* `creations/migrations/`
* `frostia_config/settings.py`

## Modifications réalisées

* Création du modèle `Creation`.
* Ajout des champs du modèle.
* Enregistrement du modèle dans l’administration Django.
* Ajout de l’application dans `INSTALLED_APPS`.
* Création et application des migrations.

## Validation

Commandes utilisées :

* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py check`

## Statut

Validé.

---

# 5. Création de l’application `playable`

## Résumé

Ajout d’une application Django dédiée aux futurs projets jouables.

## Fichiers concernés

* `playable/models.py`
* `playable/admin.py`
* `playable/apps.py`
* `playable/migrations/`
* `frostia_config/settings.py`

## Modifications réalisées

* Création du modèle `PlayableProject`.
* Ajout des champs du modèle.
* Enregistrement du modèle dans l’administration Django.
* Ajout de l’application dans `INSTALLED_APPS`.
* Création et application des migrations.

## Validation

Commandes utilisées :

* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py check`

## Statut

Validé.

---

# 6. Connexion des vues à la base de données

## Résumé

Connexion des pages aux modèles Django afin d’afficher les données enregistrées en base SQLite.

## Fichiers concernés

* `core/views.py`
* `templates/pages/creation.html`
* `templates/pages/projet_jouable.html`

## Modifications réalisées

* Import des modèles `Creation` et `PlayableProject`.
* Récupération des données visibles avec `is_visible=True`.
* Ajout d’un ordre d’affichage avec `order_by`.
* Envoi des données aux templates.
* Affichage des données dans les pages.

## Validation

Pages testées :

* `/mes-creations/`
* `/projets-jouables/`

Les données ajoutées dans l’administration apparaissent bien côté site.

## Statut

Validé.

---

# 7. Mise en place de l’administration Django

## Résumé

Configuration de l’administration Django pour gérer les contenus dynamiques du site.

## Fichiers concernés

* `creations/admin.py`
* `playable/admin.py`

## Modifications réalisées

* Ajout des colonnes visibles dans l’admin.
* Ajout des filtres.
* Ajout des champs de recherche.
* Ajout de la génération automatique du slug.
* Ajout des champs en lecture seule pour les dates.

## Validation

Interface testée :

* `/admin/`

Actions testées :

* ajout d’une création ;
* modification d’une création ;
* ajout d’un projet jouable ;
* modification d’un projet jouable ;
* vérification de l’affichage côté site.

## Statut

Validé.

---

# 8. Ajout de Docker

## Résumé

Ajout d’une configuration Docker simple pour rendre le projet reproductible.

## Fichiers concernés

* `Dockerfile`
* `docker-compose.yml`
* `.dockerignore`
* `requirements.txt`

## Modifications réalisées

* Création du `Dockerfile`.
* Création du fichier `docker-compose.yml`.
* Création du fichier `.dockerignore`.
* Ajout du fichier `requirements.txt`.
* Test du lancement avec Docker Compose.

## Validation

Commande utilisée :

`docker compose up --build`

Résultat obtenu :

* image construite ;
* conteneur créé ;
* serveur Django lancé ;
* site accessible sur `http://127.0.0.1:8000/`.

## Statut

Validé.

---

# 9. Ajout du schéma SQL documentaire

## Résumé

Création d’un fichier SQL documentaire pour présenter la structure de la base.

## Fichiers concernés

* `doc/sql/schema.sql`

## Modifications réalisées

* Ajout des instructions `CREATE TABLE`.
* Ajout d’exemples `INSERT INTO`.
* Ajout de commentaires expliquant le rôle des tables.

## Validation

Le fichier permet de documenter les tables principales :

* `creations_creation`
* `playable_playableproject`

## Statut

Validé.

---

# 10. Ajout de la réflexion NoSQL

## Résumé

Ajout d’un document expliquant la place du NoSQL dans les évolutions futures du projet.

## Fichiers concernés

* `doc/sql/nosql.md`

## Modifications réalisées

* Explication du choix de ne pas intégrer NoSQL dans la V1.
* Présentation des usages possibles du NoSQL.
* Exemple de document MongoDB théorique.
* Ajout du NoSQL dans la roadmap.

## Statut

Validé.

---

# 11. Ajout de la documentation backend

## Résumé

Ajout des documents de justification technique du backend.

## Fichiers concernés

* `doc/00-index-documentation.md`
* `doc/01-modernisation-interface.md`
* `doc/02-journal-de-bord.md`
* `doc/03-modelisation-backend.md`
* `doc/04-docker-et-lancement.md`
* `doc/05-securite-backend.md`
* `doc/06-manuel-utilisateur.md`
* `doc/07-base-de-donnees.md`
* `doc/08-changelog.md`
* `doc/sql/schema.sql`
* `doc/sql/nosql.md`

## Modifications réalisées

* Ajout du MCD simplifié.
* Ajout des cas d’utilisation.
* Ajout des diagrammes de séquence.
* Ajout de la documentation Docker.
* Ajout de la documentation sécurité.
* Ajout du manuel utilisateur.
* Ajout de la documentation base de données.
* Ajout du changelog.
* Mise à jour du journal de bord.
* Mise à jour de la documentation de modernisation.
* Mise à jour de l’index.

## Statut

Validé.

---

# 12. Nettoyage des alertes inutiles VS Code

## Résumé

Correction des faux positifs liés au typage Django dans VS Code / Pylance.

## Fichiers concernés

* `.vscode/settings.json`
* `creations/admin.py`
* `playable/admin.py`

## Modifications réalisées

* Passage du type checking Pylance de `strict` à `basic`.
* Neutralisation des alertes inutiles liées aux types inconnus de Django.
* Ajout de `# type: ignore[type-arg]` sur les classes admin.

## Validation

Les erreurs inutiles ont disparu.

Django reste validé avec :

`python manage.py check`

## Statut

Validé.

---

# 13. Documentation des technologies envisagées

## Résumé

Ajout d’une réflexion sur les technologies envisagées mais non retenues pour la V1.

## Fichiers concernés

* `doc/02-journal-de-bord.md`

## Modifications réalisées

* Ajout d’une partie expliquant les technologies mises de côté.
* Explication du choix de ne pas repartir de zéro avec une nouvelle technologie.
* Présentation du compromis entre préférence technique, stabilité et délai.
* Justification du choix de conserver Django et Python pour la V1.

## Validation

La réflexion technique est maintenant documentée dans le journal de bord.

Elle montre que certaines technologies ont été écartées volontairement afin de préserver le périmètre du projet.

## Statut

Validé.

---

# 14. État actuel

La V1 actuelle contient :

* pages principales fonctionnelles ;
* backend Django fonctionnel ;
* base SQLite ;
* modèles Django ;
* administration Django ;
* données dynamiques ;
* interface préparatoire de projet jouable ;
* Docker ;
* documentation SQL ;
* réflexion NoSQL ;
* documentation de sécurité ;
* manuel utilisateur ;
* changelog ;
* journal de bord ;
* documentation de modernisation.

## Statut général

V1 backend validée.

---

# 15. Prochaines étapes

Les prochaines étapes prévues sont :

1. Vérifier la cohérence finale de la documentation.
2. Ajouter les captures écran.
3. Préparer les extraits de code à intégrer au dossier.
4. Moderniser légèrement l’interface si nécessaire.
5. Préparer la présentation du projet.
6. Prévoir un futur hébergement compatible Django.

---

# 16. Conclusion

Le projet Frostia Games a évolué d’un simple site statique vers une V1 Django complète et documentée.

Le backend reste volontairement simple, mais il est fonctionnel, administrable, relié à une base SQLite, lançable avec Docker et documenté.

Les technologies mises de côté ont été identifiées et expliquées. Le choix de conserver Django/Python dans cette V1 permet de protéger la stabilité du projet et d’éviter de repartir de zéro.

Cette approche permet de présenter un projet stable, maintenable et évolutif.
