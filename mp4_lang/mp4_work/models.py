from django.db import models
#import uuid
from django.core.exceptions import ValidationError
import ffmpy

convert = None

def validate_video(image):
    """ validate video 1) extends 2) size """
    file_size = image.file.size
    if image.name.endswith("mp4"):
        pass
    else:
        raise ValidationError("This not mp4!")

    limit_kb = 2500
    global convert
    if file_size > limit_kb * 1024:
        convert = True
        #raise ValidationError("Max size of file is %s KB" % limit_kb)
    else:
        #pass
        convert = False

    #limit_mb = 8
    #if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)


class Mp4(models.Model):
    #image = models.ImageField('Image', upload_to=image_upload_path, validators=[validate_image])
    file_name = models.CharField(max_length=100,  blank=True,  null=True) #или уид. надо еще прикинуть.
    file_path = models.FileField(max_length=500,  verbose_name='загрузить файл!',  upload_to='archives/%Y/%m/%d/',  validators=[validate_video])
    file_type = models.CharField(max_length=100,  blank=True,  null=True)
    file_size = models.IntegerField(blank=True,  null=True)
    file_hash = models.CharField(max_length=100,  blank=True,  null=True)
    desc = models.CharField(max_length=100, verbose_name='описание') #опционально - описание
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_convert = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Видеоролик"
        verbose_name_plural = "Видеоролики"

    def __str__(self):
        return self.desc
        
    def save(self,  *args,  **kwargs):
        global convert
        if convert is True:
            self.file_convert = True
        else:
            self.file_convert = False
        super(Mp4, self).save(*args, **kwargs)
