import os
from decimal import *

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')

from parkingApp.models import Crime
from parkingApp.models import Placemark
from parkingApp.models import LowCrimePlacemark

DIST = Decimal(0.0005)

markers = Placemark.objects.values('name', 'lat', 'lon', 'placemark_id', 'rate', 'credit_card', 'location', 'intersection', 'time', 'link')
crimes = Crime.objects.values('description', 'address', 'lat', 'lon')

#for testing: count = 0
for m in markers:

	for c in crimes:
		create = True
		#for testing
		#print((c['lon'] - DIST <= m['lat'] <= c['lon'] + DIST) and (c['lat'] - DIST <= m['lon'] <= c['lat'] + DIST))

		if ((c['lon'] - DIST <= m['lat'] <= c['lon'] + DIST) and (c['lat'] - DIST <= m['lon'] <= c['lat'] + DIST)):
			create = False
			break

		#old algorithm
		'''
		if ((str(m['lat'])[:RADIUS] == str(c['lon'])[:RADIUS]) and (str(m['lon'])[:RADIUS] == str(c['lat'])[:RADIUS])):
			create = False
			break
		'''
	if (create == True):
		LowCrimePlacemark.objects.get_or_create(placemark_id = m['placemark_id'], 
    	name = m['name'], 
    	rate = m['rate'], 
    	credit_card = m['credit_card'],
    	location = m['location'],
    	intersection = m['intersection'],
    	time = m['time'],
    	link = m['link'],
    	lat = m['lat'], 
    	lon = m['lon'])		
		


