#!/bin/bash

echo '' >> /code/bomrole/.env
python manage.py migrate
python manage.py collectstatic --noinput
rm /etc/nginx/sites-available/default
envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/sites-available/default
# cp .docker/default /etc/nginx/sites-available/default
service nginx start \
 && gunicorn bomrole.wsgi:application --bind 127.0.0.1:8000