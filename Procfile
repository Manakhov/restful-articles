release: python ArticlesProject/manage.py migrate
web: gunicorn --chdir ArticlesProject ArticlesProject.wsgi --log-file=-
