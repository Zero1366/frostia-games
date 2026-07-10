# Bilan de la V1 — Frostia Games

## Objectif de la V1

L'objectif de cette V1 était de créer une première version fonctionnelle du portfolio **Frostia Games**.

Cette version devait fournir une base Django stable permettant de présenter des créations vidéoludiques actuelles et futures.

La V1 ne représente pas le projet final complet.

Elle sert de fondation technique, documentaire et visuelle pour continuer le projet sans repartir de zéro.

L’objectif principal était de produire une version :

- fonctionnelle ;
- stable ;
- documentée ;
- déployée en ligne ;
- consultable ;
- maintenable ;
- prouvable par captures ;
- défendable dans un dossier projet.

Après le renforcement du dossier, la V1 contient également :

- une documentation de conception plus complète ;
- des extraits SQL natifs ;
- une expérimentation NoSQL avec TinyDB ;
- un affichage des notes de progression sur l’accueil ;
- une documentation du JavaScript dynamique ;
- un accès d’évaluation en lecture seule ;
- une commande d’initialisation automatique pour Render ;
- une documentation backend et frontend complémentaire ;
- des preuves organisées dans `docs/preuves/`.

La V1 est complète dans son périmètre actuel.

Les évolutions restantes concernent les futures versions du projet, pas la validation de cette première version.

---

# 1. État global du projet

| Partie du projet | État | Avancement estimé |
| ---------------- | ---- | ----------------: |
| Installation du projet Django | Terminé | 100 % |
| Structure de base du projet | Terminé | 100 % |
| Pages principales du site | Fonctionnelles | 100 % |
| Design et intégration visuelle | Première version terminée | 100 % |
| Navigation | Fonctionnelle | 100 % |
| Menu mobile JavaScript | Fonctionnel | 100 % |
| Responsive / affichage mobile | Fonctionnel pour la V1 | 100 % |
| Backend Django | Fonctionnel pour la V1 | 100 % |
| Modèles Django | Fonctionnels | 100 % |
| Base SQLite | Fonctionnelle pour la V1 | 100 % |
| Interface admin Django | Fonctionnelle | 100 % |
| Affichage dynamique des données SQLite | Fonctionnel | 100 % |
| TinyDB | Intégré comme démonstration NoSQL légère | 100 % |
| Affichage des notes TinyDB sur l’accueil | Fonctionnel | 100 % |
| Docker | Fonctionnel pour le lancement local | 100 % |
| Déploiement Render | Terminé | 100 % |
| Initialisation automatique Render | En place avec `setup_render_data` | 100 % |
| Variables d'environnement | En place | 100 % |
| Fichier `.env.example` | En place | 100 % |
| Fichier `.gitignore` | En place | 100 % |
| Fichier `README.md` | En place | 100 % |
| Fichier `CHOIX_TECHNIQUES.md` | En place | 100 % |
| Documentation technique principale `doc/` | Complète pour la V1 | 100 % |
| Documentation complémentaire `docs/` | En place | 100 % |
| Documentation de déploiement | En place | 100 % |
| Documentation SQL | En place | 100 % |
| SQL natif complémentaire | En place | 100 % |
| Documentation NoSQL | En place | 100 % |
| Sécurité minimale | Correcte pour une V1 | 100 % |
| Compte d’évaluation lecture seule | Fonctionnel en ligne | 100 % |
| Maquettes Figma | Utilisées comme preuves visuelles | Finalisation |
| Captures d'écran du site | À intégrer ou vérifier | Finalisation |
| Captures de l'administration Django | À intégrer ou vérifier | Finalisation |
| Captures Render | À intégrer ou vérifier | Finalisation |
| Dossier de preuves `docs/preuves/` | À compléter si nécessaire | Finalisation |
| Commit final | À effectuer après dernières corrections | Finalisation |
| PostgreSQL | Reporté volontairement | 0 % |
| Jeu jouable dans le navigateur | Reporté volontairement | 0 % |
| Upload serveur réel | Reporté volontairement | 0 % |

---

# 2. Avancement global estimé

La V1 technique peut être estimée à :

```text
100 %
```

Ce pourcentage correspond à l'état de la **V1 prévue**, pas à l'état final du projet complet.

La V1 est considérée comme complète dans son périmètre technique car les éléments suivants ont été finalisés :

- les pages principales ;
- le backend Django ;
- les modèles Django ;
- la base SQLite ;
- l'administration Django ;
- l'affichage dynamique ;
- le lancement local ;
- le lancement Docker ;
- le déploiement Render ;
- l'initialisation automatique des données Render ;
- les variables d'environnement ;
- la documentation technique ;
- les choix techniques ;
- les fichiers SQL documentaires ;
- les fichiers SQL natifs complémentaires ;
- l’expérimentation NoSQL TinyDB ;
- l’affichage des notes TinyDB sur l’accueil ;
- le compte d’évaluation en lecture seule ;
- la documentation de conception ;
- la documentation backend et frontend complémentaire.

Les éléments restants relèvent surtout de la finalisation du dossier :

- captures ;
- preuves ;
- annexes ;
- relecture ;
- mise en forme finale ;
- export éventuel en PDF ;
- dernier commit si correction.

---

# 3. Ce qui est terminé

Les éléments suivants sont terminés ou suffisamment stables pour la V1 :

- création du projet Django ;
- structure principale du site ;
- création des applications Django ;
- pages publiques de base ;
- interface visuelle moderne pour une V1 ;
- navigation principale ;
- menu mobile ;
- modèles Django ;
- base SQLite ;
- migrations ;
- administration Django ;
- compte d’évaluation en lecture seule ;
- affichage dynamique de certaines données ;
- page Mes créations reliée au backend ;
- page Projets jouables reliée au backend ;
- affichage des notes TinyDB sur l’accueil ;
- interface préparatoire pour les futurs projets jouables ;
- configuration Docker ;
- lancement avec Docker Compose ;
- fichier `requirements.txt` ;
- dépendance TinyDB ;
- fichier `build.sh` ;
- fichier `.env.example` ;
- fichier `.gitignore` ;
- fichier `README.md` ;
- fichier `CHOIX_TECHNIQUES.md` ;
- configuration Render ;
- lancement avec Gunicorn ;
- commande Render `setup_render_data` ;
- gestion des fichiers statiques avec WhiteNoise ;
- déploiement en ligne ;
- accès à l'administration Django ;
- documentation du déploiement ;
- documentation de sécurité ;
- documentation de base de données ;
- documentation SQL ;
- documentation SQL native complémentaire ;
- documentation NoSQL ;
- documentation Docker ;
- documentation d'architecture ;
- documentation de tests ;
- documentation des captures et preuves ;
- documentation des limites et évolutions ;
- documentation des pistes explorées et non retenues ;
- documentation des choix techniques ;
- journal de bord ;
- changelog ;
- plan de finalisation V1 ;
- documents de conception complémentaires ;
- documentation JavaScript ;
- documentation backend complémentaire.

---

# 4. Derniers éléments renforcés

Plusieurs éléments ont été ajoutés ou renforcés après le retour formateur.

## Documentation de conception

Documents ajoutés :

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
```

Ces documents renforcent la partie conception du dossier projet.

Ils permettent de montrer :

- les entités principales ;
- les acteurs ;
- les cas d’utilisation ;
- le parcours visiteur ;
- le rôle de l’administration ;
- le fonctionnement d’une page publique.

## SQL natif complémentaire

Fichiers ajoutés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers permettent de montrer :

- des structures `CREATE TABLE` ;
- des exemples `INSERT INTO` ;
- le lien entre Django, l’ORM, les migrations et SQL ;
- la compréhension de la structure réelle de la base.

Le SQL natif reste documentaire.

Les tables réelles restent gérées par les migrations Django.

## NoSQL TinyDB

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/__init__.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

TinyDB sert à démontrer une logique NoSQL légère.

Il permet de stocker des notes de progression dans un fichier JSON.

Il ne remplace pas SQLite.

SQLite reste la base principale du projet.

Commande de vérification :

```powershell
python -m scripts.demo_tinydb_notes
```

## Affichage des notes TinyDB

Fichiers concernés :

```text
core/views.py
templates/pages/home.html
core/services/nosql_notes.py
data/nosql/project_notes_db.json
```

La page d’accueil peut afficher des notes de progression issues de TinyDB.

Chaîne technique :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

## Accès d’évaluation en lecture seule

Un compte d’évaluation en lecture seule est disponible pour permettre une consultation limitée de l’administration Django.

Ce compte :

- n’est pas superutilisateur ;
- ne possède pas les droits d’ajout ;
- ne possède pas les droits de modification ;
- ne possède pas les droits de suppression ;
- peut consulter les créations ;
- peut consulter les projets jouables.

Les identifiants ne doivent pas être affichés dans les captures publiques.

Ils peuvent être transmis séparément uniquement si l’évaluateur les demande.

## Initialisation automatique Render

Une difficulté a été identifiée sur Render : la base SQLite de l'environnement gratuit peut se retrouver vide après redémarrage ou redéploiement.

Pour stabiliser la démonstration en ligne, une commande Django personnalisée a été ajoutée :

```bash
python manage.py setup_render_data
```

Elle recrée automatiquement :

- la création principale Frostia Games ;
- le projet jouable de démonstration ;
- le groupe `Evaluation lecture seule` ;
- le compte d’évaluation ;
- les droits de lecture seule.

Le Start Command Render applique cette commande au démarrage du service.

---

# 5. Rôle des maquettes Figma

Les maquettes Figma servent de preuves visuelles de conception.

Elles montrent que l'interface n'a pas été construite uniquement au hasard dans le code.

Elles permettent de justifier :

- la structure des pages ;
- l'organisation des sections ;
- la hiérarchie visuelle ;
- la navigation ;
- les cartes de présentation ;
- la cohérence générale de l'interface.

Les maquettes Figma ne remplacent pas le site final.

Elles montrent la préparation graphique et la logique d'interface avant ou pendant l'intégration dans Django.

---

# 6. Organisation des preuves

Les preuves sont organisées principalement dans :

```text
docs/preuves/
```

Organisation utilisée ou recommandée :

```text
docs/preuves/
├── admin/
├── js/
├── nosql/
├── render/
├── sql/
└── test/
```

Le fichier principal d’index des preuves est :

```text
PREUVES-FONCTIONNEMENT.md
```

Cette organisation permet de séparer :

- la documentation écrite ;
- les captures du site ;
- les captures Render ;
- les captures de l'administration Django ;
- les preuves techniques ;
- les preuves NoSQL ;
- les preuves SQL ;
- les captures de validation.

---

# 7. Captures à préparer ou à intégrer

Les captures importantes concernent plusieurs parties du projet.

## Site public

- page d'accueil desktop ;
- page d’accueil avec notes TinyDB ;
- page Mes créations ;
- page Projets jouables ;
- page d'accueil mobile ;
- menu mobile ouvert.

## Figma

- maquette de la page d'accueil ;
- maquette de la page Mes créations ;
- maquette de la page Projets jouables.

## Administration Django

- page de connexion admin ;
- tableau de bord admin ;
- modèle `Creation` ;
- modèle `PlayableProject` ;
- compte d’évaluation en lecture seule ;
- affichage limité avec le compte lecture seule.

## Docker

- commande `docker compose up --build` ;
- serveur lancé dans le conteneur ;
- site accessible après lancement Docker ;
- conteneur actif si nécessaire.

## Render

- service Render actif ;
- logs montrant que le service est en ligne ;
- logs montrant `setup_render_data` ;
- Build Command ;
- Start Command ;
- variables d'environnement masquées.

## Technique

- `python manage.py check` ;
- `python -m scripts.demo_tinydb_notes` ;
- `git status` propre ;
- structure du projet dans VS Code ;
- dépôt GitHub ;
- fichiers importants comme `build.sh`, `models.py`, `admin.py`, `views.py`, `nosql_notes.py`, `menu.js`.

Les informations sensibles doivent être évitées ou masquées dans les captures.

---

# 8. Vérifications finales à effectuer

Avant de considérer la V1 comme prête pour le dossier final, les vérifications suivantes doivent être faites :

- relire les pages publiques ;
- vérifier le responsive mobile ;
- vérifier le menu mobile ;
- vérifier les maquettes Figma propres ;
- préparer les captures d'écran du site ;
- préparer les captures de l'administration Django ;
- préparer les captures Render ;
- préparer la capture de TinyDB ;
- ranger les images dans `docs/preuves/` ;
- vérifier l'absence de données sensibles dans les captures ;
- vérifier le README à la racine ;
- vérifier le fichier `CHOIX_TECHNIQUES.md` ;
- vérifier le site en ligne sur Render ;
- tester l'administration Django ;
- tester le compte d’évaluation en lecture seule ;
- préparer les extraits de code importants ;
- exécuter `python manage.py check` ;
- exécuter `python -m scripts.demo_tinydb_notes` ;
- vérifier `git status` ;
- effectuer un dernier commit Git si des corrections sont faites.

Ces actions relèvent de la finalisation, pas de l'ajout de nouvelles fonctionnalités.

---

# 9. Ce qui reste à améliorer plus tard

Les éléments suivants pourront être améliorés dans une prochaine version :

- améliorer le design général ;
- renforcer le responsive mobile ;
- enrichir le contenu des pages ;
- ajouter des fiches projets plus détaillées ;
- préparer une meilleure présentation des créations futures ;
- améliorer l'expérience utilisateur ;
- ajouter des captures ou visuels définitifs ;
- créer une administration personnalisée ;
- ajouter des tests automatisés Django ;
- améliorer la gestion des erreurs ;
- ajouter une base PostgreSQL ;
- étudier MongoDB si les contenus deviennent plus variables ;
- créer un système de sauvegarde automatique ;
- préparer une vraie intégration de projet jouable ;
- améliorer la persistance de la partie NoSQL si elle devient utile en production.

Ces améliorations ne sont pas nécessaires pour valider la V1 actuelle.

---

# 10. Ce qui est volontairement reporté

Certains éléments ne sont pas intégrés dans cette V1 afin d'éviter d'élargir trop vite le périmètre du projet.

Éléments reportés :

- base PostgreSQL ;
- interface d'administration personnalisée ;
- vrai upload serveur ;
- lecteur vidéo réel ;
- fiches projet détaillées complètes ;
- statistiques avec graphiques ;
- graphiques Plotly.js ;
- intégration d'un jeu jouable dans le navigateur ;
- espace privé complet ;
- API REST ;
- comptes utilisateurs publics ;
- rôles publics avancés ;
- base NoSQL avancée comme MongoDB ;
- système de sauvegarde automatique ;
- système de restauration des contenus ;
- tests automatisés complets ;
- mini-jeu intégré ;
- système de score ;
- téléchargement public de projet jouable.

Ces éléments pourront être ajoutés plus tard si le projet devient une base plus avancée.

Ils ne sont pas oubliés.

Ils sont volontairement reportés pour conserver une V1 stable, présentable et maintenable.

---

# 11. Éléments initialement reportés mais finalement ajoutés

Certains éléments prévus au départ comme évolutions possibles ont finalement été ajoutés de manière limitée et contrôlée.

## Compte d’évaluation en lecture seule

Le compte de consultation n'est plus seulement une piste future.

Il existe maintenant comme accès limité.

Il ne remplace pas l’administrateur.

Il sert seulement à donner un droit de regard contrôlé.

## TinyDB

Le NoSQL n’est plus seulement théorique.

TinyDB a été ajouté pour démontrer une logique NoSQL légère.

Cette intégration reste volontairement limitée.

## SQL natif complémentaire

Le SQL natif a été renforcé avec des fichiers dédiés.

Il reste documentaire et ne remplace pas les migrations Django.

## Initialisation Render

L'initialisation des données Render a été automatisée afin d’éviter une démonstration vide après redémarrage.

Cette solution reste simple et adaptée au périmètre de la V1.

---

# 12. Justification du périmètre

Le projet aurait pu être élargi avec davantage de fonctionnalités.

Cependant, ajouter trop d'éléments dans cette V1 aurait créé plusieurs risques :

- perte de stabilité ;
- dette technique ;
- complexité excessive ;
- documentation difficile à maintenir ;
- fonctionnalités commencées mais non terminées ;
- difficulté à tester correctement ;
- risque de transformer le projet en usine à gaz.

Le choix retenu a donc été de privilégier une V1 simple, fonctionnelle, documentée, déployée et prouvable par captures.

Cette décision montre une capacité à cadrer le projet et à protéger sa stabilité.

---

# 13. Points forts de la V1

La V1 possède plusieurs points solides :

- projet Django fonctionnel ;
- structure claire ;
- séparation entre templates, vues, modèles et fichiers statiques ;
- base SQLite opérationnelle pour la V1 ;
- expérimentation NoSQL TinyDB ;
- administration Django fonctionnelle ;
- compte d’évaluation en lecture seule ;
- données Render recréées automatiquement ;
- affichage dynamique des données ;
- affichage des notes TinyDB ;
- lancement local possible ;
- lancement Docker possible ;
- déploiement Render fonctionnel ;
- documentation technique complète ;
- README à la racine ;
- fichier de choix techniques ;
- documentation SQL ;
- documentation SQL native complémentaire ;
- documentation NoSQL ;
- documentation des pistes explorées ;
- documentation des limites et évolutions ;
- variables d'environnement documentées ;
- sécurité minimale cohérente avec le périmètre ;
- maquettes Figma propres ;
- preuves techniques identifiables ;
- documents de conception complémentaires ;
- documentation JavaScript ;
- documentation backend complémentaire.

Ces éléments permettent de présenter le projet comme une base sérieuse et évolutive.

---

# 14. Limites assumées

La V1 possède aussi des limites assumées :

- l'interface graphique pourra encore évoluer ;
- le responsive pourra être amélioré dans une prochaine version ;
- SQLite reste une base simple ;
- SQLite sur Render gratuit n’est pas traité comme une persistance durable avancée ;
- TinyDB reste une expérimentation limitée ;
- aucun vrai upload serveur n'est implanté ;
- aucun jeu n'est jouable directement dans le navigateur ;
- l'administration reste celle fournie par Django ;
- les fiches détaillées des projets ne sont pas encore intégrées ;
- les tests automatisés complets ne sont pas encore présents ;
- PostgreSQL n'est pas encore connecté ;
- MongoDB n'est pas utilisé ;
- le compte d’évaluation en lecture seule ne doit pas être considéré comme un système de rôles avancé.

Ces limites sont cohérentes avec l'objectif de la V1.

Le projet ne doit pas être présenté comme une plateforme finale complète, mais comme une première version fonctionnelle et évolutive.

---

# 15. Positionnement correct du projet

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

La dernière formulation serait trop ambitieuse par rapport à l'état réel de la V1.

---

# 16. Conclusion

La V1 de **Frostia Games** est fonctionnelle, documentée, déployée et renforcée.

Elle atteint son objectif principal : disposer d'une base Django stable, visible en ligne, administrable et prête à évoluer.

Le projet n'est pas terminé dans sa forme finale, mais il possède maintenant une fondation propre pour continuer sans repartir de zéro.

Cette V1 montre une progression cohérente :

```text
conception
maquettes Figma
développement
backend
base de données
administration
SQL
NoSQL
JavaScript
Docker
déploiement
documentation
preuves
bilan
```

Le choix de limiter le périmètre est volontaire.

Il permet de conserver un projet stable, maintenable et présentable.

La V1 est complète dans son périmètre prévu.

Elle ne représente pas le projet final, mais une première version stable, documentée, déployée, renforcée et prouvable par captures.

À ce stade, la priorité n'est plus d'ajouter de nouvelles fonctionnalités lourdes.

La priorité est de finaliser les captures, les preuves, les annexes et la mise en forme du dossier projet final.
