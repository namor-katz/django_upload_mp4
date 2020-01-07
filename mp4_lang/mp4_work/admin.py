from django.contrib import admin
from .models import Mp4
# Register your models here.

#admin.site.register(Mp4)
@admin.register(Mp4)
class pMp4(admin.ModelAdmin):
    list_display = ("file_path",  "desc") #это что. переопределение __string-a?
    prepopulated_fields = {'file_name': ("file_path", )}
