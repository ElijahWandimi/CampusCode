from django.db import models
from admin_dash.models import Question

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=32)
    course = models.CharField(max_length=100)


class Answer(models.Model):
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    code_text = models.TextField(max_length=2000)
    student_answer = models.TextField(max_length=2000)

class StudentMarks(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
