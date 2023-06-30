#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
# --workers - 4 uWSGI workers (binded to number of CPUs)
# --master - for mark app as master thread
# --enable-threads - if we using multithreading in app
# --module - telling uWSGI service where's the entrypoint of the project