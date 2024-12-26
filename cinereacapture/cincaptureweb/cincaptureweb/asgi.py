"""
ASGI config for cincaptureweb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import reports.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cincaptureweb.settings')

django_asgi_app = get_asgi_application()
#application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(reports.routing.websocket_urlpatterns))
    ),

})
