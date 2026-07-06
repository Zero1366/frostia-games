# JavaScript dynamique — Menu mobile

## Objectif

Cette partie présente l’utilisation de JavaScript dans le projet **Frostia Games**.

L’objectif est de montrer que l’interface ne repose pas uniquement sur du HTML et du CSS statique.

Un script JavaScript est utilisé pour gérer l’ouverture et la fermeture du menu mobile.

Cette fonctionnalité permet d’améliorer la navigation sur les petits écrans et de rendre l’interface plus dynamique.

---

# 1. Fonctionnalité concernée

La fonctionnalité présentée est le **menu de navigation mobile**.

Sur écran réduit, le menu doit pouvoir être ouvert ou fermé par l’utilisateur afin de permettre la navigation entre les différentes pages du site.

Cette fonctionnalité améliore l’expérience utilisateur sur mobile.

Elle concerne principalement :

```text
static/js/menu.js
templates/base.html
static/css/main.css
```

---

# 2. Rôle du fichier JavaScript

Le fichier JavaScript utilisé est :

```text
static/js/menu.js
```

Son rôle est de contrôler le comportement du menu mobile.

Il permet notamment :

* de récupérer le bouton du menu mobile ;
* de récupérer la sidebar ou le conteneur de navigation ;
* d’écouter le clic de l’utilisateur ;
* d’ajouter ou retirer une classe CSS ;
* d’ouvrir ou fermer le menu ;
* de mettre à jour l’attribut `aria-expanded` ;
* de fermer le menu après un clic sur un lien de navigation.

---

# 3. Fonctionnement général

Le fonctionnement repose sur une logique simple :

1. l’utilisateur clique sur le bouton du menu ;
2. JavaScript détecte l’événement avec `addEventListener` ;
3. le script ajoute ou retire une classe CSS avec `classList.toggle` ;
4. le menu change d’état visuel ;
5. l’attribut `aria-expanded` est mis à jour ;
6. l’utilisateur peut accéder aux liens de navigation ;
7. le menu peut se refermer après un clic sur un lien.

Cette logique permet de modifier l’interface sans recharger la page.

---

# 4. Sélection des éléments HTML

Le script doit d’abord récupérer les éléments HTML nécessaires.

Exemple de logique :

```javascript
const menuButton = document.querySelector("[data-menu-button]");
const sidebar = document.querySelector("[data-sidebar]");
const navLinks = document.querySelectorAll("[data-sidebar] a");
```

Ces sélecteurs permettent de cibler les éléments grâce à des attributs `data-*`.

Les attributs `data-*` sont utiles car ils évitent de dépendre uniquement des classes CSS visuelles.

Ils permettent de séparer :

* le rôle JavaScript ;
* le style CSS ;
* la structure HTML.

---

# 5. Attributs utilisés dans le template

Le template principal doit contenir des attributs permettant au JavaScript de retrouver les bons éléments.

Exemple de structure HTML possible :

```html
<button
    class="menu-toggle"
    type="button"
    data-menu-button
    aria-expanded="false"
>
    Menu
</button>

<aside class="sidebar" data-sidebar>
    <nav>
        <a href="/">Accueil</a>
        <a href="/mes-creations/">Mes créations</a>
        <a href="/projets-jouables/">Projets jouables</a>
    </nav>
</aside>
```

Le bouton possède :

```text
data-menu-button
```

La sidebar possède :

```text
data-sidebar
```

L’attribut `aria-expanded` indique si le menu est ouvert ou fermé.

---

# 6. Écoute du clic utilisateur

Le script utilise `addEventListener` pour détecter le clic sur le bouton du menu.

Exemple :

```javascript
menuButton.addEventListener("click", () => {
    sidebar.classList.toggle("is-open");
});
```

Cette logique signifie :

* si la sidebar n’a pas la classe `is-open`, elle l’ajoute ;
* si la sidebar a déjà la classe `is-open`, elle la retire.

La classe `is-open` permet ensuite au CSS de modifier l’affichage du menu.

---

# 7. Mise à jour de `aria-expanded`

Pour améliorer l’accessibilité, le script met à jour l’attribut `aria-expanded`.

Exemple :

```javascript
const isOpen = sidebar.classList.toggle("is-open");
menuButton.setAttribute("aria-expanded", String(isOpen));
```

Si le menu est ouvert :

```text
aria-expanded="true"
```

Si le menu est fermé :

```text
aria-expanded="false"
```

Cela permet d’indiquer l’état du menu aux technologies d’assistance.

---

# 8. Fermeture du menu après un clic sur un lien

Sur mobile, il est utile de refermer le menu lorsqu’un utilisateur clique sur un lien de navigation.

Exemple :

```javascript
navLinks.forEach((link) => {
    link.addEventListener("click", () => {
        sidebar.classList.remove("is-open");
        menuButton.setAttribute("aria-expanded", "false");
    });
});
```

Cette logique permet :

* d’éviter que le menu reste ouvert après navigation ;
* d’améliorer le confort d’utilisation ;
* de garder un comportement plus propre sur mobile.

---

# 9. Exemple complet de script

Exemple complet simplifié :

```javascript
const menuButton = document.querySelector("[data-menu-button]");
const sidebar = document.querySelector("[data-sidebar]");
const navLinks = document.querySelectorAll("[data-sidebar] a");

if (menuButton && sidebar) {
    menuButton.addEventListener("click", () => {
        const isOpen = sidebar.classList.toggle("is-open");
        menuButton.setAttribute("aria-expanded", String(isOpen));
    });

    navLinks.forEach((link) => {
        link.addEventListener("click", () => {
            sidebar.classList.remove("is-open");
            menuButton.setAttribute("aria-expanded", "false");
        });
    });
}
```

Ce script reste volontairement simple.

Il ne dépend pas d’un framework JavaScript.

Il utilise uniquement du JavaScript natif.

---

# 10. Lien avec le CSS

Le JavaScript ajoute ou retire la classe :

```text
is-open
```

Le CSS peut ensuite utiliser cette classe pour afficher ou masquer la sidebar.

Exemple logique :

```css
.sidebar {
    transform: translateX(-100%);
}

.sidebar.is-open {
    transform: translateX(0);
}
```

Le JavaScript ne gère donc pas directement tout le style.

Il change l’état du menu, puis le CSS applique le rendu visuel.

---

# 11. Lien avec Django

Le JavaScript est chargé depuis le template principal Django.

Fichier concerné :

```text
templates/base.html
```

Exemple :

```django
{% load static %}

<script src="{% static 'js/menu.js' %}" defer></script>
```

L’attribut `defer` permet de charger le script sans bloquer l’affichage de la page.

Il permet aussi d’attendre que la structure HTML soit disponible avant l’exécution du script.

---

# 12. Pourquoi ne pas utiliser un framework JavaScript

Pour cette V1, aucun framework JavaScript lourd n’est nécessaire.

Le projet n’a pas besoin de React, Vue ou Angular pour gérer un menu mobile.

Le choix du JavaScript natif permet de garder :

* un code simple ;
* une dépendance faible ;
* une maintenance plus facile ;
* une intégration directe avec Django ;
* un périmètre adapté à une V1.

Cette décision permet d’éviter une complexité inutile.

---

# 13. Limites de cette fonctionnalité

La fonctionnalité reste volontairement simple.

Elle ne gère pas encore :

* des animations avancées ;
* un système complet de composants ;
* des transitions complexes ;
* un menu multi-niveaux ;
* une navigation dynamique complète ;
* une gestion avancée du focus clavier.

Ces améliorations pourront être étudiées plus tard si le projet évolue.

---

# 14. Tests réalisés

La fonctionnalité doit être testée sur écran réduit.

Points à vérifier :

* le bouton du menu apparaît sur mobile ;
* le clic ouvre le menu ;
* le second clic ferme le menu ;
* la classe `is-open` est bien ajoutée ou retirée ;
* `aria-expanded` passe de `false` à `true` ;
* `aria-expanded` repasse de `true` à `false` ;
* le menu se ferme après un clic sur un lien ;
* les liens restent accessibles ;
* aucun débordement horizontal important n’apparaît.

---

# 15. Preuves à intégrer dans le dossier

Pour cette fonctionnalité, les preuves à ajouter sont :

| Élément | Preuve |
| ------- | ------ |
| Code JavaScript | Capture du fichier `static/js/menu.js` |
| Sélection des éléments | Capture montrant `querySelector` |
| Événement utilisateur | Capture montrant `addEventListener` |
| Changement d’état | Capture montrant `classList.toggle` |
| Accessibilité | Capture montrant `aria-expanded` |
| Template Django | Capture de `base.html` avec le chargement du script |
| Rendu final fermé | Capture du menu mobile fermé |
| Rendu final ouvert | Capture du menu mobile ouvert |

---

# 16. Intérêt pour le projet

Cette fonctionnalité permet de rendre la navigation utilisable sur mobile.

Elle montre l’utilisation de JavaScript pour modifier dynamiquement l’interface en fonction de l’action de l’utilisateur.

Elle complète le travail réalisé avec :

* HTML ;
* CSS ;
* Django templates ;
* responsive ;
* fichiers statiques.

Elle permet aussi de répondre au besoin de montrer une vraie interaction front-end dans le dossier projet.

---

# 17. Conclusion

Le menu mobile de Frostia Games montre une utilisation simple mais concrète de JavaScript dynamique.

Le script permet de détecter une action utilisateur, de modifier l’état visuel du menu, de mettre à jour l’accessibilité avec `aria-expanded` et de refermer la navigation après un clic sur un lien.

Cette fonctionnalité reste limitée, mais elle est adaptée au périmètre de la V1.

Elle montre que l’interface n’est pas uniquement statique et qu’un comportement dynamique a bien été intégré au projet.
