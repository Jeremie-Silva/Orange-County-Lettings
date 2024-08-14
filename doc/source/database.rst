Structure de la Base de Données
===============================

Le projet utilise une base de données SQLite pour stocker les informations sur les utilisateurs et les locations.

### Modèles de données

**Address** :
- `id` : Identifiant unique (clé primaire).
- `street` : Rue de l'adresse.
- `city` : Ville.
- `state` : État.
- `zip_code` : Code postal.

**Letting** :
- `id` : Identifiant unique (clé primaire).
- `title` : Titre de la location.
- `address` : Référence vers le modèle `Address`.

**Profile** :
- `id` : Identifiant unique (clé primaire).
- `user` : Référence vers un utilisateur (clé étrangère).
- `favorite_city` : Ville favorite de l'utilisateur.
