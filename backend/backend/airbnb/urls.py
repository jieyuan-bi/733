from django.urls import path
from airbnb import views

urlpatterns = [
    # kevin
    path('avg_price_license/', views.avg_price_license_list),
    path('corela_rooms_beds_accommodates/', views.corela_rooms_beds_accommodates_list),
    path('price_numberOfBedRoom/', views.price_numberOfBedRoom_list),

    # tony
    path('priceWithMonth/', views.priceWithMonth_list),
    path('priceWithSpace/', views.priceWithSpace_list),
    path('priceWithType/', views.priceWithType_list),
    path('priceWithWeek/', views.priceWithWeek_list),

    #calla
]