# In `nfc/bus/routing.py` (or wherever your routing configuration is)

from django.urls import re_path
from . import consumers  # Import the WebSocket consumer for bus attendance

websocket_urlpatterns = [
    re_path(r'ws/bus-attendance/(?P<bus_id>\w+)/$', consumers.BusAttendanceConsumer.as_asgi()),
]
