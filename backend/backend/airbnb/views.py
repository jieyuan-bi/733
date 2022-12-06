from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

import json
from .utils import *


# api views of kevin data
@api_view(['GET'])
def avg_price_license_list(request):
    """
    Data processed by Kevin
    Average Price by having License or not
    Return a json format of avg_price_license
    """
    if request.method == 'GET':
        avg_price_license = Avg_Price_License.objects.all()
        if avg_price_license.exists():
            serializer = Avg_Price_LicenseSerializer(avg_price_license, many=True)
        # init the data from reading the csv file
        else:
            read_avg_price_license()
            serializer = Avg_Price_LicenseSerializer(avg_price_license, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def corela_rooms_beds_accommodates_list(request):
    """
    Data processed by Kevin
    Correlation between bedrooms_num, beds_num and accommodates
    Return a json format of corela_rooms_beds_accommodates
    """
    if request.method == 'GET':
        corela_rooms_beds_accommodates = Corela_Rooms_Beds_Accommodates.objects.all()
        if corela_rooms_beds_accommodates.exists():
            serializer = Corela_Rooms_Beds_AccommodatesSerializer(corela_rooms_beds_accommodates, many=True)
        # init the data from reading the csv file
        else:
            read_corela_rooms_beds_accommodates()
            serializer = Corela_Rooms_Beds_AccommodatesSerializer(corela_rooms_beds_accommodates, many=True)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def price_numberOfBedRoom_list(request):
    """
    Data processed by Kevin
    Price Distribution by BedRooms_number
    Return a json format of price_numberOfBedRoom
    """
    if request.method == 'GET':
        price_numberOfBedRoom = Price_NumberOfBedRoom.objects.all()
        if price_numberOfBedRoom.exists():
            serializer = Price_NumberOfBedRoomSerializer(price_numberOfBedRoom, many=True)
        # init the data from reading the csv file
        else:
            read_price_numberOfBedRoom()
            serializer = Price_NumberOfBedRoomSerializer(price_numberOfBedRoom, many=True)
        # print(serializer.data)
        return Response(serializer.data)




# api views of tony data
@api_view(['GET'])
def priceWithMonth_list(request):
    """
    Data processed by Kevin
    Return a json format of priceWithMonth
    """
    if request.method == 'GET':
        price_with_month = priceWithMonth.objects.all()
        if price_with_month.exists():
            serializer = PriceWithMonthSerializer(price_with_month, many=True)
        # init the data from reading the csv file
        else:
            read_priceWithMonth()
            serializer = PriceWithMonthSerializer(price_with_month, many=True)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def priceWithSpace_list(request):
    """
    Data processed by Kevin
    Return a json format of price_with_space
    """
    if request.method == 'GET':
        price_with_space = priceWithSpace.objects.all()
        if price_with_space.exists():
            serializer = PriceWithSpaceSerializer(price_with_space, many=True)
        # init the data from reading the csv file
        else:
            read_priceWithSpace()
            serializer = PriceWithSpaceSerializer(price_with_space, many=True)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def priceWithType_list(request):
    """
    Data processed by Kevin
    Return a json format of price_numberOfBedRoom
    """
    if request.method == 'GET':
        price_with_type = priceWithType.objects.all()
        if price_with_type.exists():
            serializer = PriceWithTypeSerializer(price_with_type, many=True)
        # init the data from reading the csv file
        else:
            read_priceWithType()
            serializer = PriceWithTypeSerializer(price_with_type, many=True)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def priceWithWeek_list(request):
    """
    Data processed by Kevin
    Return a json format of priceWithWeek
    """
    if request.method == 'GET':
        price_with_week = priceWithWeek.objects.all()
        if price_with_week.exists():
            serializer = PriceWithWeekSerializer(price_with_week, many=True)
        # init the data from reading the csv file
        else:
            read_priceWithWeek()
            serializer = PriceWithWeekSerializer(price_with_week, many=True)
        # print(serializer.data)
        return Response(serializer.data)



# api views of calla data


