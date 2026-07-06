# Pistes explorées et non retenues - Frostia Games

## Objectif du document

Ce document présente les pistes techniques et fonctionnelles envisagées pendant le développement du projet **Frostia Games**, ainsi que leur état actuel.

L'objectif est de montrer que les choix réalisés ne sont pas dus au hasard.

Plusieurs solutions ont été réfléchies, comparées, puis certaines ont été :

* retenues ;
* intégrées de manière limitée ;
* reportées ;
* abandonnées ;
* conservées comme pistes futures.

Le principe retenu pour ce projet est le suivant :

```text
Toutes les pistes intéressantes peuvent être envisagées et explorées, mais seules les fonctionnalités utiles à une V1 stable doivent être intégrées immédiatement.
```

Une V1 évolue constamment.

Certaines idées peuvent rester dans la roadmap, tandis que d'autres peuvent être abandonnées pendant la phase de stabilisation si elles ne servent plus réellement le projet.

Ce document a été mis à jour après le renforcement du dossier projet afin de ne plus présenter comme absents certains éléments désormais ajoutés :

* le compte temporaire de lecture seule ;
* TinyDB ;
* les fichiers SQL natifs documentaires ;
* la documentation JavaScript ;
* la documentation de conception ;
* la documentation backend et frontend complémentaire.

---

# 1. Principe général

Au début du projet, plusieurs pistes étaient possibles.

Le projet aurait pu évoluer vers :

* une application Django simple ;
* une application plus avancée avec PostgreSQL ;
* une solution C# / ASP.NET Core / Razor ;
* une interface d'administration personnalisée ;
* un espace privé complet ;
* un système de gestion de projets plus dynamique ;
* une plateforme permettant plus tard d'intégrer des projets jouables ;
* une base NoSQL plus avancée ;
* des graphiques de suivi ;
* un système d'upload serveur.

Cependant, l'objectif de cette V1 n'était pas de tout faire immédiatement.

L'objectif était de créer une base :

* fonctionnelle ;
* stable ;
* claire ;
* documentée ;
* déployée ;
* évolutive ;
* maîtrisable.

Certaines pistes ont donc été écartées, reportées ou limitées afin d'éviter de transformer la V1 en projet trop lourd.

---

# 2. Méthode de décision

Avant d'ajouter une technologie ou une fonctionnalité, plusieurs questions ont été utilisées :

* est-ce indispensable pour la V1 ?
* est-ce utile pour présenter le projet ?
* est-ce que cela améliore réellement la version actuelle ?
* est-ce que cela risque de casser l'existant ?
* est-ce que cela demande trop de temps ?
* est-ce que cela complexifie la documentation ?
* est-ce que cela peut être ajouté plus tard ?
* est-ce que cela doit vraiment être conservé ?
* est-ce que cela peut être simplifié ?
* est-ce que cela risque de transformer le projet en usine à gaz ?

Si une piste n'était pas indispensable, elle a été reportée.

Si une idée risquait de fragiliser la V1 ou d'ajouter trop de complexité, elle pouvait aussi être abandonnée.

Si une piste pouvait renforcer le dossier sans alourdir fortement le projet, elle a pu être intégrée de manière limitée.

---

# 3. Piste C# / ASP.NET Core / Razor

## Description

Au départ, une piste envisagée était de développer le projet avec une technologie liée à **C#**, par exemple **ASP.NET Core** avec **Razor**.

Cette piste était intéressante car C# est un langage que j'apprécie particulièrement.

C# offre plusieurs qualités :

* typage fort ;
* structure claire ;
* rigueur du code ;
* bonne lisibilité ;
* équilibre entre propreté et puissance ;
* meilleure détection de certaines erreurs avant l'exécution ;
* organisation adaptée aux projets applicatifs plus structurés.

C# reste un langage intéressant pour mes futurs projets, notamment parce qu'il impose une discipline plus forte que Python.

---

## Pourquoi cette piste n'a pas été retenue pour la V1

Même si C# / Razor était une piste intéressante, elle n'a pas été retenue pour cette V1.

Le risque était de repartir dans une architecture plus lourde, avec plus de configuration, plus de temps d'adaptation et une documentation plus complexe.

Pour une première version, cela aurait pu créer :

* une perte de temps importante ;
* un risque de ne pas terminer la V1 ;
* une architecture trop ambitieuse ;
* une difficulté de déploiement supplémentaire ;
* une documentation plus longue à produire ;
* une dérive du périmètre.

Le projet avait besoin d'une solution rapide à mettre en place, facile à déployer et adaptée à un portfolio Django.

---

## Décision

La piste C# / ASP.NET Core / Razor est reportée.

Elle reste intéressante pour de futurs projets, mais elle n'était pas la solution la plus adaptée au périmètre court de la V1.

La V1 reste donc développée avec Python et Django.

---

# 4. Choix final : Python et Django

## Description

Le choix final s'est porté sur **Python avec Django**.

Django a été retenu car il offre une structure web complète et rapide à mettre en place.

Django apporte directement :

* routes ;
* vues ;
* templates ;
* modèles ;
* migrations ;
* base de données ;
* administration intégrée ;
* gestion des fichiers statiques ;
* organisation claire du projet.

Pour une V1 de portfolio avec backend, administration et déploiement, Django était une solution cohérente.

---

## Pourquoi Django a été retenu

Django permettait de produire plus rapidement une V1 fonctionnelle.

Ses avantages dans ce projet :

* structure déjà organisée ;
* administration native ;
* simplicité de SQLite pour démarrer ;
* templates faciles à utiliser ;
* bon équilibre entre rapidité et structure ;
* déploiement possible sur Render ;
* documentation abondante ;
* architecture compréhensible pour un dossier projet.

Django a donc été choisi pour sa capacité à produire une base stable sans multiplier les couches techniques.

---

## Limite de Python

Python reste un langage très permissif.

Cette permissivité peut être une force pour avancer rapidement, mais elle peut aussi laisser passer plus d'erreurs qu'un langage fortement typé comme C#.

Risques possibles :

* erreurs détectées plus tard ;
* typage moins strict ;
* variables mal utilisées ;
* dépendance plus forte aux tests ;
* besoin de discipline supplémentaire ;
* alertes parfois imprécises dans l'éditeur.

Ce point a été pris en compte dans la manière de travailler sur le projet.

---

## Garde-fous ajoutés

Pour compenser la souplesse de Python, plusieurs garde-fous ont été mis en place :

* documentation régulière ;
* journal de bord ;
* changelog ;
* vérification avec `python manage.py check` ;
* test TinyDB avec `python -m scripts.demo_tinydb_notes` ;
* utilisation d'un environnement virtuel `.venv` ;
* séparation entre templates, vues et fichiers statiques ;
* migrations Django ;
* administration Django contrôlée ;
* compte temporaire de lecture seule ;
* variables d'environnement pour les informations sensibles ;
* déploiement Render documenté ;
* tests manuels des pages ;
* vérification de l'administration ;
* vérification du responsive ;
* documentation des limites et évolutions.

Ces garde-fous permettent de rendre le projet plus fiable malgré la permissivité de Python.

---

# 5. PostgreSQL

## Description

PostgreSQL a été envisagé comme base de données de production plus robuste que SQLite.

PostgreSQL serait plus adapté à une vraie production avec plusieurs utilisateurs, davantage de données et une meilleure persistance.

---

## Pourquoi PostgreSQL n'a pas été intégré

Pour la V1, PostgreSQL n'était pas indispensable.

L'intégrer aurait demandé :

* une configuration supplémentaire ;
* une base distante ;
* des variables d'environnement supplémentaires ;
* une adaptation du déploiement ;
* des tests de connexion ;
* une documentation dédiée.

SQLite suffit actuellement pour un portfolio simple.

---

## Décision

PostgreSQL est reporté à une version future.

La V1 conserve SQLite afin de rester simple et stable.

---

# 6. Compte temporaire de lecture seule

## Description

Un compte temporaire pour le jury ou l'évaluateur avait été envisagé.

Ce compte devait permettre de consulter l'administration Django sans utiliser le vrai compte administrateur.

---

## Évolution de la décision

Cette piste n'est plus seulement reportée.

Un compte temporaire de lecture seule a finalement été créé de manière limitée et contrôlée.

Ce compte permet de consulter certaines parties de l'administration Django sans donner les droits complets d'un administrateur.

Il peut consulter :

* les créations ;
* les projets jouables.

Il ne doit pas donner accès :

* aux utilisateurs ;
* aux groupes ;
* aux permissions sensibles ;
* aux réglages internes ;
* aux secrets du projet.

---

## Pourquoi cette intégration reste limitée

Le compte temporaire reste une solution simple.

Il ne s'agit pas :

* d'un espace privé complet ;
* d'un système de rôles avancé ;
* d'une interface jury personnalisée ;
* d'un accès public ;
* d'un compte administrateur complet.

Les identifiants réels de ce compte ne doivent pas être écrits dans la documentation publique.

Ils peuvent être transmis séparément uniquement si l'évaluateur les demande.

---

## Décision

La piste du compte temporaire est retenue sous une forme limitée.

Le système de rôles avancé reste reporté.

---

# 7. Administration personnalisée

## Description

Une interface d'administration personnalisée a été envisagée pour remplacer ou compléter l'administration Django native.

Elle aurait pu permettre de gérer :

* projets ;
* captures ;
* versions ;
* liens ;
* statuts ;
* médias ;
* textes du portfolio.

---

## Pourquoi cette piste n'a pas été intégrée

L'administration Django native est suffisante pour une V1.

Créer une administration personnalisée aurait demandé :

* des vues privées ;
* des formulaires ;
* une gestion des permissions ;
* une interface dédiée ;
* des validations ;
* des tests supplémentaires ;
* une sécurité plus poussée.

Cela aurait fortement élargi le périmètre.

---

## Décision

L'administration personnalisée est reportée.

La V1 utilise l'administration Django native.

---

# 8. Upload serveur réel

## Description

Un système d'upload serveur a été envisagé pour permettre l'ajout de fichiers, médias ou futures démonstrations.

La page des projets jouables contient une interface préparatoire, mais aucun upload réel n'est effectué côté serveur.

---

## Pourquoi cette piste n'a pas été intégrée

L'upload serveur est une fonctionnalité sensible.

Elle demande :

* validation stricte des fichiers ;
* limitation de taille ;
* contrôle des extensions ;
* protection contre les fichiers dangereux ;
* stockage sécurisé ;
* suppression contrôlée ;
* tests de sécurité.

Ajouter cette fonctionnalité dans la V1 aurait augmenté fortement le risque technique.

---

## Décision

L'upload serveur réel est reporté.

La V1 conserve uniquement une interface préparatoire honnête.

---

# 9. Jeu jouable dans le navigateur

## Description

Une future intégration de jeux ou démonstrations jouables directement dans le navigateur a été envisagée.

Cette piste correspond à une évolution possible du portfolio vers une plateforme de présentation interactive.

---

## Pourquoi cette piste n'a pas été intégrée

Intégrer un jeu jouable dans le navigateur demande une réflexion technique plus large.

Il faudrait gérer :

* format du jeu ;
* performances ;
* compatibilité navigateur ;
* chargement ;
* sécurité ;
* contrôles ;
* stockage des fichiers ;
* intégration dans Django.

Cette fonctionnalité dépasse le périmètre de la V1.

---

## Décision

Les projets jouables dans le navigateur sont reportés.

La V1 prépare seulement l'idée avec une page dédiée.

---

# 10. Plotly.js et graphiques

## Description

Plotly.js a été envisagé pour afficher des graphiques de suivi.

Exemples possibles :

* avancement d'un projet ;
* répartition des tâches ;
* progression par version ;
* suivi de développement ;
* statistiques de production.

---

## Pourquoi cette piste n'a pas été intégrée

Les graphiques ne sont pas indispensables pour la V1.

Ils auraient demandé :

* du JavaScript supplémentaire ;
* des données structurées ;
* une logique d'affichage ;
* des tests ;
* une documentation dédiée.

Pour cette première version, le bénéfice immédiat était inférieur à l'effort nécessaire.

---

## Décision

Plotly.js est reporté.

Il pourra être intégré plus tard comme amélioration visuelle ou fonctionnelle.

---

# 11. Espace privé complet

## Description

Un espace privé complet a été envisagé pour gérer le portfolio depuis une interface dédiée.

Cet espace aurait pu contenir :

* tableau de bord ;
* gestion des projets ;
* gestion des médias ;
* gestion des versions ;
* gestion des statuts ;
* historique ;
* sauvegardes.

---

## Pourquoi cette piste n'a pas été intégrée

Un espace privé complet aurait transformé la V1 en projet beaucoup plus lourd.

Il aurait fallu gérer :

* authentification ;
* permissions ;
* formulaires ;
* routes privées ;
* sécurité ;
* validations ;
* tests ;
* interface complète.

Cela aurait dépassé le besoin immédiat.

---

## Décision

L'espace privé complet est reporté.

La V1 s'appuie sur l'administration Django native.

---

# 12. Sauvegardes automatiques

## Description

Un système de sauvegarde automatique avant modification a été envisagé.

L'idée serait de créer un historique ou des snapshots avant chaque modification importante.

---

## Pourquoi cette piste n'a pas été intégrée

Cette fonctionnalité est utile, mais elle demande une architecture plus avancée.

Il faudrait prévoir :

* système d'historique ;
* versions de données ;
* restauration ;
* interface de consultation ;
* logique de comparaison ;
* tests.

Pour la V1, Git et la documentation suffisent à conserver une trace du travail.

---

## Décision

Les sauvegardes automatiques sont reportées.

Elles pourront être ajoutées plus tard si le projet évolue vers une vraie plateforme d'administration.

---

# 13. Refonte graphique complète

## Description

Une refonte graphique plus ambitieuse a été envisagée pour obtenir une interface plus moderne.

Elle aurait pu inclure :

* animations ;
* transitions ;
* sections plus complexes ;
* identité visuelle plus forte ;
* maquettes plus détaillées ;
* effets visuels avancés.

---

## Pourquoi cette piste n'a pas été intégrée

Une refonte complète aurait demandé beaucoup de temps.

La priorité de la V1 était :

* avoir un site fonctionnel ;
* avoir un backend réel ;
* réussir le déploiement ;
* produire une documentation complète ;
* garder une version stable.

---

## Décision

La refonte graphique complète est reportée.

La V1 conserve un design simple et améliorable.

---

# 14. Tests automatisés complets

## Description

Des tests automatisés plus complets ont été envisagés.

Ils pourraient couvrir :

* modèles ;
* vues ;
* routes ;
* administration ;
* formulaires ;
* sécurité ;
* comportements attendus ;
* accès du compte lecture seule ;
* TinyDB.

---

## Pourquoi cette piste n'a pas été intégrée

La V1 a été vérifiée manuellement et avec les commandes principales.

Commandes utilisées ou prévues :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

Mettre en place une vraie suite de tests automatisés aurait demandé du temps supplémentaire.

Pour cette version, les vérifications manuelles et les commandes de contrôle suffisent à valider le périmètre actuel.

---

## Décision

Les tests automatisés complets sont reportés.

Ils pourront être ajoutés dans une prochaine version plus stabilisée.

---

# 15. Gestion complète des médias

## Description

Un système de gestion des médias a été envisagé pour stocker des images, captures, vidéos ou fichiers liés aux projets.

---

## Pourquoi cette piste n'a pas été intégrée

La gestion complète des médias demande :

* modèles dédiés ;
* upload ;
* stockage ;
* sécurité ;
* suppression contrôlée ;
* limitation de taille ;
* organisation claire des fichiers ;
* tests supplémentaires.

Cela dépasse le besoin immédiat de la V1.

---

## Décision

Le système complet de médias est reporté.

La V1 conserve une gestion simple des fichiers statiques.

---

# 16. NoSQL avancé

## Description

Une base NoSQL plus avancée a été envisagée pour stocker des contenus flexibles.

Exemples possibles :

* notes de conception ;
* journaux de développement ;
* métadonnées de projet ;
* contenus variables selon les jeux ;
* données de progression.

MongoDB aurait pu être étudié dans une version plus avancée.

---

## Ce qui a été intégré

Une solution NoSQL légère a finalement été ajoutée avec TinyDB.

TinyDB permet de stocker des notes de progression dans un fichier JSON.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

TinyDB permet de démontrer une logique NoSQL sans installer une base distante.

---

## Pourquoi MongoDB n'a pas été intégré

MongoDB aurait demandé :

* une base externe ;
* une configuration dédiée ;
* des variables d'environnement supplémentaires ;
* une gestion de connexion ;
* une réflexion de production plus avancée ;
* une documentation supplémentaire ;
* des tests supplémentaires.

Ce niveau de complexité n'était pas nécessaire pour la V1.

---

## Décision

TinyDB est retenu comme expérimentation NoSQL légère.

MongoDB ou une base NoSQL avancée sont reportés.

---

# 17. SQL natif

## Description

Le projet utilise Django ORM et les migrations pour gérer les tables.

Cependant, des fichiers SQL natifs ont été envisagés pour mieux montrer la compréhension de la base de données.

---

## Ce qui a été intégré

Des fichiers SQL natifs documentaires ont été ajoutés.

Fichiers concernés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ils montrent :

* des exemples `CREATE TABLE` ;
* des exemples `INSERT INTO` ;
* le lien entre modèles Django, migrations, ORM et SQL.

---

## Limite

Le SQL natif reste documentaire.

Le projet ne repose pas sur des scripts SQL manuels pour créer les tables.

Les migrations Django restent la source réelle de création et de mise à jour de la base.

---

## Décision

La piste SQL natif documentaire est retenue.

L'utilisation de SQL brut dans les vues Django reste non retenue pour la V1.

---

# 18. JavaScript avancé ou framework frontend

## Description

Une interface plus dynamique aurait pu être développée avec un framework frontend ou davantage de JavaScript.

Exemples possibles :

* React ;
* Vue ;
* Angular ;
* tableaux de bord dynamiques ;
* animations avancées ;
* filtres complexes ;
* composants réactifs.

---

## Pourquoi cette piste n'a pas été intégrée

Un framework frontend aurait ajouté une couche supplémentaire.

Il aurait fallu gérer :

* installation ;
* build frontend ;
* organisation des composants ;
* communication avec Django ;
* tests supplémentaires ;
* documentation supplémentaire.

Pour la V1, ce n'était pas nécessaire.

---

## Ce qui a été intégré

Un JavaScript léger a été conservé pour le menu mobile.

Fichier concerné :

```text
static/js/menu.js
```

Ce JavaScript suffit pour :

* ouvrir le menu ;
* fermer le menu ;
* gérer l'état `aria-expanded` ;
* améliorer l'expérience mobile.

---

## Décision

Le framework frontend est reporté.

Le JavaScript léger du menu mobile est retenu.

---

# 19. Documentation de conception

## Description

Des documents de conception plus complets ont été envisagés pour renforcer le dossier projet.

Ils pouvaient inclure :

* MCD ;
* cas d'utilisation ;
* diagramme de séquence ;
* documentation des modèles ;
* documentation des vues.

---

## Ce qui a été intégré

Une documentation complémentaire a été ajoutée dans le dossier `docs/`.

Fichiers concernés :

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

Ces fichiers renforcent la présentation du projet sans modifier lourdement le code.

---

## Décision

La documentation de conception est retenue.

Les diagrammes plus avancés restent optionnels pour une version future.

---

# 20. Pistes reportées ou abandonnées pendant la stabilisation

## Description

Toutes les pistes explorées ne sont pas forcément destinées à revenir plus tard.

Certaines idées sont simplement reportées, car elles restent intéressantes mais ne sont pas adaptées à la V1.

D'autres idées peuvent être abandonnées pendant la phase de stabilisation si elles ne servent plus réellement l'objectif du projet.

Une V1 évolue constamment.

Les choix faits au départ peuvent donc être ajustés après :

* les premiers tests ;
* le déploiement ;
* la mise en place du backend ;
* la rédaction de la documentation ;
* la vérification du temps disponible ;
* la stabilisation du périmètre.

---

## Pourquoi certaines idées peuvent être abandonnées

Une idée peut être abandonnée si :

* elle ajoute trop de complexité ;
* elle fragilise le projet ;
* elle demande trop de temps ;
* elle n'apporte pas assez de valeur à la V1 ;
* elle rend la documentation plus difficile à maintenir ;
* elle détourne le projet de son objectif principal ;
* elle transforme le projet en usine à gaz ;
* elle peut être remplacée par une solution plus simple.

Abandonner une idée ne signifie pas que le projet échoue.

Cela peut au contraire montrer une bonne gestion du périmètre et une capacité à protéger la stabilité de la V1.

---

## Décision

Dans le cadre de Frostia Games, certaines pistes restent dans la roadmap, tandis que d'autres pourront être abandonnées si elles ne sont plus utiles.

L'objectif n'est pas de conserver toutes les idées envisagées.

L'objectif est de garder uniquement les choix qui renforcent :

* la stabilité ;
* la lisibilité ;
* la cohérence ;
* la maintenabilité ;
* la présentation de la V1.

---

# 21. Tableau récapitulatif

| Piste explorée                 | Décision actuelle | Raison principale |
| ------------------------------ | ----------------- | ----------------- |
| C# / ASP.NET Core / Razor      | Reporté | Risque de complexité pour la V1 |
| Django                         | Retenu | Adapté à une V1 stable et rapide |
| SQLite                         | Retenu | Suffisant pour une V1 de portfolio |
| PostgreSQL                     | Reporté | Trop tôt pour le périmètre actuel |
| Compte temporaire lecture seule | Retenu de manière limitée | Utile pour consultation contrôlée |
| Système de rôles avancé        | Reporté | Trop large pour la V1 |
| Admin personnalisée            | Reporté | Trop complexe pour une V1 |
| Upload serveur réel            | Reporté | Fonction sensible |
| Jeu jouable navigateur         | Reporté | Hors périmètre immédiat |
| Plotly.js                      | Reporté | Non indispensable |
| Espace privé complet           | Reporté | Trop large |
| Sauvegardes automatiques       | Reporté | Architecture plus avancée |
| Refonte graphique complète     | Reporté | Priorité à la stabilité |
| Tests automatisés complets     | Reporté | Temps supplémentaire |
| Gestion complète des médias    | Reporté | Trop lourd pour la V1 |
| TinyDB                         | Retenu de manière limitée | Preuve NoSQL légère |
| MongoDB                        | Reporté | Trop avancé pour la V1 |
| SQL natif documentaire         | Retenu | Renforce la compréhension base de données |
| SQL brut dans les vues         | Non retenu | ORM Django plus sûr et adapté |
| Framework frontend lourd       | Reporté | Complexité inutile pour la V1 |
| JavaScript menu mobile         | Retenu | Utile et limité |
| Documentation de conception    | Retenue | Renforce le dossier projet |
| Certaines idées secondaires    | Abandon possible | Stabilisation de la V1 |

---

# 22. Ce que montre cette démarche

Cette démarche montre que le projet a été pensé avec plusieurs directions possibles.

Les choix réalisés montrent :

* une capacité à explorer plusieurs solutions ;
* une capacité à comparer les technologies ;
* une capacité à limiter le périmètre ;
* une volonté d'éviter le scope creep ;
* une priorité donnée à la stabilité ;
* une volonté de produire une V1 terminée plutôt qu'un projet trop ambitieux ;
* une capacité à abandonner certaines idées si elles ne servent plus réellement le projet ;
* une capacité à intégrer certaines pistes de manière limitée quand elles renforcent le dossier.

Cette approche permet de préserver un projet clair, livrable et défendable.

---

# 23. Bilan

Les pistes explorées ne sont pas des oublis.

Elles montrent que plusieurs directions techniques et fonctionnelles ont été étudiées avant de stabiliser la V1.

Certaines pistes sont reportées, car elles restent intéressantes pour une version future.

D'autres pourront être abandonnées si elles ne servent plus réellement le projet ou si elles risquent de fragiliser la V1.

Certaines pistes ont été retenues de manière limitée, notamment :

* TinyDB ;
* compte temporaire de lecture seule ;
* SQL natif documentaire ;
* JavaScript du menu mobile ;
* documentation de conception.

La V1 de Frostia Games reste centrée sur l'essentiel :

* un projet Django fonctionnel ;
* une base SQLite ;
* une administration Django ;
* une interface publique ;
* un déploiement Render ;
* une documentation complète ;
* une expérimentation NoSQL légère ;
* une architecture évolutive.

Les fonctionnalités non intégrées ne sont donc pas des échecs.

Elles sont volontairement écartées, reportées ou abandonnées afin de protéger la qualité, la stabilité et la lisibilité de la V1.

À ce stade, la priorité reste la finalisation des captures, des preuves, des annexes et du dossier projet final.
