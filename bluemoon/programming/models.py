from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = MarkdownxField()
    pub_datetime = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=400)
    projectgraphic = models.ImageField(upload_to="gallery")
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def formatted_markdown(self):
        return markdownify(self.text)
