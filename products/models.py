from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	stock = models.IntegerField()
	image_url = models.CharField(max_length=2083)


class Offers(models.Model):
	code = models.TextField(max_length=255)
	description = models.TextField(max_length=255)
	discount = models.FloatField()