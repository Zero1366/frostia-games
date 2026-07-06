# Vues et routes Django — Frostia Games

## Objectif du document

Ce document présente le fonctionnement des vues et des routes Django dans le projet **Frostia Games**.

L’objectif est de montrer comment les pages publiques du site sont reliées :

* aux routes URL ;
* aux vues Python ;
* aux modèles Django ;
* aux services internes ;
* aux templates HTML ;
* au rendu final dans le navigateur.

Cette partie permet de démontrer le fonctionnement du back-end Django dans l’affichage des pages du site.

Elle montre aussi que les pages publiques ne sont pas seulement des fichiers HTML statiques, mais qu’elles sont servies par Django avec une logique côté serveur.

---

# 1. Fichiers concernés

Les fichiers principaux concernés sont :

```text
frostia_config/urls.py
core/urls.py
core/views.py
templates/pages/home.html
templates/pages/creation.html
templates/pages/projet_jouable.html
```

Les vues peuvent aussi utiliser :

```text
creations/models.py
playable/models.py
core/services/nosql_notes.py
```

---

# 2. Rôle des routes URL

Les routes permettent d’associer une adresse du site à une vue Django.

Lorsqu’un visiteur accède à une URL, Django utilise les fichiers `urls.py` pour identifier la vue à exécuter.

Dans le projet, le chemin global peut être résumé ainsi :

```text
Navigateur
→ URL demandée
→ frostia_config/urls.py
→ core/urls.py
→ core/views.py
→ template HTML
→ page affichée
```

---

# 3. Routes principales du projet

Les routes publiques principales de la V1 sont :

| URL | Vue appelée | Template utilisé | Rôle |
| --- | ----------- | ---------------- | ---- |
| `/` | `home` | `templates/pages/home.html` | Affiche la page d’accueil |
| `/mes-creations/` | `creation_list` ou vue équivalente | `templates/pages/creation.html` | Affiche les créations visibles |
| `/projets-jouables/` | `playable_projects` ou vue équivalente | `templates/pages/projet_jouable.html` | Affiche les projets jouables ou prévus |
| `/admin/` | Administration Django | Interface Django Admin | Permet la gestion des contenus |

Les noms exacts des fonctions peuvent varier selon le fichier réel, mais la logique reste la même :

```text
URL
→ vue Django
→ récupération des données
→ template
→ rendu navigateur
```

---

# 4. Exemple de routes dans `core/urls.py`

Exemple de structure possible :

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mes-creations/", views.creation_list, name="creation_list"),
    path("projets-jouables/", views.playable_projects, name="playable_projects"),
]
```

Ce fichier permet de relier les adresses publiques aux vues Python.

Le fichier réel du projet reste la référence principale.

---

# 5. Rôle des vues Django

Dans Django, une vue reçoit une requête HTTP et retourne une réponse.

Dans le projet **Frostia Games**, les vues permettent notamment :

* d’afficher la page d’accueil ;
* d’afficher la page **Mes créations** ;
* d’afficher la page **Projets jouables** ;
* de récupérer les créations visibles ;
* de récupérer les projets jouables visibles ;
* de récupérer les notes TinyDB ;
* de transmettre les données aux templates HTML.

Une vue fait le lien entre le back-end et le rendu final.

---

# 6. Vue de la page d’accueil

La page d’accueil est accessible avec l’URL :

```text
/
```

Elle utilise le template :

```text
templates/pages/home.html
```

Cette page présente le projet Frostia Games.

Elle peut aussi afficher les notes de progression issues de TinyDB.

Chaîne de fonctionnement :

```text
/
→ vue home
→ récupération éventuelle des notes TinyDB
→ templates/pages/home.html
→ page d'accueil affichée
```

---

# 7. Exemple de vue d’accueil avec TinyDB

Exemple logique :

```python
from django.shortcuts import render
from core.services.nosql_notes import seed_project_notes, find_notes_by_project

def home(request):
    seed_project_notes()
    project_notes = find_notes_by_project("frostia-games")

    return render(
        request,
        "pages/home.html",
        {
            "project_notes": project_notes,
        },
    )
```

Cette vue montre plusieurs éléments importants :

* la vue reçoit une requête ;
* elle appelle un service Python ;
* elle récupère des notes TinyDB ;
* elle transmet ces notes au template ;
* le template peut ensuite les afficher.

Le code réel du projet reste la référence principale.

---

# 8. Vue de la page Mes créations

La page **Mes créations** est accessible avec l’URL :

```text
/mes-creations/
```

Elle utilise le template :

```text
templates/pages/creation.html
```

La vue récupère les créations visibles depuis le modèle `Creation`.

Exemple logique :

```python
from django.shortcuts import render
from creations.models import Creation

def creation_list(request):
    creations = Creation.objects.filter(is_visible=True)

    return render(
        request,
        "pages/creation.html",
        {
            "creations": creations,
        },
    )
```

Cette vue montre que les contenus ne sont pas écrits uniquement en dur dans le HTML.

Ils peuvent venir de la base SQLite via Django ORM.

---

# 9. Fonctionnement de la page Mes créations

Lorsqu’un visiteur consulte la page **Mes créations**, Django suit plusieurs étapes :

1. le visiteur accède à `/mes-creations/` ;
2. Django identifie la route dans `urls.py` ;
3. la vue associée est appelée ;
4. la vue récupère les créations visibles ;
5. les données sont envoyées au template ;
6. le template génère la page HTML ;
7. le navigateur affiche la page finale.

Chaîne simplifiée :

```text
/mes-creations/
→ core/urls.py
→ core/views.py
→ Creation.objects.filter(is_visible=True)
→ base SQLite
→ templates/pages/creation.html
→ navigateur
```

---

# 10. Vue de la page Projets jouables

La page **Projets jouables** est accessible avec l’URL :

```text
/projets-jouables/
```

Elle utilise le template :

```text
templates/pages/projet_jouable.html
```

La vue récupère les projets visibles depuis le modèle `PlayableProject`.

Exemple logique :

```python
from django.shortcuts import render
from playable.models import PlayableProject

def playable_projects(request):
    projects = PlayableProject.objects.filter(is_visible=True)

    return render(
        request,
        "pages/projet_jouable.html",
        {
            "projects": projects,
        },
    )
```

Cette vue permet d’afficher les projets jouables prévus ou les démonstrations futures.

Dans la V1, aucun vrai jeu jouable navigateur n’est encore intégré.

---

# 11. Fonctionnement de la page Projets jouables

Lorsqu’un visiteur consulte la page **Projets jouables**, Django suit plusieurs étapes :

1. le visiteur accède à `/projets-jouables/` ;
2. Django identifie la route correspondante ;
3. la vue associée est appelée ;
4. la vue récupère les projets visibles ;
5. les données sont envoyées au template ;
6. le template affiche les informations ;
7. le navigateur affiche la page finale.

Chaîne simplifiée :

```text
/projets-jouables/
→ core/urls.py
→ core/views.py
→ PlayableProject.objects.filter(is_visible=True)
→ base SQLite
→ templates/pages/projet_jouable.html
→ navigateur
```

---

# 12. Lien entre modèle, vue et template

Le fonctionnement repose sur une logique MVT propre à Django.

| Élément | Rôle dans le projet |
| ------- | ------------------- |
| Modèle | Définit la structure des données |
| Vue | Récupère les données et prépare la réponse |
| Template | Affiche les données dans une page HTML |
| Route | Associe une URL à une vue |

Dans Frostia Games, cette organisation permet de séparer clairement la logique du projet :

* les modèles structurent les données ;
* les vues organisent l’affichage ;
* les templates gèrent le rendu HTML ;
* les routes relient les pages aux vues.

---

# 13. Exemple complet : page Mes créations

La page **Mes créations** utilise les données du modèle `Creation`.

Fonctionnement complet :

```text
Visiteur
→ /mes-creations/
→ route Django
→ vue Django
→ modèle Creation
→ base SQLite
→ template creation.html
→ page affichée
```

Intérêt :

* les contenus peuvent être ajoutés depuis l’administration Django ;
* les contenus peuvent être masqués avec `is_visible` ;
* le HTML n’a pas besoin d’être modifié à chaque changement ;
* la page devient dynamique.

---

# 14. Exemple complet : page Projets jouables

La page **Projets jouables** utilise les données du modèle `PlayableProject`.

Fonctionnement complet :

```text
Visiteur
→ /projets-jouables/
→ route Django
→ vue Django
→ modèle PlayableProject
→ base SQLite
→ template projet_jouable.html
→ page affichée
```

Intérêt :

* la structure prépare les futures démonstrations ;
* le statut d’un projet peut être affiché ;
* un message de disponibilité peut être prévu ;
* le site reste honnête sur ce qui est disponible ou non.

---

# 15. Exemple complet : page d’accueil avec TinyDB

La page d’accueil utilise TinyDB pour afficher des notes de progression.

Fonctionnement complet :

```text
Visiteur
→ /
→ route Django
→ vue home
→ service nosql_notes.py
→ base JSON TinyDB
→ template home.html
→ notes affichées
```

Cette partie montre une logique complémentaire à SQLite.

SQLite reste la base principale.

TinyDB sert d’expérimentation NoSQL légère.

---

# 16. Lien avec les templates

Les vues transmettent des variables aux templates.

Exemple :

```python
return render(request, "pages/creation.html", {"creations": creations})
```

Dans le template, les données peuvent ensuite être parcourues :

```django
{% for creation in creations %}
    <article>
        <h2>{{ creation.title }}</h2>
        <p>{{ creation.short_description }}</p>
    </article>
{% endfor %}
```

Ce fonctionnement permet d’afficher plusieurs contenus dynamiques sans écrire chaque bloc manuellement.

---

# 17. Lien avec l’administration Django

Les contenus affichés dans les pages peuvent être gérés depuis l’administration Django.

Adresse locale :

```text
https://frostia-games.onrender.com/admin/
```

Adresse en ligne :

```text
https://frostia-games.onrender.com/admin/
```

L’administration permet notamment :

* d’ajouter une création ;
* de modifier une création ;
* de masquer une création ;
* d’ajouter un projet jouable ;
* de modifier un projet jouable ;
* de changer un statut ;
* de contrôler la visibilité publique.

Le compte temporaire de lecture seule peut consulter certains éléments sans disposer des droits complets d’un administrateur.

---

# 18. Lien avec la sécurité

Les vues utilisent l’ORM Django plutôt que du SQL brut.

Exemple :

```python
Creation.objects.filter(is_visible=True)
```

Ce choix permet :

* d’éviter d’écrire directement des requêtes SQL dans les vues ;
* de rester cohérent avec Django ;
* de limiter les risques liés à des requêtes mal construites ;
* de garder un code plus lisible.

Les routes publiques ne donnent pas accès aux variables sensibles.

Les identifiants administrateur ne sont pas affichés dans les vues.

---

# 19. Limites actuelles

Les vues et routes de la V1 restent simples.

Elles ne gèrent pas encore :

* un espace privé complet ;
* une API REST ;
* un vrai système de comptes publics ;
* des formulaires publics avancés ;
* un upload serveur réel ;
* un jeu jouable navigateur ;
* des filtres complexes ;
* une pagination avancée ;
* des recherches avancées.

Ces limites sont volontaires.

Elles permettent de garder une V1 stable et compréhensible.

---

# 20. Évolutions possibles

Une version future pourrait ajouter :

* des vues détaillées par projet ;
* une fiche complète pour chaque création ;
* une recherche ;
* des filtres ;
* une pagination ;
* une API REST ;
* des formulaires publics ;
* un espace privé ;
* des vues de statistiques ;
* une meilleure gestion des médias.

Ces évolutions ne sont pas nécessaires pour la V1.

---

# 21. Preuves à intégrer dans le dossier

Pour cette partie, les preuves à intégrer dans le dossier projet sont :

| Élément | Preuve |
| ------- | ------ |
| Routes Django | Capture de `core/urls.py` |
| Routes principales | Capture de `frostia_config/urls.py` |
| Vues Django | Capture de `core/views.py` |
| Données SQLite récupérées | Capture du code utilisant `Creation` et `PlayableProject` |
| Données TinyDB récupérées | Capture du code utilisant `nosql_notes.py` |
| Template associé | Capture de `home.html`, `creation.html` ou `projet_jouable.html` |
| Rendu final | Capture de la page affichée dans le navigateur |
| Admin Django | Capture des modèles disponibles dans `/admin/` |

---

# 22. Intérêt pour le projet

Les vues et les routes montrent le fonctionnement dynamique du site.

Elles permettent de prouver que les pages ne sont pas seulement des fichiers statiques, mais qu’elles sont servies par Django avec une logique côté serveur.

Cette partie valorise les compétences back-end suivantes :

* organisation des routes ;
* création de vues Django ;
* récupération de données SQLite ;
* récupération de données TinyDB ;
* transmission des données aux templates ;
* affichage dynamique dans le navigateur ;
* séparation entre logique Python et rendu HTML ;
* utilisation cohérente de Django ORM.

---

# 23. Conclusion

Les vues et routes Django sont une partie importante du projet Frostia Games.

Elles assurent le lien entre les URLs, les modèles, les services internes et les templates.

Elles permettent de transformer les données du projet en pages visibles dans le navigateur.

La V1 reste volontairement simple, mais elle montre déjà une structure back-end claire :

```text
URL
→ vue
→ données
→ template
→ rendu final
```

Cette structure pourra être enrichie plus tard si le projet évolue vers des pages détaillées, une API ou une interface privée.


