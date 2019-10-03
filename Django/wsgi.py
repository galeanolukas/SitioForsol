"""
WSGI config for Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

import sys

####Configuracion para el servidor WSGI
#reload(sys)
#sys.setdefaultencoding("utf-8")
#sys.path.append('/home/lukas/Django')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")

application = get_wsgi_application()
