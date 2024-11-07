# rest/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import nfc.bus.routing  # Import the WebSocket routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            nfc.bus.routing.websocket_urlpatterns
        )
    ),
})
