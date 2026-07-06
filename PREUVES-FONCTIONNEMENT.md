# Preuves de fonctionnement — Frostia Games

## Objectif du document

Ce document présente les preuves visuelles réalisées pour le projet **Frostia Games**.

L’objectif de ce fichier est de centraliser et référencer les captures montrant que la V1 du projet est fonctionnelle, organisée, documentée, testée et déployée.

Les captures sont regroupées dans le dossier suivant :

```text
Preuve De Fonctionnement/
```

Toutes les captures ne sont pas intégrées directement dans le corps du dossier projet afin de ne pas l’alourdir.

Ce fichier sert donc d’index des preuves.

---

# 1. Objectif des preuves

Les captures présentes dans ce dossier servent à démontrer plusieurs points importants du projet :

* le site fonctionne en local ;
* le site peut être lancé avec Docker ;
* le site est déployé en ligne sur Render ;
* l’interface d’administration Django est accessible ;
* les pages principales du site sont visibles ;
* le responsive mobile fonctionne ;
* les maquettes Figma ont été préparées ;
* le projet est suivi avec Git et sauvegardé sur GitHub ;
* la base SQL est documentée ;
* les extraits SQL natifs sont présents ;
* la partie NoSQL / TinyDB est documentée ;
* les éléments techniques sont accompagnés d’explications.

Ces preuves permettent de montrer que la V1 de Frostia Games ne se limite pas à du code.

Elle possède aussi :

* un environnement d’exécution ;
* une organisation documentaire ;
* une base de données relationnelle ;
* une démonstration NoSQL légère ;
* un déploiement en ligne ;
* des preuves visuelles classées.

---

# 2. Organisation du dossier de preuves

Les captures sont classées par catégorie afin de faciliter la lecture et la vérification du projet.

Structure générale :

```text
Preuve De Fonctionnement/
├── Docker/
├── Figma/
├── Github/
├── Render/
├── SiteWeb_FrostiaGame/
│   ├── Admin/
│   ├── Desktop/
│   └── Mobile/
└── Sql/
```

Des captures complémentaires peuvent aussi être ajoutées si nécessaire :

```text
Preuve De Fonctionnement/NoSQL/
Preuve De Fonctionnement/Tests/
Preuve De Fonctionnement/Code/
```

Chaque dossier correspond à un type de preuve différent.

---

# 3. Preuves Docker

Dossier concerné :

```text
Preuve De Fonctionnement/Docker/
```

Les captures Docker montrent :

* la construction de l’image Docker ;
* la présence de l’image générée ;
* le lancement du conteneur ;
* les logs du serveur ;
* l’accès au site depuis l’environnement Docker ;
* la validation du fonctionnement local dans un environnement isolé.

Ces captures prouvent que le projet peut être exécuté dans un environnement Docker, indépendamment de la configuration directe de la machine.

Le serveur utilisé dans Docker correspond à un environnement local de test.

Le message indiquant qu’il s’agit d’un serveur de développement est normal dans ce contexte.

---

# 4. Preuves Figma

Dossier concerné :

```text
Preuve De Fonctionnement/Figma/
```

Les captures Figma montrent :

* les maquettes préparatoires du projet ;
* une version wireframe ;
* une version colorisée ;
* l’organisation visuelle prévue avant l’intégration ;
* la réflexion menée sur l’interface desktop et mobile.

Ces captures prouvent que le projet a été préparé avec une phase de conception graphique avant l’intégration dans Django.

Les maquettes ne sont pas forcément identiques à 100 % au rendu final.

Elles montrent l’intention de départ, la structure des pages et la direction visuelle du site.

---

# 5. Preuves Render

Dossier concerné :

```text
Preuve De Fonctionnement/Render/
```

Les captures Render montrent :

* l’existence du service Render ;
* l’historique des déploiements ;
* les builds réalisés ;
* les logs du service ;
* les variables d’environnement configurées avec des valeurs masquées ;
* la mise en ligne du projet.

Les captures de variables d’environnement montrent uniquement les noms des variables.

Les valeurs sensibles ne sont pas affichées.

Exemples de variables visibles dans les captures :

```text
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
DJANGO_SUPERUSER_USERNAME
```

Les valeurs associées sont masquées afin de respecter les règles de sécurité.

Le projet est hébergé sur Render avec une offre gratuite.

Cette offre peut entraîner une mise en veille du service après une période d’inactivité.

Ce comportement est lié à l’hébergement et ne constitue pas une erreur du projet.

---

# 6. Preuves du site en ligne

Dossier concerné :

```text
Preuve De Fonctionnement/SiteWeb_FrostiaGame/
```

Ce dossier contient les captures du site Frostia Games exécuté en ligne sur Render.

Il est organisé en trois sous-dossiers :

```text
SiteWeb_FrostiaGame/
├── Admin/
├── Desktop/
└── Mobile/
```

---

# 7. Interface d’administration Django

Dossier concerné :

```text
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Admin/
```

Les captures de l’administration montrent :

* l’accès à l’interface d’administration Django ;
* la présence des modèles administrables ;
* la séparation entre l’espace public du site et l’espace d’administration ;
* la présence des sections liées aux créations et aux projets jouables.

Ces captures prouvent que le back-end Django est structuré et que les données peuvent être administrées via l’interface prévue par Django.

Aucun mot de passe ne doit être affiché dans ces captures.

L’administration Django est utilisée comme outil interne de gestion.

Elle n’est pas destinée à être ouverte publiquement aux visiteurs.

---

# 8. Administration en lecture seule

Une partie du projet prévoit un accès d’évaluation sécurisé.

Éléments à documenter ou capturer si nécessaire :

```text
Groupe : Evaluation lecture seule
Utilisateur : evaluation_temp
Permissions : view uniquement
Superuser : non
```

Preuves possibles :

```text
capture-admin-groupe-lecture-seule.png
capture-admin-utilisateur-evaluation-temp.png
capture-admin-permissions-view-only.png
```

Ces captures permettent de montrer que l’évaluateur peut consulter les données sans modifier le contenu du site.

---

# 9. Version desktop du site

Dossier concerné :

```text
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Desktop/
```

Les captures desktop montrent les pages principales du site en version ordinateur.

Pages concernées :

* page d’accueil ;
* page Mes créations ;
* page Projets jouables.

Ces captures prouvent que les pages publiques principales sont accessibles et que l’interface fonctionne sur un écran de type ordinateur ou laptop.

---

# 10. Version mobile du site

Dossier concerné :

```text
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Mobile/
```

Les captures mobile montrent :

* l’affichage responsive du site ;
* l’adaptation du contenu au format mobile ;
* la présence du menu mobile ;
* l’organisation des éléments en colonne ;
* la lisibilité des cartes et sections principales.

Ces captures prouvent que le site ne dépend pas uniquement d’un affichage desktop et qu’il possède une adaptation mobile exploitable.

---

# 11. Preuves GitHub

Dossier concerné :

```text
Preuve De Fonctionnement/Github/
```

Les captures GitHub montrent :

* le dépôt du projet ;
* la sauvegarde du code ;
* le suivi de version ;
* la présence des fichiers principaux ;
* la centralisation du projet dans un dépôt distant.

GitHub permet de conserver l’historique du projet et de sécuriser le travail réalisé.

Une capture du dernier commit peut aussi être ajoutée pour montrer que la version renforcée a bien été poussée.

---

# 12. Preuves SQL

Dossier concerné :

```text
Preuve De Fonctionnement/Sql/
```

Ce dossier contient les preuves liées à la base de données relationnelle.

Les fichiers SQL documentaires sont présents dans :

```text
Docs/sql/
```

Fichiers concernés :

```text
Docs/sql/create_tables_creations.sql
Docs/sql/create_tables_playable.sql
Docs/sql/exemples_insert.sql
Docs/sql/sql-natif.md
```

Ces fichiers montrent :

* les extraits `CREATE TABLE` ;
* les exemples `INSERT INTO` ;
* le lien entre Django ORM et SQL natif ;
* la structure relationnelle principale du projet.

Captures conseillées :

```text
capture-sql-schema.png
capture-sql-create-table-creations.png
capture-sql-create-table-playable.png
capture-sql-insert.png
```

Cette partie répond au besoin de valoriser les compétences SQL demandées dans le retour formateur.

---

# 13. Preuves NoSQL / TinyDB

La partie NoSQL est documentée dans :

```text
Docs/nosql/
```

Fichiers concernés :

```text
Docs/nosql/nosql.md
Docs/nosql/project_notes.json
Docs/nosql/read_project_notes.py
Docs/nosql/structure-nosql.md
Docs/nosql/tinydb-integration.md
```

Selon l’organisation applicative du projet, les fichiers techniques peuvent également être présents dans :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
```

Cette partie montre :

* une structure documentaire JSON ;
* une lecture de notes projet ;
* une intégration légère de TinyDB ;
* une complémentarité entre SQLite et NoSQL.

Captures conseillées :

```text
Preuve De Fonctionnement/NoSQL/capture-nosql-json.png
Preuve De Fonctionnement/NoSQL/capture-nosql-script.png
Preuve De Fonctionnement/NoSQL/capture-nosql-terminal.png
```

Commande de test possible :

```powershell
python -m scripts.demo_tinydb_notes
```

ou, selon l’emplacement du script :

```powershell
python Docs/nosql/read_project_notes.py
```

Cette preuve est importante car le NoSQL n’est plus seulement une évolution future.

TinyDB a été ajouté comme démonstration NoSQL légère.

---

# 14. Preuve de test Django

Une capture de vérification Django est conseillée.

Commande :

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues
```

Capture conseillée :

```text
Preuve De Fonctionnement/Tests/capture-manage-check.png
```

Cette preuve montre que le projet ne signale pas d’erreur de configuration Django au moment de la vérification.

---

# 15. Preuves de code et d’explication

Les extraits de code et explications sont documentés dans :

```text
Docs/backend/
Docs/frontend/
Docs/conception/
Docs/nosql/
Docs/sql/
```

Exemples :

```text
Docs/backend/modeles-django.md
Docs/backend/vues-et-routes.md
Docs/frontend/javascript-menu-mobile.md
Docs/conception/mcd.md
Docs/conception/cas-utilisation.md
Docs/conception/diagramme-sequence.md
Docs/sql/sql-natif.md
Docs/nosql/tinydb-integration.md
```

Ces fichiers répondent aux trois piliers attendus :

| Pilier | Preuve |
| ------ | ------ |
| Code ou extrait technique | Fichiers Python, SQL, JavaScript et Markdown techniques |
| Explication | Documentation dans `doc/` et `Docs/` |
| Rendu final ou résultat | Captures dans `Preuve De Fonctionnement/` |

Captures de code conseillées :

```text
capture-model-creation.png
capture-model-playableproject.png
capture-view-home.png
capture-javascript-menu-mobile.png
capture-nosql-service.png
```

Ces captures ne sont pas toutes obligatoires, mais elles renforcent la lisibilité du dossier.

---

# 16. Sécurité des captures

Les captures ont été préparées en évitant d’exposer les données sensibles.

Les éléments suivants ne doivent pas apparaître en clair dans les images :

* mot de passe ;
* clé secrète Django ;
* valeur complète de variable d’environnement ;
* token ;
* clé API ;
* identifiant privé inutile ;
* information personnelle non nécessaire au dossier.

Lorsque des variables d’environnement sont montrées, leurs valeurs doivent rester masquées.

---

# 17. Synthèse des éléments prouvés

Les preuves réalisées permettent de confirmer que la V1 de Frostia Games comprend :

* un projet Django fonctionnel ;
* une interface publique ;
* une interface d’administration Django ;
* des pages principales accessibles ;
* une structure responsive ;
* une exécution locale possible ;
* une exécution Docker vérifiée ;
* un déploiement Render fonctionnel ;
* une organisation des captures par catégorie ;
* une sauvegarde du projet avec GitHub ;
* une base SQL documentée ;
* des extraits SQL natifs ;
* une démonstration NoSQL légère avec TinyDB ;
* une base documentaire claire pour présenter le travail réalisé.

---

# 18. Limites assumées

Cette V1 ne représente pas la version finale complète de Frostia Games.

Certaines fonctionnalités sont volontairement reportées ou non intégrées dans cette version :

* système complet de publication de jeux ;
* téléchargement de jeux ;
* espace utilisateur public ;
* base PostgreSQL ;
* intégration complète de jeux jouables dans le navigateur ;
* automatisations avancées ;
* statistiques détaillées ;
* MongoDB en production.

La partie NoSQL n’est pas reportée totalement.

Une démonstration légère avec TinyDB est présente.

Une base NoSQL plus avancée, comme MongoDB, reste une évolution possible.

---

# 19. Conclusion

Les captures regroupées dans le dossier `Preuve De Fonctionnement/` permettent de démontrer que la V1 de Frostia Games est stable, consultable, documentée et déployée.

Le projet possède une base fonctionnelle claire :

* conception visuelle ;
* développement Django ;
* administration ;
* responsive ;
* Docker ;
* Render ;
* GitHub ;
* SQL natif ;
* NoSQL léger avec TinyDB ;
* documentation.

Cette version constitue une première base exploitable pour présenter le projet, justifier les choix techniques et préparer les évolutions futures.

Le rôle de ce fichier est de rendre les preuves faciles à trouver, sans obliger à intégrer toutes les captures dans le corps principal du dossier projet.
