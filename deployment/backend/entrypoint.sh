#!/bin/sh

until cd /app/
do
    echo "Waiting for server volume..."
done

until ./manage.py makemigrations
do
	echo "Waiting for create migrations..."
	sleep 2
done

# until ./manage.py makemigrations --merge
# do
# 	echo "Waiting for merge migrations..."
# 	sleep 2
# done

until ./manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

./manage.py collectstatic --noinput

until echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(email='$SUPER_USER_EMAIL', password='$SUPER_USER_PASSWORD', login='$SUPER_USER_EMAIL') if not User.objects.filter(email='$SUPER_USER_EMAIL').exists() else print('$SUPER_USER_EMAIL already exist.')" | ./manage.py shell
do
	echo "Creating SuperUser..."
	sleep 2
done

# Calculations:
	# Workers: 4 cores * 2 workers per core = 8 workers
	# Threads: Start with 2 threads per worker

until gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 2 --timeout 60 --access-logfile '/var/log/supervisor/access.log' --error-logfile '/var/log/supervisor/error.log'
do
	echo "Waiting for server..."
	sleep 2
done
