from django.db import models
from nfc.students.models import Student

class Bus(models.Model):
    bus_id = models.CharField(max_length=10, unique=True)  # Unique identifier, e.g., "PB", "MB"
    name = models.CharField(max_length=50)  # Name of the bus, e.g., "P1 Bus", "Muthaiga Bus"
    route = models.TextField(blank=True, null=True)  # Optional field for the route or description

    def __str__(self):
        return f"{self.name} ({self.bus_id})"
    
    
    
class BusAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set date and time
    status = models.CharField(max_length=10, default="Present")  # Default status as Present

    class Meta:
        unique_together = ('student', 'bus', 'timestamp')  # Ensure one attendance record per student, bus, and timestamp (by day)
        verbose_name = "Bus Attendance"
        verbose_name_plural = "Bus Attendance Records"

    def __str__(self):
        return f"{self.student.student_name} on {self.bus.name} - {self.timestamp} ({self.status})"


