from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.course_title

class Student_Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.user.username

class TrainingSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_title} - {self.date}"

class StudentTraining(models.Model):
    student = models.ForeignKey(Student_Details, on_delete=models.CASCADE)
    schedule = models.ForeignKey(TrainingSchedule, on_delete=models.CASCADE)
    opted_in = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username} - {self.schedule.course.name}"
