from django.db import models
#import uuid
from django.core.validators import FileExtensionValidator #это тестовое, не пробовал ранее

class Mp4(models.Model):
    file_name = models.CharField(max_length=100) #или уид. надо еще прикинуть.
    file_path = models.FileField(max_length=500,  verbose_name='загрузить файл!',  validators=[FileExtensionValidator(['mp4'])])
    file_type = models.CharField(max_length=100)
    file_size = models.IntegerField()
    file_hash = models.CharField(max_length=100)
    desc = models.CharField(max_length=100, verbose_name='описание') #опционально - описание
    
    class Meta:
        verbose_name = "Видеоролик"
        verbose_name_plural = "Видеоролики"
