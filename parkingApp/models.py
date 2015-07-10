from django.db import models

# Create your models here.

class Placemark(models.Model):
	placemark_id = models.CharField(max_length=30)
	name = models.CharField(max_length=50)
	#description = models.CharField(max_length=300)
	rate = models.CharField(max_length=300, default = "")
	credit_card = models.CharField(max_length=300, default = "")
	location = models.CharField(max_length=300, default = "")
	intersection = models.CharField(max_length=300, default = "")
	time = models.CharField(max_length=300, default = "")
	link = models.CharField(max_length=300, default = "")
	lat = models.DecimalField(max_digits=20, decimal_places=14)
	lon = models.DecimalField(max_digits=20, decimal_places=14)
	def __str__(self):
		return self.placemark_id

class BikeTheft(models.Model):
	district = models.IntegerField(default=0)
	Weekday = models.IntegerField(default=0)
	Month = models.CharField(max_length=300, default="")
	Year = models.IntegerField(default=0)
	Block = models.CharField(max_length=300, default="")
	BlockCleaned= models.CharField(max_length=300, default="")
	AddressConsolidated = models.CharField(max_length=300, default="")
	lat = models.DecimalField(max_digits=20, decimal_places=14)
	lon = models.DecimalField(max_digits=20, decimal_places=14)
	def __str__(self):
		return self.Block