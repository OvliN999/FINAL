#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p staticfiles media

# Collect static files
python manage.py collectstatic --noinput

# Run migrations (if needed)
# python manage.py migrate
