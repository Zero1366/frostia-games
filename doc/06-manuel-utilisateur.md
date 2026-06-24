# Manuel utilisateur - Frostia Games

## Objectif du document

Ce document explique comment utiliser la V1 du projet **Frostia Games**.

Il présente :

* le lancement du projet ;
* les pages principales ;
* l'accès à l'administration Django ;
* l'ajout d'une création ;
* l'ajout d'un projet jouable ;
* les fonctionnalités disponibles ;
* les limites de la V1.

---

# 1. Présentation du site

Frostia Games est un portfolio personnel destiné à présenter des projets de jeux vidéo.

La V1 contient trois pages principales :

* Accueil ;
* Mes créations ;
* Projets jouables.

Le site utilise Django pour gérer :

* les routes ;
* les templates ;
* les modèles ;
* l'administration ;
* la base SQLite.

---

# 2. Lancer le projet en local

## 2.1 Activer l'environnement virtuel

Depuis la racine du projet :

```powershell
.\.venv\Scripts\Activate.ps1
```

## 2.2 Installer les dépendances

```powershell
pip install -r requirements.txt
```

## 2.3 Appliquer les migrations

```powershell
python manage.py migrate
```

## 2.4 Vérifier le projet

```powershell
python manage.py check
```

Résultat attendu :

```text
System check identified no issues (0 silenced).
```

## 2.5 Lancer le serveur

```powershell
python manage.py runserver
```

Le site est accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

---

# 3. Lancer le projet avec Docker

Le projet peut aussi être lancé avec Docker Compose.

Depuis la racine du projet :

```powershell
docker compose up --build
```

Le site est ensuite accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

Si nécessaire, les migrations peuvent être lancées dans le conteneur :

```powershell
docker compose exec web python manage.py migrate
```

Pour vérifier Django dans Docker :

```powershell
docker compose exec web python manage.py check
```

Pour arrêter Docker :

```powershell
docker compose down
```

---

# 4. Pages publiques

## 4.1 Page Accueil

Adresse :

```text
http://127.0.0.1:8000/
```

La page d'accueil présente :

* le nom Frostia Games ;
* l'objectif du portfolio ;
* les sections principales ;
* l'état général de la V1.

Cette page sert de point d'entrée au site.

---

## 4.2 Page Mes créations

Adresse :

```text
http://127.0.0.1:8000/mes-creations/
```

Cette page présente les créations enregistrées dans la base de données.

La V1 utilise un lexique alphabétique. La lettre `K` permet d'afficher le projet KryonCore lorsque celui-ci est enregistré dans l'administration Django.

Les créations affichées sont filtrées avec le champ :

```text
is_visible = True
```

Cela permet de masquer une création sans la supprimer de la base.

---

## 4.3 Page Projets jouables

Adresse :

```text
http://127.0.0.1:8000/projets-jouables/
```

Cette page présente l'espace prévu pour de futurs projets jouables, vidéos, teasers ou prototypes.

Dans la V1, aucun vrai projet jouable n'est encore disponible.

La page contient :

* une zone de lecteur préparatoire ;
* un bouton Lecture affichant un message ;
* un bouton de sélection de fichier local ;
* les informations enregistrées en base pour les futurs projets jouables.

Aucun vrai upload serveur n'est implanté dans cette version.

---

# 5. Accéder à l'administration Django

Adresse :

```text
http://127.0.0.1:8000/admin/
```

L'administration Django permet de gérer les contenus dynamiques du site.

Elle nécessite un compte administrateur.

Pour créer un compte administrateur si nécessaire :

```powershell
python manage.py createsuperuser
```

Avec Docker :

```powershell
docker compose exec web python manage.py createsuperuser
```

---

# 6. Ajouter une création

Depuis l'administration Django :

1. Aller dans la section **Créations**.
2. Cliquer sur **Ajouter une création**.
3. Remplir les champs.
4. Enregistrer.

## Champs principaux

| Champ               | Rôle                                           |
| ------------------- | ---------------------------------------------- |
| Titre               | Nom de la création                             |
| Identifiant URL     | Slug unique utilisé pour identifier le contenu |
| Lettre alphabétique | Lettre utilisée dans le lexique                |
| Nom de code         | Nom interne ou nom du projet                   |
| Type de projet      | Exemple : Jeu vidéo PC                         |
| Statut              | État du projet                                 |
| Description courte  | Texte affiché sur le site                      |
| Visible sur le site | Permet d'afficher ou masquer la création       |

## Exemple

```text
Titre : KryonCore
Identifiant URL : kryoncore
Lettre alphabétique : K
Nom de code : KryonCore
Type de projet : Jeu vidéo PC
Statut : En préparation
Visible sur le site : Oui
```

Une fois enregistrée, la création peut apparaître sur la page **Mes créations**.

---

# 7. Modifier une création

Depuis l'administration :

1. Aller dans **Créations**.
2. Cliquer sur la création à modifier.
3. Modifier les champs nécessaires.
4. Enregistrer.

Il est possible de masquer temporairement une création en décochant :

```text
Visible sur le site
```

La création reste en base mais n'apparaît plus sur le site public.

---

# 8. Ajouter un projet jouable

Depuis l'administration Django :

1. Aller dans la section **Projets jouables**.
2. Cliquer sur **Ajouter un projet jouable**.
3. Remplir les champs.
4. Enregistrer.

## Champs principaux

| Champ                    | Rôle                                            |
| ------------------------ | ----------------------------------------------- |
| Titre                    | Nom du futur contenu jouable                    |
| Identifiant URL          | Slug unique                                     |
| Statut                   | État du contenu                                 |
| Type de contenu prévu    | Exemple : démonstration, teaser, prototype      |
| Description courte       | Résumé affiché sur le site                      |
| Message de disponibilité | Message indiquant si le contenu est disponible  |
| Disponible               | Indique si le contenu est réellement disponible |
| Visible sur le site      | Permet d'afficher ou masquer l'entrée           |

## Exemple

```text
Titre : Prototype jouable à venir
Identifiant URL : prototype-jouable-a-venir
Statut : Non disponible
Type prévu : Démonstration / teaser
Disponible : Non
Visible sur le site : Oui
```

---

# 9. Modifier un projet jouable

Depuis l'administration :

1. Aller dans **Projets jouables**.
2. Cliquer sur le projet à modifier.
3. Modifier le statut, le message ou la visibilité.
4. Enregistrer.

Dans la V1, le champ `Disponible` permet uniquement d'indiquer l'état du contenu. Il ne lance pas encore de vraie démo ou vidéo.

---

# 10. Fonctionnement de l'interface préparatoire d'upload

La page **Projets jouables** contient une interface de sélection de fichier.

Cette interface permet :

* de cliquer sur un bouton de sélection ;
* d'ouvrir l'explorateur de fichiers ;
* d'afficher le nom du fichier choisi ;
* d'indiquer clairement que l'upload n'est pas implanté.

Dans la V1 :

* aucun fichier n'est envoyé au serveur ;
* aucun fichier n'est enregistré en base ;
* aucun fichier n'est exécuté ;
* aucune vidéo n'est réellement lue.

Cette interface sert uniquement à préparer une future fonctionnalité.

---

# 11. Données dynamiques

Les pages récupèrent les données via les vues Django.

Exemples :

```python
Creation.objects.filter(is_visible=True)
```

```python
PlayableProject.objects.filter(is_visible=True)
```

Les données sont ensuite envoyées aux templates HTML pour être affichées.

Cela permet de modifier certains contenus depuis l'administration sans modifier directement le code HTML.

---

# 12. Fonctionnalités disponibles dans la V1

La V1 permet :

* de lancer le site en local ;
* de lancer le site avec Docker ;
* de consulter les trois pages principales ;
* d'accéder à l'administration Django ;
* d'ajouter une création ;
* d'ajouter un projet jouable ;
* d'afficher des données depuis la base SQLite ;
* de masquer ou afficher des contenus ;
* de tester une interface préparatoire pour les projets jouables.

---

# 13. Fonctionnalités non disponibles dans la V1

La V1 ne contient pas encore :

* de vraie page détail projet ;
* de vrai upload serveur ;
* de vrai lecteur vidéo ;
* de système de compte utilisateur public ;
* d'API REST ;
* de rôles avancés ;
* de base NoSQL connectée ;
* de déploiement de production complet.

Ces fonctionnalités sont prévues comme évolutions possibles.

---

# 14. Vérifications à faire avant une démonstration

Avant de présenter le projet, vérifier :

```powershell
python manage.py check
```

Puis tester :

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/mes-creations/
http://127.0.0.1:8000/projets-jouables/
http://127.0.0.1:8000/admin/
```

Vérifier aussi :

* que les données SQL apparaissent ;
* que la lettre K affiche KryonCore ;
* que l'administration est accessible ;
* que la page Projets jouables affiche le message de disponibilité ;
* que le bouton de sélection de fichier affiche bien le nom du fichier choisi ;
* qu'aucun vrai upload serveur n'est déclenché.

---

# 15. Conclusion

La V1 de Frostia Games permet de présenter un portfolio Django simple, fonctionnel et évolutif.

Le site dispose :

* d'une structure de pages claire ;
* d'un backend Django minimal ;
* d'une base SQLite ;
* d'une administration ;
* d'un lancement local ;
* d'un lancement Docker ;
* d'une documentation technique.

Le projet reste volontairement limité afin de conserver une base stable, testable et maintenable.
