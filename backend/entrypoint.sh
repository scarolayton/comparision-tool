#!/bin/sh


python manage.py makemigartions
python manage.py migrate --no-input


gunicorn backend.wsgi:application --bind 0.0.0.0:8000
