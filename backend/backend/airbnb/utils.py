import csv
import json
import os
from django.conf import settings

from .models import *
from .serializers import *

'''
data from kevin
read the csv file and init the data to database
'''
def read_avg_price_license():
    file_name = "airbnb/analysis_results/avg_price_license/avg_price_license.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'license': row['license'], 'avg_price': float(row['avg_price'])}
            serializer = Avg_Price_LicenseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Avg_Price_LicenseSerializer failed!")

'''
data from kevin
read the csv file and init the data to database
'''
def read_corela_rooms_beds_accommodates():
    file_name = "airbnb/analysis_results/corela_rooms_beds_accommodates/corela_rooms_beds_accommodates.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'bedrooms': float(row['bedrooms']), 'beds': float(row['beds']), 'accommodates': float(row['accommodates'])}
            serializer = Corela_Rooms_Beds_AccommodatesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Corela_Rooms_Beds_AccommodatesSerializer failed!")    


'''
data from kevin
read the csv file and init the data to database
'''
def read_price_numberOfBedRoom():
    file_name = "airbnb/analysis_results/price_numberOfBedRoom/price_numberOfBedRoom.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'bedrooms_nums': int(row['bedrooms_nums']), 'min': float(row['min']), 'q1': float(row['Q1']),
            'median': float(row['median']), 'q3': float(row['Q3']), 'max': float(row['max'])}
            serializer = Price_NumberOfBedRoomSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------read_price_numberOfBedRoom failed!")  



'''
data from tony
read the csv file and init the data to database
'''
def read_priceWithMonth():
    file_name = "airbnb/analysis_results/priceWithMonth/priceWithMonth.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'month': row['Month'], 'average_price': float(row['average_price($)'])}
            serializer = PriceWithMonthSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------PriceWithMonthSerializer failed!")  

'''
data from tony
read the csv file and init the data to database
'''
def read_priceWithSpace():
    file_name = "airbnb/analysis_results/priceWithSpace/priceWithSpace.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'neighbourhood': row['neighbourhood'], 'average_price': float(row['average_price($)'])}
            serializer = PriceWithSpaceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------PriceWithSpaceSerializer failed!")  

'''
data from tony
read the csv file and init the data to database
'''
def read_priceWithType():
    file_name = "airbnb/analysis_results/priceWithType/priceWithType.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'room_type': row['room_type'], 'average_price': float(row['average_price($)'])}
            serializer = PriceWithTypeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------PriceWithTypeSerializer failed!")  

'''
data from tony
read the csv file and init the data to database
'''
def read_priceWithWeek():
    file_name = "airbnb/analysis_results/priceWithWeek/priceWithWeek.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'week': row['week'], 'average_price': float(row['priceWithWeek($)'])}
            serializer = PriceWithWeekSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------PriceWithWeekSerializer failed!")  

