BEGIN;
--
-- Create model PlayableProject
--
CREATE TABLE "playable_playableproject" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(120) NOT NULL, "slug" varchar(140) NOT NULL UNIQUE, "status" varchar(100) NOT NULL, "content_type" varchar(100) NOT NULL, "short_description" text NOT NULL, "availability_message" text NOT NULL, "is_available" bool NOT NULL, "is_visible" bool NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
COMMIT;
