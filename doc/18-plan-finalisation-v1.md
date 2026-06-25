# Plan de finalisation V1 - Frostia Games

## Objectif du document

Ce document présente le plan de finalisation de la V1 du projet **Frostia Games**.

L'objectif est de définir clairement les dernières actions à réaliser avant de considérer la V1 comme terminée, présentable et défendable.

Ce document sert aussi à éviter d'ajouter de nouvelles fonctionnalités inutiles à la fin du projet.

La priorité est maintenant de finaliser, vérifier, capturer, relire et stabiliser.

---

## État actuel de la V1

Le projet Frostia Games dispose actuellement :

* d'un projet Django fonctionnel ;
* d'une interface publique ;
* de pages principales ;
* d'une base SQLite ;
* d'une administration Django ;
* d'un affichage dynamique ;
* d'un déploiement Render fonctionnel ;
* d'une documentation technique complète ;
* d'une réflexion sur les limites et évolutions ;
* d'une liste de pistes explorées et reportées.

La V1 est donc déjà exploitable comme base de présentation.

---

## Objectif de la finalisation

La finalisation ne consiste pas à ajouter de nouvelles grosses fonctionnalités.

Elle consiste à rendre le projet :

* propre ;
* stable ;
* lisible ;
* cohérent ;
* documenté ;
* présentable ;
* vérifiable ;
* prêt à être montré.

L'objectif est de passer d'une V1 fonctionnelle à une V1 correctement finalisée.

---

## Règle principale

À partir de cette étape, aucune nouvelle fonctionnalité importante ne doit être ajoutée.

Les éléments suivants sont reportés :

* PostgreSQL ;
* compte jury temporaire ;
* administration personnalisée ;
* upload serveur réel ;
* jeu jouable dans le navigateur ;
* graphiques Plotly.js ;
* espace privé complet ;
* système de sauvegarde automatique ;
* tests automatisés complets.

Ces fonctionnalités sont documentées comme pistes futures, mais elles ne font pas partie de la finalisation de la V1.

---

## Étape 1 - Vérification du contenu des pages

## Objectif

Relire les pages principales du site pour vérifier que le contenu est clair, cohérent et adapté à une V1.

## Pages à vérifier

* Accueil ;
* Mes créations ;
* Projets jouables à venir.

## Points à contrôler

* pas de texte provisoire inutile ;
* pas de phrase trop vague ;
* pas de promesse excessive ;
* pas de faute trop visible ;
* titres clairs ;
* textes courts ;
* contenu honnête sur l'état du projet ;
* distinction claire entre ce qui existe et ce qui est prévu.

## Statut

```txt
À faire
```

---

## Étape 2 - Vérification du responsive

## Objectif

Contrôler que le site reste consultable sur mobile.

## Points à vérifier

* pas de débordement horizontal important ;
* menu mobile utilisable ;
* textes lisibles ;
* cartes correctement empilées ;
* boutons accessibles ;
* sections lisibles ;
* espacement correct.

## Résultat attendu

Le responsive n'a pas besoin d'être parfait, mais il doit être suffisamment propre pour une V1.

## Statut

```txt
À faire
```

---

## Étape 3 - Captures d'écran

## Objectif

Préparer les preuves visuelles du fonctionnement du projet.

## Captures prioritaires

Les captures indispensables sont :

* page d'accueil desktop ;
* page Mes créations ;
* page Projets jouables à venir ;
* page d'accueil mobile ;
* page de connexion admin Django ;
* tableau de bord admin Django ;
* service Render actif ;
* logs Render avec `Your service is live` ;
* configuration Build Command et Start Command ;
* structure du projet dans VS Code ;
* commande `python manage.py check` ;
* commande `git status` propre ;
* dossier `doc`.

## Règle de sécurité

Aucune capture ne doit afficher :

* mot de passe ;
* clé secrète ;
* valeur de `DJANGO_SECRET_KEY` ;
* valeur de `DJANGO_SUPERUSER_PASSWORD` ;
* information sensible inutile.

## Statut

```txt
À faire
```

---

## Étape 4 - README à la racine

## Objectif

Créer un fichier `README.md` à la racine du projet.

Ce fichier doit permettre à une personne extérieure de comprendre rapidement :

* ce qu'est le projet ;
* comment l'installer ;
* comment le lancer ;
* quelles technologies sont utilisées ;
* comment le projet est déployé ;
* quelles sont les limites de la V1.

## Emplacement

```txt
README.md
```

Le fichier doit être placé à la racine du projet, au même niveau que :

```txt
manage.py
requirements.txt
build.sh
Dockerfile
docker-compose.yml
```

## Contenu attendu

Le README doit contenir :

* présentation du projet ;
* objectif de la V1 ;
* technologies utilisées ;
* installation locale ;
* lancement local ;
* lancement Docker ;
* déploiement Render ;
* variables d'environnement ;
* administration Django ;
* limites ;
* évolutions prévues.

## Statut

```txt
À faire
```

---

## Étape 5 - Fichier de choix techniques à la racine

## Objectif

Ajouter un fichier expliquant les choix techniques et les pistes explorées.

## Emplacement conseillé

```txt
CHOIX_TECHNIQUES.md
```

Ce fichier doit être placé à la racine du projet.

## Rôle

Il permet d'expliquer :

* pourquoi Django a été retenu ;
* pourquoi C# / Razor a été envisagé mais reporté ;
* pourquoi PostgreSQL n'est pas intégré en V1 ;
* pourquoi certaines fonctionnalités sont reportées ;
* pourquoi le projet évite de devenir une usine à gaz.

## Statut

```txt
À faire
```

---

## Étape 6 - Maquettes Figma

## Objectif

Préparer ou compléter les maquettes Figma pour montrer la réflexion visuelle du projet.

## Maquettes minimales conseillées

* page d'accueil ;
* page Mes créations ;
* page Projets jouables à venir ;
* version mobile simple.

## Objectif des maquettes

Les maquettes n'ont pas besoin d'être parfaites.

Elles doivent surtout montrer :

* l'intention visuelle ;
* l'organisation des pages ;
* la navigation ;
* la cohérence du projet ;
* la préparation de l'interface.

## Statut

```txt
À faire
```

---

## Étape 7 - Vérification technique finale

## Objectif

S'assurer que le projet ne contient pas d'erreur bloquante avant la présentation.

## Commandes à lancer

```powershell
python manage.py check
```

Résultat attendu :

```txt
System check identified no issues (0 silenced).
```

Puis :

```powershell
python manage.py runserver
```

Pages à tester :

```txt
/
 /mes-creations/
 /projets-jouables/
 /admin/
```

## Points à vérifier

* le serveur local démarre ;
* les pages s'affichent ;
* le CSS est chargé ;
* le menu fonctionne ;
* l'admin Django est accessible ;
* aucune erreur Django visible.

## Statut

```txt
À faire
```

---

## Étape 8 - Vérification Render

## Objectif

Contrôler que la version en ligne fonctionne toujours après les derniers commits.

## URL de production

```txt
https://frostia-games.onrender.com
```

## Points à vérifier

* site accessible ;
* page d'accueil chargée ;
* CSS chargé ;
* navigation fonctionnelle ;
* admin Django accessible ;
* Render indique le service actif ;
* logs sans erreur bloquante.

## Attention

Sur l'offre gratuite Render, le premier chargement peut être lent si le service est en veille.

Ce comportement n'est pas une erreur du projet.

## Statut

```txt
À faire
```

---

## Étape 9 - Relecture de la documentation

## Objectif

Vérifier que la documentation est cohérente et ne contient pas de contradiction importante.

## Documents à relire en priorité

* `00-index-documentation.md` ;
* `09-deploiement-render.md` ;
* `10-bilan-v1-frostia-games.md` ;
* `12-architecture.md` ;
* `13-test-et-vérification.md` ;
* `15-limites-et-évolutions.md` ;
* `16-presentation-projet-2.md` ;
* `17-pistes-explorees-et-non-retenues.md`.

## Points à vérifier

* noms de fichiers cohérents ;
* pas de promesse excessive ;
* limites clairement assumées ;
* technologies correctement expliquées ;
* déploiement bien documenté ;
* sécurité correctement présentée ;
* captures prévues.

## Statut

```txt
À faire
```

---

## Étape 10 - Git final

## Objectif

S'assurer que tout est sauvegardé dans Git et envoyé sur GitHub.

## Commandes à utiliser

```powershell
git status
```

Puis si des fichiers sont modifiés :

```powershell
git add .
git commit -m "Finalize Frostia Games V1 documentation"
git push
```

Après le push, relancer :

```powershell
git status
```

Résultat attendu :

```txt
nothing to commit, working tree clean
```

## Statut

```txt
À faire
```

---

## Étape 11 - Déploiement final Render

## Objectif

Vérifier que le dernier commit déclenche bien un redéploiement ou que Render utilise bien la dernière version du projet.

## Points à vérifier

* dernier commit visible ;
* déploiement terminé ;
* service live ;
* URL fonctionnelle ;
* pas d'erreur dans les logs.

## Statut

```txt
À faire
```

---

## Étape 12 - Préparation du dossier projet

## Objectif

Préparer la version présentable du projet pour une évaluation ou une proposition de projet 2.

## Éléments à inclure

* présentation du projet ;
* objectif de la V1 ;
* technologies utilisées ;
* architecture ;
* captures du site ;
* captures de l'administration ;
* captures Render ;
* explication du déploiement ;
* sécurité ;
* limites ;
* évolutions prévues ;
* bilan personnel.

## Positionnement à garder

Le projet doit être présenté comme :

```txt
Une V1 Django fonctionnelle, documentée, déployée et évolutive.
```

Il ne doit pas être présenté comme :

```txt
Une plateforme finale complète de gestion de projets de jeux vidéo.
```

## Statut

```txt
À faire
```

---

## Checklist finale

| Élément                         | Statut  |
| ------------------------------- | ------- |
| Pages relues                    | À faire |
| Responsive vérifié              | À faire |
| Captures réalisées              | À faire |
| README racine créé              | À faire |
| CHOIX_TECHNIQUES.md créé        | À faire |
| Maquettes Figma préparées       | À faire |
| `python manage.py check` validé | À faire |
| Site local testé                | À faire |
| Site Render testé               | À faire |
| Admin Django testé              | À faire |
| Documentation relue             | À faire |
| Git propre                      | À faire |
| Dernier push effectué           | À faire |
| Déploiement final vérifié       | À faire |

---

## Ce qui ne doit plus être ajouté dans cette V1

Pour éviter d'élargir le projet, les éléments suivants ne doivent plus être ajoutés maintenant :

```txt
PostgreSQL
Compte jury temporaire
Admin personnalisée
Upload serveur réel
Jeu jouable navigateur
Plotly.js
Espace privé complet
Système de sauvegarde automatique
Refonte complète du design
Nouvelle application Django importante
```

Ces éléments sont déjà identifiés comme évolutions futures.

La priorité est maintenant la finalisation.

---

## Critère de validation final

La V1 peut être considérée comme terminée lorsque :

* le site fonctionne en local ;
* le site fonctionne sur Render ;
* les pages principales sont accessibles ;
* l'administration Django est accessible ;
* la documentation est complète ;
* les captures sont prêtes ;
* le README racine existe ;
* le dépôt GitHub est propre ;
* le dernier déploiement Render est fonctionnel ;
* les limites et évolutions sont clairement expliquées.

---

## Bilan attendu

Une fois ce plan terminé, Frostia Games pourra être présenté comme une V1 propre et maîtrisée.

Le projet montrera :

* une base Django fonctionnelle ;
* une interface publique ;
* un backend simple ;
* une base SQLite ;
* une administration Django ;
* un déploiement Render ;
* une documentation complète ;
* une réflexion claire sur les choix techniques ;
* une maîtrise du périmètre.

La V1 ne sera pas une version finale complète, mais elle sera stable, cohérente, défendable et prête à évoluer.
