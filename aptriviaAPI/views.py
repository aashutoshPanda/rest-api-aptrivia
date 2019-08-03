from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here
class AllStudents(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):

    def get(self, request, pk, format=None):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_200_OK)