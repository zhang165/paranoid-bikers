import os
import unittest
from django.test import TestCase

if __name__ == "__main__":
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')
	from parkingApp.models import Crime, LowCrimePlacemark
	#import parser, importer

class SimpleTestCase(unittest.TestCase):

	def setUp(self):
		print("Running tests")
		
	def testPopulate(self):
		print("Running importer")
		markers = Crime.objects.values('description', 'address', 'lat', 'lon')
		assert len(markers) == 7864

	def testFilter(self):
		print("Running filter")
		markers = LowCrimePlacemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')
		assert len(markers) == 29

unittest.main()
