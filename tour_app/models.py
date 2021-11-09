from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Itinerary(models.Model):
    """A user's saved itinerary of locations 

    Attributes:
        - id (PRIMARY KEY)
        - itinerary_name (NOT NULL)
        - locations (need another table for locations)
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
    )
    itinerary_name = models.CharField(max_length=100)

class Itinerary_location(models.Model):
    """Holds the locations of a given itinerary 

    Attributes:
        - id (PRIMARY KEY)
        - itinerary_id
        - location_name (NOT NULL) 
        - latitude (REAL UNIQUE NOT NULL)
        - longitude (REAL UNIQUE NOT NULL)       
    """
    itinerary = models.ForeignKey(
        Itinerary, 
        on_delete=models.CASCADE, 
    )
    loc_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=17, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)



class UserLocation(models.Model):
    """Stores a user's saved location

    Attributes:
        - id (PRIMARY KEY)
        - address (NOT NULL)
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=200)


class HistoricalLocation(models.Model):
    """Stores information regarding a historically relevant location

    Attributes:
        - id (PRIMARY KEY)
        - location_name (NOT NULL)
        - location_address (NOT NULL)
        - latitude (REAL UNIQUE NOT NULL)
        - longitude (REAL UNIQUE NOT NULL)
        - description (TEXT)
        - operation_hours (TIME)
        - pictures (BLOB)

    Notes:
        - latitude ranges from -90 - 90
        - longitude ranges from -180 to 80
        - both can store up to 15 decimal numbers 
    """
    loc_name = models.CharField(max_length=100)
    loc_address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=17, decimal_places=15, unique=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, unique=True)
    description = models.TextField()
    operation_hours = models.TimeField()
    pictures = models.BinaryField() 