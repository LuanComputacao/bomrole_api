#!/bin/bash
rm /etc/nginx/sites-available/default
cp .docker/default /etc/nginx/sites-available/default
systemctl enable --now gunicorn.socket
service nginx start \
 && gunicorn bomrole.wsgi:application --bind 0.0.0.0:8000