# Changelog - Frostia Games

## Objectif du document

Ce document regroupe les changements importants réalisés pendant le développement du projet **Frostia Games**.

Il permet de conserver une trace claire :

* des étapes réalisées ;
* des fichiers modifiés ;
* des fonctionnalités ajoutées ;
* des vérifications effectuées ;
* de l’état de validation de chaque étape ;
* des choix techniques importants ;
* des éléments volontairement reportés ;
* du déploiement en ligne ;
* des fichiers de documentation ajoutés au projet.

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

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

## Statut

Validé.

---

# 2. Création des applications Django internes

## Résumé

Création des applications internes utilisées par le projet.

## Applications créées

* `core`
* `creations`
* `playable`

## Fichiers concernés

* `core/`
* `creations/`
* `playable/`
* `frostia_config/settings.py`

## Modifications réalisées

* Création de l’application `core` pour les vues principales.
* Création de l’application `creations` pour les créations du portfolio.
* Création de l’application `playable` pour les futurs projets jouables.
* Ajout des applications dans `INSTALLED_APPS`.

## Statut

Validé.

---

# 3. Création des pages principales

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

```text
/
 /mes-creations/
 /projets-jouables/
```

## Statut

Validé.

---

# 4. Ajout de l’interface visuelle

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
* Amélioration progressive de la lisibilité des pages.
* Adaptation de l’interface à l’affichage des données Django.

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

# 5. Modernisation de l’interface

## Résumé

Modernisation de l’interface afin de passer d’un wireframe simple à une présentation plus professionnelle.

## Fichiers concernés

* `static/css/main.css`
* `templates/base.html`
* `templates/pages/home.html`
* `templates/pages/creation.html`
* `templates/pages/projet_jouable.html`
* `doc/01-modernisation-interface.md`

## Modifications réalisées

* Harmonisation des couleurs bleues.
* Ajout d’un fond dégradé.
* Amélioration des cartes.
* Amélioration de la sidebar.
* Amélioration du footer.
* Amélioration de l’état actif de navigation.
* Préparation du responsive mobile.
* Documentation de la modernisation dans un fichier dédié.

## Statut

Validé.

---

# 6. Création du modèle `Creation`

## Résumé

Ajout d’un modèle Django dédié aux créations du portfolio.

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

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

## Statut

Validé.

---

# 7. Création du modèle `PlayableProject`

## Résumé

Ajout d’un modèle Django dédié aux futurs projets jouables.

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

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

## Statut

Validé.

---

# 8. Connexion des vues à la base de données

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

```text
/mes-creations/
/projets-jouables/
```

Résultat :

* les données ajoutées dans l’administration apparaissent bien côté site ;
* les contenus invisibles ne sont pas affichés ;
* les pages restent accessibles.

## Statut

Validé.

---

# 9. Mise en place de l’administration Django

## Résumé

Configuration de l’administration Django pour gérer les contenus dynamiques du site.

## Fichiers concernés

* `creations/admin.py`
* `playable/admin.py`

## Modifications réalisées

* Ajout des colonnes visibles dans l’administration.
* Ajout des filtres.
* Ajout des champs de recherche.
* Ajout de la génération automatique du slug.
* Ajout des champs en lecture seule pour les dates.
* Amélioration de la gestion des contenus depuis l’interface `/admin/`.

## Validation

Interface testée :

```text
/admin/
```

Actions testées :

* ajout d’une création ;
* modification d’une création ;
* ajout d’un projet jouable ;
* modification d’un projet jouable ;
* vérification de l’affichage côté site.

## Statut

Validé.

---

# 10. Ajout de l’interface préparatoire des projets jouables

## Résumé

Préparation de la page **Projets jouables** sans activer de vrai upload serveur.

## Fichiers concernés

* `templates/pages/projet_jouable.html`
* `static/css/main.css`
* `static/js/menu.js`
* `core/views.py`
* `playable/models.py`

## Modifications réalisées

* Ajout d’une zone de lecteur préparatoire.
* Ajout d’un bouton Lecture affichant un message.
* Ajout d’un bouton de sélection de fichier local.
* Affichage du nom du fichier sélectionné.
* Message indiquant que l’upload réel n’est pas implanté.
* Affichage des projets jouables enregistrés en base.

## Validation

Tests effectués :

* page accessible ;
* bouton Lecture fonctionnel ;
* sélection locale de fichier fonctionnelle ;
* aucun fichier envoyé au serveur ;
* message de limite visible.

## Statut

Validé.

---

# 11. Ajout de Docker

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

```powershell
docker compose up --build
```

Résultat obtenu :

* image construite ;
* conteneur créé ;
* serveur Django lancé ;
* site accessible sur `http://127.0.0.1:8000/`.

## Statut

Validé.

---

# 12. Ajout du schéma SQL documentaire

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

# 13. Ajout de la réflexion NoSQL

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

# 14. Ajout de la documentation backend initiale

## Résumé

Ajout des premiers documents de justification technique du backend.

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

# 15. Nettoyage des alertes inutiles VS Code

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

```powershell
python manage.py check
```

## Statut

Validé.

---

# 16. Documentation des technologies envisagées

## Résumé

Ajout d’une réflexion sur les technologies envisagées mais non retenues pour la V1.

## Fichiers concernés

* `doc/02-journal-de-bord.md`
* `CHOIX_TECHNIQUES.md`
* `doc/17-pistes-explorees-et-non-retenues.md`

## Modifications réalisées

* Ajout d’une partie expliquant les technologies mises de côté.
* Explication du choix de ne pas repartir de zéro avec une nouvelle technologie.
* Présentation du compromis entre préférence technique, stabilité et délai.
* Justification du choix de conserver Django et Python pour la V1.
* Documentation du report de C# / ASP.NET / Razor.
* Documentation des risques de scope creep et d’usine à gaz.

## Validation

La réflexion technique est maintenant documentée dans plusieurs fichiers.

Elle montre que certaines technologies ont été écartées volontairement afin de préserver le périmètre du projet.

## Statut

Validé.

---

# 17. Préparation du déploiement Render

## Résumé

Préparation du projet pour une mise en ligne sur Render.

## Fichiers concernés

* `requirements.txt`
* `build.sh`
* `frostia_config/settings.py`
* `frostia_config/wsgi.py`
* `.gitignore`
* `.env.example`
* `doc/09-deploiement-render.md`

## Modifications réalisées

* Ajout de Gunicorn.
* Ajout ou vérification de WhiteNoise.
* Création ou correction du fichier `build.sh`.
* Configuration du projet pour Render.
* Préparation des variables d’environnement.
* Vérification de la commande WSGI.
* Préparation de la commande de build.
* Préparation de la commande de démarrage.

## Commande de build Render

```bash
bash build.sh
```

## Commande de démarrage Render

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

## Statut

Validé.

---

# 18. Déploiement Render

## Résumé

Mise en ligne de la V1 sur Render.

## URL de production

```text
https://frostia-games.onrender.com
```

## Modifications ou réglages réalisés

* Configuration du service Render.
* Configuration des variables d’environnement.
* Configuration du Build Command.
* Configuration du Start Command.
* Vérification des logs Render.
* Vérification de l’accès au site.
* Vérification de l’accès à l’administration Django.

## Variables d’environnement utilisées

* `DJANGO_DEBUG`
* `DJANGO_SECRET_KEY`
* `DJANGO_SUPERUSER_USERNAME`
* `DJANGO_SUPERUSER_EMAIL`
* `DJANGO_SUPERUSER_PASSWORD`

## Validation

Résultat attendu :

* le site est accessible en ligne ;
* les pages principales se chargent ;
* l’administration est accessible ;
* les fichiers statiques sont chargés ;
* le service Render indique que l’application est active.

## Statut

Validé.

---

# 19. Ajout de la documentation Render

## Résumé

Ajout d’un document dédié au déploiement Render.

## Fichier concerné

* `doc/09-deploiement-render.md`

## Modifications réalisées

* Explication de la configuration Render.
* Description du rôle de `build.sh`.
* Description de Gunicorn.
* Description des variables d’environnement.
* Ajout des commandes utilisées.
* Ajout des vérifications après déploiement.
* Ajout des limites de l’offre gratuite Render.

## Statut

Validé.

---

# 20. Ajout du bilan V1

## Résumé

Ajout d’un bilan de la V1 du projet.

## Fichier concerné

* `doc/10-bilan-v1-frostia-games.md`

## Modifications réalisées

* Présentation de l’état global du projet.
* Liste des éléments fonctionnels.
* Liste des éléments encore améliorables.
* Liste des éléments volontairement reportés.
* Estimation de l’avancement de la V1.
* Clarification du fait que la V1 n’est pas une plateforme complète.

## Statut

Validé.

---

# 21. Ajout de la documentation finale

## Résumé

Ajout des documents complémentaires pour finaliser la documentation du projet.

## Fichiers concernés

* `doc/11-installation-locale.md`
* `doc/12-architecture.md`
* `doc/13-test-et-vérification.md`
* `doc/14-Capture-et Preuve.md`
* `doc/15-limites-et-évolutions.md`
* `doc/16-presentation-projet-2.md`
* `doc/17-pistes-explorees-et-non-retenues.md`
* `doc/18-plan-finalisation-v1.md`

## Modifications réalisées

* Ajout de la documentation d’installation locale.
* Ajout de la documentation d’architecture.
* Ajout de la documentation de tests.
* Ajout de la checklist de captures et preuves.
* Ajout de la documentation des limites et évolutions.
* Ajout de la présentation du projet 2.
* Ajout des pistes explorées et non retenues.
* Ajout du plan de finalisation V1.

## Statut

Validé.

---

# 22. Ajout des fichiers racine du projet

## Résumé

Ajout ou mise à jour des fichiers importants à la racine du dépôt GitHub.

## Fichiers concernés

* `README.md`
* `CHOIX_TECHNIQUES.md`
* `.env.example`
* `.gitignore`
* `build.sh`

## Modifications réalisées

* Création ou mise à jour du README.
* Création ou mise à jour du fichier de choix techniques.
* Ajout du fichier `.env.example`.
* Vérification du fichier `.gitignore`.
* Vérification du fichier `build.sh`.

## Rôle des fichiers

`README.md` présente rapidement le projet, son installation, son lancement, son déploiement et ses limites.

`CHOIX_TECHNIQUES.md` explique les décisions techniques, les pistes envisagées et les choix volontairement reportés.

`.env.example` documente les variables d’environnement sans exposer les vraies valeurs sensibles.

`.gitignore` évite d’envoyer dans GitHub les fichiers sensibles ou inutiles.

`build.sh` prépare le projet pendant le déploiement Render.

## Statut

Validé.

---

# 23. Mise à jour de la sécurité backend

## Résumé

Mise à jour de la documentation sécurité pour tenir compte du déploiement Render.

## Fichier concerné

* `doc/05-securite-backend.md`

## Modifications réalisées

* Ajout du rôle des variables d’environnement.
* Ajout de `.env.example`.
* Ajout de `.gitignore`.
* Ajout de `DJANGO_DEBUG=False`.
* Ajout de la gestion de `DJANGO_SECRET_KEY`.
* Ajout de la protection des identifiants administrateur.
* Ajout de WhiteNoise et `collectstatic`.
* Ajout des limites de sécurité de la V1.

## Statut

Validé.

---

# 24. Mise à jour de la documentation Docker

## Résumé

Mise à jour de la documentation Docker pour distinguer Docker et Render.

## Fichier concerné

* `doc/04-docker-et-lancement.md`

## Modifications réalisées

* Clarification du rôle de Docker.
* Explication du lancement local.
* Explication du lancement Docker.
* Ajout du lien avec Render.
* Ajout du rôle de `build.sh`.
* Ajout des variables d’environnement.
* Clarification du fait que Docker n’est pas la méthode de production actuelle.

## Statut

Validé.

---

# 25. Mise à jour du manuel utilisateur

## Résumé

Mise à jour du manuel utilisateur pour inclure le site en ligne.

## Fichier concerné

* `doc/06-manuel-utilisateur.md`

## Modifications réalisées

* Ajout de l’URL Render.
* Ajout des pages en ligne.
* Ajout de l’administration en ligne.
* Ajout des vérifications avant démonstration.
* Ajout des fichiers utiles : `README.md`, `CHOIX_TECHNIQUES.md`, `.env.example`, `build.sh`.
* Ajout des conseils pour les captures d’écran.

## Statut

Validé.

---

# 26. Mise à jour de la documentation base de données

## Résumé

Mise à jour de la documentation base de données.

## Fichier concerné

* `doc/07-base-de-donnees.md`

## Modifications réalisées

* Ajout du lien avec Render.
* Ajout des variables d’environnement.
* Ajout du rôle de `.gitignore`.
* Ajout du lien avec `README.md`.
* Ajout du lien avec `CHOIX_TECHNIQUES.md`.
* Clarification des limites de SQLite.
* Clarification du report de PostgreSQL.

## Statut

Validé.

---

# 27. Mise à jour de l’index de documentation

## Résumé

Mise à jour de l’index pour qu’il corresponde à l’état réel de la documentation.

## Fichier concerné

* `doc/00-index-documentation.md`

## Modifications réalisées

* Ajout des documents `09` à `18`.
* Suppression de l’ancienne référence à `installation-django.md`.
* Ajout de `11-installation-locale.md`.
* Ajout des fichiers racine importants.
* Mise à jour de l’état actuel de la V1.
* Mise à jour des limites et prochaines actions.

## Statut

Validé.

---

# 28. Mise à jour du journal de bord

## Résumé

Mise à jour du journal de bord pour intégrer les dernières étapes du projet.

## Fichier concerné

* `doc/02-journal-de-bord.md`

## Modifications réalisées

* Ajout de la préparation du déploiement Render.
* Ajout du déploiement Render.
* Ajout des fichiers racine.
* Ajout de la documentation finale.
* Ajout de la synchronisation GitHub.
* Mise à jour de l’état actuel du projet.

## Statut

Validé.

---

# 29. Synchronisation Git et GitHub

## Résumé

Sauvegarde du projet avec Git et synchronisation sur GitHub.

## Commandes utilisées

```powershell
git status
git add .
git commit -m "Complete Frostia Games documentation"
git push
git status
```

## Résultat attendu

```text
nothing to commit, working tree clean
```

## Statut

Validé.

---

# 30. État actuel de la V1

## Résumé

La V1 actuelle contient :

* pages principales fonctionnelles ;
* backend Django fonctionnel ;
* base SQLite ;
* modèles Django ;
* administration Django ;
* données dynamiques ;
* interface préparatoire de projet jouable ;
* Docker ;
* déploiement Render ;
* documentation SQL ;
* réflexion NoSQL ;
* documentation de sécurité ;
* manuel utilisateur ;
* changelog ;
* journal de bord ;
* documentation de modernisation ;
* documentation d’architecture ;
* documentation de tests ;
* documentation de déploiement ;
* README racine ;
* fichier de choix techniques ;
* fichier `.env.example`.

## Statut général

V1 fonctionnelle, documentée et déployée.

---

# 31. Prochaines étapes

Les prochaines étapes prévues sont limitées à la finalisation :

1. Vérifier la cohérence finale de la documentation.
2. Vérifier le README à la racine.
3. Vérifier le fichier `CHOIX_TECHNIQUES.md`.
4. Tester le site en ligne sur Render.
5. Tester l’administration Django.
6. Vérifier le responsive mobile.
7. Préparer les captures d’écran.
8. Préparer les extraits de code à intégrer au dossier.
9. Préparer la présentation du projet.
10. Effectuer un dernier commit si des corrections sont faites.

---

# 32. Éléments volontairement reportés

Les éléments suivants sont reportés à une version future :

* PostgreSQL ;
* compte jury temporaire ;
* administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* lecteur vidéo réel ;
* fiches projet détaillées ;
* API REST ;
* comptes utilisateurs publics ;
* rôles avancés ;
* base NoSQL connectée ;
* graphiques Plotly.js ;
* tests automatisés complets ;
* système de sauvegarde automatique.

Ces éléments ne sont pas oubliés.

Ils sont volontairement reportés afin de conserver une V1 stable, maintenable et présentable.

---

# 33. Conclusion

Le projet Frostia Games a évolué d’un simple site statique vers une V1 Django complète, documentée et déployée.

Le backend reste volontairement simple, mais il est fonctionnel, administrable, relié à une base SQLite, lançable avec Docker et disponible en ligne via Render.

Les technologies mises de côté ont été identifiées et expliquées.

Le choix de conserver Django/Python dans cette V1 permet de protéger la stabilité du projet et d’éviter de repartir de zéro.

Cette approche permet de présenter un projet stable, maintenable, documenté, déployé et évolutif.
