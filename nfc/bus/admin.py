# In `nfc/bus/admin.py`
from django.contrib import admin
from .models import Bus, BusAttendance


admin.site.register(Bus)
admin.site.register(BusAttendance)
