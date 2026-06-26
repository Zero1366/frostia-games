# Limites et évolutions - Frostia Games

## Objectif du document

Ce document présente les limites actuelles de la V1 du projet **Frostia Games** ainsi que les évolutions possibles pour les prochaines versions.

L'objectif est de montrer que le projet a été volontairement cadré afin de produire une version stable, fonctionnelle, documentée et déployée, sans ajouter trop de fonctionnalités en même temps.

Cette démarche permet d'éviter une dérive du périmètre, une dette technique trop importante ou une complexité inutile pour une première version.

Le document sert aussi à expliquer que certaines idées peuvent être conservées, reportées, simplifiées ou abandonnées pendant la phase de stabilisation.

Une V1 évolue constamment. L'objectif n'est donc pas de tout ajouter, mais de conserver uniquement ce qui renforce réellement le projet.

---

## Rappel du périmètre de la V1

La V1 du projet Frostia Games a pour objectif de proposer un portfolio Django simple et fonctionnel permettant de présenter des projets de jeux vidéo actuels et futurs.

Le périmètre retenu pour cette première version comprend :

* une application Django fonctionnelle ;
* trois pages principales ;
* une interface publique responsive ;
* une base SQLite ;
* une administration Django ;
* un affichage dynamique de certaines données ;
* une documentation technique ;
* un déploiement en ligne sur Render ;
* une sécurité minimale adaptée à une V1.

Cette V1 ne cherche pas encore à devenir une plateforme complète de gestion de projets, ni un espace privé avancé.

---

## Limites générales de la V1

La V1 est volontairement limitée.

Elle sert à poser une base stable, mais certaines fonctionnalités restent absentes ou incomplètes.

Limites principales :

* design encore améliorable ;
* responsive fonctionnel mais perfectible ;
* base de données SQLite ;
* pas de PostgreSQL ;
* pas de compte jury temporaire ;
* pas d'administration personnalisée ;
* pas d'espace privé complet ;
* pas de système complet d'ajout dynamique de projets ;
* pas d'upload serveur réel ;
* pas de jeu jouable directement dans le navigateur ;
* pas de statistiques avancées ;
* pas de graphiques Plotly.js intégrés ;
* pas de tests automatisés complets.

Ces limites sont assumées dans le cadre d'une première version.

Elles ne sont pas considérées comme des échecs, mais comme des choix de cadrage.

---

## Limite 01 - Design encore perfectible

## Description

Le design actuel est fonctionnel et cohérent avec l'identité du projet, mais il peut encore être amélioré.

La V1 propose déjà une interface propre, mais certains éléments pourront être retravaillés :

* espacement ;
* hiérarchie visuelle ;
* animations ;
* cartes ;
* transitions ;
* lisibilité de certaines sections ;
* rendu mobile ;
* cohérence graphique globale.

## Raison du report

Le design complet n'a pas été poussé trop loin afin de garder du temps pour la stabilisation technique, la documentation et le déploiement.

L'objectif principal était d'obtenir une V1 fonctionnelle et déployée, pas une version graphique définitive.

## Évolution possible

Dans une prochaine version, le design pourra être modernisé avec :

* une identité visuelle plus complète ;
* des maquettes Figma ;
* une meilleure organisation des sections ;
* des animations légères ;
* un responsive plus travaillé ;
* une meilleure mise en valeur des projets.

---

## Limite 02 - Responsive mobile à améliorer

## Description

Le site est consultable sur mobile, mais l'affichage peut encore être amélioré.

Certains éléments pourront être optimisés :

* taille des textes ;
* espacement des cartes ;
* affichage du menu mobile ;
* confort de lecture ;
* adaptation des sections longues ;
* cohérence entre desktop et mobile.

## Raison du report

Le responsive est suffisant pour une V1, mais une optimisation complète aurait demandé du temps supplémentaire.

La priorité a été donnée à la stabilité générale du projet.

## Évolution possible

Une prochaine version pourra intégrer :

* une meilleure sidebar mobile ;
* des cartes plus adaptées aux petits écrans ;
* des espacements plus réguliers ;
* des tests sur plusieurs formats ;
* une amélioration de l'expérience utilisateur mobile.

---

## Limite 03 - Utilisation de SQLite

## Description

La V1 utilise SQLite comme base de données.

SQLite est suffisant pour un portfolio simple, mais ce n'est pas la solution idéale pour une vraie production avec plusieurs utilisateurs ou beaucoup de données.

Base actuelle :

```txt
db.sqlite3
```

## Raison du choix

SQLite a été conservé car :

* il est simple à utiliser ;
* il est intégré facilement avec Django ;
* il suffit pour une V1 ;
* il permet de tester les modèles rapidement ;
* il évite une complexité supplémentaire.

## Limite

Sur Render, SQLite peut poser des limites, notamment car le stockage local d'un service gratuit n'est pas conçu comme une base de production durable.

## Évolution possible

Une version future pourra migrer vers PostgreSQL.

PostgreSQL permettrait :

* une base plus robuste ;
* une meilleure compatibilité production ;
* une meilleure gestion des données ;
* une persistance plus fiable ;
* une architecture plus professionnelle.

Cette évolution est reportée pour éviter de complexifier trop tôt la V1.

---

## Limite 04 - Pas de compte jury temporaire

## Description

Aucun compte jury temporaire n'a été créé dans la V1.

L'administration Django est fonctionnelle, mais l'accès reste réservé à l'administrateur du projet.

## Raison du report

Créer un compte jury maintenant aurait ajouté une couche de gestion supplémentaire :

* mot de passe temporaire ;
* droits à limiter ;
* accès à surveiller ;
* compte à supprimer après évaluation ;
* risque de donner trop de permissions.

Pour la V1, les captures d'écran et la documentation suffisent à montrer que l'administration fonctionne.

## Évolution possible

Si le projet est validé comme second projet ou si l'évaluateur demande un accès direct, un compte temporaire pourra être créé.

Ce compte devra être :

* limité ;
* temporaire ;
* en consultation si possible ;
* supprimé après l'évaluation ;
* séparé du compte administrateur principal.

Exemple de compte possible :

```txt
jury_demo
```

Ce compte ne devra jamais avoir les pleins droits administrateur.

---

## Limite 05 - Administration Django non personnalisée

## Description

La V1 utilise l'administration Django intégrée.

Cette interface permet déjà de gérer les modèles du projet, mais elle n'est pas personnalisée graphiquement.

## Raison du choix

L'admin Django est suffisante pour une V1 car elle permet :

* d'ajouter des données ;
* de modifier des données ;
* de tester les modèles ;
* de vérifier le fonctionnement du backend ;
* de gagner du temps.

Créer une interface d'administration personnalisée aurait demandé beaucoup plus de développement.

## Évolution possible

Une future version pourra proposer une interface d'administration personnalisée avec :

* tableau de bord privé ;
* formulaire d'ajout de projet ;
* gestion des captures ;
* gestion des statuts ;
* gestion des liens ;
* sauvegarde automatique avant modification ;
* historique des changements.

Cette évolution sera utile si le site devient une vraie plateforme de gestion de projets.

---

## Limite 06 - Ajout dynamique de projets encore limité

## Description

Le projet dispose déjà de modèles Django et d'un affichage dynamique, mais le système complet d'ajout et de gestion de projets n'est pas encore finalisé.

La V1 ne propose pas encore une interface complète permettant de gérer toutes les informations d'un projet de manière avancée.

## Raison du report

Le système dynamique complet aurait demandé :

* plus de modèles ;
* plus de champs ;
* plus de templates ;
* plus de validations ;
* une meilleure gestion des médias ;
* des tests supplémentaires ;
* une interface plus complexe.

Pour la V1, il était préférable de conserver un système simple.

## Évolution possible

Une future version pourra ajouter des modèles plus détaillés :

```txt
Projet
Version
Capture
Lien
Statut
Article
Journal de développement
```

Ces modèles permettraient de transformer le portfolio en véritable base de suivi des projets.

---

## Limite 07 - Pas d'upload serveur réel

## Description

La page des projets jouables contient une interface préparatoire, mais aucun upload serveur réel n'est implanté dans la V1.

Cela signifie que :

* aucun fichier n'est envoyé au serveur ;
* aucun fichier n'est stocké ;
* aucun fichier n'est exécuté ;
* aucun vrai système de lecture serveur n'est actif.

## Raison du report

L'upload serveur est une fonctionnalité sensible.

Elle demande :

* des contrôles de sécurité ;
* une vérification des extensions ;
* une limitation de taille ;
* une gestion du stockage ;
* une protection contre les fichiers dangereux ;
* une logique de suppression ;
* des tests supplémentaires.

Ajouter cette fonctionnalité trop tôt aurait augmenté le risque technique.

## Évolution possible

Une future version pourra intégrer :

* upload sécurisé de médias ;
* stockage organisé ;
* validation des fichiers ;
* limitation de taille ;
* gestion des miniatures ;
* suppression contrôlée ;
* stockage externe si nécessaire.

---

## Limite 08 - Pas de jeu jouable dans le navigateur

## Description

La V1 ne contient pas encore de jeu jouable directement dans le navigateur.

La page des projets jouables sert actuellement de préparation à une évolution future.

## Raison du report

Intégrer un jeu jouable dans un site web demande une réflexion technique importante.

Il faut gérer :

* le format du jeu ;
* l'intégration dans le navigateur ;
* les performances ;
* le chargement ;
* la compatibilité ;
* la sécurité ;
* les contrôles ;
* l'expérience utilisateur.

Pour cette V1, ce travail aurait été trop ambitieux.

## Évolution possible

Une future version pourra prévoir :

* une page de démonstration jouable ;
* une intégration WebGL ou équivalent ;
* un lecteur de démo ;
* une page dédiée par projet ;
* des informations techniques sur chaque build.

Cette fonctionnalité doit rester une évolution future, pas une priorité immédiate.

---

## Limite 09 - Pas de statistiques avancées

## Description

La V1 ne contient pas encore de statistiques ou graphiques avancés.

Plotly.js a été envisagé comme future amélioration, mais n'est pas intégré pour l'instant.

## Raison du report

Les graphiques ne sont pas indispensables au fonctionnement de la V1.

Les intégrer maintenant aurait ajouté :

* du JavaScript supplémentaire ;
* des données à structurer ;
* des graphiques à concevoir ;
* une logique d'affichage ;
* une documentation supplémentaire.

## Évolution possible

Une prochaine version pourra intégrer Plotly.js pour afficher :

* progression d'un projet ;
* état des versions ;
* répartition des tâches ;
* avancement global ;
* historique de développement.

Cette évolution pourra être présentée comme une amélioration future.

---

## Limite 10 - Tests automatisés incomplets

## Description

La V1 a été vérifiée manuellement, mais ne dispose pas encore d'une couverture complète de tests automatisés.

Les vérifications actuelles reposent surtout sur :

* `python manage.py check` ;
* tests manuels des pages ;
* tests de l'administration ;
* tests du déploiement Render ;
* tests visuels ;
* vérifications fonctionnelles.

## Raison du report

Mettre en place une vraie campagne de tests automatisés demande du temps.

Pour cette V1, la priorité a été donnée à :

* la stabilité ;
* le fonctionnement visible ;
* le déploiement ;
* la documentation ;
* les vérifications manuelles.

## Évolution possible

Une version future pourra ajouter :

* tests unitaires Django ;
* tests des vues ;
* tests des modèles ;
* tests des URLs ;
* tests de formulaires ;
* tests d'accès admin ;
* tests de sécurité ;
* tests responsive plus systématiques.

---

## Limite 11 - Documentation encore à maintenir

## Description

La documentation du projet est déjà importante, mais elle devra être maintenue au fur et à mesure des évolutions.

Chaque nouvelle fonctionnalité devra être documentée.

## Risque

Si la documentation n'est pas mise à jour, elle peut devenir incohérente avec le projet réel.

## Évolution possible

Pour éviter cela, chaque étape future devra suivre la règle suivante :

```txt
Une fonctionnalité ajoutée = une documentation mise à jour.
```

Documents à maintenir :

* journal de bord ;
* changelog ;
* documentation d'installation ;
* documentation de déploiement ;
* documentation architecture ;
* documentation sécurité ;
* documentation utilisateur.

---

## Limite 12 - Offre gratuite Render

## Description

Le projet est déployé sur l'offre gratuite de Render.

Cette offre permet de rendre le site accessible en ligne, mais elle possède des limites.

Limites possibles :

* mise en veille après inactivité ;
* premier chargement plus lent ;
* ressources limitées ;
* pas de disque persistant gratuit pour certains usages ;
* performances limitées.

## Raison du choix

L'offre gratuite est suffisante pour une V1, une démonstration et un projet de formation.

Elle permet de tester un vrai déploiement sans coût immédiat.

## Évolution possible

Si le projet devient plus important, il pourra évoluer vers :

* une offre Render payante ;
* un hébergement plus robuste ;
* une base PostgreSQL hébergée ;
* un stockage externe ;
* une configuration de production plus avancée.

---

## Ce qui est volontairement exclu de la V1

Les éléments suivants sont volontairement exclus de la V1 :

```txt
PostgreSQL
Compte jury temporaire
Interface admin personnalisée
Upload serveur réel
Jeu jouable navigateur
Statistiques avancées
Graphiques Plotly.js
Espace privé complet
Système de sauvegarde automatique
Gestion avancée des médias
Tests automatisés complets
```

Ces éléments ne sont pas oubliés.

Ils sont reportés afin de protéger la stabilité du projet.

---

## Risques évités

Le cadrage de la V1 permet d'éviter plusieurs risques classiques :

* scope creep ;
* dette technique ;
* fonctionnalités commencées mais non terminées ;
* projet trop complexe ;
* perte de stabilité ;
* documentation impossible à maintenir ;
* déploiement plus difficile ;
* retard important ;
* transformation du projet en usine à gaz.

La priorité a été donnée à une version simple, stable, déployée et défendable.

---

## Idées pouvant être abandonnées pendant la stabilisation

Pendant la phase de stabilisation d'une V1, certaines idées peuvent être reportées, simplifiées ou même abandonnées.

Un projet en V1 évolue constamment.

Toutes les idées envisagées au départ ne sont pas forcément conservées jusqu'à la version présentable.

Certaines idées peuvent sembler intéressantes au début, mais devenir moins pertinentes après :

* les premiers tests ;
* la mise en place du backend ;
* le déploiement ;
* la rédaction de la documentation ;
* la vérification du temps disponible ;
* la stabilisation du périmètre.

Abandonner une idée ne signifie pas que le projet échoue.

Cela peut au contraire montrer une bonne gestion du périmètre.

Une idée peut être abandonnée si :

* elle ajoute trop de complexité ;
* elle n'est pas indispensable pour la V1 ;
* elle risque de fragiliser le projet ;
* elle demande trop de temps par rapport à sa valeur réelle ;
* elle rend la documentation plus difficile à maintenir ;
* elle détourne le projet de son objectif principal ;
* elle transforme une version stable en projet trop lourd ;
* elle peut être remplacée par une solution plus simple ;
* elle n'apporte pas assez de valeur à l'évaluateur ou à l'utilisateur final.

Dans le cadre de Frostia Games, la priorité de la phase de stabilisation est de conserver une version :

* fonctionnelle ;
* claire ;
* déployée ;
* documentée ;
* testable ;
* présentable.

Certaines idées pourront donc être conservées dans la roadmap, tandis que d'autres pourront être abandonnées si elles ne servent plus réellement le projet.

Cette démarche permet d'éviter de conserver des fonctionnalités uniquement parce qu'elles avaient été envisagées au départ.

Une V1 doit rester vivante, mais elle doit aussi être protégée contre l'accumulation excessive d'idées.

L'objectif n'est pas de tout garder.

L'objectif est de garder ce qui renforce réellement le projet.

---

## Évolutions prioritaires

Les évolutions futures doivent être ajoutées progressivement.

Priorité 1 :

* améliorer le contenu des pages ;
* corriger les textes ;
* améliorer le responsive ;
* finaliser les captures ;
* améliorer le README ;
* finaliser le dossier projet.

Priorité 2 :

* améliorer le design ;
* créer des maquettes Figma ;
* enrichir les fiches projets ;
* structurer davantage les données ;
* améliorer l'administration Django.

Priorité 3 :

* ajouter PostgreSQL ;
* créer un compte jury temporaire si demandé ;
* intégrer Plotly.js ;
* préparer une vraie section de projets jouables ;
* étudier l'intégration d'une démonstration dans le navigateur.

---

## Roadmap possible

## Version 1.1

Objectif : améliorer la présentation sans changer l'architecture.

Évolutions possibles :

* nettoyage des textes ;
* amélioration mobile ;
* meilleure mise en page ;
* captures propres ;
* README plus complet ;
* dossier projet finalisé.

---

## Version 1.2

Objectif : améliorer la gestion des contenus.

Évolutions possibles :

* modèles Django plus détaillés ;
* fiches projets complètes ;
* meilleure utilisation de l'administration ;
* champs supplémentaires ;
* tri des projets ;
* statuts plus précis.

---

## Version 2.0

Objectif : transformer le portfolio en plateforme plus complète.

Évolutions possibles :

* PostgreSQL ;
* espace privé ;
* administration personnalisée ;
* compte jury temporaire ;
* upload sécurisé ;
* gestion avancée des médias ;
* graphiques de suivi ;
* intégration éventuelle de démonstrations jouables.

---

## Conditions avant d'ajouter une nouvelle fonctionnalité

Avant d'ajouter une nouvelle fonctionnalité, il faudra vérifier :

* est-ce utile pour le projet ?
* est-ce nécessaire pour la V1 ?
* combien d'heures cela demande ?
* est-ce que cela risque de casser l'existant ?
* est-ce documentable simplement ?
* est-ce testable ?
* est-ce que cela ajoute trop de complexité ?
* est-ce que cela peut être reporté ?
* est-ce que cette idée doit vraiment être conservée ?
* est-ce que cette idée peut être simplifiée ?
* est-ce que cette idée doit être abandonnée pour stabiliser la V1 ?

Si une fonctionnalité n'est pas indispensable, elle doit être reportée.

Si une idée fragilise la V1, elle doit être simplifiée ou abandonnée.

---

## Bilan

La V1 de Frostia Games est volontairement limitée, mais elle est fonctionnelle.

Elle permet déjà de montrer :

* une base Django ;
* une interface publique ;
* une base SQLite ;
* une administration Django ;
* un affichage dynamique ;
* un déploiement Render ;
* une documentation complète ;
* une réflexion technique sur les limites et évolutions.

Les limites actuelles ne sont pas des échecs.

Elles montrent que le projet a été cadré pour rester stable et présentable.

Les évolutions futures sont identifiées, mais elles seront ajoutées progressivement, uniquement si elles apportent une vraie valeur au projet.

Certaines idées pourront aussi être abandonnées pendant la stabilisation si elles ne servent plus l'objectif principal de la V1.

La priorité reste de conserver un projet clair, stable, maintenable, documenté et défendable.
