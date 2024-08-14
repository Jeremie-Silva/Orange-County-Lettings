Procédures de Déploiement
==========================

Déploiement avec Docker :

Assurez-vous que Docker est installé sur votre machine.

Construisez l'image Docker :
docker build -t orange-county-lettings .

Lancez un conteneur à partir de l'image :
docker run -d -p 8000:8000 --name app_container -e SECRET_KEY=$SECRET_KEY -e SENTRY_DSN=$SENTRY_DSN -e ALLOWED_HOSTS=$ALLOWED_HOSTS orange-county-lettings

Accédez à l'application via http://localhost:8000.

Déploiement en Production :

Configurez les variables d'environnement spécifiques à la production (par exemple, pour une base de données PostgreSQL).
Utilisez un service cloud comme AWS ou Azure pour héberger votre application.
Suivez les bonnes pratiques de sécurité et de configuration pour le déploiement en production.