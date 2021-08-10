from django.db import models

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True)
	description = models.TextField()

	def __str__(self):
		return self.title


class SubCategory(models.Model):
	title = models.CharField(max_length = 400)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	slug = models.CharField(max_length = 500, unique = True)
	description = models.TextField()

	def __str__(self):
		return self.title

class Slider(models.Model):
	title = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True)
	description = models.TextField()
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField()
	status = models.CharField(max_length = 100,choices = (('active','active'),('','inactive')))

	def __str__(self):
		return self.title

class Product(models.Model):
	title = models.CharField(max_length = 500)
	price = models.IntegerField()
	discounted_price = models.IntegerField()
	status =  models.CharField(max_length = 100,choices = (('active','active'),('','inactive')))
	image = models.ImageField(upload_to = 'media')
	description = models.TextField(blank = True)
	labels = models.CharField(max_length = 100,choices = (('new','new'),('hot','hot'),('sale','sale')))
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory,on_delete = models.CASCADE)
	stock = models.CharField(max_length = 100,choices = (('In Stock','In Stock'),('Out of Stock','Out of Stock')))

	def __str__(self):
		return self.title