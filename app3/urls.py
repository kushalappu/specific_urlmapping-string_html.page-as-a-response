app_name='helo'
from django.urls import path
from app3.views import *
urlpatterns = [
    path('bhai/',bhai,name='bhai'),
    path('bhai1/',bhai1,name='bhai1'),
]