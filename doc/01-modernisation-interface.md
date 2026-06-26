# Fiche d’étape — Modernisation de l’interface Frostia Games

## Objectif de l’étape

Cette étape avait pour objectif de transformer la première maquette wireframe du portfolio **Frostia Games** en une interface plus moderne, plus lisible et plus professionnelle, sans utiliser de template Django lourd ni créer d’éléments graphiques avancés dans Krita.

Le but était de conserver une structure simple, mais de donner au site une identité visuelle plus forte, cohérente et exploitable pour une V1 Django.

L’objectif n’était pas de créer une interface définitive, mais de mettre en place une base visuelle stable, maintenable, responsive et compatible avec les futures évolutions du projet.

---

## Décisions prises

La structure du site a été volontairement limitée à trois pages principales :

* Accueil ;
* Mes créations ;
* Projets jouables.

Le nom **Frostia Games** est utilisé comme nom temporaire de présentation du projet.

Le logo actuel est également temporaire et pourra être remplacé lors d’une future mise à jour.

La direction visuelle retenue repose sur une identité bleue moderne, froide et cohérente avec le nom Frostia.

L’objectif est d’obtenir un rendu sérieux et professionnel sans dépendre d’illustrations personnalisées ou d’un template externe.

Cette décision permet de garder le contrôle sur la structure HTML, le CSS, le responsive et l’évolution future du projet.

---

## Choix d’interface

L’interface repose sur une structure avec :

* une barre supérieure contenant le nom temporaire du site ;
* une sidebar à gauche pour la navigation desktop ;
* un contenu principal avec un fond bleu dégradé ;
* des cartes blanches modernes ;
* une page d’accueil claire ;
* une page dédiée aux créations ;
* une page dédiée aux futurs projets jouables ;
* un bloc d’information sur l’état de la V1 ;
* une barre de bas de page intégrée proprement ;
* une version mobile avec menu dépliable.

Sur desktop, la sidebar reste visible en permanence.

Sur mobile, elle se replie automatiquement et peut être ouverte avec un bouton menu.

Ce choix permet d’avoir une interface simple à comprendre, sans ajouter de dépendance graphique lourde.

---

## Travail réalisé

Le fichier CSS principal a été retravaillé pour obtenir une interface plus propre et plus cohérente.

Les améliorations principales sont :

* harmonisation des bleus ;
* ajout d’un effet lumineux sur le logo temporaire ;
* amélioration des cartes d’accueil ;
* ajout d’ombres plus modernes ;
* ajout de dégradés sur le fond principal ;
* meilleure distinction de l’élément actif dans la navigation ;
* correction du footer pour qu’il s’intègre mieux à la page ;
* préparation du responsive mobile ;
* création d’une interface cohérente sur les trois pages principales ;
* ajout d’une zone préparatoire pour les projets jouables ;
* ajout d’un affichage visuel pour les données provenant du backend.

L’interface a également été adaptée pour afficher certaines données provenant des modèles Django, ce qui permet à la V1 de ne plus être uniquement statique.

---

## Pages concernées

Les pages concernées par cette étape sont :

* `home.html` ;
* `creation.html` ;
* `projet_jouable.html` ;
* `base.html`.

Le fichier CSS principal concerné est :

* `static/css/main.css`.

Le fichier JavaScript lié au menu mobile est :

* `static/js/menu.js`.

---

## Page Accueil

La page d’accueil dispose maintenant :

* d’un hero clair ;
* de trois cartes principales ;
* d’un bloc d’actualité du projet ;
* d’un bloc “À propos du site” ;
* d’un footer propre ;
* d’une navigation active ;
* d’une base responsive.

Cette page sert de point d’entrée du portfolio.

Elle présente le site, son objectif et les sections principales sans surcharger l’utilisateur.

---

## Page Mes créations

La page **Mes créations** a été préparée pour présenter les projets enregistrés dans la base de données.

Elle contient :

* une introduction ;
* un lexique alphabétique ;
* une lettre disponible pour afficher KryonCore ;
* une section reliée aux données enregistrées en base ;
* une indication claire sur les futures fiches détaillées ;
* une section expliquant les contenus prévus pour plus tard.

Cette page prépare l’évolution future vers des fiches projet détaillées, sans les ajouter trop tôt dans la V1.

Elle permet aussi de montrer que certains contenus peuvent être affichés depuis Django plutôt que d’être uniquement écrits en dur dans les templates.

---

## Page Projets jouables

La page **Projets jouables** a été préparée pour accueillir plus tard des vidéos, teasers, prototypes ou démonstrations jouables.

Dans la V1, elle contient :

* une zone de lecteur préparatoire ;
* un bouton Lecture affichant un message ;
* un bouton de sélection de fichier local ;
* un message indiquant que l’upload réel n’est pas implanté ;
* une section affichant les projets jouables enregistrés en base ;
* une explication claire des limites de la V1 ;
* une section sur les évolutions prévues.

Aucun vrai upload serveur n’est activé dans cette version.

Ce choix évite d’intégrer une fonctionnalité sensible sans avoir encore mis en place les protections nécessaires.

La page permet donc de montrer une intention d’évolution sans exposer le projet à une complexité trop importante.

---

## Problèmes rencontrés

Plusieurs problèmes sont apparus pendant l’intégration :

* certains styles ne s’appliquaient pas car le HTML ne contenait pas encore les bonnes classes ;
* le fichier CSS contenait des erreurs de variables et de placement ;
* certains ajustements avaient été placés par erreur dans le bloc mobile ;
* le footer ne s’affichait pas comme prévu car il était contenu dans le padding principal ;
* l’état actif du menu n’était pas assez visible ;
* certaines alertes VS Code étaient liées à des faux positifs de typage Django ;
* certaines parties de l’interface ont dû être adaptées après l’ajout du backend.

Ces problèmes ont été corrigés progressivement.

Cette étape a aussi permis de mieux séparer ce qui relève de l’interface, du backend et des futures évolutions.

---

## Résultat obtenu

L’interface actuelle est plus moderne, plus cohérente et plus présentable pour une V1.

Le site possède maintenant :

* une identité visuelle bleue cohérente ;
* une navigation claire ;
* une sidebar desktop ;
* un menu mobile ;
* des cartes lisibles ;
* des pages principales fonctionnelles ;
* une mise en page responsive ;
* une interface compatible avec l’affichage des données Django ;
* une zone préparatoire pour les futurs projets jouables.

L’objectif de cette étape est atteint : le site possède une base graphique exploitable pour continuer le développement et présenter le projet.

L’interface reste volontairement simple afin de préserver la stabilité de la V1.

---

## Lien avec le backend

L’interface n’est plus uniquement statique.

Certaines sections affichent maintenant des données provenant de la base SQLite via les modèles Django.

Les pages concernées sont :

* Mes créations ;
* Projets jouables.

Les données sont ajoutées dans l’administration Django puis affichées dans les templates.

Ce fonctionnement permet de modifier certains contenus sans toucher directement au code HTML.

Cette évolution donne au projet une dimension backend réelle, tout en conservant une interface simple à maintenir.

---

## Lien avec le déploiement

L’interface a été vérifiée après la mise en ligne du projet sur Render.

Le site est accessible en ligne et les pages principales peuvent être consultées depuis l’URL de production.

Le déploiement permet de vérifier que l’interface fonctionne en dehors de l’environnement local.

Points vérifiés :

* chargement de la page d’accueil ;
* chargement du CSS ;
* navigation entre les pages ;
* accès aux pages principales ;
* cohérence générale de l’affichage ;
* compatibilité avec la configuration Render.

---

## Ce qui reste à faire

Les prochaines améliorations visuelles possibles sont :

* améliorer légèrement les espacements ;
* rendre certaines cartes plus premium ;
* harmoniser certains textes ;
* améliorer la lisibilité de quelques sections ;
* préparer des captures propres pour le dossier ;
* ajouter plus tard des visuels définitifs ;
* ajouter une future fiche projet détaillée lorsque le contenu sera prêt.

Ces améliorations restent secondaires par rapport à la finalisation de la V1 : captures, relecture, vérification responsive, README racine et dossier projet.

L’objectif n’est pas de relancer une refonte complète, mais de terminer une version propre, stable et défendable.

---

## Ce qui n’est pas prévu dans la V1

La V1 ne prévoit pas :

* de refonte graphique complète ;
* de template Django lourd ;
* de système d’animation avancé ;
* de galerie complexe ;
* de vraie lecture vidéo ;
* de vrai upload serveur ;
* de page détail complète pour chaque projet ;
* d’interface graphique définitive.

Ces choix permettent de conserver une interface stable, simple et maintenable.

Ils évitent aussi d’ajouter une complexité excessive alors que la priorité est de finaliser une V1 fonctionnelle et documentée.

---

## Bilan

Cette étape a permis de passer d’un wireframe simple à une interface moderne, lisible et utilisable.

Le projet reste volontairement limité, mais l’interface donne maintenant une impression plus sérieuse et plus professionnelle.

Le choix retenu est de continuer avec cette base plutôt que d’installer un template Django lourd.

Cela permet de garder le contrôle sur :

* le code ;
* la structure ;
* le style ;
* le responsive ;
* l’évolution future du portfolio.

La modernisation lourde de l’interface est reportée à une version future afin de conserver une V1 stable, documentée et déployée.

Cette étape valide donc la base visuelle du projet Frostia Games pour la V1.
