from .views import *
from django.urls import path

app_name= "app"

urlpatterns = [
    path('', landing, name="landing_page"),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('single/', single_product, name="single_product"),
    path('all/', all_product, name="all_product"),

    
    
]