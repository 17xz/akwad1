from django.db import models
import os.path

class Imges(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    desc = models.TextField()
    code = models.TextField(default="code")


