from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
	productID = models.IntegerField(primary_key=True)
	productName= models.CharField(max_length=100)
	productDesc = models.CharField(max_length=500)
	productStock = models.IntegerField()
	productPrice = models.IntegerField()
	productCPrice= models.IntegerField(default=0)
	
	def __str__(self):
		return self.productName

class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='images')
	image = models.ImageField(upload_to='product/')
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title