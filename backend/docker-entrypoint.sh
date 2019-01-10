#!/bin/bash

python3 manage.py migrate
python3 manage.py create_test_user
python3 manage.py runserver 0.0.0.0:8000