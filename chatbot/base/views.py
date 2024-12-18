from django.shortcuts import render, redirect 
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id' : 1, 'name': 'Lets learn Python'},
#     {'id' : 2, 'name': 'I am django developer'},
#     {'id' : 3, 'name': 'I am Data Scientist'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request,'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    # topics = Topic.objects.all()
    # if request.method == 'POST':
    #     topic_name = request.POST.get('topic')
    #     topic, created = Topic.objects.get_or_create(name = topic_name)
        
    #     Room.objects.create(
    #         host = request.user,
    #         topic = topic,
    #         name = request.POST.get('description'),
    #     )
    #     return redirect('home')
        
    # context = {'form': form, 'topics': topics}
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)
    # topics = Topic.objects.all()
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    # if request.user != room.host:
    #    return HttpResponse('You are not allowed here!!') 
   
    # if request.method == 'POST':
    #     topic_name = request.POST.get('topic')
    #     topic, created = Topic.objects.get_or_create(name = topic_name)
    #     room.name = request.POST.get('name')
    #     room.topic = topic
    #     room.description = request.POST.get('description')
    #     room.save()
    #     return redirect('home')
    
    # context = {'form': form, 'topics': topics, 'room': room}
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    # if request.user != room.host:
    #    return HttpResponse('You are not allowed here!!') 
   
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
