from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField(default='')
    running_time = models.IntegerField(default=0)
