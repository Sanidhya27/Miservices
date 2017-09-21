from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name=models.CharField(max_length=100,blank=False)
	def __str__(self):
		return self.name
class ProductRequest(models.Model):
	Department=models.TextField(default="")
	quantityname=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantitydemanded=models.IntegerField(default=0)
	quantitysupplied=models.IntegerField(default=0)
	