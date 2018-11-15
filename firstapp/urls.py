from django.contrib import admin
from django.urls import path
from firstapp.views import *
urlpatterns = [
    path('main/', main),
    path('show/',show)
]