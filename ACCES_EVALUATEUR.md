# Accès évaluateur / jury — Frostia Games

Un accès temporaire de consultation est prévu pour permettre à l’évaluateur ou au jury de vérifier l’administration Django du projet **Frostia Games**.

Cet accès peut être utilisé uniquement si une preuve directe de l’espace d’administration est demandée.

Ce fichier doit rester dans un dépôt privé. Si le dépôt devient public, le compte devra être désactivé ou le mot de passe devra être changé.

---

## Site public

https://frostia-games.onrender.com/

---

## Administration Django

https://frostia-games.onrender.com/admin/

---

## Compte de consultation

Identifiant :

```text
evaluation_temp
```

Mot de passe :

```text
Lecture2026!
```

---

## Utilisation prévue

Ce compte est destiné à un accès de consultation pour l’évaluateur ou le jury.

Il permet de vérifier :

- l’accès à l’espace d’administration Django ;
- la présence des créations administrables ;
- la présence des projets jouables administrables ;
- la structure des contenus gérés depuis l’administration ;
- le fonctionnement général de la partie administration du projet ;
- la mise en place d’un accès limité en lecture seule.

---

## Limites de l’accès

Ce compte est prévu uniquement pour la consultation.

Il ne permet pas :

- d’ajouter du contenu ;
- de modifier du contenu ;
- de supprimer du contenu ;
- de gérer les utilisateurs ;
- de gérer les groupes ;
- de modifier les permissions ;
- d’accéder aux variables d’environnement ;
- d’accéder aux secrets du projet.

L’accès administrateur complet reste privé.

---

## Droits attendus

Le compte d’évaluation est configuré avec des droits limités.

```text
Utilisateur : evaluation_temp
Groupe : Evaluation lecture seule
Staff : oui
Superutilisateur : non
Droits : lecture seule
```

Permissions prévues :

```text
Can view Création
Can view Projet jouable
```

Permissions non prévues :

```text
Can add
Can change
Can delete
```

---

## Sécurité

Le mot de passe du compte d’évaluation est fourni côté Render par une variable d’environnement :

```text
EVALUATION_USER_PASSWORD
```

Le mot de passe présent dans ce fichier correspond à l’accès transmis pour l’évaluation.

Il ne doit pas être affiché dans les captures publiques du dossier projet.

---

## Durée de validité

Cet accès est temporaire.

Le compte sera désactivé, supprimé ou son mot de passe sera modifié après l’évaluation.