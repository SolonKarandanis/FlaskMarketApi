#!/bin/bash
# this script is used to boot a Docker container
source venv/bin/activate
exec gunicorn -b :8000 --access-logfile - --error-logfile - 'src:create_app()'