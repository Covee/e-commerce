from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20, default=9900)

	def __init__(self):
		return self.title

	# for Python 2
	def __unicode__(self):
		return self.title