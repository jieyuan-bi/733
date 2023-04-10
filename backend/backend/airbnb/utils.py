import csv
import json
import os
from django.conf import settings



from .models import *
from .serializers import *

import operator
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing
import pandas as pd
import numpy as np

def get_similar_product(request_data):
    data = pd.read_csv(os.path.join(settings.BASE_DIR, 'airbnb/src/ratings_Beauty.csv'))
    print('----------------------------checkpoint')

    label_encoder = preprocessing.LabelEncoder()
    encoded_data = data
    encoded_data["User"] = label_encoder.fit_transform(data["UserId"])
    encoded_data["Product"] = label_encoder.fit_transform(data["ProductId"])
    print('----------------------------checkpoint1.1')
    # Find the average ratings by each user 
    average_rating = encoded_data.groupby("User")["Rating"].mean()
    # Merge it with the dataset 
    encoded_data = pd.merge(encoded_data, average_rating, on = "User")
    # Rename the columns
    encoded_data = encoded_data.rename(columns = {"Rating_x": "Original_rating", "Rating_y": "Average_rating"})
    # Normalize the ratings
    encoded_data["Normalized_rating"] = encoded_data["Original_rating"] - encoded_data["Average_rating"]
    rated_products_encoded = encoded_data.groupby("Product")["Original_rating"].count()
    rated_products_encoded_df = pd.DataFrame(rated_products_encoded)
    filtered_rated_products = rated_products_encoded_df[rated_products_encoded_df.Original_rating >= 200]
    popular_products = filtered_rated_products.index.tolist()
    remaining_data = encoded_data[encoded_data["Product"].isin(popular_products)]
    print('----------------------------checkpoint1.2')
    try:
        user_item_matrix = pd.pivot_table(remaining_data, values = "Normalized_rating", index = "UserId", columns = "Product")
        user_item_matrix = user_item_matrix.fillna(0)
    except Exception as e:
        print('--------------------------error',e)
    print('----------------------------checkpoint2')

    k = request_data['nums']
    user_id = request_data['user_id']
    #calculate the k similarity
    similar_users = top_k_similar(user_id, user_item_matrix, k)
    print('----------------------------checkpoint3')
    # Get the encoded product values using the top_m_products function
    encoded_product_ids = top_m_products(user_id, similar_users, user_item_matrix, k, encoded_data)
    print('----------------------------checkpoint4')
    # Convert the encoded values back to the original ProductId
    decoded_product_ids = decode_product_ids(encoded_product_ids, label_encoder)

    print('------------------------done',decoded_product_ids)
    result = ['pid1','pid2',request_data['user_id']]
    return decoded_product_ids

'''a function used for get_similar_product'''
def top_k_similar(user_id, user_item_matrix, k):
    selected_user = user_item_matrix.loc[user_id]
    remaining_users = user_item_matrix.drop(index=user_id)
    similarity_scores = cosine_similarity([selected_user], remaining_users)[0]
    user_similarity_mapping = dict(zip(remaining_users.index, similarity_scores))
    sorted_user_similarity = sorted(user_similarity_mapping.items(), key=operator.itemgetter(1), reverse=True)
    top_similar_users = [user[0] for user in sorted_user_similarity[:k]]
    return top_similar_users

'''a function used for get_similar_product'''
def top_m_products(user_id, similar_users, user_item_matrix, k, encoded_data):
    related_user_products = encoded_data[encoded_data.UserId.isin(similar_users)]
    related_user_ratings = user_item_matrix.loc[similar_users]

    related_user_avg = related_user_ratings.mean(axis=0)
    related_user_avg_df = pd.DataFrame(related_user_avg, columns=["Average"])

    target_user_ratings = user_item_matrix.loc[user_id]

    target_user_ratings_df = target_user_ratings.to_frame(name="Rating")
    unrated_products_indices = target_user_ratings_df[target_user_ratings_df["Rating"] == 0].index

    filtered_avg_ratings = related_user_avg_df[related_user_avg_df.index.isin(unrated_products_indices)]
    sorted_avg_ratings = filtered_avg_ratings.sort_values(by=["Average"], ascending=False)

    top_k_products = sorted_avg_ratings.head(k).index.tolist()

    return top_k_products

'''a function used for get_similar_product'''
def decode_product_ids(encoded_product_ids, label_encoder):
    return label_encoder.inverse_transform(encoded_product_ids)











# '''
# data from calla
# read the csv file and init the data to database
# '''
# def read_sub_category_predict_review():
#     file_name = "airbnb/analysis_results/sub_category_predict_review/sub_category_predict_review.csv"
#     with open(os.path.join(settings.BASE_DIR, file_name), newline='') as csvfile:
#         reader = csv.DictReader(csvfile)

#         for row in reader:
#             data = {'feature': row['feature'], 'feature_importance_mean': float(row['feature_importance_mean']), 
#             'feature_importance_std': float(row['feature_importance_std']),}
#             serializer = SubCategory_Predict_ReviewSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#             else:
#                 print("!!!-------SubCategory_Predict_ReviewSerializer failed!")  


# '''
# Advanced feature by Kevin
# Predict price
# '''
# def price_predict(data):
#     spark = SparkSession.builder.appName('price train').getOrCreate()
#     assert spark.version >= '3.0' # make sure we have Spark 3.0+
#     sc = spark.sparkContext
#     sc.setLogLevel('WARN')
#     model_path = "airbnb/analysis_results/predict_price"
#     model = PipelineModel.load(model_path)
#     # data format: 'accommodates','bedrooms','beds','license','bathrooms','room_type','neighbourhood_cleansed'
#     predict_data = [(float(data['accommodates']),float(data['bedrooms']),float(data['beds']),float(data['license']),float(data['bathrooms']),'','')]
#     schema = types.StructType([
#     types.StructField('accommodates', types.FloatType()),
#     types.StructField('bedrooms', types.FloatType()),
#     types.StructField('beds', types.FloatType()),
#     types.StructField('license', types.FloatType()),
#     types.StructField('bathrooms', types.FloatType()),
#     types.StructField('room_type', types.StringType()),
#     types.StructField('neighbourhood_cleansed', types.StringType()),
#     # types.StructField('room_type_Scaled', types.FloatType()),
#     # types.StructField('neighbourhood_cleansed_Scaled', types.FloatType()),
#     ])
#     predict = spark.createDataFrame(predict_data,schema)
#     df = predict.select('accommodates', 'bedrooms', 'beds', F.col('license').cast('double').alias('license'),
#                             'bathrooms', 'room_type', 'neighbourhood_cleansed')

#     cate_features = [ 'room_type', 'neighbourhood_cleansed']

#     ## categorical
#     for f in cate_features:
#         indexer = StringIndexer(inputCol=f, outputCol=f + "_Scaled",
#                                             handleInvalid="error",
#                                             stringOrderType="frequencyDesc")
#         pipeline = Pipeline(stages=[
#             indexer
#         ])
#         df = pipeline.fit(df).transform(df)

#     df = df.select('accommodates',
#                     'bedrooms',
#                     'beds',
#                     'license',
#                     'bathrooms',
#                     # 'city_Scaled',
#                         'room_type_Scaled',
#                         'neighbourhood_cleansed_Scaled').\
#                                 withColumn('accommodates', df['accommodates'] ** 0.5).\
#                                 withColumn('bathrooms', df['bathrooms'] ** 0.5).\
#                                 withColumn('bedrooms', df['bedrooms'] ** 0.5).\
#                                 withColumn('beds', df['beds'] ** 0.5)

#     predictions = model.transform(df)
#     result = predictions.select("prediction").collect()[0]['prediction']
#     return result**2

