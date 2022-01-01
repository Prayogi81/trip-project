from django.db import models

# Create your models here.

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    wifi = models.CharField(max_length=3)
    toilet = models.CharField(max_length=3)
    smokingarea = models.CharField(max_length=3)
    ac_room = models.CharField(max_length=3)
    avg_price = models.IntegerField()

    def __str__(self):
        return self.name