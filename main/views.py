from django.shortcuts import render
from .models import Restaurant, Delivery, Courier
# Create your views here.

def home(request):
    return render(request, "home.html")

def restaurant(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants':restaurants
    }
    return render(request, "restaurant.html", context)

def courier(request):
    couriers = Courier.objects.all()
    context = {
        'couriers': couriers
    }
    return render(request, "courier.html", context)

def delivery(request):
    deliveries = Delivery.objects.all()
    context = {
        'deliveries': deliveries
    }
    return render(request, "delivery.html", context) 