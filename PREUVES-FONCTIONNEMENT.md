# Preuves de fonctionnement — Frostia Games

## Objectif du document

Ce document centralise les preuves visuelles et techniques réalisées pour le projet **Frostia Games**.

Il sert d'index afin de retrouver rapidement les captures et les fichiers permettant de vérifier que la V1 du projet est fonctionnelle, documentée, testée, sécurisée et déployée en ligne.

Les preuves principales sont regroupées dans le dossier :

```text
Preuve De Fonctionnement/
```

Ce répertoire constitue une banque de preuves complète. Toutes les captures ne sont pas intégrées directement dans le dossier projet afin de ne pas l’alourdir. Le dossier principal et les annexes utilisent seulement les éléments les plus lisibles, tandis que ce fichier permet de retrouver l’ensemble des preuves disponibles.

---

# 1. Objectif des preuves

Les preuves réalisées permettent de démontrer plusieurs points importants :

- le site public est accessible en ligne sur Render ;
- l'administration Django est accessible ;
- un compte d'évaluation en lecture seule est disponible ;
- les données initiales sont recréées automatiquement sur Render ;
- le projet peut être lancé localement ;
- le projet peut être exécuté avec Docker ;
- le responsive mobile est présent ;
- le dépôt GitHub contient l'historique et les fichiers du projet ;
- la base SQL est documentée ;
- des extraits SQL natifs sont présents ;
- une démonstration NoSQL légère avec TinyDB est documentée ;
- les éléments techniques sont accompagnés d'explications.

Ces preuves montrent que la V1 de Frostia Games ne se limite pas à du code. Elle possède également une organisation documentaire, un déploiement en ligne, une structure de données, des captures classées et une logique de vérification.

---

# 2. Organisation du dossier de preuves

Les captures sont regroupées dans `Preuve De Fonctionnement/`. L’organisation actuelle conserve les dossiers créés au fil du projet afin de ne perdre aucune preuve.

Structure principale :

```text
Preuve De Fonctionnement/
├── admin/
│   └── nosql/
├── architecture/
├── Cas de test/
├── Docker/
├── Extrait de Code/
├── Figma/
├── Github/
├── js/
├── Mcd/
├── Modèle Django/
├── Probleme et solution/
├── Présentation des besoin/
│   └── Preuve/
├── Render/
├── SiteWeb_FrostiaGame/
│   ├── Admin/
│   │   └── evaluateur/
│   ├── Desktop/
│   ├── Mobile/
│   └── Tablette/
├── Sql/
├── sql/
├── Sécurité/
├── test/
└── viewpy/
```

Certains noms de dossiers utilisent encore des majuscules, des espaces ou des variantes historiques. Cette organisation reste volontairement conservée pendant la finalisation afin d’éviter de casser les chemins ou de supprimer une preuve utile.

Un grand nombre d’images a été ajouté. Certains fichiers peuvent donc sembler proches ou être présents en plusieurs exemplaires. Ces doublons sont conservés lorsqu’ils montrent :

- une résolution différente : ordinateur, tablette ou smartphone ;
- un environnement différent : local, Docker ou Render ;
- une étape différente d’un test ou d’un déploiement ;
- une ancienne et une nouvelle version utile à la comparaison ;
- une preuve complémentaire destinée aux annexes ou au dossier professionnel.

Le dossier projet principal utilise uniquement les captures les plus représentatives. Le répertoire complet reste une banque de preuves.

---

# 3. Preuves Render

Dossier concerné :

```text
Preuve De Fonctionnement/Render/
```

Les captures Render montrent :

- l'existence du service Render ;
- le déploiement du projet ;
- les logs du service ;
- l'exécution de la commande de démarrage ;
- la présence des variables d'environnement, avec les valeurs sensibles masquées ;
- l'accès à la version en ligne du site.

Adresse de la version en ligne :

```text
https://frostia-games.onrender.com
```

La version en ligne utilise Render avec une offre gratuite. Cette offre peut entraîner une mise en veille du service après une période d'inactivité. Ce comportement est lié à l'hébergement et ne constitue pas une erreur du projet.

---

# 4. Initialisation automatique des données Render

La base utilisée sur Render peut être réinitialisée lors d'un redémarrage ou d'un redéploiement. Pour éviter une perte des données de démonstration, une commande Django personnalisée a été ajoutée :

```bash
python manage.py setup_render_data
```

Cette commande recrée automatiquement :

- la création principale **Frostia Games** ;
- le projet **Prototype jouable à venir** ;
- le groupe **Evaluation lecture seule** ;
- le compte d'évaluation **evaluation_temp** ;
- les droits de lecture seule nécessaires à la consultation de l'administration.

La commande est exécutée au démarrage du service Render avec le Start Command :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Le mot de passe du compte d'évaluation n'est pas stocké directement dans le code source. Il est fourni par une variable d'environnement Render :

```text
EVALUATION_USER_PASSWORD
```

Les captures Render ne doivent pas afficher la valeur de cette variable.

---

# 5. Preuves de l'administration Django

Dossier concerné :

```text
Preuve De Fonctionnement/admin/
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Admin/
```

Les captures de l'administration montrent :

- l'accès à l'interface d'administration Django ;
- la présence des modèles administrables ;
- la séparation entre l'espace public du site et l'espace d'administration ;
- la présence des sections liées aux créations et aux projets jouables ;
- la présence du compte d'évaluation ;
- la limitation des droits en lecture seule.

L'administration Django est utilisée comme outil interne de gestion. Elle n'est pas destinée à être ouverte librement aux visiteurs.

Aucun mot de passe ne doit être visible dans les captures.

---

# 6. Administration en lecture seule

Un accès d'évaluation a été configuré afin de permettre au jury de consulter l'administration Django sans pouvoir modifier les données.

Éléments configurés :

```text
Groupe : Evaluation lecture seule
Utilisateur : evaluation_temp
Permissions : view uniquement
Superutilisateur : non
Staff : oui
```

Droits accordés :

```text
Can view Création
Can view Projet jouable
```

Droits non accordés :

```text
Can add
Can change
Can delete
```

Captures conseillées :

```text
Preuve De Fonctionnement/admin/capture-admin-evaluation-lecture-seule-local.png
Preuve De Fonctionnement/admin/capture-admin-deconnexion-local.png
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Admin/
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Admin/evaluateur/
```

Ces captures permettent de montrer que l'évaluateur peut consulter les données sans pouvoir modifier le contenu du site.

---

# 7. Preuves du site public

Dossier concerné :

```text
Preuve De Fonctionnement/SiteWeb_FrostiaGame/
```

Les captures du site public montrent les pages principales accessibles en ligne :

- page d'accueil ;
- page Mes créations ;
- page Projets jouables.

Ces captures prouvent que les pages publiques principales sont accessibles depuis la version Render.

Captures disponibles :

```text
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Desktop/
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Tablette/
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Mobile/
```

Ces dossiers contiennent les pages d’accueil, Mes créations et Projets jouables dans plusieurs formats.


---

# 8. Preuves responsive mobile

Les captures mobile montrent :

- l'affichage responsive du site ;
- l'adaptation du contenu au format mobile ;
- la présence du menu mobile ;
- l'organisation des éléments en colonne ;
- la lisibilité des cartes et sections principales.

Ces preuves montrent que le site ne dépend pas uniquement d'un affichage desktop.

Dossiers concernés :

```text
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Desktop/
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Tablette/
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Mobile/
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Admin/evaluateur/
```

---

# 9. Preuves Docker

Dossier concerné :

```text
Preuve De Fonctionnement/Docker/
```

Les captures Docker montrent :

- la construction de l'image Docker ;
- la présence de l'image générée ;
- le lancement du conteneur ;
- les logs du serveur ;
- l'accès au site depuis un environnement isolé.

Ces captures prouvent que le projet peut être exécuté dans un environnement Docker, indépendamment de la configuration directe de la machine.

Le serveur utilisé dans Docker correspond à un environnement local de test. Le message indiquant qu'il s'agit d'un serveur de développement est normal dans ce contexte.

---

# 10. Preuves Figma

Dossier concerné :

```text
Preuve De Fonctionnement/Figma/
```

Les captures Figma montrent :

- les maquettes préparatoires du projet ;
- une version wireframe ;
- une version colorisée ;
- l'organisation visuelle prévue avant l'intégration ;
- la réflexion menée sur l'interface desktop et mobile.

Les maquettes ne sont pas forcément identiques à 100 % au rendu final. Elles montrent l'intention de départ, la structure des pages et la direction visuelle du site.

---

# 11. Preuves GitHub

Dossier concerné :

```text
Preuve De Fonctionnement/Github/
```

Les captures GitHub montrent :

- le dépôt du projet ;
- la sauvegarde du code ;
- le suivi de version ;
- la présence des fichiers principaux ;
- la centralisation du projet dans un dépôt distant ;
- le dernier commit correspondant à la version finalisée.

GitHub permet de conserver l'historique du projet et de sécuriser le travail réalisé.

---

# 12. Preuves SQL

Dossier concerné :

```text
Preuve De Fonctionnement/Sql/
Preuve De Fonctionnement/sql/
```

Les fichiers SQL documentaires sont présents dans :

```text
docs/sql/
```

Fichiers concernés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers montrent :

- les extraits `CREATE TABLE` ;
- les exemples `INSERT INTO` ;
- le lien entre Django ORM et SQL natif ;
- la structure relationnelle principale du projet.

Captures conseillées :

```text
Preuve De Fonctionnement/Sql/Schema.png
Preuve De Fonctionnement/sql/create_tables_creations.png
Preuve De Fonctionnement/sql/create_tables_playable.png
Preuve De Fonctionnement/sql/_exemples_insert.png
Preuve De Fonctionnement/sql/_SQL natif.png
```

Cette partie répond au besoin de valoriser les compétences SQL demandées dans le retour formateur.

---

# 13. Preuves NoSQL / TinyDB

Dossier concerné :

```text
Preuve De Fonctionnement/admin/nosql/
```

La partie NoSQL est documentée dans :

```text
docs/nosql/
```

Fichiers concernés :

```text
docs/nosql/nosql.md
docs/nosql/structure-nosql.md
docs/nosql/tinydb-integration.md
```

Selon l'organisation applicative du projet, les fichiers techniques peuvent également être présents dans :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
```

Cette partie montre :

- une structure documentaire JSON ;
- une lecture de notes projet ;
- une intégration légère de TinyDB ;
- une complémentarité entre SQLite et NoSQL.

Captures conseillées :

```text
Preuve De Fonctionnement/admin/nosql/capture-nosql-documentation.png
Preuve De Fonctionnement/admin/nosql/capture-nosql-json.png
Preuve De Fonctionnement/admin/nosql/capture-nosql-script.png
Preuve De Fonctionnement/admin/nosql/capture-nosql-terminal.png
```

Commande de test possible :

```powershell
python -m scripts.demo_tinydb_notes
```

Cette preuve est importante car le NoSQL n'est plus seulement une évolution future. TinyDB a été ajouté comme démonstration NoSQL légère.

---

# 14. Preuve de test Django

Dossier concerné :

```text
Preuve De Fonctionnement/test/
```

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
Preuve De Fonctionnement/test/capture-manage-check.png
```

Cette preuve montre que le projet ne signale pas d'erreur de configuration Django au moment de la vérification.

---

# 15. Preuves de code et d'explication

Les extraits de code et explications sont documentés dans :

```text
docs/backend/
docs/frontend/
docs/conception/
docs/nosql/
docs/sql/
```

Exemples :

```text
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
docs/frontend/javascript-menu-mobile.md
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
docs/sql/sql-natif.md
docs/nosql/tinydb-integration.md
```

Ces fichiers répondent aux trois piliers attendus :

| Pilier | Preuve |
| ------ | ------ |
| Code ou extrait technique | Fichiers Python, SQL, JavaScript et Markdown techniques |
| Explication | Documentation regroupée dans `docs/` |
| Rendu final ou résultat | Captures centralisées dans `Preuve De Fonctionnement/` |

Emplacements des principales captures de code :

```text
Preuve De Fonctionnement/Extrait de Code/
Preuve De Fonctionnement/js/
Preuve De Fonctionnement/viewpy/
Preuve De Fonctionnement/Modèle Django/
Preuve De Fonctionnement/architecture/
Preuve De Fonctionnement/Mcd/
Preuve De Fonctionnement/Présentation des besoin/Preuve/
Preuve De Fonctionnement/Sécurité/
Preuve De Fonctionnement/Cas de test/
Preuve De Fonctionnement/Probleme et solution/
```

Ces captures ne sont pas toutes intégrées dans le corps principal. Elles restent disponibles pour les annexes et les démonstrations complémentaires.

---

# 16. Sécurité des captures

Les captures ont été préparées en évitant d'exposer les données sensibles.

Les éléments suivants ne doivent pas apparaître en clair dans les images :

- mot de passe ;
- clé secrète Django ;
- valeur complète de variable d'environnement ;
- token ;
- clé API ;
- identifiant privé inutile ;
- information personnelle non nécessaire au dossier.

Lorsque des variables d'environnement sont montrées, leurs valeurs doivent rester masquées.

Le fichier d'accès évaluateur peut être conservé dans un cadre privé, mais le mot de passe ne doit pas être exposé dans les captures publiques du dossier.

---

# 17. Synthèse des éléments prouvés

Les preuves réalisées permettent de confirmer que la V1 de Frostia Games comprend :

- un projet Django fonctionnel ;
- une interface publique ;
- une interface d'administration Django ;
- des pages principales accessibles ;
- une structure responsive ;
- une exécution locale possible ;
- une exécution Docker vérifiée ;
- un déploiement Render fonctionnel ;
- une initialisation automatique des données en ligne ;
- un compte d'évaluation en lecture seule ;
- une organisation des captures par catégorie ;
- une sauvegarde du projet avec GitHub ;
- une base SQL documentée ;
- des extraits SQL natifs ;
- une démonstration NoSQL légère avec TinyDB ;
- des jeux d’essai documentés ;
- les difficultés rencontrées et les corrections appliquées ;
- une base documentaire claire pour présenter le travail réalisé.

---

# 18. Limites assumées

Cette V1 ne représente pas la version finale complète de Frostia Games.

Certaines fonctionnalités sont volontairement reportées ou non intégrées dans cette version :

- système complet de publication de jeux ;
- téléchargement de jeux ;
- espace utilisateur public ;
- base PostgreSQL ;
- intégration complète de jeux jouables dans le navigateur ;
- automatisations avancées ;
- statistiques détaillées ;
- MongoDB en production.

La partie NoSQL n'est pas reportée totalement. Une démonstration légère avec TinyDB est présente. Une base NoSQL plus avancée, comme MongoDB, reste une évolution possible.

---

# 19. Conclusion

Les captures regroupées dans le dossier `Preuve De Fonctionnement/` permettent de démontrer que la V1 de Frostia Games est stable, consultable, documentée et déployée.

Le volume important de fichiers est assumé : certains doublons ont été conservés parce qu’ils montrent plusieurs formats d’écran, plusieurs environnements ou différentes étapes de validation. Le dossier principal utilise une sélection courte, tandis que le répertoire complet conserve la traçabilité du travail.

Le projet possède une base fonctionnelle claire :

- conception visuelle ;
- développement Django ;
- administration ;
- accès d'évaluation en lecture seule ;
- responsive ;
- Docker ;
- Render ;
- GitHub ;
- SQL natif ;
- NoSQL léger avec TinyDB ;
- documentation.

Cette version constitue une première base exploitable pour présenter le projet, justifier les choix techniques et préparer les évolutions futures.

Le rôle de ce fichier est de rendre les preuves faciles à trouver, sans obliger à intégrer toutes les captures dans le corps principal du dossier projet.