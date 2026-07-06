BEGIN;

--
-- Frostia Games
-- SQL natif documentaire
-- Fichier : create_tables_playable.sql
-- Table correspondant au modèle Django PlayableProject
-- Source réelle de création des tables : migrations Django
--

--
-- Create model PlayableProject
--
CREATE TABLE "playable_playableproject" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(120) NOT NULL,
    "slug" varchar(140) NOT NULL UNIQUE,
    "status" varchar(100) NOT NULL,
    "content_type" varchar(100) NOT NULL,
    "short_description" text NOT NULL,
    "availability_message" text NOT NULL,
    "is_available" bool NOT NULL,
    "is_visible" bool NOT NULL,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

--
-- Explication des champs
--
-- id                   : identifiant unique généré automatiquement.
-- title                : titre public du projet jouable.
-- slug                 : identifiant lisible utilisé dans les URL, unique.
-- status               : état d’avancement ou disponibilité du projet.
-- content_type         : type de contenu présenté, par exemple prototype, démo ou jeu à venir.
-- short_description    : description courte affichée sur le site.
-- availability_message : message indiquant si le projet est jouable ou prévu plus tard.
-- is_available         : indique si le projet est actuellement disponible.
-- is_visible           : indique si le projet est visible publiquement.
-- created_at           : date de création de l’entrée.
-- updated_at           : date de dernière modification.

COMMIT;