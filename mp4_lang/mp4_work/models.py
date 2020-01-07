from django.db import models
#import uuid

class Mp4(models.Model):
    file_name = models.CharField(max_length=100,  blank=True,  null=True) #или уид. надо еще прикинуть.
    file_path = models.FileField(max_length=500,  verbose_name='загрузить файл!')
    file_type = models.CharField(max_length=100,  blank=True,  null=True)
    file_size = models.IntegerField(blank=True,  null=True)
    file_hash = models.CharField(max_length=100,  blank=True,  null=True)
    desc = models.CharField(max_length=100, verbose_name='описание') #опционально - описание
    
    class Meta:
        verbose_name = "Видеоролик"
        verbose_name_plural = "Видеоролики"
        
    def __str__(self):
        return self.desc
