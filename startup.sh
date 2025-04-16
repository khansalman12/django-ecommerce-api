#!/bin/bash

# Run migrations
python manage.py migrate

# Create superuser if doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Admin123!')
    print('Superuser created successfully');
else:
    print('Superuser already exists');
"

# Start gunicorn server
gunicorn storefront2.wsgi:application
