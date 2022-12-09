import os

from pyspark.sql import SparkSession, types
import pyspark.sql.dataframe
import pyspark.sql.functions as F
import sys
import json
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+


# add more functions as necessary
def main(input, output):

    listings_dir = input + '/' + 'listings'
    ## TODO price with the number of bedrooms
    ## 1 2 3 4 5 over_6
    listings = spark.read.parquet(listings_dir)
    bedRoom_num = listings.select('bedrooms', 'price').\
        withColumn('bedrooms_nums', F.when(F.col('bedrooms') > 5, '-1'). ## for frontend => change to over_5

                   otherwise(F.col('bedrooms').cast('string'))).select('bedrooms_nums', 'price')
    bedRoom_num.createOrReplaceTempView("bedRoom_num")
    bedRoom_num = spark.sql("SELECT bedrooms_nums, MIN(price) AS min, percentile_approx(price, 0.25) AS Q1,\
     percentile_approx(price, 0.5)AS median, percentile_approx(price, 0.75) AS Q3, MAX(price) AS max \
                FROM bedRoom_num \
                GROUP BY bedrooms_nums").orderBy('bedrooms_nums')

    diretory = '/price_numberOfBedRoom'
    output_path = output + diretory
    bedRoom_num.write.csv(output_path, mode='overwrite', header='true')

    ## TODO How to read
    #spark.read.csv(output_path, header=True).show()


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
    input = 'data'
    # processed data path
    output = 'analysis_results'
    spark = SparkSession.builder.appName('data process').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(input, output)
