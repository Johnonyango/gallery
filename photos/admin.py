from django.contrib import admin

from .models import Postor,Image,tags


# Register your models here.
admin.site.register(Postor)
admin.site.register(Image)
admin.site.register(tags)
