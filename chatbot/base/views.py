from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Room, Topic, User
from django.contrib.auth import authenticate, login, logout
from .forms import RoomForm

# rooms = [
#     {'id' : 1, 'name': 'Lets learn Python'},
#     {'id' : 2, 'name': 'I am django developer'},
#     {'id' : 3, 'name': 'I am Data Scientist'},
# ]

def loginPage(request):
    # page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except: 
            messages.error(request, 'user does not exist')
            
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist") 
        
    # context = {'page': page}
    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |     
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    topics = Topic.objects.all() 
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count' : room_count}
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
