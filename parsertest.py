import os
import unittest
from django.test import TestCase

if __name__ == "__main__":
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')
	from parkingApp.models import Placemark
	from parkingApp.models import LowCrimePlacemark
	#import parser, importer

class SimpleTestCase(unittest.TestCase):

	def setUp(self):
		print("Running tests")
		
	def testPopulate(self):
		markers = Placemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')
		assert len(markers) == 242

	def testCrimes(self):
		crimes = Crime.objects.values('description', 'address', 'lat', 'lon')
		assert len(crimes) == 100

unittest.main()
