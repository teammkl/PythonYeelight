from django.shortcuts import render, redirect
from yeelight import Bulb
from yeelight import *

# Create your views here.
def test(request):
    return render(request, 'test/test.html')

