"""
WSGI config for test_rest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_rest.settings")




application = DjangoWhiteNoise(application)