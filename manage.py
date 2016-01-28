#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_phq9_screener.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
