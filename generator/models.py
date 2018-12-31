from django.db import models

# Create your models here.
class Response(models.Model):
    date = models.TextField(default="")
    prompt = models.TextField(default="")
    response = models.TextField(default="")
