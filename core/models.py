from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=225)
    position = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)




