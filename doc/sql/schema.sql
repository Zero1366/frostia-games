-- ============================================================
-- Schéma SQL documentaire - Frostia Games
-- Projet Django / SQLite
-- ============================================================
--
-- Ce fichier présente l'équivalent SQL simplifié des tables
-- utilisées dans la V1 du projet Frostia Games.
--
-- Dans le projet réel, les tables sont générées par Django
-- à partir des modèles Python et des migrations.
--
-- Fichier à but documentaire pour le dossier projet.
-- ============================================================


-- ============================================================
-- TABLE : creations_creation
-- Rôle :
-- Stocke les créations et projets présentés dans la page
-- "Mes créations".
-- ============================================================

CREATE TABLE creations_creation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title VARCHAR(120) NOT NULL,
    slug VARCHAR(140) NOT NULL UNIQUE,
    alphabet_letter VARCHAR(1) NOT NULL,
    code_name VARCHAR(120) NOT NULL,

    project_type VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL,
    short_description TEXT NOT NULL,

    is_visible BOOLEAN NOT NULL DEFAULT 1,

    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);


-- ============================================================
-- TABLE : playable_playableproject
-- Rôle :
-- Stocke les futurs projets jouables, vidéos, teasers ou
-- prototypes prévus dans la page "Projets jouables".
-- ============================================================

CREATE TABLE playable_playableproject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title VARCHAR(120) NOT NULL,
    slug VARCHAR(140) NOT NULL UNIQUE,

    status VARCHAR(100) NOT NULL,
    content_type VARCHAR(100) NOT NULL,
    short_description TEXT NOT NULL,
    availability_message TEXT NOT NULL,

    is_available BOOLEAN NOT NULL DEFAULT 0,
    is_visible BOOLEAN NOT NULL DEFAULT 1,

    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);


-- ============================================================
-- DONNÉE D'EXEMPLE : creations_creation
-- Rôle :
-- Exemple d'insertion d'une création visible sur le site.
-- ============================================================

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
)
VALUES (
    'KryonCore',
    'kryoncore',
    'K',
    'KryonCore',
    'Jeu vidéo PC',
    'En préparation',
    'Projet de jeu vidéo servant de base à mes recherches techniques et créatives.',
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);


-- ============================================================
-- DONNÉE D'EXEMPLE : playable_playableproject
-- Rôle :
-- Exemple d'insertion d'un futur projet jouable non disponible.
-- ============================================================

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
)
VALUES (
    'Prototype jouable à venir',
    'prototype-jouable-a-venir',
    'Non disponible',
    'Démonstration / teaser',
    'Espace prévu pour accueillir plus tard une vidéo, un teaser ou une démonstration jouable.',
    'Aucun projet jouable n’est encore disponible dans cette V1.',
    0,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);