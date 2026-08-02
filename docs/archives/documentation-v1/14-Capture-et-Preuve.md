# Captures et preuves — Frostia Games

## Objectif du document

Ce document liste les captures et preuves retenues pour le projet **Frostia Games**.

Il sert de checklist de finalisation pour le dossier projet.  
L’objectif n’est pas d’accumuler toutes les captures possibles, mais de conserver les preuves utiles permettant de montrer que la V1 est :

- fonctionnelle ;
- documentée ;
- déployée en ligne ;
- vérifiable ;
- sécurisée au niveau de l’accès d’évaluation ;
- cohérente avec le périmètre annoncé.

Les preuves finales doivent privilégier la version en ligne Render :

```text
https://frostia-games.onrender.com
```

Les captures `localhost` ne sont pas utilisées comme preuves principales du dossier final.

---

# 1. Organisation retenue des preuves

Les preuves sont regroupées dans le dossier :

```text
docs/preuves/
```

Organisation recommandée :

```text
docs/preuves/
├── admin/
├── render/
├── site/
├── mobile/
├── sql/
├── nosql/
├── js/
├── backend/
├── tests/
└── github/
```

Cette organisation permet de séparer les captures par thème et de faciliter la lecture du dossier projet.

Le dossier `docs/preuves/admin/` contient les captures liées à l’administration Django en ligne et au compte d’évaluation.

---

# 2. Règles de sécurité des captures

Avant d’ajouter une capture dans le projet, il faut vérifier qu’elle ne montre pas d’information sensible.

Ne pas afficher :

- mot de passe ;
- clé secrète Django ;
- valeur de `DJANGO_SECRET_KEY` ;
- valeur de `DJANGO_SUPERUSER_PASSWORD` ;
- valeur de `EVALUATION_USER_PASSWORD` ;
- jeton privé ;
- clé API ;
- vraie valeur complète de variable d’environnement ;
- information personnelle inutile.

Les captures Render peuvent montrer les **noms** des variables d’environnement, mais pas leurs valeurs.

Les identifiants d’évaluation peuvent être transmis séparément si nécessaire, mais ils ne doivent pas être affichés dans une capture.

---

# 3. Règle des trois preuves

Pour chaque compétence importante, le dossier doit si possible montrer trois éléments :

| Élément | Rôle |
| ------ | ---- |
| Code ou extrait technique | Montrer que la fonctionnalité est réellement développée |
| Explication | Montrer la compréhension du fonctionnement |
| Rendu ou vérification | Montrer que le résultat fonctionne |

Exemples :

| Sujet | Code | Explication | Preuve visible |
| ----- | ---- | ----------- | -------------- |
| Modèles Django | `creations/models.py`, `playable/models.py` | `docs/backend/modeles-django.md` | Admin ou page publique |
| SQL natif | `docs/sql/*.sql` | `docs/sql/sql-natif.md` | Capture des fichiers SQL |
| TinyDB | `core/services/nosql_notes.py` | `docs/nosql/tinydb-integration.md` | Notes affichées ou terminal |
| JavaScript | `static/js/menu.js` | `docs/frontend/javascript-menu-mobile.md` | Menu mobile ouvert |
| Déploiement | `build.sh`, Render | `doc/09-deploiement-render.md` | Site en ligne et logs Render |

---

# 4. Captures prioritaires finales

Les captures prioritaires sont celles qui doivent être conservées pour le dossier final.

## 4.1 Site public Render

Dossier conseillé :

```text
docs/preuves/site/
```

Captures conseillées :

```text
capture-site-accueil-render.png
capture-site-mes-creations-render.png
capture-site-projets-jouables-render.png
```

Ces captures montrent :

- l’URL Render ;
- l’interface publique ;
- les pages principales ;
- les données affichées ;
- le rendu général du site.

---

## 4.2 Administration Django Render

Dossier conseillé :

```text
docs/preuves/admin/
```

Captures conseillées :

```text
capture-admin-evaluation-accueil-render.png
capture-admin-evaluation-creations-render.png
capture-admin-evaluation-projets-jouables-render.png
capture-admin-evaluation-compte-render.png
```

Ces captures montrent :

- l’accès à l’administration Django en ligne ;
- le compte `evaluation_temp` connecté ;
- la présence des créations ;
- la présence des projets jouables ;
- les droits limités à la lecture seule ;
- l’absence de super-utilisateur sur le compte d’évaluation.

Les captures ne doivent pas montrer le mot de passe.

---

## 4.3 Déploiement Render

Dossier conseillé :

```text
docs/preuves/render/
```

Captures conseillées :

```text
capture-render-service-live.png
capture-render-start-command.png
capture-render-logs-setup-render-data.png
capture-render-variables-masquees.png
```

Ces captures montrent :

- le service Render actif ;
- la branche `main` utilisée ;
- le Build Command ;
- le Start Command ;
- les logs de déploiement ;
- l’exécution de `setup_render_data` ;
- les variables d’environnement sans afficher leurs valeurs.

Le Start Command actuel est :

```bash
python manage.py migrate --noinput && python manage.py setup_render_data && gunicorn frostia_config.wsgi:application --bind 0.0.0.0:$PORT
```

Cette commande permet de relancer les migrations, de recréer les données nécessaires à la démonstration, puis de démarrer l’application.

---

## 4.4 SQL natif

Dossier conseillé :

```text
docs/preuves/sql/
```

Captures ou fichiers concernés :

```text
docs/sql/create_tables_creations.sql
docs/sql/create_tables_playable.sql
docs/sql/exemples_insert.sql
docs/sql/sql-natif.md
```

Ces preuves montrent :

- les extraits `CREATE TABLE` ;
- les exemples `INSERT INTO` ;
- le lien entre l’ORM Django et le SQL natif ;
- la compétence base de données relationnelle.

---

## 4.5 NoSQL / TinyDB

Dossier conseillé :

```text
docs/preuves/nosql/
```

Captures ou fichiers concernés :

```text
core/services/nosql_notes.py
scripts/demo_tinydb_notes.py
data/nosql/project_notes_db.json
docs/nosql/tinydb-integration.md
```

Commande de vérification :

```powershell
python -m scripts.demo_tinydb_notes
```

Ces preuves montrent :

- l’utilisation de TinyDB ;
- une structure JSON ;
- une démonstration NoSQL légère ;
- l’affichage ou la lecture de notes de progression.

TinyDB ne remplace pas SQLite.  
Il sert uniquement de démonstration NoSQL contrôlée dans le périmètre de la V1.

---

## 4.6 JavaScript mobile

Dossier conseillé :

```text
docs/preuves/js/
```

Captures ou fichiers concernés :

```text
static/js/menu.js
docs/frontend/javascript-menu-mobile.md
```

Captures conseillées :

```text
capture-menu-mobile-ferme.png
capture-menu-mobile-ouvert.png
capture-code-menu-js.png
```

Ces preuves montrent :

- l’existence d’un JavaScript dynamique ;
- le fonctionnement du menu mobile ;
- l’utilisation d’événements ;
- la modification de classes CSS ;
- la prise en compte de `aria-expanded`.

---

## 4.7 Backend Django

Dossier conseillé :

```text
docs/preuves/backend/
```

Captures ou fichiers concernés :

```text
creations/models.py
playable/models.py
creations/admin.py
playable/admin.py
core/views.py
docs/backend/modeles-django.md
docs/backend/vues-et-routes.md
```

Ces preuves montrent :

- les modèles Django ;
- la configuration de l’administration ;
- les vues ;
- la liaison entre base de données, vues et templates.

---

## 4.8 Validation technique

Dossier conseillé :

```text
docs/preuves/tests/
```

Captures conseillées :

```text
capture-manage-check.png
capture-git-status-clean.png
```

Commandes :

```powershell
python manage.py check
git status
```

Résultats attendus :

```text
System check identified no issues
nothing to commit, working tree clean
```

Ces captures prouvent que le projet est vérifié et sauvegardé proprement.

---

# 5. Captures optionnelles

Certaines captures peuvent renforcer le dossier, mais ne sont pas obligatoires si le temps est limité.

Captures optionnelles :

- maquettes Figma ;
- structure complète du projet dans VS Code ;
- dossier `doc/` ;
- dossier `docs/`;
- dépôt GitHub ;
- Docker ;
- responsive mobile supplémentaire ;
- documentation Render ;
- bilan V1.

Ces éléments peuvent être ajoutés si le dossier final manque de preuves visuelles, mais ils ne doivent pas faire perdre de temps si les captures prioritaires sont déjà suffisantes.

---

# 6. Captures non nécessaires pour la V1

Les captures suivantes ne sont pas nécessaires, car ces fonctionnalités ne font pas partie du périmètre actuel :

- PostgreSQL ;
- MongoDB en production ;
- API REST ;
- espace utilisateur public ;
- upload serveur réel ;
- jeu jouable dans le navigateur ;
- système de score ;
- page détail complète ;
- interface d’administration personnalisée ;
- Plotly.js intégré.

Ces éléments sont documentés comme pistes futures, mais ils ne doivent pas être présentés comme des fonctionnalités réalisées.

---

# 7. Captures Render et base de données

Une difficulté a été rencontrée avec les données créées manuellement dans l’administration Render.

Sur l’offre gratuite utilisée, la base SQLite en ligne peut être réinitialisée après certains redémarrages ou redéploiements.

Pour éviter que l’administration en ligne redevienne vide, une commande Django personnalisée a été ajoutée :

```bash
python manage.py setup_render_data
```

Cette commande recrée automatiquement :

- la création principale `Frostia Games` ;
- le projet jouable de démonstration ;
- le groupe `Evaluation lecture seule` ;
- le compte `evaluation_temp` ;
- les permissions de lecture seule.

Cette correction doit être montrée dans les preuves Render si possible, notamment avec une capture des logs où apparaissent :

```text
Données initiales créées.
Accès d'évaluation configuré.
Utilisateur : evaluation_temp
Droits : lecture seule
```

---

# 8. Statut des preuves finales

Tableau de suivi simplifié :

| Preuve | Priorité | Statut |
| ------ | -------- | ------ |
| Site Render — accueil | Haute | À ajouter si non présent |
| Site Render — Mes créations | Haute | À ajouter si non présent |
| Site Render — Projets jouables | Haute | À ajouter si non présent |
| Admin Render — accueil evaluation_temp | Haute | À ajouter si non présent |
| Admin Render — Créations lecture seule | Haute | À ajouter si non présent |
| Admin Render — Projets jouables lecture seule | Haute | À ajouter si non présent |
| Render — logs `setup_render_data` | Haute | À ajouter si non présent |
| SQL natif | Haute | Déjà documenté, capture à conserver |
| TinyDB | Haute | Déjà documenté, capture à conserver |
| JavaScript menu mobile | Haute | Déjà documenté, capture à conserver |
| `python manage.py check` | Haute | À conserver |
| `git status` propre | Haute | À faire après commit final |

---

# 9. Vérification avant commit des captures

Avant de faire le commit final, vérifier :

```powershell
git status
```

Puis ajouter les preuves :

```powershell
git add docs/preuves
git commit -m "Ajout captures finales Render"
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

# 10. Bilan

Les captures et preuves doivent montrer que Frostia Games est une V1 Django fonctionnelle, déployée et documentée.

Les points principaux à prouver sont :

- site public en ligne ;
- administration Django en ligne ;
- compte d’évaluation en lecture seule ;
- données automatiquement recréées sur Render ;
- backend Django ;
- SQL natif ;
- TinyDB ;
- JavaScript mobile ;
- documentation ;
- dépôt Git propre.

Ce document sert de checklist finale.  
Il doit rester pratique, clair et aligné avec l’état réel du projet.
