from django.contrib import admin


# Register your models here.
from .models import Para, File , Word , Unique

admin.site.register(Para)
admin.site.register(Unique)
# admin.site.register(File)
# admin.site.register(Word)