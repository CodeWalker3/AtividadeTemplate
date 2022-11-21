from django import forms
from .models import Restaurant, Delivery, Courier

class RestaurantForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Restaurant
        # specify fields to be used
        fields = [
            "name",
            "cnpj",
            "email",
            "active",
            "delivery"
        ]

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            "name",
            "total",
            "status",
            "courier"
        ]

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = [
            "name",
            "cpf",
            "email"
        ]
            