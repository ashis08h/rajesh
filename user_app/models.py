#Importing requied class and methods
from django.db import models

# Create your models here.

#This Model is Used to store the user information in database fields of this model are real name and tz(time zone)
class Category(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Language(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name
class Programmer(models.Model):
	name=models.CharField(max_length=50)
	language=models.ManyToManyField(Language)
	category=models.ManyToManyField(Category)

	def __str__(self):
		return self.name
