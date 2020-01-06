from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from .models import Mp4

def index(request):
    ''' вернуть список фильмов-роликов '''
    mp4 = Mp4.objects.all()
    context = {'mp4': mp4}
    print(mp4)
    return render(request, 'mp4_work/index.html',  context)
