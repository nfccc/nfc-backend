from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    date_registered = serializers.DateTimeField(format="%Y-%m-%d %H:%M")  # Custom format for display

    class Meta:
        model = Student
        fields = ['student_name', 'uid_number', 'parent_contact', 'parent_email', 'student_class']
