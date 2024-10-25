from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    uid_number = models.CharField(max_length=50)
    parent_contact = models.CharField(max_length=20)
    parent_email = models.EmailField()
    student_class = models.CharField(max_length=50)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student_name
