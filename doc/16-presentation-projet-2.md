# Présentation du projet 2 - Frostia Games

## Objectif du document

Ce document présente le projet **Frostia Games** comme proposition de second projet.

L'objectif est d'expliquer clairement :

* la nature du projet ;
* son périmètre ;
* les choix techniques réalisés ;
* les fonctionnalités présentes dans la V1 ;
* les éléments ajoutés lors du renforcement du dossier ;
* les limites assumées ;
* les évolutions possibles.

Ce document sert de base pour présenter le projet de manière claire, structurée et défendable.

Il a été mis à jour après le renforcement du dossier afin d’intégrer :

* le SQL natif documentaire ;
* TinyDB ;
* les notes de progression affichées sur l’accueil ;
* le JavaScript du menu mobile ;
* le compte temporaire de lecture seule ;
* la documentation complémentaire `docs/` ;
* les documents de conception ;
* les preuves techniques à préparer.

---

# 1. Présentation générale

**Frostia Games** est un portfolio développé avec **Django**.

Le projet a pour objectif de présenter des créations vidéoludiques actuelles et futures dans une interface web simple, moderne, documentée et évolutive.

Il ne s'agit pas d'un simple site statique.

Le projet repose sur une vraie structure Django comprenant :

* une architecture backend ;
* une base de données SQLite ;
* une administration Django ;
* des modèles de données ;
* des vues Django ;
* des routes ;
* des templates HTML ;
* des fichiers statiques ;
* du JavaScript léger ;
* une expérimentation NoSQL avec TinyDB ;
* un déploiement en ligne ;
* une documentation technique complète ;
* une documentation de conception ;
* des preuves techniques.

---

# 2. Positionnement du projet

Frostia Games doit être présenté comme une **V1 fonctionnelle et maîtrisée**.

Le projet ne doit pas être présenté comme une plateforme finale complète.

Formulation correcte :

```text
Frostia Games est une première version fonctionnelle d'un portfolio Django destiné à présenter mes projets vidéoludiques. Le projet est déployé en ligne, documenté et conçu pour évoluer progressivement.
```

Autre formulation correcte :

```text
Frostia Games est une V1 stable et documentée. Elle démontre une base Django, une base SQLite, une administration, un déploiement Render, une expérimentation NoSQL légère et une organisation de preuves pour le dossier projet.
```

Formulation à éviter :

```text
Frostia Games est une plateforme complète de gestion de projets de jeux vidéo.
```

La dernière formulation serait trop ambitieuse par rapport au périmètre réel de la V1.

---

# 3. Pourquoi ce projet peut être proposé comme projet 2

Frostia Games peut être proposé comme second projet car il présente un travail différent et complémentaire du premier dossier projet.

Le projet met en avant :

* la création d'un projet Django ;
* l'organisation d'une architecture web ;
* la gestion de pages publiques ;
* la mise en place d'un backend simple ;
* l'utilisation d'une base de données SQL ;
* l'utilisation de l'administration Django ;
* l'affichage dynamique de contenus ;
* l'utilisation d'un NoSQL léger avec TinyDB ;
* la documentation de SQL natif ;
* la documentation du JavaScript ;
* la documentation de conception ;
* la mise en place d'un compte temporaire de lecture seule ;
* la documentation technique ;
* le déploiement en ligne avec Render ;
* la réflexion sur les limites et les évolutions.

Ce projet montre une autre facette du développement web, plus orientée :

* backend Django ;
* structuration ;
* documentation ;
* base de données ;
* déploiement ;
* sécurité minimale ;
* capacité à cadrer un périmètre.

---

# 4. Objectif de la V1

L'objectif de la V1 n'est pas de créer une plateforme complète.

L'objectif est de produire une première version :

* fonctionnelle ;
* stable ;
* documentée ;
* déployée ;
* consultable en ligne ;
* évolutive ;
* défendable dans un dossier projet.

Cette V1 sert de fondation pour présenter des projets vidéoludiques et préparer de futures améliorations.

Elle permet aussi de montrer que le projet peut être construit progressivement sans chercher à tout ajouter dès le départ.

---

# 5. Fonctionnalités réalisées

La V1 contient les fonctionnalités suivantes :

* page d'accueil ;
* page de présentation des créations ;
* page des projets jouables à venir ;
* navigation principale ;
* menu responsive ;
* menu mobile JavaScript ;
* interface publique ;
* modèles Django ;
* administration Django ;
* base SQLite ;
* affichage dynamique de certaines données ;
* expérimentation NoSQL avec TinyDB ;
* affichage de notes de progression sur l’accueil ;
* compte temporaire de lecture seule ;
* déploiement Render ;
* documentation de déploiement ;
* documentation d'architecture ;
* documentation de tests ;
* documentation des limites et évolutions ;
* documentation SQL native ;
* documentation NoSQL ;
* documentation frontend ;
* documentation backend ;
* documents de conception.

---

# 6. Pages principales

Le site contient trois pages publiques principales.

| Page                     | Rôle                                                            |
| ------------------------ | --------------------------------------------------------------- |
| Accueil                  | Présenter le portfolio Frostia Games et les notes de progression |
| Mes créations            | Présenter les créations et projets en cours                     |
| Projets jouables à venir | Présenter les futurs projets jouables ou démonstrations prévues |

Ces pages permettent de présenter le projet de manière claire sans surcharger la V1.

La page d’accueil a été renforcée avec l’affichage de notes issues de TinyDB.

---

# 7. Backend Django

Le projet utilise Django comme framework principal.

Django permet de structurer le projet autour :

* des routes ;
* des vues ;
* des templates ;
* des modèles ;
* des migrations ;
* de l'administration ;
* de la base de données ;
* des fichiers statiques ;
* de la configuration de production.

Le backend reste volontairement simple pour cette V1, mais il montre déjà une organisation réelle et exploitable.

Fichiers importants :

```text
core/views.py
core/urls.py
creations/models.py
playable/models.py
creations/admin.py
playable/admin.py
```

---

# 8. Base de données SQL

La V1 utilise SQLite comme base principale.

La base de données permet de gérer certains contenus du projet, notamment :

* les créations ;
* les projets jouables à venir ;
* les utilisateurs Django ;
* les permissions Django ;
* les groupes Django.

SQLite est suffisant pour cette première version, car le projet reste un portfolio simple.

Une migration vers PostgreSQL pourra être envisagée plus tard si le projet évolue vers une version plus avancée.

---

# 9. Modèles Django

Deux modèles principaux sont utilisés dans le projet.

## `Creation`

Le modèle `Creation` permet de représenter une création ou un projet présenté dans le portfolio.

Il contient notamment :

* un titre ;
* un slug ;
* une lettre alphabétique ;
* un nom de code ;
* un type de projet ;
* un statut ;
* une description courte ;
* un champ de visibilité ;
* des dates de création et de modification.

## `PlayableProject`

Le modèle `PlayableProject` permet de représenter un futur contenu jouable ou une démonstration prévue.

Il contient notamment :

* un titre ;
* un slug ;
* un statut ;
* un type de contenu ;
* une description courte ;
* un message de disponibilité ;
* un état de disponibilité ;
* un champ de visibilité ;
* des dates de création et de modification.

Ces deux modèles permettent de montrer que le site ne repose pas uniquement sur du HTML statique.

---

# 10. SQL natif documentaire

Des fichiers SQL natifs ont été ajoutés pour renforcer le dossier projet.

Fichiers concernés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers permettent de montrer :

* la structure SQL des tables ;
* les champs principaux ;
* des exemples `CREATE TABLE` ;
* des exemples `INSERT INTO` ;
* le lien entre modèles Django, migrations, ORM et SQL.

Le SQL natif reste documentaire.

Dans le fonctionnement réel du projet, les tables sont créées par les migrations Django.

---

# 11. NoSQL TinyDB

Une expérimentation NoSQL légère a été ajoutée avec TinyDB.

TinyDB permet de stocker des notes de progression dans un fichier JSON.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

Commande de test :

```powershell
python -m scripts.demo_tinydb_notes
```

TinyDB ne remplace pas SQLite.

SQLite reste la base principale du projet.

TinyDB sert à démontrer une logique NoSQL simple, limitée et adaptée au périmètre de la V1.

---

# 12. Affichage des notes TinyDB

Les notes TinyDB sont affichées sur la page d’accueil.

Chaîne technique :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

Cette fonctionnalité permet de montrer :

* une lecture de données JSON ;
* un service Python séparé ;
* une intégration dans une vue Django ;
* un affichage dans un template ;
* une preuve NoSQL visible.

---

# 13. Administration Django

L'administration Django est fonctionnelle.

Elle permet de gérer les données du projet depuis l'interface `/admin/`.

Elle permet notamment :

* d’ajouter une création ;
* de modifier une création ;
* de masquer une création ;
* d’ajouter un futur projet jouable ;
* de modifier un futur projet jouable ;
* de contrôler les contenus visibles sur le site.

L'accès administrateur reste privé.

Aucun identifiant ni mot de passe n'est publié dans le dépôt GitHub ou dans la documentation publique.

---

# 14. Compte temporaire de lecture seule

Un compte temporaire de lecture seule a été mis en place pour l’évaluation.

Ce compte permet une consultation limitée de l’administration Django sans donner les pleins droits administrateur.

Il peut consulter :

* les créations ;
* les projets jouables.

Il ne doit pas donner accès :

* aux utilisateurs ;
* aux groupes ;
* aux permissions sensibles ;
* aux réglages internes ;
* aux secrets du projet.

Les identifiants réels ne doivent jamais être écrits dans la documentation publique.

Ils peuvent être transmis séparément uniquement si l’évaluateur les demande.

---

# 15. Frontend et JavaScript

La partie frontend repose sur :

* les templates Django ;
* HTML ;
* CSS ;
* JavaScript léger.

Le fichier JavaScript principal est :

```text
static/js/menu.js
```

Il sert à gérer le menu mobile.

Il permet notamment :

* d’ouvrir le menu ;
* de fermer le menu ;
* de modifier l’état visuel de la sidebar ;
* de mettre à jour `aria-expanded` ;
* de fermer le menu après clic sur un lien.

Le JavaScript est documenté dans :

```text
docs/frontend/javascript-menu-mobile.md
```

---

# 16. Déploiement

Le projet est déployé sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

La configuration Render utilise :

```bash
bash build.sh
```

comme commande de build, puis :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

comme commande de démarrage.

Le déploiement permet de montrer que le projet fonctionne en dehors de l'environnement local.

Il permet aussi de montrer :

* l’installation des dépendances ;
* la collecte des fichiers statiques ;
* l’application des migrations ;
* l’utilisation de Gunicorn ;
* l’utilisation de WhiteNoise ;
* l’utilisation de variables d’environnement.

---

# 17. Documentation produite

Le projet dispose d'une documentation technique organisée.

Documents principaux :

* index de documentation ;
* journal de bord ;
* modernisation de l'interface ;
* modélisation backend ;
* Docker et lancement ;
* sécurité backend ;
* manuel utilisateur ;
* base de données ;
* changelog ;
* déploiement Render ;
* bilan V1 ;
* installation locale ;
* architecture ;
* tests et vérifications ;
* captures et preuves ;
* limites et évolutions ;
* présentation du projet 2 ;
* pistes explorées et non retenues ;
* plan de finalisation V1 ;
* renforcement du dossier projet.

Cette documentation montre :

* les choix réalisés ;
* les problèmes rencontrés ;
* les solutions appliquées ;
* les évolutions possibles ;
* les limites assumées ;
* les preuves à préparer.

---

# 18. Documentation complémentaire `docs/`

Un dossier complémentaire `docs/` a été ajouté pour renforcer le dossier projet.

Structure :

```text
docs/
├── backend/
├── conception/
├── frontend/
├── nosql/
├── preuves/
└── sql/
```

## `docs/backend/`

Contient :

```text
modeles-django.md
vues-et-routes.md
```

Ces fichiers expliquent les modèles, les vues et les routes.

## `docs/conception/`

Contient :

```text
mcd.md
cas-utilisation.md
diagramme-sequence.md
```

Ces fichiers renforcent la partie conception.

## `docs/frontend/`

Contient :

```text
javascript-menu-mobile.md
```

Ce fichier documente le JavaScript du menu mobile.

## `docs/nosql/`

Contient :

```text
tinydb-integration.md
```

Ce fichier documente TinyDB.

## `docs/sql/`

Contient :

```text
create_tables_creations.sql
create_tables_playable.sql
exemples_insert.sql
sql-natif.md
```

Ces fichiers documentent le SQL natif.

---

# 19. Choix techniques

Les choix techniques principaux sont :

| Élément            | Choix                                    |
| ------------------ | ---------------------------------------- |
| Framework          | Django                                   |
| Langage            | Python                                   |
| Base principale    | SQLite                                   |
| NoSQL léger        | TinyDB                                   |
| Interface          | Templates Django, HTML, CSS, JavaScript |
| Déploiement        | Render                                   |
| Serveur production | Gunicorn                                 |
| Fichiers statiques | WhiteNoise                               |
| Versioning         | Git et GitHub                            |
| Documentation      | Markdown                                 |

Ces choix permettent de garder un projet simple, stable et compréhensible.

Ils montrent aussi que le projet peut évoluer progressivement.

---

# 20. Compétences mises en avant

Le projet permet de montrer plusieurs compétences :

* création d'un projet Django ;
* organisation d'une structure web ;
* gestion des routes ;
* création de vues ;
* utilisation de templates ;
* création de modèles ;
* utilisation de migrations ;
* gestion de l'administration Django ;
* utilisation d'une base SQLite ;
* documentation SQL native ;
* utilisation de TinyDB ;
* création d’un service Python ;
* création d’un script de démonstration ;
* intégration de données dans un template ;
* configuration des fichiers statiques ;
* JavaScript de menu mobile ;
* déploiement avec Render ;
* utilisation de variables d'environnement ;
* sécurité minimale ;
* compte temporaire de lecture seule ;
* documentation technique ;
* documentation de conception ;
* cadrage du périmètre ;
* gestion des limites et évolutions.

---

# 21. Limites assumées

Certaines fonctionnalités ne sont pas intégrées dans la V1.

Éléments reportés :

* PostgreSQL ;
* interface admin personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* graphiques Plotly.js ;
* statistiques avancées ;
* espace privé complet ;
* tests automatisés complets ;
* API REST ;
* MongoDB ;
* mini-jeu intégré ;
* système de score ;
* téléchargement public de projet jouable.

Ces éléments ne sont pas oubliés.

Ils sont volontairement reportés afin de conserver une V1 stable et maîtrisable.

Le compte temporaire de lecture seule et TinyDB ne sont plus présentés comme des éléments absents, car ils ont été ajoutés de manière limitée.

---

# 22. Pourquoi ne pas avoir tout ajouté maintenant

Ajouter trop de fonctionnalités dans cette V1 aurait augmenté les risques :

* perte de stabilité ;
* complexité excessive ;
* dette technique ;
* documentation difficile à maintenir ;
* projet trop long à terminer ;
* fonctionnalités commencées mais non finalisées ;
* risque de transformer le projet en usine à gaz.

Le choix a donc été de privilégier une V1 propre, testable, documentée et déployée.

Les ajouts récents ont été limités à des éléments utiles pour renforcer le dossier sans transformer le projet en plateforme trop lourde.

---

# 23. État actuel

État actuel de la V1 :

| Partie                            | État                                      |
| --------------------------------- | ----------------------------------------- |
| Projet Django                     | Fonctionnel                               |
| Pages publiques                   | Fonctionnelles                            |
| Backend                           | Fonctionnel pour V1                       |
| Base SQLite                       | Fonctionnelle                             |
| Admin Django                      | Fonctionnel                               |
| Compte temporaire lecture seule   | Fonctionnel et limité                     |
| TinyDB                            | Fonctionnel comme expérimentation NoSQL   |
| Notes TinyDB sur l’accueil        | Fonctionnelles                            |
| JavaScript menu mobile            | Fonctionnel                               |
| SQL natif documentaire            | En place                                  |
| Déploiement Render                | Fonctionnel                               |
| Documentation principale          | Avancée                                   |
| Documentation complémentaire      | En place                                  |
| Responsive                        | Fonctionnel mais améliorable              |
| Sécurité minimale                 | Correcte pour V1                          |

---

# 24. Prochaines étapes avant présentation

Avant de présenter officiellement ce projet comme projet 2, il reste à finaliser :

* les captures d'écran ;
* la vérification finale du README à la racine ;
* la vérification du fichier `CHOIX_TECHNIQUES.md` ;
* les maquettes Figma si nécessaires ;
* la relecture des textes ;
* la vérification mobile ;
* la vérification du compte temporaire de lecture seule ;
* la capture de TinyDB ;
* la capture du SQL natif ;
* la capture du JavaScript ;
* le dossier projet final ;
* les annexes ;
* le commit final propre.

Ces étapes relèvent de la finalisation du dossier, pas de l’ajout de nouvelles fonctionnalités lourdes.

---

# 25. Preuves à préparer

Pour défendre le projet, les preuves importantes sont :

* capture de la page d’accueil ;
* capture des notes TinyDB sur l’accueil ;
* capture de la page Mes créations ;
* capture de la page Projets jouables ;
* capture du menu mobile ;
* capture de l’administration Django ;
* capture du compte temporaire de lecture seule ;
* capture du service Render actif ;
* capture des commandes Render ;
* capture de `python manage.py check` ;
* capture de `python -m scripts.demo_tinydb_notes` ;
* capture des modèles Django ;
* capture de `core/views.py` ;
* capture de `core/services/nosql_notes.py` ;
* capture de `scripts/demo_tinydb_notes.py` ;
* capture de `static/js/menu.js` ;
* capture des fichiers SQL natifs ;
* capture de la documentation `doc/` ;
* capture de la documentation `docs/`.

Aucune preuve ne doit afficher :

* mot de passe ;
* clé secrète ;
* vraie variable sensible ;
* identifiant administrateur complet ;
* identifiant du compte temporaire ;
* information privée inutile.

---

# 26. Valeur du projet

Frostia Games montre une démarche complète :

```text
conception
développement
backend
base de données SQL
NoSQL léger
JavaScript
tests
documentation
déploiement
preuves
bilan
évolutions prévues
```

Le projet montre aussi une capacité à limiter le périmètre pour éviter d'ajouter trop de fonctionnalités en même temps.

Cette démarche est importante, car un projet réussi n'est pas seulement un projet avec beaucoup d'idées.

C'est aussi un projet stable, compréhensible, terminé et présentable.

---

# 27. Bilan défendable à l’oral

Pour présenter le projet à l’oral, le message principal peut être :

```text
J’ai choisi de construire une V1 Django stable plutôt qu’une plateforme trop large. Le projet contient des pages publiques, une base SQLite, une administration Django, un déploiement Render, une expérimentation TinyDB, du SQL natif documentaire et une documentation complète. Les limites sont assumées pour protéger la stabilité du projet.
```

Ce bilan permet de montrer :

* la maîtrise du périmètre ;
* la capacité à documenter ;
* la capacité à déployer ;
* la capacité à distinguer une V1 d’une version finale ;
* la capacité à intégrer des demandes sans casser l’architecture.

---

# 28. Conclusion

Frostia Games peut être proposé comme second projet car il possède une base technique réelle, un backend Django, une administration, une base de données, une expérimentation NoSQL, un déploiement en ligne et une documentation complète.

Le projet reste volontairement limité, mais il est stable, cohérent et défendable.

Il montre une capacité à créer un projet web complet dans son périmètre, à le documenter, à le déployer et à préparer ses futures évolutions sans élargir trop vite le périmètre.

À ce stade, la priorité n’est plus d’ajouter de nouvelles fonctionnalités lourdes.

La priorité est de finaliser les captures, les preuves, les annexes et le dossier projet final.
