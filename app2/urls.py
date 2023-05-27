app_name='hey'
from django.urls import path
from app2.views import *
urlpatterns = [
    path('akash/',akash,name='akash'),
    path('akash1/',akash1,name='akash1'),
]