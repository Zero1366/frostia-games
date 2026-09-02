# Correspondance ORM Django → SQL natif — Frostia Games

## Objectif du document

Ce document montre, pour plusieurs requêtes réelles de l'application, le code Python écrit avec l'ORM Django et le SQL brut réellement exécuté sur la base SQLite. L'objectif est de démontrer la compréhension de ce que fait l'ORM en interne (jointures, agrégations, filtres).

Le SQL a été extrait avec `str(queryset.query)` après exécution des requêtes dans un shell Django (`python manage.py shell`), sur une base ayant appliqué la migration `0002_category_tag_creation_category_creation_tags`.

---

## 1. Nouveau modèle de données

Deux entités ont été ajoutées au modèle `Creation` pour donner un vrai sens relationnel au MCD :

| Entité | Relation avec `Creation` | Cardinalité |
| ------ | ------------------------- | ----------- |
| `Category` | Une catégorie regroupe plusieurs créations (ForeignKey sur `Creation`) | 1,n — 0,1 |
| `Tag` | Une création peut avoir plusieurs tags, un tag peut être utilisé par plusieurs créations (ManyToMany) | n,n |

### SQL généré par la migration (`sqlmigrate creations 0002`)

```sql
CREATE TABLE "creations_category" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(80) NOT NULL UNIQUE,
    "slug" varchar(100) NOT NULL UNIQUE
);

CREATE TABLE "creations_tag" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(50) NOT NULL UNIQUE
);

ALTER TABLE "creations_creation"
    ADD COLUMN "category_id" bigint NULL
    REFERENCES "creations_category" ("id") DEFERRABLE INITIALLY DEFERRED;

-- Table associative pour la relation N,N Creation <-> Tag
CREATE TABLE "creations_creation_tags" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "creation_id" bigint NOT NULL REFERENCES "creations_creation" ("id") DEFERRABLE INITIALLY DEFERRED,
    "tag_id" bigint NOT NULL REFERENCES "creations_tag" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE UNIQUE INDEX "creations_creation_tags_creation_id_tag_id_226c1fb8_uniq"
    ON "creations_creation_tags" ("creation_id", "tag_id");
```

La table `creations_creation_tags` est la table de jonction générée automatiquement par Django pour matérialiser la relation many-to-many : c'est le mécanisme SQL qu'utilise Merise pour représenter une association n,n (une table associative avec les deux clés étrangères).

---

## 2. Requête 1 — Filtrer sur une relation 1,N (`select_related`)

### But
Récupérer les créations visibles appartenant à la catégorie "Jeu vidéo", en récupérant la catégorie dans la même requête (évite une requête N+1).

### Code Python (ORM)

```python
Creation.objects.filter(
    is_visible=True,
    category__slug="jeu-video",
).select_related("category")
```

### SQL généré

```sql
SELECT
    creations_creation.id, creations_creation.category_id, creations_creation.title,
    creations_creation.slug, creations_creation.alphabet_letter, creations_creation.code_name,
    creations_creation.project_type, creations_creation.status, creations_creation.short_description,
    creations_creation.is_visible, creations_creation.created_at, creations_creation.updated_at,
    creations_category.id, creations_category.name, creations_category.slug
FROM creations_creation
INNER JOIN creations_category
    ON (creations_creation.category_id = creations_category.id)
WHERE (
    creations_category.slug = 'jeu-video'
    AND creations_creation.is_visible
)
ORDER BY creations_creation.alphabet_letter ASC, creations_creation.title ASC;
```

### Ce que ça démontre

- `category__slug="jeu-video"` traverse la relation ForeignKey et Django génère automatiquement un `INNER JOIN` vers `creations_category`.
- `select_related("category")` force Django à ramener les colonnes de `Category` dans la même requête SQL (au lieu de faire une 2e requête à chaque accès à `creation.category`).

---

## 3. Requête 2 — Filtrer sur une relation N,N (jointure via table associative)

### But
Récupérer les créations qui possèdent le tag "Prototype".

### Code Python (ORM)

```python
Creation.objects.filter(tags__name="Prototype").distinct()
```

### SQL généré

```sql
SELECT DISTINCT
    creations_creation.id, creations_creation.category_id, creations_creation.title,
    creations_creation.slug, creations_creation.alphabet_letter, creations_creation.code_name,
    creations_creation.project_type, creations_creation.status, creations_creation.short_description,
    creations_creation.is_visible, creations_creation.created_at, creations_creation.updated_at
FROM creations_creation
INNER JOIN creations_creation_tags
    ON (creations_creation.id = creations_creation_tags.creation_id)
INNER JOIN creations_tag
    ON (creations_creation_tags.tag_id = creations_tag.id)
WHERE creations_tag.name = 'Prototype'
ORDER BY creations_creation.alphabet_letter ASC, creations_creation.title ASC;
```

### Ce que ça démontre

- `tags__name="Prototype"` traverse la relation ManyToMany. Django doit passer par la **table associative** `creations_creation_tags` : on voit bien les **deux `INNER JOIN`** nécessaires (Creation → table de jonction → Tag).
- `.distinct()` est nécessaire côté ORM (et se traduit par `SELECT DISTINCT` en SQL) car une création avec plusieurs tags correspondants au filtre pourrait apparaître plusieurs fois à cause de la jointure.

---

## 4. Requête 3 — Agrégation (`Count` + `GROUP BY`)

### But
Compter le nombre de créations par catégorie.

### Code Python (ORM)

```python
from django.db.models import Count

Category.objects.annotate(nb_creations=Count("creations"))
```

### SQL généré

```sql
SELECT
    creations_category.id, creations_category.name, creations_category.slug,
    COUNT(creations_creation.id) AS nb_creations
FROM creations_category
LEFT OUTER JOIN creations_creation
    ON (creations_category.id = creations_creation.category_id)
GROUP BY creations_category.id, creations_category.name, creations_category.slug;
```

### Ce que ça démontre

- `annotate(Count(...))` traduit une agrégation SQL classique : `LEFT OUTER JOIN` (pour inclure les catégories sans création, avec un compte à 0) + `GROUP BY` sur toutes les colonnes non agrégées.
- Le `related_name="creations"` défini sur la ForeignKey (`category = models.ForeignKey(..., related_name="creations")`) est ce qui permet d'écrire `Count("creations")` depuis `Category`.

---

## 5. Conclusion

Ces trois exemples couvrent les trois mécanismes SQL les plus importants à maîtriser :

1. **Jointure simple (1,N)** via `ForeignKey` + `select_related`
2. **Jointure via table associative (N,N)** via `ManyToMany`
3. **Agrégation avec `GROUP BY`** via `annotate(Count(...))`

Dans les trois cas, l'ORM ne fait rien de magique : il traduit une intention exprimée en Python en une requête SQL standard, en gérant automatiquement les jointures nécessaires à partir des relations définies dans les modèles.