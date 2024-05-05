from rest_framework import generics
from .models import Course, Student_Details, TrainingSchedule, StudentTraining
from .serializers import CourseSerializer, StudentSerializer, TrainingScheduleSerializer, StudentTrainingSerializer
from rest_framework.permissions import IsAuthenticate

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_Details.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student_Details.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class TrainingScheduleListCreate(generics.ListCreateAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer
    permission_classes = [IsAuthenticated]

class TrainingScheduleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer
    permission_classes = [IsAuthenticated]

class StudentTrainingListCreate(generics.ListCreateAPIView):
    queryset = StudentTraining.objects.all()
    serializer_class = StudentTrainingSerializer
    permission_classes = [IsAuthenticated]

class StudentTrainingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentTraining.objects.all()
    serializer_class = StudentTrainingSerializer
    permission_classes = [IsAuthenticated]