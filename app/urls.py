from .views import *
from django.urls import path

app_name= "app"

urlpatterns = [
    path('', landing, name="landing_page"),

    
    
]