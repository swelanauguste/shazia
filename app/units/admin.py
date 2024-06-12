from django.contrib import admin

from .models import Condition, Location, Unit


admin.site.register(Condition)
admin.site.register(Location)
admin.site.register(Unit)
