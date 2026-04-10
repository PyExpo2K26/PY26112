#!/usr/bin/env bash
# Render Build Script for WSP (Water Surveillance Portal)
set -o errexit

# Install Python dependencies
pip install -r docs/requirements.txt

# Navigate to Django source directory
cd code/source

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
