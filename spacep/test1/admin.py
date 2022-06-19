from django.contrib import admin
from .models import Imges

class ImgesAdmin(admin.ModelAdmin):
  list_display = ('title','desc','image','code')


admin.site.register(Imges,ImgesAdmin)


