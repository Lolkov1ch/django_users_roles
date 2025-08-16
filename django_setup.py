import os
import django
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "users_roles.settings")
django.setup()