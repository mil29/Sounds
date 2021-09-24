#!/bin/bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo yes | python manage.py collectstatic --settings=djangoapp1.settings_mark && 
./start_server.sh
sudo systemctl restart gunicorn
sudo systemctl restart nginx