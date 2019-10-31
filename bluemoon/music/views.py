from django.shortcuts import render
from music.models import Music
# Create your views here.
def index(request):
    musiclist=Music.objects.all()
    context={'music':musiclist}
    return render(request,'music/index.htm',context)
