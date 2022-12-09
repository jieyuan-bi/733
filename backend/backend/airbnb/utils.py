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
            data = {'month': row['Month'], 'average_price': float(row['average_price($)']), 'median_price': float(row['median_price($)'])}
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
        reader = csv.DictReader(csvfile,delimiter='\t')

        for row in reader:
            data = {'neighbourhood': row['neighbourhood'], 'average_price': float(row['avg_price($)']), 
            'avg_latitute': float(row['avg_latitute']), 'avg_longitude': float(row['avg_longitude'])}
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
            data = {'room_type': row['room_type'], 'average_price': float(row['average_price($)']), 
            'median_price': float(row['median_price($)']), 'max_price': float(row['max_price($)']),
            'min_price': float(row['min_price($)'])}
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
            data = {'week': row['week'], 'average_price': float(row['average_price($)']),
            'median_price': float(row['median_price($)'])}
            serializer = PriceWithWeekSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------PriceWithWeekSerializer failed!")  


'''
data from calla
read the csv file and init the data to database
'''
def read_avg_review_by_city():
    file_name = "airbnb/analysis_results/avg_review_by_city/avg_review_by_city.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'city': row['city'], 'avg_overall': float(row['avg_overall']), 'avg_accuracy': float(row['avg_accuracy']),
            'avg_cleanliness': float(row['avg_cleanliness']), 'avg_checkin': float(row['avg_checkin']), 
            'avg_communication': float(row['avg_communication']),
            'avg_location': float(row['avg_location']), 'avg_value': float(row['avg_value'])}
            serializer = Avg_Review_by_CitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Avg_Review_by_CitySerializer failed!")  

'''
data from calla
read the csv file and init the data to database
'''
def read_avg_review_by_room_type():
    file_name = "airbnb/analysis_results/avg_review_by_room_type/avg_review_by_room_type.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'room_type': row['room_type'], 'avg_overall': float(row['avg_overall']), 'avg_accuracy': float(row['avg_accuracy']),
            'avg_cleanliness': float(row['avg_cleanliness']), 'avg_checkin': float(row['avg_checkin']), 
            'avg_communication': float(row['avg_communication']),
            'avg_location': float(row['avg_location']), 'avg_value': float(row['avg_value'])}
            serializer = Avg_Review_by_RoomTypeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Avg_Review_by_RoomTypeSerializer failed!")  

'''
data from calla
read the csv file and init the data to database
'''
def read_avg_review_by_price_bucket():
    file_name = "airbnb/analysis_results/avg_review_by_price_bucket/avg_review_by_price_bucket.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'price_bucket': row['price_bucket'], 'avg_overall': float(row['avg_overall']), 'avg_accuracy': float(row['avg_accuracy']),
            'avg_cleanliness': float(row['avg_cleanliness']), 'avg_checkin': float(row['avg_checkin']), 
            'avg_communication': float(row['avg_communication']),
            'avg_location': float(row['avg_location']), 'avg_value': float(row['avg_value'])}
            serializer = Avg_Review_by_PriceBucketSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Avg_Review_by_PriceBucketSerializer failed!")  

'''
data from calla
read the csv file and init the data to database
'''
def read_avg_review_by_superhosts():
    file_name = "airbnb/analysis_results/avg_review_for_superhosts/avg_review_for_superhosts.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'host_is_superhost': row['host_is_superhost'], 'avg_overall': float(row['avg_overall']), 'avg_accuracy': float(row['avg_accuracy']),
            'avg_cleanliness': float(row['avg_cleanliness']), 'avg_checkin': float(row['avg_checkin']), 
            'avg_communication': float(row['avg_communication']),
            'avg_location': float(row['avg_location']), 'avg_value': float(row['avg_value'])}
            serializer = Avg_Review_by_SuperhostsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Avg_Review_by_SuperhostsSerializer failed!")  


'''
data from calla
read the csv file and init the data to database
'''
def read_factors_predict_review():
    file_name = "airbnb/analysis_results/factors_predict_review/factors_predict_review.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'feature': row['feature'], 'feature_importance_mean': float(row['feature_importance_mean']), 
            'feature_importance_std': float(row['feature_importance_std']),}
            serializer = Factors_Predict_ReviewSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Factors_Predict_ReviewSerializer failed!")  

'''
data from calla
read the csv file and init the data to database
'''
def read_sub_category_predict_review():
    file_name = "airbnb/analysis_results/sub_category_predict_review/sub_category_predict_review.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'feature': row['feature'], 'feature_importance_mean': float(row['feature_importance_mean']), 
            'feature_importance_std': float(row['feature_importance_std']),}
            serializer = SubCategory_Predict_ReviewSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------SubCategory_Predict_ReviewSerializer failed!")  
