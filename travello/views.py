from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):

    dest1 = destination() 
    dest1.name = 'Munbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jgp'

    dest2 =  destination()
    dest2.name = 'Vung Tau'
    dest2.desc = 'Thanh Pho Bien'
    dest2.price = 300
    dest2.img = 'destination_2.jgp'

    dest3 = destination()
    dest3.name = 'Da Lat'
    dest3.desc = 'Thanh Pho Suong Mu'
    dest3.price = 200
    dest3.img = 'destination_3.jpg'

    dests = [dest1, dest2, dest3]

    return render (request, "index.html", {'dests': dests})

