#!/bin/bash

echo '' >> /app/bomrole/.env
python manage.py migrate
python manage.py collectstatic --noinput
rm /etc/nginx/sites-available/default
envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/sites-available/default
# cp .docker/default /etc/nginx/sites-available/default
bash /app/heroku-exec.sh
service nginx start
gunicorn bomrole.wsgi:application --access-logfile - --error-logfile - --log-level debug --bind 127.0.0.1:8000