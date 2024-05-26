#!/bin/bash
pdm venv create --with venv 3.11 
pdm use -f 3.11
pdm install --no-lock --no-editable
pdm run python manage.py collectstatic
pdm run python manage.py makemigrations
pdm run python manage.py migrate
pdm run python -m uvicorn src.django_project.asgi:application --host 0.0.0.0 --port 8000
