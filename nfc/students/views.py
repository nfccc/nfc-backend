from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # date_registered will be set automatically
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
