#!/bin/bash

create_superuser() {
  local cmd="from django.contrib.auth.models import User;               \
             User.objects.create_superuser('${ADMIN_USER}',    \
                                           '${ADMIN_EMAIL}',                          \
                                           '${ADMIN_PASSWORD}')"

  if [ -z ${ADMIN_USER+x} ]; then
    echo "[ERROR] Fail to create super user, the environment variable ADMIN_USER is not defined"
    exit 1
  fi

  if [ -z ${ADMIN_PASSWORD+x} ]; then
    echo "[ERROR] Fail to create super user, the environment variable ADMIN_PASSWORD is not defined"
    exit 1
  fi

  export DJANGO_SUPERUSER_PASSWORD=${ADMIN_PASSWORD}
  export DJANGO_SUPERUSER_USERNAME=${ADMIN_USER}
  export DJANGO_SUPERUSER_EMAIL=${ADMIN_EMAIL}

  python manage.py createsuperuser --noinput
}

setup_database() {
  python manage.py migrate
}


main() {
  setup_database
  create_superuser
  python manage.py runserver 0.0.0.0:8000
}

main "$@"
