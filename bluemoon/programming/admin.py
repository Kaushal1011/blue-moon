from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post
# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)
