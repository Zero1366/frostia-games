# Sécurité backend - Frostia Games

## Objectif du document

Ce document présente les choix de sécurité appliqués ou prévus dans la V1 du projet **Frostia Games**.

L'objectif est de montrer que le backend Django est conçu avec une attention particulière à la sécurité, même si le projet reste une V1 locale et de démonstration.

---

# 1. Contexte de sécurité

Frostia Games utilise Django pour gérer :

* les routes ;
* les vues ;
* les modèles ;
* l'administration ;
* la base de données ;
* les templates ;
* les fichiers statiques.

Django fournit déjà plusieurs protections intégrées. La V1 s'appuie sur ces protections tout en limitant volontairement les fonctionnalités sensibles.

L'objectif n'est pas de prétendre que le projet est prêt pour une production complète, mais de montrer que les risques principaux ont été identifiés et que les fonctionnalités sensibles sont volontairement encadrées ou reportées.

---

# 2. Utilisation de l'ORM Django

Le projet utilise l'ORM Django pour manipuler les données.

Exemple :

```python
Creation.objects.filter(is_visible=True).order_by(
    "alphabet_letter",
    "title",
)
```

L'ORM permet d'éviter d'écrire directement des requêtes SQL brutes dans les vues.

Cela réduit le risque d'injection SQL, car Django prépare les requêtes et protège les valeurs utilisées dans les filtres.

---

# 3. Absence de SQL brut dans les vues

Dans la V1, le projet n'utilise pas de requêtes SQL construites manuellement avec des chaînes de caractères.

Exemple de pratique évitée :

```python
cursor.execute("SELECT * FROM creations WHERE slug = '" + slug + "'")
```

Ce type de code est dangereux si une valeur utilisateur est intégrée directement dans la requête.

Le projet utilise plutôt les modèles Django :

```python
Creation.objects.filter(slug=slug)
```

Cette approche permet de garder un code plus sûr, plus lisible et mieux intégré à Django.

---

# 4. Protection contre l'injection SQL

Le risque d'injection SQL est limité par plusieurs choix :

* utilisation des modèles Django ;
* utilisation de l'ORM ;
* absence de SQL brut dans les vues ;
* champs structurés dans les modèles ;
* routes contrôlées par Django ;
* absence de formulaire public manipulant directement la base dans la V1.

La base SQLite est manipulée par Django, pas directement par du SQL écrit dans les pages.

---

# 5. Administration protégée

L'administration Django est accessible via :

```text
/admin/
```

Elle est protégée par le système d'authentification Django.

Seul un utilisateur administrateur peut :

* ajouter une création ;
* modifier une création ;
* ajouter un projet jouable ;
* modifier un projet jouable ;
* rendre un contenu visible ou invisible.

Dans la V1, l'administration sert à gérer les contenus sans modifier directement les templates HTML.

---

# 6. Validation des mots de passe

Le fichier `settings.py` conserve les validateurs de mots de passe Django.

Ces validateurs permettent notamment :

* la vérification de similarité avec les informations utilisateur ;
* l'imposition d'une longueur minimale ;
* la détection des mots de passe trop communs ;
* le refus des mots de passe uniquement numériques.

Ces règles renforcent la sécurité des comptes administrateurs.

---

# 7. Protection CSRF

Django inclut une protection CSRF pour les formulaires.

La protection CSRF permet de limiter les attaques où un site externe essaie de soumettre une requête à la place d'un utilisateur connecté.

Dans la V1 actuelle, les formulaires publics ne sont pas encore développés. Cependant, la protection CSRF est disponible dans la configuration Django pour les évolutions futures.

L'administration Django bénéficie déjà des mécanismes de sécurité fournis par Django.

---

# 8. Échappement automatique dans les templates

Les templates Django échappent automatiquement les variables affichées dans les pages.

Exemple :

```django
{{ creation.title }}
```

Django évite que du code HTML ou JavaScript non souhaité soit exécuté directement dans le navigateur lorsque les variables sont affichées normalement.

Cela réduit le risque d'injection de code dans les pages.

---

# 9. Gestion de la visibilité des contenus

Les modèles utilisent des champs de visibilité :

```python
is_visible = models.BooleanField(default=True)
```

Ces champs permettent de masquer un contenu sans le supprimer de la base.

Les vues utilisent ce filtre :

```python
Creation.objects.filter(is_visible=True)
PlayableProject.objects.filter(is_visible=True)
```

Cela permet de contrôler ce qui est réellement affiché sur le site public.

Un contenu peut donc exister dans l'administration sans être visible par les visiteurs.

---

# 10. Upload réel non implanté dans la V1

La page **Projets jouables** contient une interface préparatoire permettant de sélectionner un fichier local.

Cependant, aucun vrai upload serveur n'est implanté dans la V1.

Cela signifie que :

* aucun fichier n'est envoyé au serveur ;
* aucun fichier n'est stocké côté backend ;
* aucun fichier utilisateur n'est exécuté ;
* aucune gestion de média uploadé n'est encore active.

Ce choix est volontaire, car l'upload de fichiers demande des protections supplémentaires.

---

# 11. Risques liés à un futur upload

Si un vrai upload est ajouté plus tard, il faudra prévoir :

* validation des extensions ;
* limitation de la taille des fichiers ;
* stockage dans un dossier sécurisé ;
* renommage des fichiers ;
* contrôle des types MIME ;
* interdiction d'exécuter les fichiers uploadés ;
* séparation entre fichiers publics et fichiers internes ;
* suppression sécurisée ;
* éventuellement scan antivirus ou contrôle externe.

Pour cette raison, l'upload réel est placé hors périmètre de la V1.

Cela permet d'éviter d'ajouter une fonctionnalité sensible sans sécurité adaptée.

---

# 12. Configuration de développement

Dans la V1 locale, le projet utilise :

```python
DEBUG = True
```

Ce mode est utile pendant le développement, car il affiche les erreurs de manière détaillée.

Cependant, il ne doit pas être utilisé en production.

Pour une mise en ligne réelle, il faudra configurer :

```python
DEBUG = False
```

---

# 13. SECRET_KEY

La clé secrète Django est actuellement présente dans `settings.py` pour le développement local.

Ce choix est acceptable pour une V1 locale, mais il n'est pas adapté à une production.

Pour un déploiement réel, la clé devra être déplacée dans une variable d'environnement.

Exemple d'évolution future :

```python
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
```

La clé ne devra pas être partagée publiquement dans un dépôt ou dans une documentation de production.

---

# 14. ALLOWED_HOSTS

Dans la V1 locale, la configuration est adaptée au développement.

Pour un déploiement en ligne, il faudra définir les hôtes autorisés.

Exemple :

```python
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "nom-du-site.onrender.com",
]
```

Cette configuration permet d'éviter que l'application Django réponde à n'importe quel domaine.

---

# 15. Base de données

La V1 utilise SQLite.

SQLite est adapté pour :

* le développement local ;
* les tests ;
* une V1 simple ;
* un projet de démonstration ;
* une base backend légère.

Pour une version plus avancée ou déployée en production, une base comme PostgreSQL pourrait être envisagée.

---

# 16. Docker et sécurité

Docker est utilisé pour fournir un environnement reproductible.

La configuration actuelle est volontairement simple :

* Python ;
* Django ;
* SQLite ;
* serveur de développement Django.

Elle ne remplace pas une configuration de production complète.

Pour une production, il faudrait ajouter :

* variables d'environnement ;
* serveur applicatif comme Gunicorn ;
* serveur frontal comme Nginx ;
* configuration HTTPS ;
* gestion sécurisée des fichiers statiques et médias ;
* configuration stricte des hôtes autorisés ;
* séparation claire entre développement et production.

---

# 17. Sécurité non implantée dans la V1

La V1 ne contient pas encore :

* authentification utilisateur publique ;
* rôles avancés ;
* API REST ;
* vrai upload serveur ;
* permissions personnalisées ;
* journalisation avancée ;
* limitation de requêtes ;
* configuration de production complète.

Ces éléments ne sont pas oubliés. Ils sont volontairement placés dans les évolutions futures afin de garder une V1 stable.

---

# 18. Bonnes pratiques appliquées

Les bonnes pratiques actuellement appliquées sont :

* utilisation du framework Django ;
* séparation entre modèles, vues et templates ;
* utilisation de l'ORM ;
* absence de SQL brut ;
* administration protégée ;
* champs de visibilité ;
* validation des champs par les modèles ;
* configuration claire des fichiers statiques ;
* documentation de Docker ;
* documentation du schéma SQL ;
* documentation des limites de la V1 ;
* absence de fonctionnalité sensible non maîtrisée.

---

# 19. Évolutions de sécurité prévues

Les évolutions possibles sont :

1. Déplacer `SECRET_KEY` dans une variable d'environnement.
2. Passer `DEBUG` à `False` en production.
3. Configurer `ALLOWED_HOSTS`.
4. Ajouter une configuration `.env`.
5. Sécuriser un futur système d'upload.
6. Ajouter des permissions plus fines dans l'administration.
7. Mettre en place une base PostgreSQL si le projet évolue.
8. Préparer une configuration de production avec Gunicorn.
9. Ajouter HTTPS via l'hébergeur.
10. Ajouter une journalisation plus complète.
11. Séparer clairement les paramètres de développement et de production.

---

# 20. Conclusion

La V1 de Frostia Games utilise les protections de base de Django et limite volontairement les fonctionnalités sensibles.

Le projet est actuellement sécurisé pour un usage local et de démonstration :

* données manipulées via l'ORM ;
* administration protégée ;
* pas de SQL brut ;
* pas de vrai upload serveur ;
* templates avec échappement automatique ;
* configuration claire de développement ;
* risques de production identifiés.

Les protections de production seront ajoutées dans une version future, lorsque le projet sera prêt pour une mise en ligne complète.
