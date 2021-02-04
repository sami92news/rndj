from django.db import models


class Student(models.Model):
    class Meta:
        ordering = ('-id',)
    student_name = models.CharField(max_length=255, null=True)
    student_phone_number = models.CharField(max_length=255, null=True)
    student_email = models.CharField(max_length=255, null=True)