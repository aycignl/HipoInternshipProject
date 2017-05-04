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
This project deploys on [PythonAnywhere](http://gonul.pythonanywhere.com/)

# References
* http://tutorial.djangogirls.org/
* https://docs.djangoproject.com/en/1.11/#first-steps
* https://docs.djangoproject.com/en/1.11/topics/class-based-views/#
* http://docs.python-requests.org/en/master/
* https://developer.foursquare.com/docs/venues/search
* https://developer.foursquare.com/overview/auth.html#userless
* https://devcenter.heroku.com/articles/deploying-python
* https://docs.djangoproject.com/en/1.11/ref/templates/builtins/#for-empty
* http://getskeleton.com/
* https://docs.python.org/3/library/urllib.request.html
* https://tutorial.djangogirls.org/tr/deploy/
