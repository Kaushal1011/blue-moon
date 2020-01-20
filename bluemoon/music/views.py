from django.shortcuts import render
from programming.models import Post
# Create your views here.


def index(request):
    postlist = Post.objects.all()
    context = {'post': postlist}
    return render(request, 'programming/index.htm', context)
