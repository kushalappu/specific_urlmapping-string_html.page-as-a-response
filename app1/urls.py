app_name='hii'
from django.urls import path
from app1.views import *
urlpatterns = [
    path('kushal/',kushal,name='kushal'),
    path('kushal1/',kushal1,name='kushal1'),
]
