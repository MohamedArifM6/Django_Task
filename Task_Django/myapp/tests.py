from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Course, Student_Details, TrainingSchedule, StudentTraining

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_course_list_create(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_retrieve_update_destroy(self):
        course = Course.objects.create(course_title='Test Course', description='Test Description')
        response = self.client.get(f'/courses/{course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_list_create(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_retrieve_update_destroy(self):
        student = Student_Details.objects.create(user=self.user)
        response = self.client.get(f'/students/{student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schedule_list_create(self):
        response = self.client.get('/schedules/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schedule_retrieve_update_destroy(self):
        course = Course.objects.create(course_title='Test Course', description='Test Description')
        schedule = TrainingSchedule.objects.create(course=course, date='2024-05-10', start_time='09:00:00', end_time='12:00:00')
        response = self.client.get(f'/schedules/{schedule.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_training_list_create(self):
        response = self.client.get('/student-trainings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_training_retrieve_update_destroy(self):
        student = Student_Details.objects.create(user=self.user)
        course = Course.objects.create(course_title='Test Course', description='Test Description')
        schedule = TrainingSchedule.objects.create(course=course, date='2024-05-10', start_time='09:00:00', end_time='12:00:00')
        training = StudentTraining.objects.create(student=student, schedule=schedule, opted_in=True)
        response = self.client.get(f'/student-trainings/{training.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
