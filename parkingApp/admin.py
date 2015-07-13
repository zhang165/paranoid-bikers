from django.contrib import admin

from .models import Placemark, Crime, LowCrimePlacemark

# Register your models here.

class PlacemarkAdmin(admin.ModelAdmin):
	list_display = ('placemark_id', 'name', 'lat', 'lon')
admin.site.register(Placemark, PlacemarkAdmin)

class CrimeAdmin(admin.ModelAdmin):
	list_display = ('description','lat', 'lon')
admin.site.register(Crime, CrimeAdmin)

class LowCrimePlacemarkAdmin(admin.ModelAdmin):
	list_display = ('placemark_id', 'name', 'lat', 'lon')
admin.site.register(LowCrimePlacemark, LowCrimePlacemarkAdmin)
