# Vues et routes Django — Frostia Games

## Objectif du document

Ce document présente le fonctionnement des vues et des routes Django dans le projet **Frostia Games**.

L’objectif est de montrer comment les pages publiques du site sont reliées aux vues Python, aux routes URL et aux templates HTML.

Cette partie permet de démontrer le fonctionnement du back-end Django dans l’affichage des pages du site.

---

## Rôle des vues Django

Dans Django, une vue reçoit une requête HTTP et retourne une réponse.

Dans le projet **Frostia Games**, les vues permettent notamment :

* d’afficher la page d’accueil ;
* d’afficher la page “Mes créations” ;
* d’afficher la page “Projets jouables” ;
* de récupérer les données nécessaires ;
* de transmettre les données aux templates HTML.

---

## Rôle des routes URL

Les routes permettent d’associer une adresse du site à une vue Django.

Lorsqu’un visiteur accède à une URL, Django utilise le fichier `urls.py` pour identifier la vue à exécuter.

Exemple de fonctionnement :

| URL           | Vue appelée              | Rôle                                   |
| ------------- | ------------------------ | -------------------------------------- |
| `/`           | Vue d’accueil            | Affiche la page d’accueil du site      |
| `/creations/` | Vue des créations        | Affiche les créations visibles         |
| `/playable/`  | Vue des projets jouables | Affiche les projets jouables ou prévus |

---

## Exemple : affichage des créations

Lorsqu’un visiteur consulte la page **Mes créations**, Django suit plusieurs étapes :

1. le visiteur accède à l’URL correspondante ;
2. Django identifie la route dans `urls.py` ;
3. la vue associée est appelée ;
4. la vue récupère les créations visibles ;
5. les données sont envoyées au template ;
6. le template génère la page HTML ;
7. le navigateur affiche la page finale.

---

## Lien entre modèle, vue et template

Le fonctionnement repose sur une logique MVC/MVT propre à Django.

| Élément  | Rôle dans le projet                        |
| -------- | ------------------------------------------ |
| Modèle   | Définit la structure des données           |
| Vue      | Récupère les données et prépare la réponse |
| Template | Affiche les données dans une page HTML     |
| Route    | Associe une URL à une vue                  |

Dans Frostia Games, cette organisation permet de séparer clairement la logique du projet :

* les modèles structurent les données ;
* les vues organisent l’affichage ;
* les templates gèrent le rendu HTML ;
* les routes relient les pages aux vues.

---

## Exemple : page Mes créations

La page **Mes créations** utilise les données du modèle `Creation`.

La vue récupère les créations visibles, puis les transmet au template afin de les afficher dans la page publique.

Ce fonctionnement permet de modifier les contenus depuis l’administration Django sans réécrire directement le HTML de la page.

---

## Exemple : page Projets jouables

La page **Projets jouables** utilise les données du modèle `PlayableProject`.

La vue permet de récupérer les projets visibles et de les afficher dans le template correspondant.

Cette organisation permet de préparer de futures démonstrations ou projets jouables tout en gardant une structure claire.

---

## Preuves à intégrer dans le dossier

Pour cette partie, les preuves à intégrer dans le dossier projet sont :

| Élément            | Preuve                                         |
| ------------------ | ---------------------------------------------- |
| Routes Django      | Capture du fichier `urls.py`                   |
| Vues Django        | Capture du fichier `views.py`                  |
| Données récupérées | Capture du code utilisant les modèles          |
| Template associé   | Capture d’un template HTML                     |
| Rendu final        | Capture de la page affichée dans le navigateur |

---

## Intérêt pour le projet

Les vues et les routes montrent le fonctionnement dynamique du site.

Elles permettent de prouver que les pages ne sont pas seulement des fichiers statiques, mais qu’elles sont servies par Django avec une logique côté serveur.

Cette partie valorise les compétences back-end suivantes :

* organisation des routes ;
* création de vues Django ;
* récupération de données ;
* transmission des données aux templates ;
* affichage dynamique dans le navigateur.
