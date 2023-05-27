from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kushal(request):
    return HttpResponse('hii myself kushal')

def kushal1(request):
    return render(request,'kushal.html')