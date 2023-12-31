#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv

dotenv_path = os.path.join('.env')
load_dotenv(dotenv_path)


def main():
    """Run administrative tasks."""
    if os.getenv('STATUS') == 'develope':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develope')
    if os.getenv('STATUS') == 'deployment':
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deployment')
    if os.getenv('STATUS') == 'kubernetes':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.kubernetes')
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
