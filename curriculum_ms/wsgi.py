"""
WSGI config for curriculum_ms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the sys.path
project_home = '/home/buqlex/curriculum_ms'
if project_home not in sys.path:
    sys.path.append(project_home)

# Point to the application settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'curriculum_ms.settings'

# Activate the virtual environment
activate_env = os.path.expanduser('/home/buqlex/.virtualenvs/venv/bin/activate_this.py')
with open(activate_env) as f:
    exec(f.read(), {'__file__': activate_env})

# Import and set up the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
