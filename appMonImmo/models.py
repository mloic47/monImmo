from django.db import models

# Create your models here.
class Property(models.Model):
    PROPERTY_STATUS_CHOICES = (
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=PROPERTY_STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class House(Property):
    nb_of_rooms = models.IntegerField()
    garden = models.BooleanField(default=False)

class Apartment(Property):
    nb_of_rooms = models.IntegerField()
    floor = models.IntegerField()
    elevator = models.BooleanField(default=False)

class Land(Property):
    area = models.DecimalField(max_digits=10, decimal_places=2)

class Office(Property):
    nb_of_halls = models.IntegerField()
    office_description = models.TextField()
    floor = models.IntegerField()
    elevator = models.BooleanField(default=False)

class Shop(Property):
    shop_description = models.TextField()
    floor = models.IntegerField()
    elevator = models.BooleanField(default=False)

class GuestHouse(Property):
    nb_of_rooms = models.IntegerField()
    garden = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    amenities = models.TextField()



    
