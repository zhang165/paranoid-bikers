from django.db import models

# Create your models here.

class Placemark(models.Model):
	placemark_id = models.CharField(max_length=30)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	lat = models.DecimalField(max_digits=20, decimal_places=14)
	lon = models.DecimalField(max_digits=20, decimal_places=14)
	def __str__(self):
		return self.placemark_id
