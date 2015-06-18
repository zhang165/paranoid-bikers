import os

import xml.etree.ElementTree as ET
import urllib.request
from zipfile import ZipFile
from decimal import *
def createXML(kml, filename):
	'''
	String, String -> None

	takes a kml filename and xml filename and parses
	through the kml to write into an xml 
	'''
	root = ET.Element("Document")
	comment = ET.Comment("Prepared for ParanoidBikers")
	root.append(comment)

	for i in range(1, len(kml)):
		placemark = ET.Element("Placemark")
		root.append(placemark)

		# add id to Placemark
		placemark_id = ET.SubElement(placemark, "id")
		placemark_id_text = kml[i].get('id')
		placemark_id.text = placemark_id_text
 
		# add name to Placemark
		name = ET.SubElement(placemark, "name")
		name_text = kml[i][0].text
		name.text = name_text

		# add description to Placemark
		description = ET.SubElement(placemark, "description")
		description_text = kml[i][1].text
		joiner = "<br>"
		description_list = description_text.split(joiner)
		description_text = joiner
		for desc in description_list[3:8]:
			description_text += desc + joiner
		description_text += description_list[10] + joiner
		description.text = description_text


		# add a Point to Placemark
		point = ET.SubElement(placemark, "Point")

		# add coordinates to Point called lat and lon
		coordinates = ET.SubElement(point, "coordinates")
		# first split lat from lon using , splitting
		latlon = kml[i][3][0].text.split(",")

		lat = ET.SubElement(coordinates, "lat")
		lat_text = latlon[0]
		lat.text = lat_text
		lat_dec = Decimal(lat_text)

		lon = ET.SubElement(coordinates, "lon")
		lon_text = latlon[1]
		lon.text = lon_text
		lon_dec = Decimal(lon_text)

		# create a Placemark object in the database
		add_placemark(placemark_id = placemark_id_text, 
						name = name_text,
						#description = description_text,
						rate = description_list[3],
						credit_card = description_list[4],
						location = description_list[5],
						intersection = description_list[6],
						time = description_list[7],
						link = description_list[10],
						lat = lat_dec,
						lon = lon_dec)

	tree = ET.ElementTree(root)
	with open(filename, "wb") as fh:
		tree.write(fh)


def toKML(url):
	'''
	string -> None

	takes url of kmz file and unzips it and extracts the kml file
	'''
	kmz_path = url
	urllib.request.urlretrieve(kmz_path, 'parkingData/kmz_file.kmz')
	kmz_file = ZipFile('parkingData/kmz_file.kmz')
	kml_file = kmz_file.extract('motorcycle_parking.kml', 'parkingData')
	kmz_file.close()

def getRoot(kmlFilename):
	tree = ET.parse(kmlFilename)
	root = tree.getroot()
	folder = root[0][3]
	return folder


def parser(url, kmlFilename, xmlfilename):
	toKML(url)
	kmlFilename = 'parkingData/motorcycle_parking.kml'
	kml = getRoot(kmlFilename)
	createXML(kml, xmlfilename)

def add_placemark(placemark_id, name, rate, credit_card, location, intersection,
time, link, lat=1, lon=2):
    p = Placemark.objects.get_or_create(placemark_id = placemark_id, 
    	name = name, 
    	rate = rate, 
    	credit_card = credit_card,
    	location = location,
    	intersection = intersection,
    	time = time,
    	link = link,
    	lat = lat, 
    	lon = lon)[0]
    return p

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')
	# creates a 'parkingData' directory if one does not exist
	if  not (os.path.exists('parkingData')):
		os.mkdir('parkingData')
	from parkingApp.models import Placemark
	print("parsing and populating for parkingApp")
	# The path to our kmz file
	KMZ_PATH = 'http://data.vancouver.ca/download/kml/motorcycle_parking.kmz'
	# Retrieve the file and save it locally
	#urllib.request.urlretrieve(KMZ_PATH, 'motorcycle_parking.kmz')
	# Unzip the kmz file
	#KMZ_FILE = ZipFile('motorcycle_parking.kmz', 'r')
	# Open the kml file or extract the kml file from the kmz file
	#KML_FILE = KMZ_FILE.extract('motorcycle_parking.kml')
	# Close the kmz file
	#KMZ_FILE.close()

	#tree = ET.parse(KML_FILE)
	#root = tree.getroot()
	#folder = root[0][3]

	xmlfilename = "parkingData/motorcycle_parking.xml"
	kmlfilename = "parkingData/motorcycle_parking.kml"
	# createXML(folder, xmlfilename)
	parser(KMZ_PATH, kmlfilename, xmlfilename)
	