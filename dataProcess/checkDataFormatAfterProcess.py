import os

from pyspark.sql import SparkSession, types
import pyspark.sql.functions as F
import sys
import json
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+


# add more functions as necessary
def main(inputs, output):

    listings_dir = output + '/' + 'listings'
    reviews_dir = output + '/' + 'reviews'

    l = spark.read.parquet(listings_dir)
    r = spark.read.parquet(reviews_dir)
    print(l.count()) #   51625
    print(r.count()) #  1747857

    ## TODO schema for check columns ## parquet read file not need for schema
    # views_schema = types.StructType([
    #     types.StructField('listing_id', types.StringType()),
    #     types.StructField('id', types.StringType()),
    #     types.StructField('date', types.DateType()),
    #     types.StructField('reviewer_id', types.LongType()),
    #     types.StructField('reviewer_name', types.StringType()),
    #     types.StructField('comments', types.StringType()),
    #     types.StructField('country', types.StringType()),
    #     types.StructField('city', types.StringType()),
    # ])
    #
    # listings_schema = types.StructType([
    #     types.StructField('id', types.IntegerType(), False),
    #     types.StructField('listing_url', types.StringType(), False),
    #     types.StructField('neighbourhood_cleansed', types.StringType(), False),
    #     types.StructField('latitude', types.DoubleType(), False),
    #     types.StructField('longitude', types.DoubleType(), False),
    #     types.StructField('room_type', types.StringType(), False),
    #     types.StructField('accommodates', types.IntegerType(), False),
    #     types.StructField('bedrooms', types.IntegerType(), False),
    #     types.StructField('beds', types.IntegerType(), False),
    #     types.StructField('price', types.DoubleType(), False),
    #     types.StructField('license', types.StringType(), False),
    #     types.StructField('number_of_reviews', types.IntegerType(), False),
    #     types.StructField('review_scores_rating', types.DoubleType(), False),
    #     types.StructField('review_scores_accuracy', types.DoubleType(), False),
    #     types.StructField('review_scores_cleanliness', types.DoubleType(), False),
    #     types.StructField('review_scores_checkin', types.DoubleType(), False),
    #     types.StructField('review_scores_communication', types.DoubleType(), False),
    #     types.StructField('review_scores_location', types.DoubleType(), False),
    #     types.StructField('review_scores_value', types.DoubleType(), False),
    #     types.StructField('reviews_per_month', types.DoubleType(), False),
    #     types.StructField('country', types.StringType()),
    #     types.StructField('city', types.StringType()),
    #     types.StructField('bathrooms', types.DoubleType()),
    # ])

if __name__ == '__main__':
    # TODO hardcode file path rawData & data
    # raw data path
    inputs = 'rawData'
    # processed data path
    output = 'data'
    spark = SparkSession.builder.appName('data process').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(inputs, output)
