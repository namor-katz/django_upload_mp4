from django.forms import ModelForm
from .models import Mp4
#форму необходимо объявить во вьюхе

class Mp4Form(ModelForm):
    '''this form from upload files'''
    class Meta:
        model = Mp4
        fields = ('file_path',  'desc')
