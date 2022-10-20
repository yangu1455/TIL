from email import contentmanager
from django.db import models

# Create your models here.
class Review(models.Model):
    # max_length는 byte 단위
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    movie_name = models.CharField(max_length=150)
    grade = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
