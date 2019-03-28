from django.http import HttpResponse
from django.shortcuts import render
from yeelight import Bulb

def about(request):
    return render(request, 'about.html')

def index(request):
    # return HttpResponse('index')
    if request.GET.get('connect'):
        print(request.GET.get('connect'))
        print("Button pressed")
        bulb = Bulb("10.3.3.127")
        bulb.turn_on()
    return render(request, 'index.html')

