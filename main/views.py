from django.shortcuts import render
from .models import Restaurant, Delivery, Courier
from .forms import RestaurantForm, CourierForm, DeliveryForm
# Create your views here.

def home(request):
    return render(request, "home.html")

def restaurant(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants':restaurants
    }
    return render(request, "restaurant.html", context)

def restaurant_create_view(request):
    context = {}
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "restaurant_form.html", context)
    

def courier(request):
    couriers = Courier.objects.all()
    context = {
        'couriers': couriers
    }
    return render(request, "courier.html", context)

def courier_create_view(request):
    context = {}
    form = CourierForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "courier_form.html", context)

def delivery(request):
    deliveries = Delivery.objects.all()
    context = {
        'deliveries': deliveries
    }
    return render(request, "delivery.html", context) 
def delivery_create_view(request):
    context = {}
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "delivery_form.html", context)