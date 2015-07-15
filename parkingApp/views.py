from django.shortcuts import render, render_to_response
from django.template import RequestContext
from parkingApp.models import Placemark, BikeTheft
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from django import forms

import django_excel as excel

import pyexcel.ext.xls
import pyexcel.ext.xlsx
#import pyexcel.ext.ods3
import sys

# Create your views here.
def index(request):
	markers = Placemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')
	markers_dict = {'markers': markers}
	return render(request, "index.html", markers_dict)

# Creating the View for IMPORTING bike theft data

data = [
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
]

class UploadFileForm(forms.Form):
	file = forms.FileField()


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        def choice_func(row):
            q = BikeTheft.objects.filter(BLock=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[BikeTheft],
                initializers=[None, choice_func],
                mapdicts=[
                    ['district', 'Weekday', 'Month', 'Year', 'Block', 'BlockCleaned', 'AddressConsolidated', 'lat', 'lon']
                 ]
                )
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render_to_response(
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        },
        context_instance=RequestContext(request))


