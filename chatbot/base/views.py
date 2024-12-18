from django.shortcuts import render
from .models import Room


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
    # form = RoomForm()
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
    context = {}
    return render(request, 'base/room_form.html', context)

