from django.contrib import admin
from .models import (
    Restaurant,
    Courier,
    Delivery
)
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Courier)
admin.site.register(Delivery)