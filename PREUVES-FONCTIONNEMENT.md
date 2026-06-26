# Preuves de fonctionnement — Frostia Games

Ce document présente les preuves visuelles réalisées pour le projet **Frostia Games**.

L’objectif de ce fichier est de centraliser les captures montrant que la V1 du projet est fonctionnelle, organisée, documentée et déployée.

Les captures sont regroupées dans le dossier suivant :

```txt
Preuve De Fonctionnement/
```

---

## 1. Objectif des preuves

Les captures présentes dans ce dossier servent à démontrer plusieurs points importants du projet :

* le site fonctionne en local ;
* le site peut être lancé avec Docker ;
* le site est déployé en ligne sur Render ;
* l’interface d’administration Django est accessible ;
* les pages principales du site sont visibles ;
* le responsive mobile fonctionne ;
* les maquettes Figma ont été préparées ;
* le projet est suivi avec Git et sauvegardé sur GitHub.

Ces preuves permettent de montrer que la V1 de Frostia Games ne se limite pas à du code, mais qu’elle possède aussi un environnement d’exécution, une organisation documentaire et une mise en ligne fonctionnelle.

---

## 2. Organisation du dossier de preuves

Les captures sont classées par catégorie afin de faciliter la lecture et la vérification du projet.

Structure générale :

```txt
Preuve De Fonctionnement/
├── Docker/
├── Figma/
├── Github/
├── Render/
└── SiteWeb_FrostiaGame/
    ├── Admin/
    ├── Desktop/
    └── Mobile/
```

Chaque dossier correspond à un type de preuve différent.

---

## 3. Preuves Docker

Dossier concerné :

```txt
Preuve De Fonctionnement/Docker/
```

Les captures Docker montrent :

* la construction de l’image Docker ;
* la présence de l’image générée ;
* le lancement du conteneur ;
* les logs du serveur ;
* l’accès au site depuis l’environnement Docker ;
* la validation du fonctionnement local dans un environnement isolé.

Ces captures prouvent que le projet peut être exécuté dans un environnement Docker, indépendamment de la configuration directe de la machine.

Le serveur utilisé dans Docker correspond à un environnement local de test. Le message indiquant qu’il s’agit d’un serveur de développement est normal dans ce contexte.

---

## 4. Preuves Figma

Dossier concerné :

```txt
Preuve De Fonctionnement/Figma/
```

Les captures Figma montrent :

* les maquettes préparatoires du projet ;
* une version wireframe ;
* une version colorisée ;
* l’organisation visuelle prévue avant l’intégration ;
* la réflexion menée sur l’interface desktop et mobile.

Ces captures prouvent que le projet a été préparé avec une phase de conception graphique avant l’intégration dans Django.

Les maquettes ne sont pas forcément identiques à 100 % au rendu final, mais elles montrent l’intention de départ, la structure des pages et la direction visuelle du site.

---

## 5. Preuves Render

Dossier concerné :

```txt
Preuve De Fonctionnement/Render/
```

Les captures Render montrent :

* l’existence du service Render ;
* l’historique des déploiements ;
* les builds réalisés ;
* les logs du service ;
* les variables d’environnement configurées avec des valeurs masquées ;
* la mise en ligne du projet.

Les captures de variables d’environnement montrent uniquement les noms des variables. Les valeurs sensibles ne sont pas affichées.

Exemples de variables visibles dans les captures :

```txt
DJANGO_DEBUG
DJANGO_SECRET_KEY
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD
DJANGO_SUPERUSER_USERNAME
```

Les valeurs associées sont masquées afin de respecter les règles de sécurité.

Le projet est hébergé sur Render avec une offre gratuite. Cette offre peut entraîner une mise en veille du service après une période d’inactivité. Ce comportement est lié à l’hébergement et ne constitue pas une erreur du projet.

---

## 6. Preuves du site en ligne

Dossier concerné :

```txt
Preuve De Fonctionnement/SiteWeb_FrostiaGame/
```

Ce dossier contient les captures du site Frostia Games exécuté en ligne sur Render.

Il est organisé en trois sous-dossiers :

```txt
SiteWeb_FrostiaGame/
├── Admin/
├── Desktop/
└── Mobile/
```

---

## 7. Interface d’administration Django

Dossier concerné :

```txt
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Admin/
```

Les captures de l’administration montrent :

* l’accès à l’interface d’administration Django ;
* la présence des modèles administrables ;
* la séparation entre l’espace public du site et l’espace d’administration ;
* la présence des sections liées aux créations et aux projets jouables.

Ces captures prouvent que le back-end Django est bien structuré et que les données peuvent être administrées via l’interface prévue par Django.

Aucun mot de passe n’est affiché dans ces captures.

L’administration Django est utilisée comme outil interne de gestion. Elle n’est pas destinée à être ouverte publiquement aux visiteurs.

---

## 8. Version desktop du site

Dossier concerné :

```txt
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Desktop/
```

Les captures desktop montrent les pages principales du site en version ordinateur.

Pages concernées :

* page d’accueil ;
* page Mes créations ;
* page Projets jouables.

Ces captures prouvent que les pages publiques principales sont accessibles et que l’interface fonctionne sur un écran de type ordinateur ou laptop.

---

## 9. Version mobile du site

Dossier concerné :

```txt
Preuve De Fonctionnement/SiteWeb_FrostiaGame/Mobile/
```

Les captures mobile montrent :

* l’affichage responsive du site ;
* l’adaptation du contenu au format mobile ;
* la présence du menu mobile ;
* l’organisation des éléments en colonne ;
* la lisibilité des cartes et sections principales.

Ces captures prouvent que le site ne dépend pas uniquement d’un affichage desktop et qu’il possède une adaptation mobile exploitable.

---

## 10. Preuves GitHub

Dossier concerné :

```txt
Preuve De Fonctionnement/Github/
```

Les captures GitHub montrent :

* le dépôt du projet ;
* la sauvegarde du code ;
* le suivi de version ;
* la présence des fichiers principaux ;
* la centralisation du projet dans un dépôt distant.

GitHub permet de conserver l’historique du projet et de sécuriser le travail réalisé.

---

## 11. Sécurité des captures

Les captures ont été préparées en évitant d’exposer les données sensibles.

Les éléments suivants ne doivent pas apparaître en clair dans les images :

* mot de passe ;
* clé secrète Django ;
* valeur complète de variable d’environnement ;
* identifiant privé inutile ;
* information personnelle non nécessaire au dossier.

Lorsque des variables d’environnement sont montrées, leurs valeurs doivent rester masquées.

---

## 12. Synthèse des éléments prouvés

Les preuves réalisées permettent de confirmer que la V1 de Frostia Games comprend :

* un projet Django fonctionnel ;
* une interface publique ;
* une interface d’administration Django ;
* des pages principales accessibles ;
* une structure responsive ;
* une exécution locale possible ;
* une exécution Docker vérifiée ;
* un déploiement Render fonctionnel ;
* une organisation des captures par catégorie ;
* une sauvegarde du projet avec GitHub ;
* une base documentaire claire pour présenter le travail réalisé.

---

## 13. Limites assumées

Cette V1 ne représente pas la version finale complète de Frostia Games.

Certaines fonctionnalités sont volontairement reportées ou non intégrées dans cette version :

* système complet de publication de jeux ;
* téléchargement de jeux ;
* espace utilisateur public ;
* accès spécifique jury ;
* base PostgreSQL ;
* système NoSQL ;
* intégration de jeux jouables dans le navigateur ;
* automatisations avancées ;
* statistiques détaillées.

Ces éléments pourront être étudiés dans une version future, mais ils ne font pas partie du périmètre stabilisé de la V1.

---

## 14. Conclusion

Les captures regroupées dans le dossier `Preuve De Fonctionnement/` permettent de démontrer que la V1 de Frostia Games est stable, consultable, documentée et déployée.

Le projet possède une base fonctionnelle claire :

* conception visuelle ;
* développement Django ;
* administration ;
* responsive ;
* Docker ;
* Render ;
* GitHub ;
* documentation.

Cette version constitue une première base exploitable pour présenter le projet, justifier les choix techniques et préparer les évolutions futures.
