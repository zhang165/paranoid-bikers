from django.db import models

# Create your models here.

class Location(models.Model):
	lat = models.FloatField()
	lon = models.FloatField()

	def __unicode__(self):
		return self.Location

class ParkingSpot(models.Model):
	location = models.OneToOneField(Location)
	name = models.CharField(max_length=120)
	toll = models.DecimalField(max_digits= 4, decimal_places=2)
	#picture

	def __unicode__(self):
		return self.ParkingSpot