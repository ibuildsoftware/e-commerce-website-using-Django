from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # view
    return render(request, 'core/index.html') # return the templates/core/index.html file
