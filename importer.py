import os

from xlrd import open_workbook
import urllib.request
from zipfile import ZipFile

def toXLSX(url):
	'''
	string -> None
	takes url of kmz file and unzips it and extracts the kml file
	'''
	urllib.request.urlretrieve(url, 'crimeData/crime_file.zip')
	kmz_file = ZipFile('crimeData/kmz_file.kmz')
	kml_file = kmz_file.extract('motorcycle_parking.kml', 'crimeData')
	kmz_file.close()

XLSX_PATH = 'https://drive.google.com/file/d/0B5AELJGlYc4JN2NXSktGWE5lNEk/edit?usp=sharing'

#toXLSX(XLSX_PATH)
book = open_workbook("crimeData/crimeData.xlsx")
sheet = book.sheet_by_index(0)

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')
	# creates a 'crimeData' directory if one does not exist
	if  not (os.path.exists('crimeData')):
		os.mkdir('crimeData')

from parkingApp.models import Crime

print('Begin parsing')

for i in range(1, sheet.nrows):
	if (sheet.cell(i,12).value != '' and sheet.cell(i,13).value != ''):
		Crime.objects.get_or_create(description = (sheet.cell(i,4).value), 
    	address = (sheet.cell(i,11).value), 
    	lat = sheet.cell(i,12).value,
    	lon = sheet.cell(i,13).value)
		#print('Parsed line: '+ str(i))
		
print('Finished parsing')