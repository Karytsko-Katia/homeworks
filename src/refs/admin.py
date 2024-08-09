from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Region)
admin.site.register(models.Genre)
admin.site.register(models.Publishing)
admin.site.register(models.Author)
admin.site.register(models.Serie)
admin.site.register(models.SeriesPrivately)
admin.site.register(models.Publishingnew)