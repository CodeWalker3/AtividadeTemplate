from django.db import models

# Create your models here.
class Courier(models.Model):
    name = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    def __str__(self):
        return self.name
class Delivery(models.Model):
    name = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=6,decimal_places=2)
    status = models.CharField(max_length=25)
    courier = models.ForeignKey(Courier, on_delete = models.CASCADE)
    def __str__(self):
        return self.name
class Restaurant(models.Model):
    name = models.CharField(max_length=25)
    cnpj = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    active = models.BooleanField(default=1)
    delivery = models.OneToOneField(Delivery, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.name