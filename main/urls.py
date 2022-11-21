from django.contrib import admin
from django.urls import path
from .views import delivery, restaurant, courier, home, restaurant_create_view, delivery_create_view, courier_create_view


urlpatterns = [
    # path('', teste),
    path('couriers', courier, name ='couriers'),
    path('deliveries', delivery, name= 'deliveries'),
    path('restaurants', restaurant, name = 'restaurants'),
    path('restaurants_new', restaurant_create_view, name= 'restaurant_create'),
    path('courier_new', courier_create_view, name= 'courier_create'),
    path('delivery_new', delivery_create_view, name= 'delivery_create'),
    path('', home, name='home')
]