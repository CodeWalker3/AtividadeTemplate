from django.contrib import admin
from django.urls import path
from .views import delivery, restaurant, courier, home


urlpatterns = [
    # path('', teste),
    path('couriers', courier, name ='couriers'),
    path('deliveries', delivery, name= 'deliveries'),
    path('restaurants', restaurant, name = 'restaurants'),
    path('', home, name='home')
]