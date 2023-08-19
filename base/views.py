from django.shortcuts import render
from .models import Room

# rooms = [
#     {"id": 1, "name": "lets learn python!"},
#     {"id": 2, "name": "Django go go!"},
#     {"id": 3, "name": "Water in  the Flask!"},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {"room": room}  # context used here as dictionary

    return render(request, "base/room.html", context)

def createRoom(request):
    context={}
    return render(request, "base/room_form.html", context)
# Create your views here.
