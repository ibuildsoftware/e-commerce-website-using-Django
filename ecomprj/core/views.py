from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # view
    return HttpResponse("welcome to my shop")
