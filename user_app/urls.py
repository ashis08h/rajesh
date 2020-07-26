#Importing requied class and methods
from django.urls import path,include
from user_app import views
from rest_framework import routers

#All the routing url for the application 
router = routers.DefaultRouter()
router.register("language", views.LanguageView)
router.register("category", views.CategoryView)
router.register("programmer", views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls)),
    
]
