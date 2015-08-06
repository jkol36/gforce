from django.contrib import admin
from gforce.app.models import ImpactEvent, TimeStamp

# Register your models here.

admin.site.register(ImpactEvent)
admin.site.register(TimeStamp)
