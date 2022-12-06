from rest_framework import serializers
from .models import *


class Avg_Price_LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avg_Price_License
        fields = ['license', 'avg_price']
    # license = serializers.CharField(max_length=100)
    # avg_price = serializers.FloatField()


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Avg_Price_License` instance, given the validated data.
    #     """
    #     return Avg_Price_License.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Avg_Price_License` instance, given the validated data.
    #     """
    #     instance.license = validated_data.get('license', instance.license)
    #     instance.avg_price = validated_data.get('avg_price', instance.avg_price)
    #     instance.save()
    #     return instance

class Corela_Rooms_Beds_AccommodatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corela_Rooms_Beds_Accommodates
        fields = ['bedrooms', 'beds', 'accommodates']

    # bedrooms = serializers.FloatField()
    # beds = serializers.FloatField()
    # accommodates = serializers.FloatField()

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Corela_Rooms_Beds_Accommodates` instance, given the validated data.
    #     """
    #     return Corela_Rooms_Beds_Accommodates.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Corela_Rooms_Beds_Accommodates` instance, given the validated data.
    #     """
    #     instance.bedrooms = validated_data.get('bedrooms', instance.bedrooms)
    #     instance.beds = validated_data.get('beds', instance.beds)
    #     instance.accommodates = validated_data.get('accommodates', instance.accommodates)
    #     instance.save()
    #     return instance

class Price_NumberOfBedRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price_NumberOfBedRoom
        fields = ['bedrooms_nums', 'min', 'q1', 'median', 'q3', 'max']

    # bedrooms_nums = serializers.IntegerField()
    # min = serializers.FloatField()
    # q1 = serializers.FloatField()
    # median = serializers.FloatField()
    # q3 = serializers.FloatField()
    # max = serializers.FloatField()

    # def create(self, validated_data):
    #     """
    #     Create and return a new `price_numberOfBedRoom` instance, given the validated data.
    #     """
    #     return price_numberOfBedRoom.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `price_numberOfBedRoom` instance, given the validated data.
    #     """
    #     instance.bedrooms_nums = validated_data.get('bedrooms_nums', instance.bedrooms_nums)
    #     instance.min = validated_data.get('min', instance.min)
    #     instance.q1 = validated_data.get('q1', instance.q1)
    #     instance.median = validated_data.get('median', instance.median)
    #     instance.q3 = validated_data.get('q3', instance.q3)
    #     instance.max = validated_data.get('max', instance.max)
    #     instance.save()
    #     return instance

