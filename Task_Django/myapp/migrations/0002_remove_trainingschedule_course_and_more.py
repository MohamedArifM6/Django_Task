# Generated by Django 5.0.4 on 2024-05-05 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingschedule',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student_details',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='student_details',
            name='user',
        ),
        migrations.RemoveField(
            model_name='studenttraining',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studenttraining',
            name='schedule',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student_Details',
        ),
        migrations.DeleteModel(
            name='StudentTraining',
        ),
        migrations.DeleteModel(
            name='TrainingSchedule',
        ),
    ]
