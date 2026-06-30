-- ==========================================================
-- Exemples d'insertions SQL natives
-- Projet : Frostia Games
-- Objectif : montrer des exemples d'ajout de données
-- dans les tables principales du projet.
-- ==========================================================

-- Exemple d'insertion dans la table creations_creation
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
'Portfolio Django permettant de présenter des projets vidéoludiques.',
1,
CURRENT_TIMESTAMP,
CURRENT_TIMESTAMP
);

-- Exemple d'insertion dans la table playable_playableproject
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
'Aucune version jouable disponible actuellement.',
0,
1,
CURRENT_TIMESTAMP,
CURRENT_TIMESTAMP
);
