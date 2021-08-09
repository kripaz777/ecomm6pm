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
	status = models.CharField(choices = (('active','active'),('','inactive')))

	def __str__(self):
		return self.title