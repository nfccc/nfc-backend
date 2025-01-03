import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import nfc.bus.routing  # Ensure this is the correct import path for your WebSocket routing

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
