from django.contrib import admin
from django.urls import path

#from .views import GetUsers
from .views import *
app_name = 'api'

urlpatterns = [
    path('drivers/', GetDrivers.as_view()),
    path('drivers/<int:pk>', GetDrivers.as_view()),
    path('ad/', GetAdvertisers.as_view()),
    path('ad/<int:pk>', GetAdvertisers.as_view())
]
