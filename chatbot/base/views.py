from django.shortcuts import render



rooms = [
    {'id' : 1, 'name': 'Lets learn Python'},
    {'id' : 2, 'name': 'I am django developer'},
    {'id' : 1, 'name': 'I am Data Scientist'},
]

def home(request):
    # context = {'rooms': rooms}
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request,'room.html')


