from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Journal)
admin.site.register(models.Project)
admin.site.register(models.Certification)
admin.site.register(models.MessageContact)