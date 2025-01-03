from django.core.management.base import BaseCommand
from nfc.bus.models import Bus

class Command(BaseCommand):
    help = 'Populates the Bus model with initial data'

    def handle(self, *args, **kwargs):
        buses = [
            {'bus_id': 'PB', 'name': 'P1 Bus'},
            {'bus_id': 'MB', 'name': 'Muthaiga Bus'},
            {'bus_id': 'LB', 'name': 'Lavington Bus'},
            {'bus_id': 'SB', 'name': 'SSD Bus'},
            {'bus_id': 'KB', 'name': 'Karen Bus'},
        ]
        for bus_data in buses:
            Bus.objects.update_or_create(bus_id=bus_data['bus_id'], defaults=bus_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated Bus model with initial data'))
