from django.contrib import admin

from shop import models

admin.site.register(models.Good)
admin.site.register(models.Shop)