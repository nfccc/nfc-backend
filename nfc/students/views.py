from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from django.core.mail import send_mail
from django.conf import settings

# POST request to add a new student
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # date_registered will be set automatically
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET request to retrieve all students (name, UID, parent contact, parent email, student class, and total count)
@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    total_students = students.count()
    # Get student details
    data = students.values('student_name', 'uid_number', 'parent_contact', 'parent_email', 'student_class', 'date_registered')
    
    return Response({
        "total_students": total_students,
        "students": list(data)
    })

# GET request to retrieve students by class (full details and total count per class)
@api_view(['GET'])
def get_students_by_class(request, student_class):
    students = Student.objects.filter(student_class=student_class)
    total_students = students.count()
    # Get full details: name, UID, parent contact, parent email, date registered
    data = students.values('student_name', 'uid_number', 'parent_contact', 'parent_email', 'date_registered')
    
    return Response({
        "total_students": total_students,
        "students": list(data)
    })
    
    
    
@api_view(['PUT', 'PATCH'])
def update_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        # Full update
        serializer = StudentSerializer(student, data=request.data)
    elif request.method == 'PATCH':
        # Partial update
        serializer = StudentSerializer(student, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




@api_view(['POST'])
def handle_nfc_scan(request):
    # Retrieve UID from the request data
    uid_number = request.data.get('uid_number')
    
    if not uid_number:
        return Response({"error": "UID number is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Retrieve the student by UID
        student = Student.objects.get(uid_number=uid_number)
        
        # Compose the email
        subject = f"NFC Scan Alert for {student.student_name}"
        message = f"Hello,\n\nThis is to notify you that your child, {student.student_name}, has ."
        recipient_email = student.parent_email

        # Send the email
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False
        )

        return Response({"message": "Notification sent successfully"}, status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)