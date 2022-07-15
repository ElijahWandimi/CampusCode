from django.db import models
# from ide.models import Student

# Create your models here.
class Question(models.Model):
    question = models.TextField(max_length=2000)
    correct_answer = models.TextField(max_length=2000)
    description = models.TextField(max_length=1000)

class Lecturer(models.Model):
    full_name = models.CharField(max_length=70)
    admin_password = models.CharField(max_length=32)
    admin_email = models.EmailField(max_length=100)

# class StudentProgress(models.Model):
#     student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
#     student_marks = models.ForeignKey(StudentMarks, on_delete=models.CASCADE)
