# nfc/bus/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/bus-attendance/(?P<bus_id>\w+)/$', consumers.BusAttendanceConsumer.as_asgi()),
]
