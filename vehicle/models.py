
from django.db import models

# Create your models here.
class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.vehicle_type
    
class Vehicles(models.Model):
    vehicle_number=models.CharField(max_length=50)
    type=models.ForeignKey(VehicleType,on_delete=models.CASCADE)
    vehicle_model=models.CharField(max_length=10)
    vehicle_description=models.TextField(max_length=200)
    
    def __str__(self):
        return self.vehicle_number