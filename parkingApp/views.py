from django.shortcuts import render
from parkingApp.models import Placemark
from parkingApp.models import Crime
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

# Create your views here.
def index(request):
	markers = Placemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')
	crimes = Crime.objects.values('description', 'address', 'lat', 'lon')

	return render(request, "index.html", {'markers': markers, 'crimes': crimes})
