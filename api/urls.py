from django.contrib import admin
from django.urls import path

from .views import GetUsers

app_name = 'api'

urlpatterns = [
    path('users/', GetUsers.as_view()),
    path('users/<int:pk>', GetUsers.as_view())
]
