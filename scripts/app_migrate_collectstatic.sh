#!/bin/bash
cd /home/ubuntu
source env/bin/activate
cd djangoapp1
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput