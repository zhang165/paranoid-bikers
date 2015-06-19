from django.test import TestCase
from parkingApp.models import Placemark

class PlacemarkTestCase(TestCase):

	def setUp(self):
		Placemark.objects.create(placemark_id="1234", name="metered_parking", credit_card="no", location="smith street", intersection="yes", time="3 hours", link="yes", lat="40.12345678", lon="06.0123456")
		Placemark.objects.create(placemark_id="5678", name="metered_parking", credit_card="no", location="10th street", intersection="no", time="4 hours", link="yes", lat="40.567890", lon="06.123456")
		Placemark.objects.create(placemark_id="1122", name="non_metered_parking", credit_card="no", location="Joffre Ave", intersection="yes", time="no time",link="yes", lat="50.1234567", lon="06.1234567")
	
	def test_retrieve(self):
		test1 = Placemark.objects.get(placemark_id="1234")
		test2 = Placemark.objects.get(placemark_id="1122")
		self.assertEqual(test1.name, 'metered_parking')
		self.assertEqual(test2.name, 'non_metered_parking')
		
