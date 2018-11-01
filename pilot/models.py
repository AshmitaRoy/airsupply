from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(models.User, on_delete=models.CASCADE)
    is_clinic_manager = models.BooleanField(default=False)
    is_dispatcher = models.BooleanField(default=False)

class ClinicManager(UserProfile):
    pass

class Dispatcher(UserProfile):
    pass

class Clinic(models.Model):
    clinic_manager = models.ForeignKey(ClinicManager, on_delete=models.CASCADE)
    name = models.CharField(length=200)
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    altitude = models.IntegerField()
    pass

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2)
    shipping_weight = models.DecimalField()
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
