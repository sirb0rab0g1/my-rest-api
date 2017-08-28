web:python manage.py runserver
web: gunicorn restapiproject.wsgi --log-file -
heroku ps:scale web=1