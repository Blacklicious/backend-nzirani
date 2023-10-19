#!/bin/sh
# wait-for-db.sh

set -e
  
host="$1"
shift
cmd="$@"
  
until PGPASSWORD=$DATABASE_PASSWORD psql -h "$host" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"


python manage.py migrate
python manage.py collectstatic --noinput
# Create superuser
echo "from django.contrib.auth.models import User; User.objects.filter(username='mr.diallo').exists() or User.objects.create_superuser('$SUPERUSER_NAME', '$SUPERUSER_EMAIL', '$SUPERUSER_PASSWORD')" | python manage.py shell

exec $cmd
