from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from jobseeker.models import PostCV
from django.db.models import Q
from django.conf import settings

# Create your models here.
class Post(models.Model):
    Employer = models.ForeignKey(User, on_delete=models.CASCADE)
    Job_Name = models.CharField(max_length=100)
    Job_Description = models.TextField()
    Job_Date = models.DateTimeField(default=timezone.now)
    Job_Requirements = models.TextField()
    Job_Qualifications = models.TextField()

    def __str__(self):
        return self.Job_Name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
