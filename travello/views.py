from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):

    dest1 = destination() 
    dest1.name = 'Munbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700

    return render (request, "index.html", {'dest1': dest1})

