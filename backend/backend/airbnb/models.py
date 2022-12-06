from django.db import models

# Create your models here.



class Avg_Price_License(models.Model):
    license = models.CharField(max_length=100)
    avg_price = models.FloatField()


class Corela_Rooms_Beds_Accommodates(models.Model):
    bedrooms = models.FloatField()
    beds = models.FloatField()
    accommodates = models.FloatField()


class Price_NumberOfBedRoom(models.Model):
    bedrooms_nums = models.IntegerField()
    min = models.FloatField()
    q1 = models.FloatField()
    median = models.FloatField()
    q3 = models.FloatField()
    max = models.FloatField()

