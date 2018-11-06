import uuid

from django.conf import settings
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_clinic_manager = models.BooleanField(default=False)
    is_dispatcher = models.BooleanField(default=False)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200) 
    token = models.CharField(max_length=200)

class ClinicManager(UserProfile):
    pass

class Dispatcher(UserProfile):
    pass

class Clinic(models.Model):
    clinic_manager = models.ForeignKey(ClinicManager, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    altitude = models.IntegerField()
    pass

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    shipping_weight = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField()

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clinic_manager = models.ForeignKey(ClinicManager, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    time_ordered = models.DateTimeField()
    time_dispatched = models.DateTimeField()
    time_delivered = models.DateTimeField()
    priority = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
