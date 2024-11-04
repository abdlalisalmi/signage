#!/bin/bash

until cd /app
do
    echo "Waiting for server volume..."
done

echo "Starting virtualenv..."
until source venv/bin/activate
do
        echo "Waiting for virtualenv..."
        sleep 2
done

# echo "Installing requirements..."
# until pip install -r requirements.txt
# do
#       echo "Waiting for requirements..."
#       sleep 2
# done

echo "Generating migrations..."
until ./manage.py makemigrations
do
        echo "Waiting for create migrations..."
        sleep 2
done

echo "Applying migrations..."
until ./manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

echo "Creating SuperUser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='$SUPER_USER_EMAIL', password='$SUPER_USER_PASSWORD') if not User.objects.filter(username='$SUPER_USER_EMAIL').exists() else print('$SUPER_USER_EMAIL already exist.')" | python manage.py shell


echo "Starting server..."
./manage.py runserver 0.0.0.0:8000