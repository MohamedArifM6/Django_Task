from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListCreate.as_view()),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroy.as_view()),
    path('students/', views.StudentListCreate.as_view()),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
    path('schedules/', views.TrainingScheduleListCreate.as_view()),
    path('schedules/<int:pk>/', views.TrainingScheduleRetrieveUpdateDestroy.as_view()),
    path('student-trainings/', views.StudentTrainingListCreate.as_view()),
    path('student-trainings/<int:pk>/', views.StudentTrainingRetrieveUpdateDestroy.as_view()),
]
