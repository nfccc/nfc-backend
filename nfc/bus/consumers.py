# In `nfc/bus/consumers.py`

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BusAttendanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bus_id = self.scope['url_route']['kwargs']['bus_id']
        self.room_group_name = f'bus_attendance_{self.bus_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming messages if needed
        pass

    async def attendance_update(self, event):
        # Send attendance update to WebSocket client
        await self.send(text_data=json.dumps(event['message']))
