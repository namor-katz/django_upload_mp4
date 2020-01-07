from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from .models import Mp4
from .forms import Mp4Form
from django.views.generic.edit import CreateView

def index(request):
    ''' вернуть список фильмов-роликов '''
    mp4 = Mp4.objects.all()
    context = {'mp4': mp4}
    print(mp4)
    return render(request, 'mp4_work/index.html',  context)


class Mp4CreateView(CreateView):
    '''this class attached form from upload files'''
    template_name = 'mp4_work/create.html'
    form_class = Mp4Form
    success_url = "/mp4/"
    
    #def get_context_data(self,  **kwargs):
     #   context = super().get_context_data(**kwargs)
     #   context['rubrics']
