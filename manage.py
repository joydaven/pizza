#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
project_folder = os.path.expanduser('/challenge/pizza')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

def main():
    # this changes according to .env settings
    CURRENT_ENVIRONMENT = 'pizza.settings_' + os.getenv("ENVIRONMENT")
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
