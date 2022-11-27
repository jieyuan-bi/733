# cmput732proj

### 1 DATA CLEANING
##### 1.1. file path
1.1.1 raw data path: rawData / COUNTRY_NAME / CITY_NAME / listings.csv.gz reviews.csc.gz

1.1.2 cleaned data path: data / listings   reviews
##### 1.2 Format & schema
1.2.1 format: parquet

1.2.2 schema after cleaned:

    views_schema = types.StructType([
        types.StructField('listing_id', types.StringType()),
        types.StructField('id', types.StringType()),
        types.StructField('date', types.DateType()),
        types.StructField('reviewer_id', types.LongType()),
        types.StructField('reviewer_name', types.StringType()),
        types.StructField('comments', types.StringType()),
        types.StructField('country', types.StringType()),
        types.StructField('city', types.StringType()),
    ])

    listings_schema = types.StructType([
        types.StructField('id', types.IntegerType(), False),
        types.StructField('listing_url', types.StringType(), False),
        types.StructField('neighbourhood_cleansed', types.StringType(), False),
        types.StructField('latitude', types.DoubleType(), False),
        types.StructField('longitude', types.DoubleType(), False),
        types.StructField('room_type', types.StringType(), False),
        types.StructField('accommodates', types.IntegerType(), False),
        types.StructField('bedrooms', types.IntegerType(), False),
        types.StructField('beds', types.IntegerType(), False),
        types.StructField('price', types.DoubleType(), False),
        types.StructField('license', types.StringType(), False),
        types.StructField('number_of_reviews', types.IntegerType(), False),
        types.StructField('review_scores_rating', types.DoubleType(), False),
        types.StructField('review_scores_accuracy', types.DoubleType(), False),
        types.StructField('review_scores_cleanliness', types.DoubleType(), False),
        types.StructField('review_scores_checkin', types.DoubleType(), False),
        types.StructField('review_scores_communication', types.DoubleType(), False),
        types.StructField('review_scores_location', types.DoubleType(), False),
        types.StructField('review_scores_value', types.DoubleType(), False),
        types.StructField('reviews_per_month', types.DoubleType(), False),
        types.StructField('country', types.StringType()),
        types.StructField('city', types.StringType()),
        types.StructField('bathrooms', types.DoubleType()),
    ])