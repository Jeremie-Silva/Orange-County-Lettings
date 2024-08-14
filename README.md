[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Orange County Lettings
---
Fork : https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR

### Pré-requis
Avoir un OS **Linux** avec **Python 3.11** installé  
<br/>

### Installation
Executer ces commandes dans un terminal **bash**
pour installer le projet
```bash
git clone git@github.com:Jeremie-Silva/Orange-County-Lettings.git
cd Orange-County-Lettings
virtualenv -p3.11 .venv
source .venv/bin/activate
pip install -r requirements.txt
export SECRET_KEY=<value>
export SENTRY_DSN=<value>
export ALLOWED_HOSTS=<value>
```

<br/>

### lancer l'application en local :
```bash
python manage.py runserver
```
```bash
docker container run -d -p 8000:8000 --name app_container -e SECRET_KEY=$SECRET_KEY -e SENTRY_DSN=$SENTRY_DSN -e ALLOWED_HOSTS=$ALLOWED_HOSTS mytricks/orange-county-lettings:<selected-tag>
```

### lancer les tests en local :
```bash
python manage.py test
```
```bash
pytest
```

### lancer le codingstyle en local :
```bash
flake8
```

### Générer la documentation en local :
```bash
cd doc
make html
```