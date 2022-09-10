from django.contrib import admin

# Register your models here.
from projects_api import models

admin.site.register(models.Project)
admin.site.register(models.Space)
admin.site.register(models.ProjectSpace)
