 set -o errexit
 pip install -r requirements.txt
 python manage.py collectstatic --noinput
 python manage.py makemigrations && python manage.py migrate
 python manage.py loaddata categories.json
 python manage.py loaddata items.json