from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

import json
from .utils import *

@api_view(['GET'])
def avg_price_license_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        avg_price_license = Avg_Price_License.objects.all()
        if avg_price_license.exists():
            serializer = Avg_Price_LicenseSerializer(avg_price_license, many=True)
        # init the data from reading the csv file
        else:
            read_avg_price_license()
            serializer = Avg_Price_LicenseSerializer(avg_price_license, many=True)
        print(serializer.data)
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
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        corela_rooms_beds_accommodates = Corela_Rooms_Beds_Accommodates.objects.all()
        serializer = Corela_Rooms_Beds_AccommodatesSerializer(corela_rooms_beds_accommodates, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def price_numberOfBedRoom_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        price_numberOfBedRoom = Price_NumberOfBedRoom.objects.all()
        serializer = Price_NumberOfBedRoomSerializer(price_numberOfBedRoom, many=True)
        return Response(serializer.data)


