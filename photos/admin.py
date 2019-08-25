from django.contrib import admin

from .models import Postor,Image,Location,Category

class PostorAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

# Register your models here.
admin.site.register(Postor)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
