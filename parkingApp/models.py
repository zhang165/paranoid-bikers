from django.db import models

# Create your models here.

class Placemark(models.Model):
	placemark = models.CharField(max_length=30)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	lat = models.DecimalField(max_digits=20, decimal_places=14)
	lon = models.DecimalField(max_digits=20, decimal_places=14)
