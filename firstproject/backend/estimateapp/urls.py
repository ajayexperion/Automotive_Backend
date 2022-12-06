from django.urls import path
from .views import getservices,getcustomer,addcustomer,addestimate,getservicehistory,getestimateproduct,getestimateservices
urlpatterns=[
     path('getservices/',getservices,name="services"),
     path('getcustomer/<str:key>',getcustomer,name="get customer"),
     path('addcustomer/',addcustomer,name="add customer"),
     path('addestimate/',addestimate,name="add estimate"),
     path('estimatedetails/<str:key>',getservicehistory,name="get estimate"),
     path('estimateproducts/<str:key>',getestimateproduct,name="get estimate product"),
     path('estimateservices/<str:key>',getestimateservices,name="get estimate product"),
]
