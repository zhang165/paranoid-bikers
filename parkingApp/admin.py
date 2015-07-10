from django.contrib import admin
from .models import Placemark
from .models import BikeTheft

# Register your models here.

class PlacemarkAdmin(admin.ModelAdmin):
	list_display = ('placemark_id', 'name')


admin.site.register(Placemark, PlacemarkAdmin)
admin.site.register(BikeTheft)