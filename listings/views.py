from django.shortcuts import render
from.models import Listing

# Create your views here.
def index(request):
    # ! get all data from listing databasse
    listings = Listing.objects.all()

    # ! pass database record in listing 
    context = {'listings':listings}
    return render(request,'listings/listings.html',context)

def listing(request):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')

