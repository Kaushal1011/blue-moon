from django.db import models

# Create your models here.

class Music(models.Model):
    name=models.CharField(max_length=30)
    artistname=models.CharField(max_length=30)
    albumname=models.CharField(max_length=40)
    description=models.CharField(max_length=255)
    albumart = models.ImageField(upload_to="gallery")
    link=models.CharField(max_length=255)
