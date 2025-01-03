from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    date_registered = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

    class Meta:
        model = Student
        fields = ['student_name', 'uid_number', 'parent_contact', 'parent_email', 'student_class', 'date_registered']

    def __init__(self, *args, **kwargs):
        exclude_date = kwargs.pop('exclude_date', False)
        super(StudentSerializer, self).__init__(*args, **kwargs)
        
        if exclude_date:
            self.fields.pop('date_registered')

