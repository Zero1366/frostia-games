# Parcours utilisateur — Frostia Games

## 1. Objectif

Le parcours utilisateur décrit la manière dont un visiteur navigue entre les différentes pages de Frostia Games.

Le parcours a volontairement été conçu pour rester simple, direct et adapté à un portfolio.

---

## 2. Point d’entrée

Le visiteur arrive sur la page d’accueil.

Cette page lui permet de :

- comprendre rapidement l’objectif du site ;
- découvrir l’identité Frostia Games ;
- accéder aux créations ;
- accéder aux projets jouables ;
- consulter l’état d’avancement du projet.

---

## 3. Parcours principal

```text
Page d’accueil
      |
      +--> Mes créations
      |
      +--> Projets jouables
```

Le visiteur peut revenir à la page d’accueil depuis la navigation principale.

---

## 4. Parcours desktop

Sur ordinateur, la navigation est affichée dans une barre latérale.

Le visiteur peut accéder directement à :

- Accueil ;
- Mes créations ;
- Projets jouables.

La barre latérale reste visuellement séparée de la zone de contenu.

---

## 5. Parcours mobile

Sur smartphone, la navigation est adaptée afin de réduire l’espace occupé.

Le parcours reste identique, mais l’affichage du menu est modifié :

1. le visiteur ouvre le menu ;
2. il sélectionne une page ;
3. le contenu demandé s’affiche ;
4. il peut rouvrir le menu pour changer de page.

---

## 6. Parcours administrateur

L’administration n’est pas accessible depuis la navigation publique.

```text
Page de connexion Django Admin
            |
            v
     Authentification
            |
            v
   Interface d’administration
            |
            v
     Gestion des contenus
```

L’accès est réservé à l’administrateur.

---

## 7. Cas d’utilisation principaux

### Consulter la page d’accueil

**Acteur :** visiteur  
**Objectif :** comprendre le rôle du site et accéder aux différentes rubriques.

### Consulter les créations

**Acteur :** visiteur  
**Objectif :** découvrir les projets et créations présentés.

### Consulter les projets jouables

**Acteur :** visiteur  
**Objectif :** accéder aux projets disponibles ou annoncés comme jouables.

### Administrer les contenus

**Acteur :** administrateur  
**Objectif :** gérer les données prévues par l’application à travers l’interface Django Admin.

---

## 8. Principes ergonomiques

- limiter le nombre de niveaux de navigation ;
- utiliser des intitulés compréhensibles ;
- conserver les mêmes repères visuels sur toutes les pages ;
- éviter les actions inutiles ;
- maintenir une navigation accessible sur desktop et mobile ;
- permettre un retour rapide à l’accueil.

---

## 9. Schéma à intégrer

```text
                    +------------------+
                    |     ACCUEIL      |
                    +------------------+
                      /              \
                     /                \
        +------------------+   +-------------------+
        | MES CRÉATIONS    |   | PROJETS JOUABLES |
        +------------------+   +-------------------+
```

Chemin conseillé pour la preuve :

```text
docs/preuves/conception/parcours-utilisateur.png
```

---

## 10. Vérification du parcours

Le parcours doit être vérifié sur :

- ordinateur ;
- tablette ;
- smartphone.

Points à contrôler :

- tous les liens fonctionnent ;
- la page active est identifiable ;
- aucun contenu n’est inaccessible ;
- aucun défilement horizontal indésirable n’apparaît ;
- le menu mobile reste utilisable ;
- le retour à l’accueil fonctionne.

---

## 11. Conclusion

Le parcours utilisateur de Frostia Games est volontairement simple.

Il permet au visiteur d’accéder rapidement aux informations principales tout en conservant une navigation cohérente sur les différents formats d’écran.
