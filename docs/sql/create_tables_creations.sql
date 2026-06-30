BEGIN;
--
-- Create model Creation
--
CREATE TABLE "creations_creation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(120) NOT NULL, "slug" varchar(140) NOT NULL UNIQUE, "alphabet_letter" varchar(1) NOT NULL, "code_name" varchar(120) NOT NULL, "project_type" varchar(100) NOT NULL, "status" varchar(100) NOT NULL, "short_description" text NOT NULL, "is_visible" bool NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
COMMIT;
