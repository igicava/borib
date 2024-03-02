from django.contrib import admin
from messenger import models

admin.site.register(models.Message)
admin.site.register(models.Contact)
