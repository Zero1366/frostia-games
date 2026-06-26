# Pistes explorées et non retenues - Frostia Games

## Objectif du document

Ce document présente les pistes techniques et fonctionnelles envisagées pendant le développement du projet **Frostia Games**, mais qui n'ont pas été intégrées dans la V1.

L'objectif est de montrer que les choix réalisés ne sont pas dus au hasard. Plusieurs solutions ont été réfléchies, comparées, puis certaines ont été volontairement retenues, reportées ou abandonnées afin de conserver une première version stable, livrable, documentée et déployée.

Le principe retenu pour ce projet est le suivant :

```txt
Toutes les pistes intéressantes peuvent être envisagées et explorées, mais seules les fonctionnalités utiles à une V1 stable doivent être intégrées immédiatement.
```

Une V1 évolue constamment.

Certaines idées peuvent rester dans la roadmap, tandis que d'autres peuvent être abandonnées pendant la phase de stabilisation si elles ne servent plus réellement le projet.

---

## Principe général

Au début du projet, plusieurs pistes étaient possibles.

Le projet aurait pu évoluer vers :

* une application Django simple ;
* une application plus avancée avec PostgreSQL ;
* une solution C# / ASP.NET Core / Razor ;
* une interface d'administration personnalisée ;
* un espace privé complet ;
* un système de gestion de projets plus dynamique ;
* une plateforme permettant plus tard d'intégrer des projets jouables.

Cependant, l'objectif de cette V1 n'était pas de tout faire immédiatement.

L'objectif était de créer une base :

* fonctionnelle ;
* stable ;
* claire ;
* documentée ;
* déployée ;
* évolutive ;
* maîtrisable.

Certaines pistes ont donc été écartées, reportées ou pourront être abandonnées afin d'éviter de transformer la V1 en projet trop lourd.

---

## Méthode de décision

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

---

# 1. Piste C# / ASP.NET Core / Razor

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

C# reste un langage que je considère comme très intéressant pour mes futurs projets, notamment parce qu'il impose une discipline plus forte que Python.

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

# 2. Choix final : Python et Django

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
* utilisation d'un environnement virtuel `.venv` ;
* séparation entre templates, vues et fichiers statiques ;
* migrations Django ;
* administration Django contrôlée ;
* variables d'environnement pour les informations sensibles ;
* déploiement Render documenté ;
* tests manuels des pages ;
* vérification de l'administration ;
* vérification du responsive ;
* documentation des limites et évolutions.

Ces garde-fous permettent de rendre le projet plus fiable malgré la permissivité de Python.

---

# 3. PostgreSQL

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

# 4. Compte jury temporaire

## Description

Un compte temporaire pour le jury ou l'évaluateur a été envisagé.

Ce compte permettrait de consulter l'administration Django sans utiliser le vrai compte administrateur.

---

## Pourquoi cette piste n'a pas été intégrée

Créer un compte jury demande une gestion supplémentaire :

* identifiant temporaire ;
* mot de passe temporaire ;
* droits limités ;
* risque de donner trop d'accès ;
* suppression du compte après évaluation ;
* transmission sécurisée des identifiants.

Pour la V1, les captures d'écran et la documentation suffisent à prouver que l'administration Django fonctionne.

---

## Décision

Le compte jury temporaire est reporté.

Il pourra être créé plus tard uniquement si le projet est validé comme second projet ou si l'évaluateur demande explicitement un accès direct.

---

# 5. Administration personnalisée

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

# 6. Upload serveur réel

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

# 7. Jeu jouable dans le navigateur

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

# 8. Plotly.js et graphiques

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

# 9. Espace privé complet

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

# 10. Sauvegardes automatiques

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

# 11. Refonte graphique complète

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

# 12. Tests automatisés complets

## Description

Des tests automatisés plus complets ont été envisagés.

Ils pourraient couvrir :

* modèles ;
* vues ;
* routes ;
* administration ;
* formulaires ;
* sécurité ;
* comportements attendus.

---

## Pourquoi cette piste n'a pas été intégrée

La V1 a été vérifiée manuellement et avec les commandes Django principales.

Mettre en place une vraie suite de tests automatisés aurait demandé du temps supplémentaire.

Pour cette version, les vérifications manuelles et `python manage.py check` suffisent à valider le périmètre actuel.

---

## Décision

Les tests automatisés complets sont reportés.

Ils pourront être ajoutés dans une prochaine version plus stabilisée.

---

# 13. Gestion complète des médias

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

# 14. Pistes reportées ou abandonnées pendant la stabilisation

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

# Tableau récapitulatif

| Piste explorée              | Décision         | Raison principale                 |
| --------------------------- | ---------------- | --------------------------------- |
| C# / ASP.NET Core / Razor   | Reporté          | Risque de complexité pour la V1   |
| Django                      | Retenu           | Adapté à une V1 stable et rapide  |
| PostgreSQL                  | Reporté          | Trop tôt pour le périmètre actuel |
| Compte jury temporaire      | Reporté          | Sécurité et droits à limiter      |
| Admin personnalisée         | Reporté          | Trop complexe pour une V1         |
| Upload serveur réel         | Reporté          | Fonction sensible                 |
| Jeu jouable navigateur      | Reporté          | Hors périmètre immédiat           |
| Plotly.js                   | Reporté          | Non indispensable                 |
| Espace privé complet        | Reporté          | Trop large                        |
| Sauvegardes automatiques    | Reporté          | Architecture plus avancée         |
| Refonte graphique complète  | Reporté          | Priorité à la stabilité           |
| Tests automatisés complets  | Reporté          | Temps supplémentaire              |
| Gestion complète des médias | Reporté          | Trop lourd pour la V1             |
| Certaines idées secondaires | Abandon possible | Stabilisation de la V1            |

---

## Ce que montre cette démarche

Cette démarche montre que le projet a été pensé avec plusieurs directions possibles.

Les choix réalisés montrent :

* une capacité à explorer plusieurs solutions ;
* une capacité à comparer les technologies ;
* une capacité à limiter le périmètre ;
* une volonté d'éviter le scope creep ;
* une priorité donnée à la stabilité ;
* une volonté de produire une V1 terminée plutôt qu'un projet trop ambitieux ;
* une capacité à abandonner certaines idées si elles ne servent plus réellement le projet.

Cette approche permet de préserver un projet clair, livrable et défendable.

---

## Bilan

Les pistes explorées ne sont pas des oublis.

Elles montrent que plusieurs directions techniques et fonctionnelles ont été étudiées avant de stabiliser la V1.

Certaines pistes sont reportées, car elles restent intéressantes pour une version future.

D'autres pourront être abandonnées si elles ne servent plus réellement le projet ou si elles risquent de fragiliser la V1.

La V1 de Frostia Games reste centrée sur l'essentiel :

* un projet Django fonctionnel ;
* une base SQLite ;
* une administration Django ;
* une interface publique ;
* un déploiement Render ;
* une documentation complète ;
* une architecture évolutive.

Les fonctionnalités non intégrées ne sont donc pas des échecs.

Elles sont volontairement écartées, reportées ou abandonnées afin de protéger la qualité, la stabilité et la lisibilité de la V1.
