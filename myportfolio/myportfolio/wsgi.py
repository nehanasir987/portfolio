"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Ensure project root is available in Python path
sys.path.insert(0, str(BASE_DIR))

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
