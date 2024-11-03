from rest_framework import serializers
from .models import BusAttendance

class BusAttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.student_name")
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M")  # Format to '2023-06-23 15:40'

    class Meta:
        model = BusAttendance
        fields = ['student_name', 'timestamp', 'status']
