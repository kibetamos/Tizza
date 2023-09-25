from django.db import models
from django.db import User

# Create your models here.
from django.db import models

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    