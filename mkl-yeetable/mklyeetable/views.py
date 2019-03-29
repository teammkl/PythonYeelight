from django.http import HttpResponse
from django.shortcuts import render
from yeelight import Bulb
from yeelight import discover_bulbs

def about(request):
    return render(request, 'about.html')

def index(request):
    bulb = Bulb("10.3.3.144")
    if request.GET.get('connect'):
        print(request.GET.get('connect'))
        print("Discovering")
        print(discover_bulbs())
    elif request.GET.get('turnon'):
        print(request.GET.get('turnon'))
        print("Turning On")
        bulb.turn_on()
    elif request.GET.get('turnoff'):
        print(request.GET.get('turnoff'))
        print("Turning Off")
        bulb.turn_off()
    elif request.GET.get('dimming'):
        print(request.GET.get('dimming'))
        print("Dimming")
        bulb.set_brightness(1)
    elif request.GET.get('color'):
        print(request.GET.get('color'))
        print("Setting Color")
        bulb.set_color_temp(2000)
    return render(request, 'index.html')
