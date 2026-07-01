# JavaScript dynamique — Menu mobile

## Objectif

Cette partie présente l’utilisation de JavaScript dans le projet **Frostia Games**.

L’objectif est de montrer que l’interface ne repose pas uniquement sur du HTML et du CSS statique.
Un script JavaScript est utilisé pour gérer l’ouverture et la fermeture du menu mobile.

---

## Fonctionnalité concernée

La fonctionnalité présentée est le **menu de navigation mobile**.

Sur écran réduit, le menu doit pouvoir être ouvert ou fermé par l’utilisateur afin de permettre la navigation entre les différentes pages du site.

Cette fonctionnalité améliore l’expérience utilisateur sur mobile.

---

## Fonctionnement général

Le script JavaScript permet de :

* récupérer le bouton du menu mobile ;
* récupérer le conteneur de navigation ;
* écouter le clic de l’utilisateur ;
* ajouter ou retirer une classe CSS ;
* afficher ou masquer le menu selon l’état courant.

---

## Exemple de logique utilisée

Le fonctionnement repose sur une logique simple :

1. l’utilisateur clique sur le bouton du menu ;
2. JavaScript détecte l’événement ;
3. une classe CSS est ajoutée ou retirée ;
4. le menu change d’état visuel ;
5. l’utilisateur peut accéder aux liens de navigation.

---

## Preuves à intégrer dans le dossier

Pour cette fonctionnalité, les preuves à ajouter sont :

| Élément         | Preuve                                              |
| --------------- | --------------------------------------------------- |
| Code JavaScript | Capture du fichier JavaScript gérant le menu mobile |
| Explication     | Description du fonctionnement du script             |
| Rendu final     | Capture du menu mobile fermé                        |
| Rendu final     | Capture du menu mobile ouvert                       |

---

## Intérêt pour le projet

Cette fonctionnalité permet de rendre la navigation utilisable sur mobile.

Elle montre l’utilisation de JavaScript pour modifier dynamiquement l’interface en fonction de l’action de l’utilisateur.

Elle complète le travail réalisé en HTML, CSS et Django templates.
