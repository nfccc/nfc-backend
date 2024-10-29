from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_name', 'uid_number', 'parent_contact', 'parent_email', 'student_class']
