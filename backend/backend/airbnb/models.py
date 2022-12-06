from django.db import models

# Create your models here.


# models for kevin
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




# models for Tony

class priceWithMonth(models.Model):
    month = models.CharField(max_length=100)
    average_price = models.FloatField()

class priceWithSpace(models.Model):
    neighbourhood = models.CharField(max_length=100)
    average_price = models.FloatField()

class priceWithType(models.Model):
    room_type = models.CharField(max_length=100)
    average_price = models.FloatField()

class priceWithWeek(models.Model):
    week = models.CharField(max_length=100)
    average_price = models.FloatField()




# models for Cella
