# cmput732proj
### 0 Getting Started
#### Installation:
* pyspark
```
pip install pyspark
```
* keras
```
pip install keras
```
* sklearn
```
pip install sklearn
```
* pandas
```
pip install pandas
```
* wordcloud
```
pip install wordcloud
```
* matplotlib
```
pip install matplotlib
```
### 1 Data Cleaning
#### 1.1. Data Link
Since the rawData and the data after cleaning are large, so we upload the data in Google Drive. Please download the datasets and put them to the right path.
The datasets have 3 parts. One is rawData which we combine all the data download from 'Inside Airbnb'.
One is version 1 data in Parquet format after data processed. The last one is version 2 data in csv format.
The reason why we have 2 versions of datasets is we want to compare the performance of these file formats.

Link: https://drive.google.com/drive/folders/1fS4aLfhWBYxeGBRwATOQqCe1igD7329_?usp=share_link
#### 1.2. File Path
1.2.1 raw data path: rawData / COUNTRY_NAME / CITY_NAME / listings.csv.gz reviews.csc.gz

1.2.2 cleaned data
 path: data / listings   reviews
#### 1.3 Format
1.3.1 format: parquet & csv

#### 1.4 Run Data Process
We need to download the rawData data from the link above and and set the input & output data path for 'dataProcess.py'.

### 2 Data Analysis
All data analysis Python files are in airbnb/src directory. And all analysis results are in airbnb/analysis_results.
All Python files need to set up correct input file path from the output of data processed and output the results to analysis_results.

### 3 Run Server
TODO


    