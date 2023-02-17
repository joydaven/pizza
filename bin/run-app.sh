#!/usr/bin/env bash

. /root/challenge/pizza/venv/bin/activate && gunicorn --workers 4 --bind 127.0.0.1:8000 pizza.wsgi
