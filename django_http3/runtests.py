# django_http3/runtests.py

import sys
import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line

def run_tests():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_http3.test_settings')
    django.setup()
    argv = [sys.argv[0], 'test', 'django_http3.tests']
    execute_from_command_line(argv)

if __name__ == '__main__':
    run_tests()
