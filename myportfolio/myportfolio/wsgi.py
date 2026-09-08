"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Project root directory:
# /var/task/myportfolio
BASE_DIR = Path(__file__).resolve().parent.parent

# Make the project root available for imports
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()