Guide de démarrage rapide
=========================

Pour démarrer rapidement l'application en local :

Assurez-vous que le projet est installé (voir la section Installation).

Lancer l'application en local :
python manage.py runserver

Vous pouvez également utiliser Docker :
docker container run -d -p 8000:8000 --name app_container -e SECRET_KEY=$SECRET_KEY -e SENTRY_DSN=$SENTRY_DSN -e ALLOWED_HOSTS=$ALLOWED_HOSTS mytricks/orange-county-lettings:<selected-tag>

Accéder à l'application via http://localhost:8000 dans votre navigateur.

Lancer les tests en local pour vérifier le bon fonctionnement :
python manage.py test

Vous pouvez également utiliser pytest :
pytest

Vérifier le respect des normes de codage avec Flake8 :
flake8

Générer la documentation en local :
cd doc
pip install sphinx
make html