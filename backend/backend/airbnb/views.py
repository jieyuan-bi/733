from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *



from .utils import *


@api_view(['POST'])
def similar_product(request):
    """
    Advanced feature
    Get the similar product to the current one
    """
    if request.method == 'POST':
        request_data = request.data
        print('req data---------------------------',request.data)
        try:
            result = get_similar_product(request_data)
            return_data = {'data': result}
            return_data['success']=1
        except Exception as e:
            return_data = {'success': 0}
            return_data = {'error': str(e)}
        return Response(return_data)












@api_view(['GET'])
def sub_category_predict_review_list(request):
    """
    Data processed by Calla
    sub-category review scores that mostly strongly predict overall review score
    Return a json format of sub_category_predict_review
    """
    if request.method == 'GET':
        sub_category_predict_review = SubCategory_Predict_Review.objects.all()
        if sub_category_predict_review.exists():
            serializer = SubCategory_Predict_ReviewSerializer(sub_category_predict_review, many=True)
        # init the data from reading the csv file
        else:
            read_sub_category_predict_review()
            serializer = SubCategory_Predict_ReviewSerializer(sub_category_predict_review, many=True)
        # print(serializer.data)
        return Response(serializer.data)


@api_view(['POST'])
def predict_price(request):
    """
    Advanced feature by Kevin
    Use trained model to predict the price with the following input
    'accommodates','bedrooms','beds','license','bathrooms'
    the following two arguments are ignored due to some technical issues
    'room_type','neighbourhood_cleansed'
    """
    if request.method == 'POST':
        predict_data = request.data
        print('req data---------------------------',request.data)
        try:
            result = price_predict(predict_data)
            return_data = {'data': result}
            return_data['success']=1
        except Exception as e:
            return_data = {'success': 0}
            return_data = {'error': str(e)}
        return Response(return_data)

