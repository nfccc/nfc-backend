# nfc/bus/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/bus-attendance/<str:bus_id>/', consumers.BusAttendanceConsumer.as_asgi()),
]
