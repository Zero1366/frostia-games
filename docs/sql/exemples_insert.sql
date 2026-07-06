-- ============================================================
-- Exemples d'insertions SQL natives
-- Projet : Frostia Games
-- Fichier : exemples_insert.sql
-- Objectif : montrer des exemples d'ajout de données
-- dans les tables principales du projet.
-- ============================================================

--
-- Exemple d'insertion dans la table creations_creation
-- Cette table correspond au modèle Django Creation.
--
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
    'Frostia Games',
    'frostia-games',
    'F',
    'FROSTIA',
    'Portfolio Django',
    'V1 en développement',
    'Portfolio Django permettant de présenter les projets vidéoludiques et les futures créations.',
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

--
-- Exemple d'insertion dans la table playable_playableproject
-- Cette table correspond au modèle Django PlayableProject.
--
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
    'Prévu',
    'Démonstration',
    'Projet jouable prévu pour une future évolution du site.',
    'Aucune version jouable n’est disponible actuellement. Cette section prépare les futures démonstrations.',
    0,
    1,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- ============================================================
-- Remarque
-- ============================================================
-- Ces INSERT sont documentaires.
-- Dans le fonctionnement réel de la V1, les données sont
-- principalement gérées par Django ORM et par l'administration Django.
-- Ces exemples servent à démontrer la compréhension du SQL natif.