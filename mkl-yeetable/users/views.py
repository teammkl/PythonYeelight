from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from yeelight import Bulb
from yeelight import discover_bulbs

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('users:userhome')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', { 'form': form })

def user_homepage(request):
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
        bulb.set_brightness(100)
    elif request.GET.get('color'):
        print(request.GET.get('color'))
        print("Setting Color")
        bulb.set_color_temp(2000)
    elif request.GET.get('lecrepecafe'):
        print(request.GET.get('lecrepecafe'))
        print("Clicked Le Crepe Cafe")
        bulb.turn_on()
        bulb.set_color_temp(6500)
    elif request.GET.get('starbucks'):
        print(request.GET.get('starbucks'))
        print("Clicked Starbucks")
        bulb.turn_on()
        bulb.set_color_temp(1500)
    elif request.GET.get('jamba'):
        print(request.GET.get('jamba'))
        print("Clicked Jamba")
        bulb.turn_on()
        bulb.set_color_temp(1500)
    elif request.GET.get('panda'):
        print(request.GET.get('panda'))
        print("Clicked Panda")
        bulb.turn_on()
        bulb.set_color_temp(6500)
    return render(request, 'users/userhome.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            return redirect('users:userhome')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': form })
