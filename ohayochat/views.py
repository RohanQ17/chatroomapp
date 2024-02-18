
from django.shortcuts import render, redirect
from ohayochat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
#this home function will render us to the home page whenever requested
def home(request):
    return render(request, 'home.html')

# this function will handle which room should the user go to
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
# chatexist checks if the room already exists , if not it creates the room and then the url is handled by room fnc html
def chatexist(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

# send is used to create and save a message in our database
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

# get the messages if present in that room from databases and show it in the screen
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})