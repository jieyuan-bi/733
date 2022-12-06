from django.urls import path
from airbnb import views

urlpatterns = [
    path('avg_price_license/', views.avg_price_license_list),
]