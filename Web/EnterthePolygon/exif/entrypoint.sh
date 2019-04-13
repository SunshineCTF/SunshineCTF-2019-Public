#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$RABBIT_HOST" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $RABBIT_HOST $RABBIT_PORT; do
      sleep 0.1
    done

    echo "RabbitMQ started"
fi

python manage.py flush --no-input
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DEFAULT_USER', 'notarealemail@email.com', '$DEFAULT_PASSWORD')" | python manage.py shell

exec "$@"
