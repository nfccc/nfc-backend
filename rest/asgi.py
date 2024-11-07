"""
ASGI config for rest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import nfc.bus.routing  # Import the routing from the bus app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')

# Initialize Django ASGI application early to ensure the app is loaded before importing the consumer code
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            nfc.bus.routing.websocket_urlpatterns
        )
    ),
})
