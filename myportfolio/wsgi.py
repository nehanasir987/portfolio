# ~/projects/portfolio/myportfolio/wsgi.py

"""
WSGI config for myportfolio project.
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
