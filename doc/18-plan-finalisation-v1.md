# Plan de finalisation V1 - Frostia Games

## Objectif du document

Ce document présente le plan de finalisation de la V1 du projet **Frostia Games**.

L’objectif est de cadrer les dernières actions à réaliser avant la présentation du projet dans le dossier final.

À ce stade, le projet ne doit plus être élargi avec de grosses fonctionnalités.

La priorité est de finaliser :

* les documents ;
* les captures ;
* les preuves ;
* les annexes ;
* la relecture ;
* la cohérence du dossier ;
* le dernier commit Git ;
* la vérification finale du rendu.

Ce plan sert à éviter de repartir dans du développement supplémentaire alors que la V1 est déjà fonctionnelle, documentée et déployée.

---

# 1. État actuel de la V1

La V1 de Frostia Games est considérée comme fonctionnelle dans son périmètre.

Elle contient déjà :

* un projet Django fonctionnel ;
* trois pages publiques principales ;
* une base SQLite ;
* des modèles Django ;
* une administration Django ;
* un affichage dynamique des créations ;
* un affichage dynamique des projets jouables à venir ;
* un menu mobile JavaScript ;
* une expérimentation TinyDB ;
* un affichage des notes TinyDB sur l’accueil ;
* des fichiers SQL natifs documentaires ;
* une documentation technique ;
* une documentation de conception ;
* un déploiement Render ;
* un compte temporaire de lecture seule ;
* une structure de preuves à préparer.

Le projet est donc dans une phase de finalisation.

La priorité n'est plus d'ajouter de nouvelles fonctionnalités, mais de rendre le dossier clair, propre et défendable.

---

# 2. Rappel du périmètre à ne plus dépasser

Pour protéger la stabilité de la V1, les éléments suivants ne doivent pas être ajoutés maintenant :

* PostgreSQL ;
* MongoDB ;
* interface d'administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* API REST ;
* espace privé complet ;
* graphiques Plotly.js ;
* mini-jeu intégré ;
* système de score ;
* système de sauvegarde automatique avancé ;
* gestion complète des médias ;
* refonte graphique complète ;
* tests automatisés complets.

Ces éléments peuvent rester dans la roadmap.

Ils ne doivent pas bloquer la finalisation du dossier actuel.

---

# 3. Objectif de la finalisation

La finalisation doit permettre d'obtenir un projet :

* propre ;
* cohérent ;
* stable ;
* compréhensible ;
* documenté ;
* prouvé par captures ;
* défendable à l’oral ;
* présentable dans un dossier projet.

La finalisation ne consiste pas à ajouter beaucoup de fonctionnalités.

Elle consiste à vérifier que tout ce qui existe est clair, cohérent et correctement expliqué.

---

# 4. Actions déjà réalisées

Les actions suivantes sont considérées comme réalisées ou suffisamment avancées.

## 4.1 Base Django

| Élément | État |
| ------- | ---- |
| Projet Django | Terminé |
| Applications `core`, `creations`, `playable` | Terminées |
| Templates principaux | Terminés |
| Fichiers statiques | En place |
| Menu mobile JavaScript | En place |
| Vues principales | En place |
| Routes principales | En place |

---

## 4.2 Backend et base de données

| Élément | État |
| ------- | ---- |
| Modèle `Creation` | Fonctionnel |
| Modèle `PlayableProject` | Fonctionnel |
| Migrations Django | En place |
| Base SQLite | Fonctionnelle |
| Administration Django | Fonctionnelle |
| Compte lecture seule | En place |
| SQL natif documentaire | En place |

---

## 4.3 NoSQL TinyDB

| Élément | État |
| ------- | ---- |
| Dépendance `tinydb` | Ajoutée |
| Service `nosql_notes.py` | En place |
| Script `demo_tinydb_notes.py` | En place |
| Base JSON TinyDB | En place |
| Affichage sur l’accueil | En place |
| Documentation NoSQL | En place |

---

## 4.4 Déploiement

| Élément | État |
| ------- | ---- |
| Render Web Service | En place |
| Build Command | En place |
| Start Command | En place |
| Gunicorn | En place |
| WhiteNoise | En place |
| Variables d’environnement | En place |
| URL de production | En ligne |

URL de production :

```text
https://frostia-games.onrender.com
```

---

## 4.5 Documentation principale

La documentation principale est avancée.

Documents concernés :

```text
00-index-documentation.md
01-modernisation-interface.md
02-journal-de-bord.md
03-modelisation-backend.md
04-docker-et-lancement.md
05-securite-backend.md
06-manuel-utilisateur.md
07-base-de-donnees.md
08-changelog.md
09-deploiement-render.md
10-bilan-v1-frostia-games.md
11-installation-locale.md
12-architecture.md
13-test-et-vérification.md
14-Capture-et Preuve.md
15-limites-et-évolutions.md
16-presentation-projet-2.md
17-pistes-explorees-et-non-retenues.md
18-plan-finalisation-v1.md
19-renforcement-dossier-projet.md
```

---

## 4.6 Documentation complémentaire

Le dossier complémentaire `docs/` est également en place.

Documents concernés :

```text
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
docs/frontend/javascript-menu-mobile.md
docs/nosql/nosql.md
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

---

# 5. Actions restantes prioritaires

Les actions restantes doivent être traitées dans l’ordre suivant.

## Priorité 1 - Vérifier les fichiers du projet

Vérifier que les fichiers importants existent bien :

```text
manage.py
requirements.txt
README.md
CHOIX_TECHNIQUES.md
build.sh
Dockerfile
docker-compose.yml
.env.example
.gitignore
```

Vérifier aussi :

```text
core/views.py
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
static/js/menu.js
templates/base.html
templates/pages/home.html
creations/models.py
playable/models.py
creations/admin.py
playable/admin.py
```

Objectif :

```text
S'assurer que le dossier final correspond bien au projet réel.
```

---

## Priorité 2 - Vérifier les commandes techniques

Commandes à lancer avant le dernier commit :

```powershell
python manage.py check
python -m scripts.demo_tinydb_notes
git status
```

Résultats attendus :

```text
System check identified no issues (0 silenced).
```

```text
Preuve NoSQL TinyDB — Frostia Games
```

```text
nothing to commit, working tree clean
```

Si `git status` n'est pas propre, il faut vérifier les fichiers modifiés, puis faire un commit final si les changements sont corrects.

---

## Priorité 3 - Vérifier le site en ligne

URL à vérifier :

```text
https://frostia-games.onrender.com
```

Pages à tester :

```text
https://frostia-games.onrender.com
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
https://frostia-games.onrender.com/admin/
```

À vérifier :

* la page d’accueil se charge ;
* les notes TinyDB apparaissent si elles sont prévues ;
* la page Mes créations fonctionne ;
* la page Projets jouables fonctionne ;
* le CSS est chargé ;
* le menu mobile fonctionne ;
* l'administration Django est accessible ;
* aucune erreur serveur n'apparaît.

---

## Priorité 4 - Vérifier l'administration Django

À vérifier avec le compte administrateur :

* connexion possible ;
* modèles visibles ;
* création consultable ;
* projet jouable consultable ;
* données cohérentes ;
* absence de donnée sensible affichée inutilement.

À vérifier avec le compte temporaire de lecture seule :

* connexion possible ;
* accès limité ;
* consultation des créations ;
* consultation des projets jouables ;
* absence d'accès aux utilisateurs ;
* absence d'accès aux groupes ;
* absence d'accès aux permissions sensibles.

Les identifiants réels ne doivent pas être écrits dans la documentation publique.

---

# 6. Captures à préparer

Les captures doivent servir à prouver le fonctionnement du projet.

Elles doivent être lisibles, propres et sans donnée sensible.

---

## 6.1 Captures du site public

Captures à préparer :

* page d’accueil desktop ;
* page d’accueil avec notes TinyDB ;
* page Mes créations ;
* page Projets jouables ;
* page d’accueil mobile ;
* menu mobile ouvert.

Objectif :

```text
Prouver que le site public fonctionne et que l'interface est consultable.
```

---

## 6.2 Captures de l’administration Django

Captures à préparer :

* page de connexion admin ;
* tableau de bord admin ;
* modèle `Creation` ;
* modèle `PlayableProject` ;
* compte lecture seule ;
* accès limité du compte lecture seule.

Objectif :

```text
Prouver que l'administration fonctionne et que l'accès de consultation est limité.
```

---

## 6.3 Captures Render

Captures à préparer :

* service Render actif ;
* logs avec service en ligne ;
* Build Command ;
* Start Command ;
* variables d'environnement masquées.

Objectif :

```text
Prouver que le projet est déployé en ligne.
```

---

## 6.4 Captures techniques

Captures à préparer :

* `python manage.py check` ;
* `python -m scripts.demo_tinydb_notes` ;
* `git status` propre ;
* dépôt GitHub ;
* structure du projet dans VS Code.

Objectif :

```text
Prouver que le projet est vérifié et versionné.
```

---

## 6.5 Captures du code

Captures à préparer :

* modèles Django ;
* vues Django ;
* configuration admin ;
* service TinyDB ;
* script TinyDB ;
* fichier `menu.js` ;
* fichiers SQL natifs ;
* fichier `build.sh`.

Objectif :

```text
Prouver que les éléments présentés dans le dossier existent réellement dans le code.
```

---

## 6.6 Captures de documentation

Captures à préparer :

* dossier `doc/` ;
* dossier `docs/` ;
* fichier de preuve ;
* documentation Render ;
* documentation SQL ;
* documentation NoSQL ;
* documentation frontend ;
* documentation backend ;
* bilan V1.

Objectif :

```text
Prouver que le projet est documenté.
```

---

# 7. Règles de sécurité pour les preuves

Avant d'intégrer une capture dans le dossier, vérifier qu'elle ne montre pas :

* mot de passe ;
* clé secrète Django ;
* vraie valeur de variable d'environnement ;
* valeur de `DJANGO_SECRET_KEY` ;
* valeur de `DJANGO_SUPERUSER_PASSWORD` ;
* token ;
* clé API ;
* identifiant administrateur complet ;
* identifiant du compte temporaire complet ;
* information personnelle inutile.

Les captures Render doivent afficher les noms des variables si nécessaire, mais pas leurs valeurs.

Les captures du compte temporaire doivent montrer les droits limités, mais pas le mot de passe.

---

# 8. Organisation des preuves

Organisation recommandée :

```text
doc/
└── preuves/
    ├── preuves-frostia-games.md
    └── images/
        ├── site-accueil-desktop.png
        ├── site-accueil-notes-tinydb.png
        ├── site-mes-creations.png
        ├── site-projets-jouables.png
        ├── site-menu-mobile-ouvert.png
        ├── admin-tableau-de-bord.png
        ├── admin-compte-lecture-seule.png
        ├── render-service-live.png
        ├── render-build-start-command.png
        ├── django-check.png
        ├── tinydb-demo-terminal.png
        ├── git-status-clean.png
        ├── code-tinydb-service.png
        ├── code-menu-js.png
        ├── sql-create-tables.png
        └── docs-structure.png
```

Le fichier `preuves-frostia-games.md` doit expliquer rapidement ce que chaque capture prouve.

Exemple :

```text
La capture montre que la commande python manage.py check ne détecte aucune erreur bloquante dans la configuration Django.
```

---

# 9. Relecture des documents

Avant le dossier final, relire les documents principaux.

Vérifier :

* cohérence des noms ;
* cohérence des chemins ;
* absence d'anciennes informations contradictoires ;
* absence de promesse trop ambitieuse ;
* absence de mot de passe ;
* absence de clé secrète ;
* absence de trace de brouillon ;
* absence de mention indiquant qu'une fonctionnalité est absente alors qu'elle a été ajoutée ;
* absence de mention indiquant qu'une fonctionnalité est faite alors qu'elle est seulement prévue.

---

## Points de vigilance

Les points suivants doivent être cohérents dans tous les documents :

| Sujet | Formulation correcte |
| ----- | -------------------- |
| TinyDB | Intégré comme expérimentation NoSQL légère |
| SQLite | Base principale de la V1 |
| PostgreSQL | Reporté |
| Compte lecture seule | Ajouté et limité |
| Admin personnalisée | Reportée |
| Upload serveur | Reporté |
| Jeu navigateur | Reporté |
| SQL natif | Documentaire |
| JavaScript | Menu mobile léger |
| Render | Déploiement en ligne |
| Tests automatisés | Reportés |
| Captures | À finaliser ou à intégrer |

---

# 10. Vérification du README

Le fichier `README.md` doit présenter rapidement :

* le nom du projet ;
* l'objectif ;
* les technologies ;
* l'installation locale ;
* les commandes de lancement ;
* le déploiement Render ;
* les limites de la V1.

Il doit éviter :

* les promesses trop larges ;
* les identifiants ;
* les secrets ;
* les informations contradictoires avec le dossier.

---

# 11. Vérification de `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` doit expliquer :

* pourquoi Django ;
* pourquoi SQLite ;
* pourquoi Render ;
* pourquoi Gunicorn ;
* pourquoi WhiteNoise ;
* pourquoi TinyDB est limité ;
* pourquoi PostgreSQL est reporté ;
* pourquoi certaines fonctionnalités sont reportées ;
* pourquoi le périmètre a été protégé.

Il doit montrer une réflexion technique, pas seulement une liste d’outils.

---

# 12. Vérification de la documentation complémentaire `docs/`

Le dossier `docs/` doit être cohérent.

Documents à vérifier :

```text
docs/conception/mcd.md
docs/conception/cas-utilisation.md
docs/conception/diagramme-sequence.md
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
docs/nosql/nosql.md
docs/frontend/javascript-menu-mobile.md
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

Vérifier que :

* les chemins sont corrects ;
* les fichiers existent ;
* les exemples SQL sont cohérents ;
* TinyDB est présenté comme expérimentation légère ;
* les diagrammes sont utiles ;
* les documents ne contiennent pas de secret.

---

# 13. Vérification Git et GitHub

Avant de finaliser :

```powershell
git status
```

Si des fichiers doivent être ajoutés :

```powershell
git add .
git commit -m "Finalize Frostia Games V1 documentation"
git push
```

Après le push :

```powershell
git status
```

Résultat attendu :

```text
nothing to commit, working tree clean
```

Vérifier sur GitHub :

* le dépôt est accessible ;
* la branche `main` contient les fichiers ;
* le dernier commit est visible ;
* aucun secret n'a été envoyé.

---

# 14. Vérification Render après push

Après un push final, vérifier Render.

À contrôler :

* le build démarre ;
* le build réussit ;
* le service devient live ;
* la page d’accueil s’affiche ;
* les pages principales fonctionnent ;
* l’administration reste accessible ;
* aucune variable sensible n’est visible publiquement.

Build Command :

```bash
bash build.sh
```

Start Command :

```bash
gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

---

# 15. Dernière relecture du dossier final

Avant export ou rendu final, relire le dossier projet.

À vérifier :

* introduction claire ;
* contexte clair ;
* objectifs clairs ;
* technologies présentées ;
* captures intégrées ;
* preuves cohérentes ;
* limites assumées ;
* évolutions futures réalistes ;
* conclusion propre ;
* absence de secret ;
* absence de texte incomplet ;
* absence de promesse trop ambitieuse.

Formulation à privilégier :

```text
Frostia Games est une V1 fonctionnelle, documentée, déployée et conçue pour évoluer progressivement.
```

Formulation à éviter :

```text
Frostia Games est une plateforme complète de gestion de projets de jeux vidéo.
```

---

# 16. Ordre conseillé de finalisation

Ordre recommandé :

1. relire les documents Markdown ;
2. vérifier les chemins et noms de fichiers ;
3. lancer `python manage.py check` ;
4. lancer `python -m scripts.demo_tinydb_notes` ;
5. vérifier le site local ;
6. vérifier le site Render ;
7. vérifier l’administration ;
8. vérifier le compte lecture seule ;
9. préparer les captures ;
10. ranger les captures dans `doc/preuves/images/` ;
11. compléter `preuves-frostia-games.md` ;
12. vérifier le README ;
13. vérifier `CHOIX_TECHNIQUES.md` ;
14. faire le dernier commit ;
15. vérifier GitHub ;
16. vérifier Render après le push ;
17. intégrer les captures au dossier final ;
18. relire le dossier final ;
19. exporter le dossier final si nécessaire.

---

# 17. Ce qu’il ne faut plus faire maintenant

À ce stade, il ne faut plus :

* ajouter une nouvelle grosse fonctionnalité ;
* changer d’architecture ;
* refaire le design complet ;
* migrer vers PostgreSQL ;
* ajouter MongoDB ;
* ajouter une API REST ;
* créer un espace privé complet ;
* ajouter un vrai upload serveur ;
* intégrer un jeu navigateur ;
* modifier trop fortement les modèles ;
* réécrire toute l’interface ;
* changer la structure du projet sans raison.

Ces actions peuvent attendre une version future.

La V1 doit rester stable.

---

# 18. Dernier contrôle qualité

Dernière checklist :

| Vérification | Statut |
| ------------ | ------ |
| Site local vérifié | À faire |
| Site Render vérifié | À faire |
| Admin Django vérifiée | À faire |
| Compte lecture seule vérifié | À faire |
| TinyDB testé | À faire |
| SQL natif vérifié | À faire |
| Menu mobile testé | À faire |
| README relu | À faire |
| Documentation relue | À faire |
| Captures préparées | À faire |
| Secrets absents des captures | À faire |
| Git propre | À faire |
| GitHub vérifié | À faire |
| Render vérifié après push | À faire |
| Dossier final relu | À faire |

Cette checklist doit être complétée progressivement.

---

# 19. Bilan de finalisation

La V1 de Frostia Games est déjà construite dans son périmètre.

Les dernières actions ne doivent pas transformer le projet.

Elles doivent seulement prouver, clarifier et sécuriser ce qui existe déjà.

La finalisation doit montrer :

* que le projet fonctionne ;
* que le projet est déployé ;
* que le projet est documenté ;
* que le projet est testé ;
* que le projet est cadré ;
* que les limites sont assumées ;
* que les évolutions futures sont réalistes.

Le projet doit rester présenté comme une V1 stable et évolutive, pas comme une plateforme complète.

---

# 20. Conclusion

Le plan de finalisation de Frostia Games consiste à terminer le dossier sans élargir inutilement le périmètre.

La priorité est maintenant :

```text
preuves
captures
relecture
cohérence
sécurité
commit final
dossier final
```

La V1 est suffisamment complète pour être défendue si elle est présentée clairement.

Les prochaines étapes doivent rester concentrées sur la qualité du rendu final, pas sur l'ajout de nouvelles fonctionnalités lourdes.
