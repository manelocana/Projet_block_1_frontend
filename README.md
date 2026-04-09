


# Structure et Routage d'un Frontend Statique
## Vue d'ensemble

Ce projet est un site frontend statique construit avec des technologies web standards :

- HTML pour la structure

- CSS pour le style

- JavaScript (optionnel) pour le comportement côté client

Un frontend statique signifie que le site ne nécessite aucun serveur backend (comme Python, Node, PHP, etc.) pour afficher les pages. Le navigateur charge directement les fichiers HTML.

Le site peut être hébergé sur n’importe quelle plateforme d’hébergement statique (par exemple GitHub Pages, Netlify ou un serveur web simple).

---


## Architecture d’un site statique

Dans un site statique :

Chaque page est un fichier HTML séparé

Le serveur livre simplement les fichiers au navigateur

Aucun traitement côté serveur n’a lieu

Exemple de structure de projet :

    project-root/
    │
    ├── index.html
    ├── templates/
    │   ├── pages.html
    │   ├── portfolio.html
    │   ├── blog.html
    │   └── contact.html
    │
    ├── css/
    │   ├── style.css
    │   └── home.css
    │
    ├── js/
    │   └── script.js
    │
    └── img/
        └── images...

Le dossier racine contient le point d’entrée principal du site :

# index.html

Lorsque l’utilisateur visite la racine du site, le navigateur charge automatiquement ce fichier.


---


## Navigation et routage

Comme le site est statique, la navigation entre les pages se fait via des liens HTML classiques.

Exemple :

    <a href="templates/pages.html">À PROPOS</a>

Lorsque l’utilisateur clique sur ce lien, le navigateur demande le fichier HTML correspondant au serveur.

Ce type de navigation s’appelle le routage basé sur les fichiers.

## Chemins relatifs

Les sites statiques utilisent des chemins relatifs pour référencer :

- les fichiers CSS

- les images

- les scripts JavaScript

- d’autres fichiers HTML

Exemples :

CSS

    <link rel="stylesheet" href="css/style.css">
    
Image

    <img src="img/logo.png">
    
Navigation

    <a href="templates/blog.html">Blog</a>

Les chemins relatifs sont résolus par rapport à la localisation du fichier courant.


---


## Navigation vers le dossier parent

Si un fichier est dans un sous-dossier et doit accéder à un fichier dans le dossier parent, on utilise ../.

Exemple :

Si une page est située à :

    templates/pages.html

Pour revenir à la page d’accueil :

    <a href="../index.html">ACCUEIL</a>

../ signifie :

    « remonter d’un niveau de dossier »

Pour remonter plusieurs niveaux :

    ../../

---


## Organisation des ressources

Les ressources (CSS, JS, images) doivent être dans des dossiers dédiés.

Structure typique :

- css/
- js/
- img/
- fonts/

Exemples d’utilisation :

    <link rel="stylesheet" href="css/style.css">
    <script src="js/script.js"></script>
    <img src="img/photo.jpg">

Cette organisation améliore la maintenabilité et l’évolutivité du projet.

---


## Caractéristiques d’un frontend statique
### Avantages

- Architecture simple

- Chargement rapide

- Déploiement facile

- Aucun serveur nécessaire

- Compatible avec des services d’hébergement statique

### Limitations

- Pas de logique côté serveur

- Pas d’accès à une base de données

- Pas de rendu dynamique des templates

- Les en-têtes et pieds de page doivent être dupliqués manuellement

  ---
  

## Déploiement

Étant donné que le site est entièrement statique, le déploiement consiste simplement à uploader les fichiers sur l’hébergement.

Le serveur servira :

- HTML
- CSS
- JS
- images

Aucun environnement d’exécution n’est nécessaire.


---


## Images

Les images sont en format webp


## Résumé

Ce projet suit une architecture frontend statique où :

- Chaque page est un fichier HTML autonome

 -La navigation se fait via <a href="">

- Les chemins sont gérés avec le routage relatif

- Les ressources sont organisées dans des dossiers dédiés
