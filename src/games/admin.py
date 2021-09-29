from django.contrib import admin
from .models import Engine, Platform, PlatformType, Game
# Register your models here.

admin.site.register(Engine)
admin.site.register(Platform)
admin.site.register(PlatformType)
admin.site.register(Game)
