"""
WSGI config for djBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djBlog.settings.development') ### Aqui indico el sttiengs que quiero utilizar, el development.py por defecto
## El os. permite traer cierta funcionalidades del sistema operativo.                                                                               
application = get_wsgi_application()
