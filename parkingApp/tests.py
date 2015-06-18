from django.test import TestCase
from parkingApp.models import Placemark

class PlacemarkTestCase(TestCase):

    def setUp(self):
        Placemark.objects.create(placemark_id="1304", name="metered_parking", description="this is paid parking, and you can park here any time", lat="40.97348632846234", lon="06.978678676776")
		Placemark.objects.create(placemark_id="15609", name="metered_parking", description="this is paid parking, and you can park here any time", lat="40.97348632846234", lon="06.978678676776")
        Placemark.objects.create(placemark_id="16156", name="non_metered_parking", description="&lt;br&gt;Type: Metered Motorcycle Parking&lt;br&gt;Time Limit: no time limit&lt;br&gt;Rate: $1.00&lt;br&gt;Credit Card Enabled: No&lt;br&gt;Location: n/a&lt;br&gt;Nearest Intersection: n/a&lt;br&gt;Time in Effect: METER IN EFFECT: 9:00 AM TO 10:00 PM&lt;br&gt;Rush Hour Regulation: n/a&lt;br&gt;&lt;br&gt;&lt;a,&gt;Get directions&lt;/a&gt;")

    def test_correct_parkingspot_name(self):
        #parking spots are correctly identified by id
        test1 = Placemark.objects.get(placemark_id="1304")
        test2 = Placemark.objects.get(placemark_id="16156")
        self.assertEqual(test1.name, 'metered_parking')
        self.assertEqual(test2.name, 'non_metered_parking')
		   
		
	def test_parkingspot_description(self):
		#parking spots are correctly identified by id and retrieve description
		test1 = Placemark.objects.get(placemark_id="1304")
		test2 = Placemark.objects.get(placemark_id="16156")
		self.assertEqual(test1.description, 'this is paid parking, and you can park here any time')
        self.assertEqual(test2.description, '&lt;br&gt;Type: Metered Motorcycle Parking&lt;br&gt;Time Limit: no time limit&lt;br&gt;Rate: $1.00&lt;br&gt;Credit Card Enabled: No&lt;br&gt;Location: n/a&lt;br&gt;Nearest Intersection: n/a&lt;br&gt;Time in Effect: METER IN EFFECT: 9:00 AM TO 10:00 PM&lt;br&gt;Rush Hour Regulation: n/a&lt;br&gt;&lt;br&gt;&lt;a,&gt;Get directions&lt;/a&gt;')
	
		
	
	def test_parkingspot_filter(self):
		#parking spots are correctly identified by id and retrieve description
		self.assertEqual(Placemark.objects.filter(name__startswith='non_metered_parking'),'[<placemark_id="16156", name="non_metered_parking", description="&lt;br&gt;Type: Metered Motorcycle Parking&lt;br&gt;Time Limit: no time limit&lt;br&gt;Rate: $1.00&lt;br&gt;Credit Card Enabled: No&lt;br&gt;Location: n/a&lt;br&gt;Nearest Intersection: n/a&lt;br&gt;Time in Effect: METER IN EFFECT: 9:00 AM TO 10:00 PM&lt;br&gt;Rush Hour Regulation: n/a&lt;br&gt;&lt;br&gt;&lt;a,&gt;Get directions&lt;/a&gt;">]')