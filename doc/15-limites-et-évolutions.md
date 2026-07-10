# Limites et évolutions — Frostia Games

## Objectif du document

Ce document présente les limites actuelles de la V1 du projet **Frostia Games** ainsi que les évolutions possibles pour les prochaines versions.

L'objectif est de montrer que le projet a été volontairement cadré afin de produire une version stable, fonctionnelle, documentée et déployée, sans ajouter trop de fonctionnalités en même temps.

Cette démarche permet d'éviter :

- une dérive du périmètre ;
- une dette technique trop importante ;
- une complexité inutile ;
- des fonctionnalités commencées mais non terminées ;
- une documentation incohérente avec le projet réel.

Ce document sert aussi à expliquer que certaines idées peuvent être conservées, reportées, simplifiées ou abandonnées pendant la stabilisation du projet.

La V1 ne cherche pas à tout intégrer. Elle cherche à conserver uniquement ce qui renforce réellement le projet.

---

# 1. Rappel du périmètre de la V1

La V1 de Frostia Games a pour objectif de proposer un portfolio Django simple et fonctionnel permettant de présenter des projets de jeux vidéo actuels et futurs.

Le périmètre retenu pour cette première version comprend :

- une application Django fonctionnelle ;
- trois pages principales ;
- une interface publique responsive ;
- une base SQLite ;
- une administration Django ;
- un affichage dynamique de certaines données ;
- une expérimentation NoSQL légère avec TinyDB ;
- un affichage de notes de progression sur l’accueil ;
- un menu mobile JavaScript ;
- un accès d’évaluation en lecture seule ;
- une documentation technique ;
- une documentation de conception ;
- une documentation SQL native ;
- un déploiement en ligne sur Render ;
- une commande d’initialisation automatique des données Render ;
- une sécurité minimale adaptée à une V1 ;
- des preuves organisées dans `docs/preuves/`.

Cette V1 ne cherche pas encore à devenir une plateforme complète de gestion de projets, ni un espace privé avancé.

---

# 2. Limites générales de la V1

La V1 est volontairement limitée.

Elle sert à poser une base stable, mais certaines fonctionnalités restent absentes ou incomplètes.

Limites principales :

- design encore améliorable ;
- responsive fonctionnel mais perfectible ;
- base de données principale encore en SQLite ;
- SQLite sur Render gratuit non considéré comme une persistance durable avancée ;
- pas de PostgreSQL ;
- pas d'administration personnalisée ;
- pas d'espace privé complet ;
- pas de système complet de fiches projets détaillées ;
- pas d'upload serveur réel ;
- pas de jeu jouable directement dans le navigateur ;
- pas de statistiques avancées ;
- pas de graphiques Plotly.js intégrés ;
- pas de tests automatisés complets ;
- TinyDB limité à une preuve NoSQL légère ;
- accès d’évaluation limité à la consultation, sans système de rôles avancé.

Ces limites sont assumées dans le cadre d'une première version.

Elles ne sont pas considérées comme des échecs, mais comme des choix de cadrage.

---

# 3. Éléments initialement reportés mais finalement intégrés

Certains éléments qui étaient au départ envisagés comme des pistes futures ont été intégrés de manière limitée et contrôlée pendant le renforcement du dossier.

## 3.1 TinyDB

TinyDB a été ajouté pour démontrer une logique NoSQL simple.

Il sert à stocker des notes de progression dans un fichier JSON.

Fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

Commande de vérification :

```powershell
python -m scripts.demo_tinydb_notes
```

TinyDB ne remplace pas SQLite.

Il reste une expérimentation légère.

---

## 3.2 Accès d’évaluation en lecture seule

Un compte d’évaluation en lecture seule a été mis en place.

Il permet une consultation limitée de l’administration Django.

Il peut consulter :

- les créations ;
- les projets jouables.

Il ne doit pas permettre :

- l’ajout de contenus ;
- la modification de contenus ;
- la suppression de contenus ;
- l’accès aux secrets du projet ;
- la modification des comptes et permissions sensibles.

Les identifiants réels ne doivent pas être affichés dans les captures publiques.

Ils peuvent être transmis séparément uniquement si l’évaluateur les demande.

---

## 3.3 SQL natif documentaire

Des fichiers SQL natifs ont été ajoutés pour renforcer la partie base de données du dossier projet.

Fichiers concernés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces fichiers servent à montrer la compréhension du SQL.

Ils ne remplacent pas les migrations Django.

---

## 3.4 Documentation complémentaire

Le dossier `docs/` a été ajouté pour renforcer la documentation technique.

Il contient notamment :

```text
docs/backend/
docs/conception/
docs/frontend/
docs/nosql/
docs/preuves/
docs/sql/
```

Ce dossier complète la documentation principale du dossier `doc/`.

---

## 3.5 Initialisation automatique Render

Une commande Django personnalisée a été ajoutée pour stabiliser la version en ligne :

```bash
python manage.py setup_render_data
```

Elle recrée automatiquement les données minimales nécessaires à la démonstration :

- création principale Frostia Games ;
- projet jouable de démonstration ;
- groupe `Evaluation lecture seule` ;
- compte d’évaluation ;
- permissions de lecture seule.

Cette commande permet d’éviter qu’un redémarrage Render laisse l’administration vide.

---

# 4. Limite 01 — Design encore perfectible

## Description

Le design actuel est fonctionnel et cohérent avec l'identité du projet, mais il peut encore être amélioré.

La V1 propose déjà une interface propre, mais certains éléments pourront être retravaillés :

- espacement ;
- hiérarchie visuelle ;
- animations ;
- cartes ;
- transitions ;
- lisibilité de certaines sections ;
- rendu mobile ;
- cohérence graphique globale.

## Raison du report

Le design complet n'a pas été poussé trop loin afin de garder du temps pour :

- la stabilisation technique ;
- la documentation ;
- le déploiement ;
- les preuves ;
- les captures ;
- les corrections de dossier.

L'objectif principal était d'obtenir une V1 fonctionnelle et déployée, pas une version graphique définitive.

## Évolution possible

Dans une prochaine version, le design pourra être modernisé avec :

- une identité visuelle plus complète ;
- des maquettes Figma plus poussées ;
- une meilleure organisation des sections ;
- des animations légères ;
- un responsive plus travaillé ;
- une meilleure mise en valeur des projets.

---

# 5. Limite 02 — Responsive mobile à améliorer

## Description

Le site est consultable sur mobile, mais l'affichage peut encore être amélioré.

Certains éléments pourront être optimisés :

- taille des textes ;
- espacement des cartes ;
- affichage du menu mobile ;
- confort de lecture ;
- adaptation des sections longues ;
- cohérence entre desktop et mobile.

## Raison du report

Le responsive est suffisant pour une V1, mais une optimisation complète aurait demandé du temps supplémentaire.

La priorité a été donnée à la stabilité générale du projet.

## Évolution possible

Une prochaine version pourra intégrer :

- une meilleure sidebar mobile ;
- des cartes plus adaptées aux petits écrans ;
- des espacements plus réguliers ;
- des tests sur plusieurs formats ;
- une amélioration de l'expérience utilisateur mobile.

---

# 6. Limite 03 — Utilisation de SQLite

## Description

La V1 utilise SQLite comme base de données principale.

SQLite est suffisant pour un portfolio simple, mais ce n'est pas la solution idéale pour une vraie production avec plusieurs utilisateurs ou beaucoup de données.

## Raison du choix

SQLite a été conservé car :

- il est simple à utiliser ;
- il est intégré facilement avec Django ;
- il suffit pour une V1 ;
- il permet de tester les modèles rapidement ;
- il évite une complexité supplémentaire.

## Limite sur Render

Sur Render gratuit, SQLite ne doit pas être considéré comme une base de production durable.

Une base créée ou modifiée manuellement peut se retrouver vide après redémarrage ou redéploiement.

Pour cette raison, le projet utilise `setup_render_data` afin de recréer les données de démonstration automatiquement.

## Évolution possible

Une version future pourra migrer vers PostgreSQL.

PostgreSQL permettrait :

- une base plus robuste ;
- une meilleure compatibilité production ;
- une meilleure gestion des données ;
- une persistance plus fiable ;
- une architecture plus professionnelle.

Cette évolution est reportée pour éviter de complexifier trop tôt la V1.

---

# 7. Limite 04 — Accès d’évaluation limité

## Description

Un accès d’évaluation en lecture seule existe désormais.

Il permet de consulter certaines parties de l’administration Django, mais il ne constitue pas un vrai système de rôles avancé.

## Ce qui est fait

Le compte d’évaluation permet :

- une consultation limitée ;
- un droit de regard sur les créations ;
- un droit de regard sur les projets jouables ;
- une présentation plus sécurisée qu’un compte superutilisateur.

## Limite

Ce compte ne remplace pas :

- une interface d’administration personnalisée ;
- un système de rôles complet ;
- un espace privé ;
- une gestion avancée des permissions métier.

## Évolution possible

Une future version pourra proposer :

- des rôles plus fins ;
- une interface dédiée à l’évaluation ;
- un accès temporaire mieux encadré ;
- une expiration automatique ;
- une page de consultation publique ou semi-privée.

Les identifiants du compte d’évaluation ne doivent pas être publiés dans la documentation publique.

---

# 8. Limite 05 — Administration Django non personnalisée

## Description

La V1 utilise l'administration Django intégrée.

Cette interface permet déjà de gérer les modèles du projet, mais elle n'est pas personnalisée graphiquement.

## Raison du choix

L'admin Django est suffisante pour une V1 car elle permet :

- d'ajouter des données ;
- de modifier des données ;
- de tester les modèles ;
- de vérifier le fonctionnement du backend ;
- de gagner du temps.

Créer une interface d'administration personnalisée aurait demandé beaucoup plus de développement.

## Évolution possible

Une future version pourra proposer une interface d'administration personnalisée avec :

- tableau de bord privé ;
- formulaire d'ajout de projet ;
- gestion des captures ;
- gestion des statuts ;
- gestion des liens ;
- sauvegarde automatique avant modification ;
- historique des changements.

Cette évolution sera utile si le site devient une vraie plateforme de gestion de projets.

---

# 9. Limite 06 — Ajout dynamique de projets encore limité

## Description

Le projet dispose déjà de modèles Django et d'un affichage dynamique, mais le système complet d'ajout et de gestion de projets n'est pas encore finalisé.

La V1 ne propose pas encore une interface complète permettant de gérer toutes les informations d'un projet de manière avancée.

## Raison du report

Le système dynamique complet aurait demandé :

- plus de modèles ;
- plus de champs ;
- plus de templates ;
- plus de validations ;
- une meilleure gestion des médias ;
- des tests supplémentaires ;
- une interface plus complexe.

Pour la V1, il était préférable de conserver un système simple.

## Évolution possible

Une future version pourra ajouter des modèles plus détaillés :

```text
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

# 10. Limite 07 — Pas d'upload serveur réel

## Description

La page des projets jouables contient une interface préparatoire, mais aucun upload serveur réel n'est implanté dans la V1.

Cela signifie que :

- aucun fichier n'est envoyé au serveur ;
- aucun fichier n'est stocké ;
- aucun fichier n'est exécuté ;
- aucun vrai système de lecture serveur n'est actif.

## Raison du report

L'upload serveur est une fonctionnalité sensible.

Elle demande :

- des contrôles de sécurité ;
- une vérification des extensions ;
- une limitation de taille ;
- une gestion du stockage ;
- une protection contre les fichiers dangereux ;
- une logique de suppression ;
- des tests supplémentaires.

Ajouter cette fonctionnalité trop tôt aurait augmenté le risque technique.

## Évolution possible

Une future version pourra intégrer :

- upload sécurisé de médias ;
- stockage organisé ;
- validation des fichiers ;
- limitation de taille ;
- gestion des miniatures ;
- suppression contrôlée ;
- stockage externe si nécessaire.

---

# 11. Limite 08 — Pas de jeu jouable dans le navigateur

## Description

La V1 ne contient pas encore de jeu jouable directement dans le navigateur.

La page des projets jouables sert actuellement de préparation à une évolution future.

## Raison du report

Intégrer un jeu jouable dans un site web demande une réflexion technique importante.

Il faut gérer :

- le format du jeu ;
- l'intégration dans le navigateur ;
- les performances ;
- le chargement ;
- la compatibilité ;
- la sécurité ;
- les contrôles ;
- l'expérience utilisateur.

Pour cette V1, ce travail aurait été trop ambitieux.

## Évolution possible

Une future version pourra prévoir :

- une page de démonstration jouable ;
- une intégration WebGL ou équivalent ;
- un lecteur de démo ;
- une page dédiée par projet ;
- des informations techniques sur chaque build.

Cette fonctionnalité doit rester une évolution future, pas une priorité immédiate.

---

# 12. Limite 09 — Pas de statistiques avancées

## Description

La V1 ne contient pas encore de statistiques ou graphiques avancés.

Plotly.js a été envisagé comme future amélioration, mais n'est pas intégré pour l'instant.

## Raison du report

Les graphiques ne sont pas indispensables au fonctionnement de la V1.

Les intégrer maintenant aurait ajouté :

- du JavaScript supplémentaire ;
- des données à structurer ;
- des graphiques à concevoir ;
- une logique d'affichage ;
- une documentation supplémentaire.

## Évolution possible

Une prochaine version pourra intégrer Plotly.js pour afficher :

- progression d'un projet ;
- état des versions ;
- répartition des tâches ;
- avancement global ;
- historique de développement.

Cette évolution pourra être présentée comme une amélioration future.

---

# 13. Limite 10 — Tests automatisés incomplets

## Description

La V1 a été vérifiée manuellement, mais ne dispose pas encore d'une couverture complète de tests automatisés.

Les vérifications actuelles reposent surtout sur :

- `python manage.py check` ;
- `python -m scripts.demo_tinydb_notes` ;
- tests manuels des pages ;
- tests de l'administration ;
- tests du compte d’évaluation en lecture seule ;
- tests du déploiement Render ;
- tests visuels ;
- vérifications fonctionnelles.

## Raison du report

Mettre en place une vraie campagne de tests automatisés demande du temps.

Pour cette V1, la priorité a été donnée à :

- la stabilité ;
- le fonctionnement visible ;
- le déploiement ;
- la documentation ;
- les vérifications manuelles ;
- les preuves.

## Évolution possible

Une version future pourra ajouter :

- tests unitaires Django ;
- tests des vues ;
- tests des modèles ;
- tests des URLs ;
- tests de formulaires ;
- tests d'accès admin ;
- tests TinyDB ;
- tests de sécurité ;
- tests responsive plus systématiques.

---

# 14. Limite 11 — TinyDB limité à une preuve NoSQL légère

## Description

TinyDB est intégré dans le projet, mais son usage reste volontairement limité.

Il sert à stocker des notes de progression dans un fichier JSON.

Il ne constitue pas une base NoSQL complète pour une production avancée.

## Raison du choix

TinyDB a été choisi car :

- il est léger ;
- il s’intègre rapidement ;
- il permet de démontrer une logique NoSQL ;
- il ne demande pas de serveur externe ;
- il reste cohérent avec une V1 limitée.

## Limite

TinyDB n’est pas utilisé pour :

- stocker des utilisateurs ;
- gérer des médias ;
- stocker des données sensibles ;
- remplacer SQLite ;
- gérer une forte charge ;
- devenir une vraie base NoSQL de production.

## Évolution possible

Si le projet évolue vers des contenus très variables, une solution comme MongoDB pourra être étudiée.

MongoDB pourrait être utile pour :

- notes de conception ;
- contenus flexibles ;
- fiches projets variables ;
- journaux de développement ;
- métadonnées de médias.

---

# 15. Limite 12 — Documentation à maintenir

## Description

La documentation du projet est déjà importante, mais elle devra être maintenue au fur et à mesure des évolutions.

Chaque nouvelle fonctionnalité devra être documentée.

## Risque

Si la documentation n'est pas mise à jour, elle peut devenir incohérente avec le projet réel.

## Évolution possible

Pour éviter cela, chaque étape future devra suivre la règle suivante :

```text
Une fonctionnalité ajoutée = une documentation mise à jour.
```

Documents à maintenir :

- journal de bord ;
- changelog ;
- documentation d'installation ;
- documentation de déploiement ;
- documentation architecture ;
- documentation sécurité ;
- documentation utilisateur ;
- documentation base de données ;
- documentation tests ;
- documentation captures et preuves.

---

# 16. Limite 13 — Offre gratuite Render

## Description

Le projet est déployé sur l'offre gratuite de Render.

Cette offre permet de rendre le site accessible en ligne, mais elle possède des limites.

Limites possibles :

- mise en veille après inactivité ;
- premier chargement plus lent ;
- ressources limitées ;
- absence de persistance durable adaptée à SQLite dans certains usages ;
- performances limitées.

## Raison du choix

L'offre gratuite est suffisante pour une V1, une démonstration et un projet de formation.

Elle permet de tester un vrai déploiement sans coût immédiat.

## Évolution possible

Si le projet devient plus important, il pourra évoluer vers :

- une offre Render payante ;
- un hébergement plus robuste ;
- une base PostgreSQL hébergée ;
- un stockage externe ;
- une configuration de production plus avancée.

---

# 17. Ce qui est volontairement exclu de la V1

Les éléments suivants sont volontairement exclus de la V1 :

```text
PostgreSQL
Interface admin personnalisée
Upload serveur réel
Jeu jouable navigateur
Statistiques avancées
Graphiques Plotly.js
Espace privé complet
Système de sauvegarde automatique
Gestion avancée des médias
Tests automatisés complets
API REST
MongoDB
Mini-jeu intégré
Système de score
Téléchargement public de projet jouable
```

Ces éléments ne sont pas oubliés.

Ils sont reportés afin de protéger la stabilité du projet.

Le compte d’évaluation en lecture seule, TinyDB, le SQL natif documentaire et `setup_render_data` ne sont plus dans cette liste, car ils ont été ajoutés de manière limitée.

---

# 18. Risques évités

Le cadrage de la V1 permet d'éviter plusieurs risques classiques :

- scope creep ;
- dette technique ;
- fonctionnalités commencées mais non terminées ;
- projet trop complexe ;
- perte de stabilité ;
- documentation impossible à maintenir ;
- déploiement plus difficile ;
- retard important ;
- transformation du projet en usine à gaz.

La priorité a été donnée à une version simple, stable, déployée, documentée et défendable.

---

# 19. Idées pouvant être abandonnées pendant la stabilisation

Pendant la phase de stabilisation d'une V1, certaines idées peuvent être reportées, simplifiées ou même abandonnées.

Un projet en V1 évolue constamment.

Toutes les idées envisagées au départ ne sont pas forcément conservées jusqu'à la version présentable.

Une idée peut être abandonnée si :

- elle ajoute trop de complexité ;
- elle n'est pas indispensable pour la V1 ;
- elle risque de fragiliser le projet ;
- elle demande trop de temps par rapport à sa valeur réelle ;
- elle rend la documentation plus difficile à maintenir ;
- elle détourne le projet de son objectif principal ;
- elle transforme une version stable en projet trop lourd ;
- elle peut être remplacée par une solution plus simple ;
- elle n'apporte pas assez de valeur à l'évaluateur ou à l'utilisateur final.

Abandonner une idée ne signifie pas que le projet échoue.

Cela peut au contraire montrer une bonne gestion du périmètre.

---

# 20. Évolutions prioritaires

Les évolutions futures doivent être ajoutées progressivement.

## Priorité 1 — Finalisation du dossier

- corriger les textes ;
- harmoniser les documents ;
- finaliser les captures ;
- vérifier les preuves ;
- améliorer le README ;
- finaliser le dossier projet ;
- vérifier les annexes ;
- faire un dernier commit propre.

## Priorité 2 — Amélioration de présentation

- améliorer le design ;
- améliorer le responsive ;
- enrichir les pages ;
- créer des maquettes Figma plus détaillées ;
- enrichir les fiches projets ;
- structurer davantage les données ;
- améliorer l'administration Django.

## Priorité 3 — Évolution technique

- ajouter PostgreSQL ;
- intégrer Plotly.js ;
- préparer une vraie section de projets jouables ;
- étudier l'intégration d'une démonstration dans le navigateur ;
- étudier MongoDB si les contenus deviennent très variables ;
- ajouter des tests automatisés.

---

# 21. Roadmap possible

## Version 1.1

Objectif : améliorer la présentation sans changer l'architecture.

Évolutions possibles :

- nettoyage des textes ;
- amélioration mobile ;
- meilleure mise en page ;
- captures propres ;
- README plus complet ;
- dossier projet finalisé ;
- preuves mieux organisées.

## Version 1.2

Objectif : améliorer la gestion des contenus.

Évolutions possibles :

- modèles Django plus détaillés ;
- fiches projets complètes ;
- meilleure utilisation de l'administration ;
- champs supplémentaires ;
- tri des projets ;
- statuts plus précis ;
- meilleure organisation des médias.

## Version 2.0

Objectif : transformer le portfolio en plateforme plus complète.

Évolutions possibles :

- PostgreSQL ;
- espace privé ;
- administration personnalisée ;
- upload sécurisé ;
- gestion avancée des médias ;
- graphiques de suivi ;
- intégration éventuelle de démonstrations jouables ;
- tests automatisés plus complets ;
- système de rôles plus avancé.

---

# 22. Conditions avant d'ajouter une nouvelle fonctionnalité

Avant d'ajouter une nouvelle fonctionnalité, il faudra vérifier :

- est-ce utile pour le projet ?
- est-ce nécessaire pour la V1 ?
- combien d'heures cela demande ?
- est-ce que cela risque de casser l'existant ?
- est-ce documentable simplement ?
- est-ce testable ?
- est-ce que cela ajoute trop de complexité ?
- est-ce que cela peut être reporté ?
- est-ce que cette idée doit vraiment être conservée ?
- est-ce que cette idée peut être simplifiée ?
- est-ce que cette idée doit être abandonnée pour stabiliser la V1 ?

Si une fonctionnalité n'est pas indispensable, elle doit être reportée.

Si une idée fragilise la V1, elle doit être simplifiée ou abandonnée.

---

# 23. Bilan

La V1 de Frostia Games est volontairement limitée, mais elle est fonctionnelle.

Elle permet déjà de montrer :

- une base Django ;
- une interface publique ;
- une base SQLite ;
- une administration Django ;
- un accès d’évaluation en lecture seule ;
- un affichage dynamique ;
- une expérimentation NoSQL TinyDB ;
- un affichage des notes TinyDB ;
- un menu mobile JavaScript ;
- un déploiement Render ;
- une commande d’initialisation automatique des données Render ;
- une documentation complète ;
- des fichiers SQL natifs documentaires ;
- une réflexion technique sur les limites et évolutions.

Les limites actuelles ne sont pas des échecs.

Elles montrent que le projet a été cadré pour rester stable et présentable.

Les évolutions futures sont identifiées, mais elles seront ajoutées progressivement, uniquement si elles apportent une vraie valeur au projet.

Certaines idées pourront aussi être abandonnées pendant la stabilisation si elles ne servent plus l'objectif principal de la V1.

La priorité reste de conserver un projet clair, stable, maintenable, documenté et défendable.

À ce stade, la priorité immédiate est la finalisation des captures, des preuves, des annexes et du dossier projet final, pas l’ajout de nouvelles fonctionnalités lourdes.
