from django.db import models

CLASS_CHOICES = [(i, f"Class {i}") for i in range(1, 8)]  # 1 to 7 as choices

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    uid_number = models.CharField(max_length=50)
    parent_contact = models.CharField(max_length=15)
    parent_email = models.EmailField()
    student_class = models.IntegerField(choices=CLASS_CHOICES)  # Ensure this is IntegerField

    def __str__(self):
        return self.student_name