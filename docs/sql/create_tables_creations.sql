BEGIN;

--
-- Frostia Games
-- SQL natif documentaire
-- Fichier : create_tables_creations.sql
-- Table correspondant au modèle Django Creation
-- Source réelle de création des tables : migrations Django
--

--
-- Create model Creation
--
CREATE TABLE "creations_creation" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(120) NOT NULL,
    "slug" varchar(140) NOT NULL UNIQUE,
    "alphabet_letter" varchar(1) NOT NULL,
    "code_name" varchar(120) NOT NULL,
    "project_type" varchar(100) NOT NULL,
    "status" varchar(100) NOT NULL,
    "short_description" text NOT NULL,
    "is_visible" bool NOT NULL,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

--
-- Explication des champs
--
-- id                : identifiant unique généré automatiquement.
-- title             : titre public de la création.
-- slug              : identifiant lisible utilisé dans les URL, unique.
-- alphabet_letter   : première lettre utilisée pour le classement alphabétique.
-- code_name         : nom de code interne du projet.
-- project_type      : type de projet présenté.
-- status            : état d’avancement du projet.
-- short_description : description courte affichée sur le site.
-- is_visible        : indique si la création est visible publiquement.
-- created_at        : date de création de l’entrée.
-- updated_at        : date de dernière modification.

COMMIT;