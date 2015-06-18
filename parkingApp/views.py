from django.shortcuts import render
from parkingApp.models import Placemark
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

# Create your views here.
def index(request):
	markers = Placemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')
	markers_dict = {'markers': markers}
	return render(request, "index.html", markers_dict)
