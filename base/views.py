from django.shortcuts import render
from .models import Room

rooms = [
    {"id": 1, "name": "lets learn python!"},
    {"id": 2, "name": "Django go go!"},
    {"id": 3, "name": "Water in  the Flask!"},
]


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    # rooms = Room.objects.all()
    for i in rooms:
        if i["id"] == int(pk):
            room = i
    context = {"room": room}  # context used here as dictionary
    # this for loop transfers the name from the rooms dictionary to html page

    return render(request, "base/room.html", context)


# Create your views here.
