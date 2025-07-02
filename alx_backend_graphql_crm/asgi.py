"""
ASGI config for alx_backend_graphql_crm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
>>>>>>> 275468b69b688680d4983880ca426f02ac258e14
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_backend_graphql_crm.settings')

application = get_asgi_application()
