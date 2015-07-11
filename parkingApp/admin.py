from django.contrib import admin
from .models import Placemark, Crime

# Register your models here.

class PlacemarkAdmin(admin.ModelAdmin):
	list_display = ('placemark_id', 'name')

admin.site.register(Placemark, PlacemarkAdmin)

class CrimeAdmin(admin.ModelAdmin):
	list_display = ('description','lat', 'lon')

admin.site.register(Crime, CrimeAdmin)
