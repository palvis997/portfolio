#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files with WhiteNoise compression
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Seed initial portfolio data if database is empty
python manage.py seed_data
