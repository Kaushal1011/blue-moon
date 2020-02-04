from django.http import Http404
from django.shortcuts import render
from programming.models import Post
# Create your views here.


def index(request):
    postlist = Post.objects.all()
    context = {'post': postlist}
    return render(request, 'programming/index.htm', context)


def readmore(request, title):
    try:
        p = Post.objects.get(title=title)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'programming/detail.htm', {'Post': p})
