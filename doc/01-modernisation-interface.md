# Fiche d’étape — Modernisation de l’interface Frostia Games

## Objectif de l’étape

Cette étape avait pour objectif de transformer la première maquette wireframe du portfolio **Frostia Games** en une interface plus moderne, plus lisible et plus professionnelle.

Le but était de conserver une structure simple, tout en donnant au site une identité visuelle plus forte, cohérente et exploitable pour une V1 Django.

L’objectif n’était pas de créer une interface définitive, mais de mettre en place une base visuelle :

- stable ;
- maintenable ;
- responsive ;
- compatible avec les futures évolutions ;
- compatible avec l’affichage de données venant du backend Django.

---

# 1. Décisions prises

La structure du site a été volontairement limitée à trois pages principales :

- Accueil ;
- Mes créations ;
- Projets jouables.

Le nom **Frostia Games** est utilisé comme nom temporaire de présentation du projet.

Le logo actuel est également temporaire.

La direction visuelle retenue repose sur une identité bleue moderne, froide et cohérente avec le nom **Frostia**.

L’objectif est d’obtenir un rendu sérieux et professionnel sans dépendre d’illustrations personnalisées ou d’un template externe lourd.

Cette décision permet de garder le contrôle sur :

- la structure HTML ;
- le CSS ;
- le responsive ;
- le JavaScript ;
- l’évolution future du projet.

---

# 2. Choix d’interface

L’interface repose sur une structure composée de :

- une barre supérieure contenant le nom temporaire du site ;
- une sidebar à gauche pour la navigation desktop ;
- un contenu principal avec un fond bleu dégradé ;
- des cartes blanches modernes ;
- une page d’accueil claire ;
- une page dédiée aux créations ;
- une page dédiée aux futurs projets jouables ;
- un bloc d’information sur l’état de la V1 ;
- une barre de bas de page intégrée proprement ;
- une version mobile avec menu dépliable.

Sur desktop, la sidebar reste visible en permanence.

Sur mobile, elle se replie automatiquement et peut être ouverte avec un bouton menu.

Ce choix permet d’avoir une interface simple à comprendre, sans ajouter de dépendance graphique lourde.

---

# 3. Travail réalisé

Le fichier CSS principal a été retravaillé afin d’obtenir une interface plus propre et plus cohérente.

Améliorations principales :

- harmonisation des bleus ;
- ajout d’un effet lumineux sur le logo temporaire ;
- amélioration des cartes d’accueil ;
- ajout d’ombres plus modernes ;
- ajout de dégradés sur le fond principal ;
- meilleure distinction de l’élément actif dans la navigation ;
- correction du footer afin qu’il s’intègre mieux à la page ;
- préparation du responsive mobile ;
- création d’une interface cohérente sur les trois pages principales ;
- ajout d’une zone préparatoire pour les projets jouables ;
- ajout d’un affichage visuel pour les données provenant du backend ;
- préparation de l’affichage des notes TinyDB sur l’accueil.

L’interface a également été adaptée pour afficher certaines données provenant des modèles Django.

Cela permet à la V1 de ne plus être uniquement statique.

---

# 4. Fichiers concernés

Les pages concernées par cette étape sont :

```text
templates/pages/home.html
templates/pages/creation.html
templates/pages/projet_jouable.html
templates/partials/base.html
```

Le fichier CSS principal concerné est :

```text
static/css/main.css
```

Le fichier JavaScript lié au menu mobile est :

```text
static/js/menu.js
```

La documentation complémentaire du JavaScript se trouve dans :

```text
docs/frontend/javascript-menu-mobile.md
```

---

# 5. Page Accueil

La page d’accueil dispose maintenant de :

- un hero clair ;
- trois cartes principales ;
- un bloc d’actualité du projet ;
- un bloc “À propos du site” ;
- un footer propre ;
- une navigation active ;
- une base responsive ;
- une section pouvant afficher les notes de progression TinyDB.

Cette page sert de point d’entrée au portfolio.

Elle présente le site, son objectif et les sections principales sans surcharger l’utilisateur.

L’affichage des notes TinyDB permet aussi de montrer qu’une partie de la page peut recevoir des données préparées côté backend.

---

# 6. Page Mes créations

La page **Mes créations** a été préparée pour présenter les projets enregistrés dans la base de données.

Elle contient :

- une introduction ;
- un lexique alphabétique ;
- une section reliée aux données enregistrées en base ;
- une indication claire sur les futures fiches détaillées ;
- une section expliquant les contenus prévus pour plus tard.

Cette page prépare l’évolution future vers des fiches projet détaillées, sans les ajouter trop tôt dans la V1.

Elle permet aussi de montrer que certains contenus peuvent être affichés depuis Django, plutôt que d’être uniquement écrits en dur dans les templates.

---

# 7. Page Projets jouables

La page **Projets jouables** a été préparée pour accueillir plus tard des vidéos, teasers, prototypes ou démonstrations jouables.

Dans la V1, elle contient :

- une zone de lecteur préparatoire ;
- un bouton Lecture affichant un message ;
- un bouton de sélection de fichier local ;
- un message indiquant que l’upload réel n’est pas implanté ;
- une section affichant les projets jouables enregistrés en base ;
- une explication claire des limites de la V1 ;
- une section sur les évolutions prévues.

Aucun vrai upload serveur n’est activé dans cette version.

Ce choix évite d’intégrer une fonctionnalité sensible sans avoir encore mis en place les protections nécessaires.

La page permet donc de montrer une intention d’évolution sans exposer le projet à une complexité trop importante.

---

# 8. Problèmes rencontrés

Plusieurs problèmes sont apparus pendant l’intégration :

- certains styles ne s’appliquaient pas, car le HTML ne contenait pas encore les bonnes classes ;
- le fichier CSS contenait des erreurs de variables et de placement ;
- certains ajustements avaient été placés par erreur dans le bloc mobile ;
- le footer ne s’affichait pas comme prévu, car il était contenu dans le padding principal ;
- l’état actif du menu n’était pas assez visible ;
- certaines alertes VS Code étaient liées à des faux positifs de typage Django ;
- certaines parties de l’interface ont dû être adaptées après l’ajout du backend ;
- l’affichage des données dynamiques a demandé une meilleure séparation entre interface, vues et templates.

Ces problèmes ont été corrigés progressivement.

Cette étape a aussi permis de mieux séparer ce qui relève de l’interface, du backend et des futures évolutions.

---

# 9. Résultat obtenu

L’interface actuelle est plus moderne, plus cohérente et plus présentable pour une V1.

Le site possède maintenant :

- une identité visuelle bleue cohérente ;
- une navigation claire ;
- une sidebar desktop ;
- un menu mobile ;
- des cartes lisibles ;
- des pages principales fonctionnelles ;
- une mise en page responsive ;
- une interface compatible avec l’affichage des données Django ;
- une interface compatible avec l’affichage des notes TinyDB ;
- une zone préparatoire pour les futurs projets jouables.

L’objectif de cette étape est atteint : le site possède une base graphique exploitable pour continuer le développement et présenter le projet.

L’interface reste volontairement simple afin de préserver la stabilité de la V1.

---

# 10. Lien avec le backend

L’interface n’est plus uniquement statique.

Certaines sections affichent maintenant des données provenant de la base SQLite via les modèles Django.

Pages concernées :

- Mes créations ;
- Projets jouables.

Les données sont ajoutées dans l’administration Django, puis affichées dans les templates.

Ce fonctionnement permet de modifier certains contenus sans toucher directement au code HTML.

La page d’accueil peut également afficher des notes provenant de TinyDB.

Chaîne technique TinyDB :

```text
TinyDB
→ core/services/nosql_notes.py
→ core/views.py
→ templates/pages/home.html
→ affichage sur la page d'accueil
```

Cette évolution donne au projet une dimension backend réelle, tout en conservant une interface simple à maintenir.

---

# 11. Lien avec le déploiement Render

L’interface a été vérifiée après la mise en ligne du projet sur Render.

URL de production :

```text
https://frostia-games.onrender.com
```

Le déploiement permet de vérifier que l’interface fonctionne en dehors de l’environnement local.

Points vérifiés :

- chargement de la page d’accueil ;
- chargement du CSS ;
- chargement du JavaScript ;
- navigation entre les pages ;
- accès aux pages principales ;
- cohérence générale de l’affichage ;
- compatibilité avec la configuration Render.

Le Start Command Render actuel est :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

La commande `setup_render_data` permet de recréer les données nécessaires à la démonstration et l’accès d’évaluation en lecture seule.

---

# 12. Ce qui reste à faire

Les prochaines améliorations visuelles possibles sont :

- améliorer légèrement les espacements ;
- rendre certaines cartes plus premium ;
- harmoniser certains textes ;
- améliorer la lisibilité de quelques sections ;
- préparer des captures propres pour le dossier ;
- ajouter plus tard des visuels définitifs ;
- ajouter une future fiche projet détaillée lorsque le contenu sera prêt.

Ces améliorations restent secondaires par rapport à la finalisation de la V1 :

- captures ;
- relecture ;
- vérification responsive ;
- README racine ;
- dossier projet final ;
- preuves de fonctionnement.

L’objectif n’est pas de relancer une refonte complète, mais de terminer une version propre, stable et défendable.

---

# 13. Ce qui n’est pas prévu dans la V1

La V1 ne prévoit pas :

- refonte graphique complète ;
- template Django lourd ;
- système d’animation avancé ;
- galerie complexe ;
- vraie lecture vidéo ;
- vrai upload serveur ;
- page détail complète pour chaque projet ;
- interface graphique définitive.

Ces choix permettent de conserver une interface stable, simple et maintenable.

Ils évitent aussi d’ajouter une complexité excessive alors que la priorité est de finaliser une V1 fonctionnelle et documentée.

---

# 14. Captures utiles

Pour le dossier projet, les captures utiles sont :

- page d’accueil ;
- page Mes créations ;
- page Projets jouables ;
- menu mobile ouvert ;
- fichier `static/css/main.css` ;
- fichier `static/js/menu.js` ;
- template `templates/partials/base.html` ;
- affichage des données Django ;
- affichage des notes TinyDB sur l’accueil ;
- site en ligne sur Render.

Aucune capture ne doit afficher :

- mot de passe ;
- clé secrète ;
- vraie variable d’environnement ;
- identifiant administrateur complet ;
- information sensible inutile.

---

# 15. Bilan

Cette étape a permis de passer d’un wireframe simple à une interface moderne, lisible et utilisable.

Le projet reste volontairement limité, mais l’interface donne maintenant une impression plus sérieuse et plus professionnelle.

Le choix retenu est de continuer avec cette base plutôt que d’installer un template Django lourd.

Cela permet de garder le contrôle sur :

- le code ;
- la structure ;
- le style ;
- le responsive ;
- le JavaScript ;
- l’évolution future du portfolio.

La modernisation lourde de l’interface est reportée à une version future afin de conserver une V1 stable, documentée et déployée.

Cette étape valide donc la base visuelle du projet **Frostia Games** pour la V1.