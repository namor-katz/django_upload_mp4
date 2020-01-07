from django.forms import ModelForm,  FileField,  CharField,  widgets
from django.core.validators import FileExtensionValidator #это тестовое, не пробовал ранее
from .models import Mp4
#форму необходимо объявить во вьюхе
#вотзефак? какого хера нельзя указать 1 расширение? почему оно выдаёт ошибку, но всё равно сохраняет?

class Mp4Form(ModelForm):
    '''this form from upload files'''
    file_path = FileField(label="Ролик",  validators=[FileExtensionValidator(allowed_extensions=('mp4',  'xyz'))], 
    error_messages={'invalid_extension': 'Этот формат файлов не поддерживается'}
    )
    desc = CharField(label="описание",  help_text="Укажите описание файла! Это важно!",  widget=widgets.Textarea())
    
    class Meta:
        model = Mp4
        fields = ('file_path',  'desc')
        #help_texts = {'desc': 'Укажите описание файла! Это важно!'}  #нихт арбайт. разночтения в доках, пропущу.
