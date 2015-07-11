import os

from xlrd import open_workbook
import urllib.request
from zipfile import ZipFile
from decimal import *

#xlsx_path = ''

#urllib.request.urlretrieve(xlsx_path, 'crimeData/crimeData.xlsx')

book = open_workbook("crimeData/crimeData.xlsx")

#for testing
sheet = book.sheet_by_index(0)

#for i in range(1, sheet.nrows):
#	print (sheet.cell(i,4).value) #description
#	print (sheet.cell(i,11).value) #address
#	print (sheet.cell(i,12).value) #lat
#	print (sheet.cell(i,13).value) #lon

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')
	# creates a 'crimeData' directory if one does not exist
	if  not (os.path.exists('crimeData')):
		os.mkdir('crimeData')

from parkingApp.models import Crime

for i in range(1, sheet.nrows):
	Crime.objects.get_or_create(description = (sheet.cell(i,4).value), 
    address = (sheet.cell(i,11).value), 
    lat = (sheet.cell(i,12).value),
    lon = (sheet.cell(i,13).value))