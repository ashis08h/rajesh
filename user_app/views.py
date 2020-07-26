from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Category, Programmer
from .serializers import LanguageSerializer, ProgrammerSerializer, CategorySerializer

class LanguageView(viewsets.ModelViewSet):
	queryset=Language.objects.all()
	serializer_class=LanguageSerializer

class CategoryView(viewsets.ModelViewSet):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer

class ProgrammerView(viewsets.ModelViewSet):
	queryset=Programmer.objects.all()
	serializer_class=ProgrammerSerializer