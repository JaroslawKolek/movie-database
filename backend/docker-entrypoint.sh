#!/bin/bash

python3 manage.py migrate
python3 manage.py create_test_user TestUser test1234
python3 manage.py runserver 0.0.0.0:8000