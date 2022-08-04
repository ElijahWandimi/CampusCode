from django.db import models
from admin_dash.models import Question

# Create your models here.
def upload_image(instance, filename):
    return "%s/%s" % (instance.user, filename)

class Student(models.Model):
    stud_id = models.AutoField(primary_key=True, unique=True, default=0)
    full_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=32)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, height_field='height_field', width_field='width_field')
    course = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.full_name


class Answer(models.Model):
    ans_id = models.AutoField(primary_key=True, unique=True, default=0)
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    code_text = models.TextField(max_length=2000)
    student_answer = models.TextField(max_length=2000)
    votes = models.IntegerField(default=0, null=True)

class StudentMarks(models.Model):
    mk_id = models.AutoField(primary_key=True, unique=True, default=0)
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
