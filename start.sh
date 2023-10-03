#!/bin/sh


echo "The postgres host  is: $POSTGRES_HOST $POSTGRES_DB_PORT"
# Wait for the DB to be ready
until nc -z -v -w30 $POSTGRES_HOST $(( $POSTGRES_DB_PORT ));
do
 echo 'Waiting for the DB to be ready...'
 sleep 2
done

python manage.py makemigrations
python manage.py migrate
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
    print("Superuser 'admin' has been created.")
EOF

python manage.py runserver 0:8000
