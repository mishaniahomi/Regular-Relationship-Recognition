from django.contrib import admin
from django.urls import path
from .views import index, get_results

urlpatterns = [
    path('index/', index),
    path('get_result', get_results)
]
