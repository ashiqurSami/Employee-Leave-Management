from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    date_joined=models.DateField(auto_now_add=True)
    profile_photo=models.ImageField(upload_to="profiles/",blank=True)

    def __str__(self):
        return self.user.username

# Create your models here.
