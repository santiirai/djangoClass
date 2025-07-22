from django.urls import path
from .views import hi
from myApp.views import *

urlpatterns = [
    path('', hi),
    path('index', index),
    path('about111', about, name='A'), #A is namespace and about111 is url
    path('index111', index, name='B')
]