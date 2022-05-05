from django.db import models

# Create your models here.
class UserProfile(models.Model):
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)