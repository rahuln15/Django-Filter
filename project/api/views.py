from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
# if want to apply locally than use below line 
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='Teacher_2')
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    filterset_fields = ['name','city']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)

