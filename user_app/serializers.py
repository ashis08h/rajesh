#Importing requied class and methods
from rest_framework import serializers
from .models import Language, Category, Programmer



class LanguageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model=Language
		fields=("id", "url", "name")

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model=Category
		fields=("id", "url", "name")

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model=Programmer
		fields=("id", "url", "name", "language","category")
