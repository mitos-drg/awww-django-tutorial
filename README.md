# Django tutorial

This repository contains code resulting from completing [django tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/), which was an exercise for the WWW Applications course.

## Install

To use the project clone it
```sh
git clone https://github.com/mitos-drg/awww-django-tutorial
cd awww-django-tutorial
```
then create virtual environment and install all required packages
```sh
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
create your superuser account
```sh 
./manage.py createsuperuser
```
and perform migrations
```sh 
./manage.py makemigrations
./manage.py migrate
```
now the project should be ready to run.
