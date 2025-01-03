from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BusAttendance, Bus
from nfc.students.models import Student

from datetime import date
from .serializers import BusAttendanceSerializer
from django.utils import timezone

# Log attendance for a student


# Fetch attendance records by date
@api_view(['GET'])
def get_bus_attendance_by_date(request, bus_id):
    attendance_date = request.GET.get('date', date.today().strftime('%Y-%m-%d'))
    # Filter attendance by bus and specified date
    attendance_records = BusAttendance.objects.filter(
        bus__bus_id=bus_id,
        timestamp__date=attendance_date  # Filters by date only
    ).select_related('student')
    
    # Serialize and return the data
    serializer = BusAttendanceSerializer(attendance_records, many=True)
    total_riders = attendance_records.count()

    return Response({
        "total_riders": total_riders,
        "attendance": serializer.data
    })
