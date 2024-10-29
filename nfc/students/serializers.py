from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    date_registered = serializers.DateTimeField(read_only=True)  # Read-only, so not required in input data

    class Meta:
        model = Student
        fields = ['student_name', 'uid_number', 'parent_contact', 'parent_email', 'student_class', 'date_registered']
