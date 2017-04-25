# Foursquare Client Project: Euler's 4Square Client
In this project, I need to build a Foursquare client using Django Framework.<br>
This project is prepared for [HIPO](https://hipolabs.com/).

# Installation

Install Django 
```shell
$ pip install django
```

Create and activate a virtual environment.
```shell
$ python3 -m venv venv
$ source venv/bin/activate
```

Create a project
```shell
$ django-admin startproject euler
```

Create the web apps
```shell
$ python manage.py startapp web
```

Create an admin user
```shell
$ python manage.py createsuperuser
```

Install requests
```shell
$ pip install requests
```

Create sqlite database.
```shell
$ python manage.py makemigrations
$ python manage.py migrate

```

The development server: to verify your Django project works.
```shell
$ python manage.py runserver

```

Create a file which contains requirements of technical part(version).
```shell
$ pip freeze > requirements.txt
```

# Deployment
This project deploys on [Heroku](https://hipoproject.herokuapp.com/)
