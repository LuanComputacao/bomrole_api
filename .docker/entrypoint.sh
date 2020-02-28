#!/bin/bash

service nginx start && gunicorn bomrole.wsgi:application --bind 0.0.0.0:8000