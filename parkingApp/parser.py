import xml.etree.ElementTree as ET
import urllib.request
from zipfile import ZipFile


def createXML(kml, filename):
	root = ET.Element("Document")
	comment = ET.Comment("Prepared for ParanoidBikers")
	root.append(comment)

	for i in range(1, len(kml)):
		placemark = ET.Element("Placemark")
		root.append(placemark)

		# add name to Placemark
		name = ET.SubElement(placemark, "name")
		name.text = kml[i][0].text

		# add description to Placemark
		description = ET.SubElement(placemark, "description")
		description.text = kml[i][1].text

		# add a Point to Placemark
		point = ET.SubElement(placemark, "Point")

		# add coordinates to Point
		coordinates = ET.SubElement(point, "coordinates")
		coordinates.text = kml[i][3][0].text


	tree = ET.ElementTree(root)
	with open(filename, "wb") as fh:
		tree.write(fh)

if __name__ == '__main__':
	# The path to our kmz file
	KMZ_PATH = 'http://data.vancouver.ca/download/kml/motorcycle_parking.kmz'
	# Retrieve the file and save it locally
	urllib.request.urlretrieve(KMZ_PATH, 'motorcycle_parking.kmz')
	# Unzip the kmz file
	KMZ_FILE = ZipFile('motorcycle_parking.kmz', 'r')
	# Open the kml file or extract the kml file from the kmz file
	KML_FILE = KMZ_FILE.extract('motorcycle_parking.kml')
	# Close the kmz file
	KMZ_FILE.close()

	tree = ET.parse(KML_FILE)
	root = tree.getroot()
	folder = root[0][3]

	filename = "motorcycle_parking.xml"
	createXML(folder, filename)
	