from django.db import models

# Create your models here.

class Sug(models.Model):
    name = models.CharField(max_length=10 , default="")
    email = models.EmailField(max_length=30 , default="")
    text = models.TextField(default="")

