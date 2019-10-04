## Create a virtual environment and install django

```
pipenv install pep8 --dev
pipenv install autopep8 --dev
pipenv install django
pipenv shell
```

## Create Project

```
django-admin startproject atar_matkonim .
```

## Check the server for the first time

```
manage.py migrate
manage.py runserver
```

## Create App

```
django-admin startapp matkonim
```

## Create super-user

```
manage.py createsuperuser
```
