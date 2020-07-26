from django.contrib import admin
from .models import Category, Programmer, Language 

# Register your models here.

#Here we are Registring the model to the django admin 
admin.site.register(Category)
admin.site.register(Programmer)
admin.site.register(Language)


