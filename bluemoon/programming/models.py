from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = MarkdownxField()
    pub_datetime = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=400)
    projectgraphic = models.ImageField(upload_to="gallery")
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
