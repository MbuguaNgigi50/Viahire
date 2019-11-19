from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostCV(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Current_Job = models.CharField(max_length=100)
    Age = models.CharField(max_length=2)
    Email_Address = models.CharField(max_length=100)
    Telephone_Number = models.CharField(max_length=10)
    Employment_History = models.TextField()
    Education = models.TextField()
    Skills = models.TextField()
    Hobbies = models.TextField()
    Internships = models.TextField()
    Referress = models.TextField()

def __str__(self):
    return f'{self.user.username} CV Posts'

def save(self):
    super().save()
