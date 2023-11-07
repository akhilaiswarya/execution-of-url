from django.shortcuts import render

# Create your views here
from django.http import HttpResponse
def pandu(request):
    return HttpResponse('<h1><marquee>Hii pandu How are you</h1></marquee')
