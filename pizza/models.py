from django.db import models

# Create your models here.from django.db import models
class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
