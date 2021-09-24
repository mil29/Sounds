#!/bin/bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo yes | python manage.py collectstatic
sudo systemctl restart gunicorn
sudo systemctl restart nginx