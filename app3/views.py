from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bhai(request):
    return HttpResponse('bhai is my friend')

def bhai1(request):
    return render(request,'bhai.html')