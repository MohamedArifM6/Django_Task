from rest_framework import serializers
from .models import Course, Student_Details, TrainingSchedule, StudentTraining

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Details
        fields = '__all__'

class TrainingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = '__all__'

class StudentTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTraining
        fields = '__all__'
