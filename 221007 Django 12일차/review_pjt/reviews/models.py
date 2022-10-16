from email import contentmanager
from django.db import models

# Create your models here.
class Review(models.Model):
    # max_length는 byte 단위
    title = models.CharField(max_length=100)
    content = models.TextField
    movie_name = models.CharField(max_length=150)
    grade = models.FloatField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
