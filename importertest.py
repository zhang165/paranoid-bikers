import os
import unittest
from django.test import TestCase

if __name__ == "__main__":
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')
	from parkingApp.models import Crime
	#import parser, importer

class SimpleTestCase(unittest.TestCase):

	def setUp(self):
		print("Running tests")
		
	def testPopulate(self):
		markers = Crime.objects.values('description', 'address', 'lat', 'lon')
		assert len(markers) == 7864

unittest.main()
