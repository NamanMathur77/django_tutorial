from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest2 = Destination()
    dest3 = Destination()
    dest1.name='Mumbai'
    dest1.desc='City of dreams'
    dest1.price=700
    dest1.offer=False
    dest1.img='destination_1.jpg'
    dest2.name='Agra'
    dest2.desc='The city of Taj'
    dest2.price=900
    dest2.offer=True
    dest2.img='destination_2.jpg'
    dest3.name='Jaipur'
    dest3.desc='The pink city of India'
    dest3.price=850
    dest3.offer=False
    dest3.img='destination_3.jpg'
    dest=[dest1,dest2,dest3]
    return render(request,'index.html', {'dest':dest})
