from django.contrib import admin
from .models import Tag, Title, SpotInfo, AppUser

# Register your models here.
admin.site.register(Tag)
admin.site.register(Title)
admin.site.register(SpotInfo)
admin.site.register(AppUser)