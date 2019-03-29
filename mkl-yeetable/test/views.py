from django.shortcuts import render, redirect
from yeelight import Bulb
from yeelight import *

bulb = Bulb("192.168.0.10")

# Create your views here.
def test(request):
    return render(request, 'test/test.html')

