# Plan de finalisation V1 — Frostia Games

## Objectif du document

Ce document présente le plan de finalisation de la V1 du projet **Frostia Games**.

À ce stade, le projet ne doit plus être élargi avec de grosses fonctionnalités. La priorité est de finaliser :

- la documentation ;
- les captures ;
- les preuves ;
- les annexes ;
- la relecture ;
- la cohérence générale ;
- le dernier commit Git ;
- la vérification finale du rendu.

Ce plan sert à éviter de repartir dans du développement supplémentaire alors que la V1 est déjà fonctionnelle, documentée et déployée.

---

# 1. État actuel de la V1

La V1 est considérée comme fonctionnelle dans son périmètre.

Elle contient déjà :

- un projet Django fonctionnel ;
- trois pages publiques principales ;
- une base SQLite ;
- des modèles Django ;
- une administration Django ;
- un affichage dynamique des créations et projets jouables ;
- un menu mobile JavaScript ;
- une expérimentation TinyDB ;
- un affichage de notes TinyDB sur l’accueil ;
- des fichiers SQL natifs documentaires ;
- une documentation technique et de conception ;
- un déploiement Render ;
- une commande `setup_render_data` pour recréer les données en ligne ;
- un compte d’évaluation en lecture seule ;
- des preuves organisées dans `docs/preuves/`.

La priorité n’est donc plus d’ajouter des fonctionnalités, mais de rendre l’ensemble clair, propre et défendable.

---

# 2. Périmètre à ne plus dépasser

Les éléments suivants ne doivent pas être ajoutés maintenant :

- PostgreSQL ;
- MongoDB ;
- interface d’administration personnalisée ;
- upload serveur réel ;
- jeu jouable dans le navigateur ;
- API REST ;
- espace privé complet ;
- graphiques Plotly.js ;
- mini-jeu intégré ;
- système de score ;
- système de sauvegarde avancé ;
- refonte graphique complète ;
- tests automatisés complets.

Ces éléments peuvent rester dans la roadmap, mais ils ne doivent pas bloquer la finalisation de la V1.

---

# 3. Actions déjà réalisées

## Projet Django

| Élément | État |
| ------- | ---- |
| Projet Django | Terminé |
| Applications `core`, `creations`, `playable` | Terminées |
| Templates principaux | En place |
| Fichiers statiques | En place |
| Menu mobile JavaScript | Fonctionnel |
| Routes et vues principales | En place |

## Backend et données

| Élément | État |
| ------- | ---- |
| Modèle `Creation` | Fonctionnel |
| Modèle `PlayableProject` | Fonctionnel |
| Base SQLite | Fonctionnelle pour la V1 |
| Administration Django | Fonctionnelle |
| Compte d’évaluation lecture seule | Fonctionnel |
| SQL natif documentaire | En place |

## TinyDB

| Élément | État |
| ------- | ---- |
| Service `nosql_notes.py` | En place |
| Script `demo_tinydb_notes.py` | En place |
| Base JSON TinyDB | En place |
| Affichage sur l’accueil | En place |
| Documentation NoSQL | En place |

## Render

| Élément | État |
| ------- | ---- |
| Site Render | En ligne |
| Build Command | En place |
| Start Command | En place |
| Gunicorn | En place |
| WhiteNoise | En place |
| Variables d’environnement | En place |
| Initialisation automatique | En place avec `setup_render_data` |

URL de production :

```text
https://frostia-games.onrender.com
```

---

# 4. Fichiers importants à vérifier

Vérifier que les fichiers suivants existent et correspondent à l’état actuel du projet :

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

Fichiers techniques importants :

```text
core/views.py
core/services/nosql_notes.py
core/management/commands/setup_render_data.py
scripts/demo_tinydb_notes.py
static/js/menu.js
templates/partials/base.html
templates/pages/home.html
templates/pages/creation.html
templates/pages/projet_jouable.html
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

# 5. Commandes techniques à lancer

Avant le commit final :

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

Si `git status` n’est pas propre, il faut vérifier les fichiers modifiés, puis faire un commit final.

---

# 6. Vérification du site en ligne

Pages à tester :

```text
https://frostia-games.onrender.com
https://frostia-games.onrender.com/mes-creations/
https://frostia-games.onrender.com/projets-jouables/
https://frostia-games.onrender.com/admin/
```

À vérifier :

- la page d’accueil se charge ;
- les notes TinyDB apparaissent si elles sont prévues ;
- les pages publiques fonctionnent ;
- le CSS est chargé ;
- le menu mobile fonctionne ;
- l’administration Django est accessible ;
- aucune erreur serveur n’apparaît.

---

# 7. Vérification de l’administration

Avec le compte administrateur :

- connexion possible ;
- modèles visibles ;
- création consultable ;
- projet jouable consultable ;
- données cohérentes.

Avec le compte d’évaluation en lecture seule :

- connexion possible ;
- accès limité ;
- consultation des créations ;
- consultation des projets jouables ;
- absence d’accès aux utilisateurs ;
- absence d’accès aux groupes ;
- absence de droit d’ajout ;
- absence de droit de modification ;
- absence de droit de suppression.

Les identifiants ne doivent pas être affichés dans les captures publiques.

---

# 8. Captures à préparer

## Site public

- page d’accueil desktop ;
- page d’accueil avec notes TinyDB ;
- page Mes créations ;
- page Projets jouables ;
- page mobile ;
- menu mobile ouvert.

## Administration Django

- page de connexion admin ;
- tableau de bord admin ;
- liste des créations ;
- liste des projets jouables ;
- compte d’évaluation en lecture seule ;
- preuve de limitation des droits.

## Render

- service Render actif ;
- logs indiquant que le service est live ;
- logs montrant `setup_render_data` ;
- Build Command ;
- Start Command ;
- variables d’environnement masquées.

## Technique

- `python manage.py check` ;
- `python -m scripts.demo_tinydb_notes` ;
- `git status` propre ;
- dépôt GitHub ;
- structure du projet dans VS Code.

## Code

- modèles Django ;
- vues Django ;
- fichiers `admin.py` ;
- service TinyDB ;
- script TinyDB ;
- fichier `menu.js` ;
- fichiers SQL natifs ;
- fichier `build.sh` ;
- fichier `setup_render_data.py`.

---

# 9. Règles de sécurité pour les captures

Aucune capture ne doit afficher :

- mot de passe ;
- clé secrète Django ;
- vraie valeur de variable d’environnement ;
- valeur de `DJANGO_SECRET_KEY` ;
- valeur de `DJANGO_SUPERUSER_PASSWORD` ;
- valeur de `EVALUATION_USER_PASSWORD` ;
- token ;
- clé API ;
- information personnelle inutile.

Les captures Render peuvent montrer les noms des variables, mais pas leurs valeurs.

---

# 10. Organisation des preuves

Organisation actuelle recommandée :

```text
docs/preuves/
├── admin/
├── js/
├── nosql/
├── render/
├── sql/
└── test/
```

Document principal d’index :

```text
PREUVES-FONCTIONNEMENT.md
```

Exemples de noms de captures :

```text
capture-admin-evaluation-accueil-render.png
capture-admin-evaluation-creations-render.png
capture-admin-evaluation-projets-jouables-render.png
capture-render-logs-setup-render-data.png
capture-site-accueil-render.png
capture-manage-check.png
capture-git-status-clean.png
```

---

# 11. Relecture documentaire

Avant le dossier final, vérifier :

- cohérence des noms ;
- cohérence des chemins ;
- absence d’anciennes informations contradictoires ;
- absence de promesse trop ambitieuse ;
- absence de mot de passe ;
- absence de clé secrète ;
- absence de brouillon ;
- absence de doublons inutiles.

Points à garder cohérents :

| Sujet | Formulation correcte |
| ----- | -------------------- |
| TinyDB | Expérimentation NoSQL légère |
| SQLite | Base principale de la V1 |
| SQLite sur Render | Stabilisé par `setup_render_data`, mais pas persistance durable avancée |
| PostgreSQL | Reporté |
| Compte d’évaluation | Ajouté, fonctionnel et limité |
| Admin personnalisée | Reportée |
| Upload serveur | Reporté |
| Jeu navigateur | Reporté |
| SQL natif | Documentaire |
| JavaScript | Menu mobile léger |
| Render | Déploiement en ligne |
| Preuves | Rangées dans `docs/preuves/` |

---

# 12. Vérification du README

Le fichier `README.md` doit présenter :

- le nom du projet ;
- l’objectif ;
- les technologies ;
- l’installation locale ;
- les commandes de lancement ;
- le déploiement Render ;
- l’initialisation automatique avec `setup_render_data` ;
- les limites de la V1.

Il ne doit pas contenir :

- mot de passe ;
- secret ;
- promesse trop large ;
- information contradictoire avec le dossier.

---

# 13. Vérification de `CHOIX_TECHNIQUES.md`

Le fichier `CHOIX_TECHNIQUES.md` doit expliquer :

- pourquoi Django ;
- pourquoi SQLite ;
- pourquoi Render ;
- pourquoi Gunicorn ;
- pourquoi WhiteNoise ;
- pourquoi TinyDB reste limité ;
- pourquoi PostgreSQL est reporté ;
- pourquoi le périmètre a été protégé.

Il doit montrer une réflexion technique, pas seulement une liste d’outils.

---

# 14. Vérification de `docs/`

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
docs/nosql/structure-nosql.md
docs/nosql/tinydb-integration.md
docs/frontend/javascript-menu-mobile.md
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

Vérifier que :

- les chemins sont corrects ;
- les fichiers existent ;
- les exemples SQL sont cohérents ;
- TinyDB est présenté comme expérimentation légère ;
- les documents ne contiennent pas de secret.

---

# 15. Vérification Git et GitHub

Avant de finaliser :

```powershell
git status
```

Si des fichiers doivent être ajoutés :

```powershell
git add .
git commit -m "Finalise documentation V1 Frostia Games"
git push origin main
```

Après le push :

```powershell
git status
```

Résultat attendu :

```text
nothing to commit, working tree clean
```

---

# 16. Vérification Render après push

Après un push final, vérifier Render.

Build Command :

```bash
bash build.sh
```

Start Command :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

À contrôler :

- le build démarre ;
- le service devient live ;
- la page d’accueil s’affiche ;
- les pages principales fonctionnent ;
- l’administration reste accessible ;
- le compte d’évaluation fonctionne ;
- aucune variable sensible n’est visible publiquement.

---

# 17. Ordre conseillé de finalisation

Ordre recommandé :

1. relire les documents Markdown ;
2. vérifier les chemins et noms de fichiers ;
3. lancer `python manage.py check` ;
4. lancer `python -m scripts.demo_tinydb_notes` ;
5. vérifier le site local ;
6. vérifier le site Render ;
7. vérifier l’administration ;
8. vérifier le compte d’évaluation ;
9. préparer les captures ;
10. ranger les captures dans `docs/preuves/` ;
11. vérifier `PREUVES-FONCTIONNEMENT.md` ;
12. vérifier le README ;
13. vérifier `CHOIX_TECHNIQUES.md` ;
14. faire le dernier commit ;
15. vérifier GitHub ;
16. vérifier Render après le push ;
17. intégrer les captures au dossier final ;
18. relire le dossier final ;
19. exporter le dossier final si nécessaire.

---

# 18. Ce qu’il ne faut plus faire maintenant

À ce stade, il ne faut plus :

- ajouter une nouvelle grosse fonctionnalité ;
- changer d’architecture ;
- refaire le design complet ;
- migrer vers PostgreSQL ;
- ajouter MongoDB ;
- ajouter une API REST ;
- créer un espace privé complet ;
- ajouter un vrai upload serveur ;
- intégrer un jeu navigateur ;
- modifier trop fortement les modèles ;
- réécrire toute l’interface.

Ces actions peuvent attendre une version future.

La V1 doit rester stable.

---

# 19. Checklist finale

| Vérification | Statut |
| ------------ | ------ |
| Site local vérifié | À faire |
| Site Render vérifié | À faire |
| Admin Django vérifiée | À faire |
| Compte d’évaluation vérifié | À faire |
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

---

# 20. Conclusion

La V1 de Frostia Games est déjà construite dans son périmètre.

Les dernières actions ne doivent pas transformer le projet.

Elles doivent seulement prouver, clarifier et sécuriser ce qui existe déjà.

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

Les prochaines étapes doivent rester concentrées sur la qualité du rendu final, pas sur l’ajout de nouvelles fonctionnalités lourdes.
