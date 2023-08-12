from django.contrib import admin
from .models import MainImage, SmallImages,ShoeColor,ShoeSize
# Register your models here.
 
admin.site.register(MainImage)
admin.site.register(SmallImages)
admin.site.register(ShoeColor)
admin.site.register(ShoeSize)