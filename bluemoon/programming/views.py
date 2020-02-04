from django.http import Http404
from django.shortcuts import render
from programming.models import Post
# Create your views here.


def index(request):
    postlist = Post.objects.all()
    context = {'post': postlist}
    return render(request, 'programming/index.htm', context)


def readmore(request, title):
    print(title)
    try:
        post = Post.objects.filter(title=title)[0]
    except post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'programming/detail.htm', {'post': post})
