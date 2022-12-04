import os

from pyspark.sql import SparkSession, types
import pyspark.sql.dataframe
import pyspark.sql.functions as F
import sys
import json
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+


# add more functions as necessary
def main(input, output):

    listings_dir = input + '/' + 'listings'
    ## TODO correlation between rooms beds and accommodates
    listings = spark.read.parquet(listings_dir)
    x = listings.select('bedrooms', 'beds', 'accommodates')
    features = 'corr_features'

    assembler = VectorAssembler(inputCols=x.columns,
                                outputCol=features, handleInvalid='keep')
    x_transformed = assembler.transform(x).select(features)

    # correlation will be in Matrix
    correlation = Correlation.corr(x_transformed, features, "pearson").collect()[0][0]

    # To convert Matrix into DataFrame
    rows = correlation.toArray().tolist()
    cols = x.columns
    correlation_df = spark.createDataFrame(rows, x.columns)
    diretory = '/corela_rooms_beds_accommodates'
    output_path = output + diretory
    correlation_df.coalesce(1).write.csv(output_path, mode='overwrite', header='true')


    ## TODO How to read
    # spark.read.csv(output_path, header=True).show()


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
