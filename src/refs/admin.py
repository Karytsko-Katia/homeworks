from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Region)
admin.site.register(models.Genre)
admin.site.register(models.Publishing)
