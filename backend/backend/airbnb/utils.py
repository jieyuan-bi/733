import csv
import json
import os
from django.conf import settings

from .models import *
from .serializers import *

'''
read the csv file and init the data to database
'''
def read_avg_price_license():
    file_name = "airbnb/analysis_results/avg_price_license/part-00000-af554967-bcef-4012-93a0-ebb01f614df0-c000.csv"
    with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data = {'license': row['license'], 'avg_price': float(row['avg_price'])}
            serializer = Avg_Price_LicenseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print("!!!-------Avg_Price_LicenseSerializer failed!")

    

# read_avg_price_license()
# print(a)