from django.shortcuts import render
from parkingApp.models import Placemark, Crime, LowCrimePlacemark
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

# Create your views here.
def index(request):
	markers = Placemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')
	crimes = Crime.objects.values('description', 'address', 'lat', 'lon')
	lowcrimes = LowCrimePlacemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')

	return render(request, "index.html", {'markers': markers, 'crimes': crimes, 'lowcrimes' : lowcrimes})
