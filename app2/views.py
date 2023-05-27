from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def akash(request):
    return HttpResponse('akash is my friend')

def akash1(request):
    return render(request,'akash.html')