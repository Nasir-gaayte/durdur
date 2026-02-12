#!/bin/bash
set -e

echo "Applying database migrations..."
python3 manage.py migrate

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting server..."
python3 manage.py runserver 0.0.0.0:8000
