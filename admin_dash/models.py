from django.db import models
# from ide.models import Student, StudentMarks

# Create your models here.
class Question(models.Model):
    q_id = models.AutoField(primary_key=True, unique=True, default=0)
    question_name = models.TextField(max_length=2000)
    correct_answer = models.TextField(max_length=2000)
    description = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.question_name

class Lecturer(models.Model):
    lec_id = models.AutoField(primary_key=True, unique=True, default=0)
    lec_name = models.CharField(max_length=70)
    lec_department = models.CharField(max_length=100, default='Computer Science')
    admin_password = models.CharField(max_length=32)
    admin_email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.lec_name


