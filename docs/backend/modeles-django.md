Modèles Django — Frostia Games

Objectif du document

Ce document présente les modèles Django utilisés dans le projet Frostia Games.

L’objectif est de montrer comment les données principales du site sont structurées côté back-end.

Le projet utilise Django ORM afin de définir les modèles en Python, puis de générer les tables correspondantes dans la base de données SQLite.

Ce document sert aussi à faire le lien entre :

le code Python ;

le diagramme de classes Mermaid ;

les migrations Django ;

les tables SQL ;

l’administration Django ;

les vues ;

les templates ;

le rendu final visible par l’utilisateur.

1. Fichiers concernés

Les modèles principaux sont définis dans les fichiers suivants :

creations/models.py
playable/models.py

Ils sont ensuite utilisés par :

creations/admin.py
playable/admin.py
core/views.py
templates/pages/creation.html
templates/pages/projet_jouable.html

2. Modèles principaux

Deux modèles principaux sont utilisés dans la V1 du projet.

Modèle

Rôle

Creation

Représente une création ou un projet présenté dans la page “Mes créations”.

PlayableProject

Représente un projet jouable ou une démonstration prévue.

Ces deux modèles permettent de montrer que le site ne repose pas uniquement sur du contenu statique écrit directement dans les templates.

Les données peuvent être créées, modifiées ou masquées depuis l’administration Django.

3. Modèle Creation

Rôle général

Le modèle Creation permet de stocker les informations liées aux créations présentées dans le portfolio.

Il sert principalement à alimenter la page :

/mes-creations/

Chaque création peut représenter :

un projet en cours ;

un ancien projet ;

un prototype ;

une idée de jeu ;

une création destinée au portfolio.

Champs principaux

Le modèle Creation contient notamment :

Champ

Rôle

title

Titre public de la création

slug

Identifiant utilisé dans les URLs ou références internes

alphabet_letter

Lettre de classement alphabétique

code_name

Nom de code du projet

project_type

Type de projet

status

État d’avancement

short_description

Description courte affichable côté public

is_visible

Indique si la création doit apparaître sur le site

created_at

Date de création

updated_at

Date de dernière modification

Exemple de structure logique

Exemple simplifié du modèle :

class Creation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    alphabet_letter = models.CharField(max_length=1)
    code_name = models.CharField(max_length=100, blank=True)
    project_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    short_description = models.TextField()
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

Cet extrait montre la structure générale du modèle.

Le fichier réel du projet reste la référence principale.

Rôle du champ is_visible

Le champ is_visible permet de contrôler l’affichage public d’une création.

Une création peut exister dans l’administration sans être affichée sur le site.

Cela permet de préparer un contenu sans le publier immédiatement.

Exemple de logique :

Creation.objects.filter(is_visible=True)

Cette requête récupère uniquement les créations visibles.

4. Modèle PlayableProject

Rôle général

Le modèle PlayableProject permet de stocker les informations liées aux projets jouables ou aux futures démonstrations.

Il sert principalement à alimenter la page :

/projets-jouables/

Dans la V1, aucun vrai jeu jouable dans le navigateur n’est encore intégré.

Ce modèle prépare seulement la structure future.

Champs principaux

Le modèle PlayableProject contient notamment :

Champ

Rôle

title

Titre du projet jouable ou de la démonstration

slug

Identifiant du projet

status

État du projet

content_type

Type de contenu prévu

short_description

Description courte

availability_message

Message affiché si le projet n’est pas encore disponible

is_available

Indique si le contenu est disponible

is_visible

Indique si le projet doit apparaître sur le site

created_at

Date de création

updated_at

Date de dernière modification

Exemple de structure logique

Exemple simplifié du modèle :

class PlayableProject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100)
    short_description = models.TextField()
    availability_message = models.TextField(blank=True)
    is_available = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

Cet extrait montre la structure générale du modèle.

Le fichier réel du projet reste la référence principale.

Rôle du champ is_available

Le champ is_available permet d’indiquer si un projet jouable est réellement disponible.

Dans la V1, les projets jouables sont surtout prévus comme une évolution future.

Cela permet d’afficher un message honnête au visiteur au lieu de promettre une fonctionnalité non disponible.

5. Séparation entre Creation et PlayableProject

Les deux modèles ont des rôles différents.

Modèle

Usage principal

Creation

Présenter une création ou un projet dans le portfolio

PlayableProject

Préparer l’affichage d’une démonstration ou d’un projet jouable

Cette séparation rend l’organisation du projet plus claire.

Elle évite de mélanger :

les créations générales ;

les projets futurs ;

les démonstrations prévues ;

les contenus réellement disponibles.

6. Diagramme de classes Mermaid

Le diagramme suivant représente les deux modèles Django actuellement utilisés dans la V1 de Frostia Games.

Il reprend leurs principaux champs ainsi que leur méthode __str__().

Aperçu du schéma

L’image suivante garantit l’accès au schéma même si le rendu Mermaid n’est pas activé dans l’éditeur :



Source Mermaid

classDiagram
    direction LR

    class Creation {
        +CharField title
        +SlugField slug
        +CharField alphabet_letter
        +CharField code_name
        +CharField project_type
        +CharField status
        +TextField short_description
        +BooleanField is_visible
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() str
    }

    class PlayableProject {
        +CharField title
        +SlugField slug
        +CharField status
        +CharField content_type
        +TextField short_description
        +TextField availability_message
        +BooleanField is_available
        +BooleanField is_visible
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() str
    }

Les deux classes sont représentées séparément, car aucune relation directe n’est définie entre Creation et PlayableProject dans la V1.

Le diagramme montre donc deux modèles indépendants, chacun destiné à un usage précis du portfolio.

7. Utilisation de Django ORM

Django ORM permet de manipuler les données à partir de classes Python.

Les modèles définis dans models.py sont utilisés par Django pour :

créer les migrations ;

générer les tables SQL ;

gérer les données depuis l’administration Django ;

récupérer les contenus dans les vues ;

afficher les contenus dans les templates.

L’ORM permet aussi d’éviter d’écrire directement du SQL brut dans les vues.

Cela rend le code plus lisible, plus maintenable et plus cohérent avec Django.

8. Lien avec les migrations Django

Après la création ou la modification des modèles, Django peut générer des migrations.

Commandes utilisées :

python manage.py makemigrations
python manage.py migrate

Rôle des migrations :

Commande

Rôle

makemigrations

Génère les fichiers de migration à partir des modèles

migrate

Applique les migrations dans la base de données

Les migrations permettent de transformer les classes Python en tables SQL.

9. Lien avec la base SQL

Les modèles Django sont liés aux tables SQL générées par les migrations.

Modèle Django

Table SQL générée

Creation

creations_creation

PlayableProject

playable_playableproject

Les fichiers SQL documentaires sont présents dans :

docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md

Ces fichiers permettent de montrer la structure SQL correspondant aux modèles.

Le SQL natif reste documentaire.

La création réelle des tables reste gérée par les migrations Django.

10. Exemple SQL documentaire

Exemple d’insertion pour une création :

INSERT INTO creations_creation (
    title,
    slug,
    alphabet_letter,
    code_name,
    project_type,
    status,
    short_description,
    is_visible,
    created_at,
    updated_at
) VALUES (
    'Frostia Games',
    'frostia-games',
    'F',
    'FROSTIA',
    'Portfolio Django',
    'V1 en développement',
    'Portfolio Django permettant de présenter des projets vidéoludiques.',
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

Exemple d’insertion pour un projet jouable :

INSERT INTO playable_playableproject (
    title,
    slug,
    status,
    content_type,
    short_description,
    availability_message,
    is_available,
    is_visible,
    created_at,
    updated_at
) VALUES (
    'Prototype jouable à venir',
    'prototype-jouable-a-venir',
    'Prévu',
    'Démonstration',
    'Projet jouable prévu pour une future évolution du site.',
    'Aucune version jouable disponible actuellement.',
    0,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

Ces exemples servent à montrer la compréhension du lien entre modèles Django et SQL.

11. Lien avec l’administration Django

Les modèles sont enregistrés dans l’administration Django.

Fichiers concernés :

creations/admin.py
playable/admin.py

L’administration permet :

d’ajouter une création ;

de modifier une création ;

de masquer une création ;

d’ajouter un projet jouable ;

de modifier un projet jouable ;

de contrôler la visibilité des contenus.

L’administration Django évite d’avoir à modifier directement les templates pour changer les données.

12. Lien avec les vues Django

Les modèles sont utilisés dans les vues pour récupérer les contenus visibles.

Exemple logique pour les créations :

creations = Creation.objects.filter(is_visible=True)

Exemple logique pour les projets jouables :

playable_projects = PlayableProject.objects.filter(is_visible=True)

Les vues transmettent ensuite les données aux templates.

Chaîne de fonctionnement :

Modèle Django
→ Vue Django
→ Template HTML
→ Page affichée

13. Lien avec les templates

Les données récupérées dans les vues sont affichées dans les templates.

Templates concernés :

templates/pages/creation.html
templates/pages/projet_jouable.html

Les templates peuvent afficher :

le titre ;

la description ;

le statut ;

le type de projet ;

le message de disponibilité ;

les informations visibles côté public.

14. Rendu final côté utilisateur

Le rendu final est visible sur les pages publiques :

/mes-creations/
/projets-jouables/

Le visiteur ne voit pas directement les modèles Django.

Il voit seulement les données préparées, filtrées et affichées par les templates.

Cela montre le fonctionnement complet :

Code Python
→ Base SQLite
→ Administration Django
→ Vue Django
→ Template HTML
→ Rendu navigateur

15. Limites actuelles

Les modèles actuels sont volontairement simples.

Ils ne gèrent pas encore :

les images dynamiques ;

les fichiers médias ;

les versions de projet ;

les relations complexes ;

les catégories avancées ;

les tags dynamiques ;

les historiques de modification ;

les commentaires ;

les statistiques.

Ces éléments sont reportés afin de garder une V1 stable.

16. Évolutions possibles

Une future version pourrait ajouter de nouveaux modèles comme :

ProjectDetail
ProjectVersion
MediaAsset
DevelopmentLog
ProjectTag
ProjectLink

Ces modèles permettraient d’enrichir progressivement le portfolio.

Cependant, ils ne sont pas nécessaires pour la V1.

17. Preuves à intégrer dans le dossier

Pour cette partie, les preuves à intégrer dans le dossier projet sont :

Élément

Preuve

Code du modèle Creation

Capture du fichier creations/models.py

Code du modèle PlayableProject

Capture du fichier playable/models.py

Diagramme de classes

Capture ou rendu du diagramme Mermaid des deux modèles

Table SQL générée

Extrait CREATE TABLE correspondant

Exemple SQL

Extrait INSERT INTO

Administration Django

Capture des modèles visibles dans /admin/

Vue Django

Capture de la récupération des données dans core/views.py

Rendu final

Capture de la page utilisant les données

18. Intérêt pour le projet

Les modèles Django constituent la base du back-end du projet.

Ils permettent de structurer les données, de les administrer et de les afficher dans les pages publiques du site.

Cette partie montre le lien entre :

le code Python ;

le diagramme de classes Mermaid ;

la base de données SQLite ;

l’administration Django ;

les vues ;

les templates ;

le rendu final côté utilisateur.

Elle permet aussi de démontrer la compétence back-end attendue dans un dossier projet.

19. Conclusion

Les modèles Creation et PlayableProject forment la base de la partie dynamique de Frostia Games.

Ils permettent de gérer les contenus depuis l’administration Django et de les afficher dans les pages publiques.

La V1 reste volontairement simple, mais les modèles montrent déjà une vraie structure back-end.

Le diagramme Mermaid complète cette documentation en donnant une vue synthétique des deux classes et de leurs champs principaux.

Les évolutions plus avancées pourront être ajoutées plus tard, lorsque le projet aura besoin de gérer davantage de contenus, de médias ou de relations.