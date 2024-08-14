Installation
============

Pour installer le projet sur un système Linux avec Python 3.11, suivez les étapes ci-dessous.

Prérequis :
Assurez-vous d'avoir un système d'exploitation **Linux** avec **Python 3.11** installé.

Étapes d'installation :

Cloner le dépôt GitHub :
git clone git@github.com:Jeremie-Silva/Orange-County-Lettings.git

Naviguer dans le répertoire du projet :
cd Orange-County-Lettings

Créer un environnement virtuel avec Python 3.11 :
virtualenv -p3.11 .venv

Activer l'environnement virtuel :
source .venv/bin/activate

Installer les dépendances :
pip install -r requirements.txt

Configurer les variables d'environnement :
export SECRET_KEY=<value>
export SENTRY_DSN=<value>
export ALLOWED_HOSTS=<value>
