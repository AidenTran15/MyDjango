from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):

    dest1 = destination() 

    return render (request, "index.html", {'dest1': dest1})

