from django.contrib import admin
from .models import Course, Student_Details, TrainingSchedule, StudentTraining

# Register your models here.
admin.site.register(Course)
admin.site.register(Student_Details)
admin.site.register(TrainingSchedule)
admin.site.register(StudentTraining)