import os

import xml.etree.ElementTree as ET
import urllib.request
from zipfile import ZipFile

from models import Placemark

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
		description.text = description.text


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
		p = Placemark.objects.get_or_create(id = placemark_id_text, 
											name = name_text,
											description = description_text,
											lat = lat_dec,
											lon = lon_dec)
		p.save()

	tree = ET.ElementTree(root)
	with open(filename, "wb") as fh:
		tree.write(fh)

def toKML(url):
	'''
	string -> None

	takes url of kmz file and unzips it and extracts the kml file
	'''
	kmz_path = url
	urllib.request.urlretrieve(kmz_path, 'kmz_file.kmz')
	kmz_file = ZipFile('kmz_file.kmz')
	kml_file = kmz_file.extract('motorcycle_parking.kml')
	kmz_file.close()

def getRoot(kmlFilename):
	tree = ET.parse(kmlFilename)
	root = tree.getroot()
	folder = root[0][3]
	return folder


def parser(url, kmlFilename, xmlfilename):
	toKML(url)
	kmlFilename = 'motorcycle_parking.kml'
	kml = getRoot(kmlFilename)
	createXML(kml, xmlfilename)

if __name__ == '__main__':
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

	xmlfilename = "motorcycle_parking.xml"
	kmlfilename = 'motorcycle_parking.kml'
	# createXML(folder, xmlfilename)
	parser(KMZ_PATH, kmlfilename, xmlfilename)
	