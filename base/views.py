from django.shortcuts import render

rooms = [
    {'id':1,'name': 'lets learn python!'},
    {'id':2,'name': 'Django go go!'},
    {'id':3,'name': 'Water in  the Flask!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')

# Create your views here.
