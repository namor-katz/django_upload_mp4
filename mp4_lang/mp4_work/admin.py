from django.contrib import admin
from .models import Mp4
from django.contrib.auth.models import User, Group
# Register your models here.
#unregister standard models
admin.site.unregister(User)
admin.site.unregister(Group)

#admin.site.register(Mp4)  #old
@admin.register(Mp4)
class pMp4(admin.ModelAdmin):
    list_display = ("file_path",  "desc", "file_convert",  "uploaded_at") #это что. переопределение __string-a?
    prepopulated_fields = {'file_name': ("file_path", )}
    ordering = ('uploaded_at', )
