from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from yeelight import Bulb
from yeelight import discover_bulbs
from django.views.decorators.csrf import csrf_exempt


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
    return render(request, 'users/signup.html', {'form': form})


# noinspection PyInterpreter
@csrf_exempt
def user_homepage(request):
    bulb = Bulb("192.168.1.167")
    # noinspection PyInterpreter,PyInterpreter
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
        bulb.set_color_temp(2700)
    elif request.GET.get('lecrepecafe'):
        print(request.GET.get('lecrepecafe'))
        print("Clicked Le Crepe Cafe")
        bulb.turn_on()
        bulb.set_color_temp(2700)
    elif request.GET.get('starbucks'):
        print(request.GET.get('starbucks'))
        print("Clicked Starbucks")
        bulb.turn_on()
        bulb.set_color_temp(6500)
    elif request.GET.get('jamba'):
        print(request.GET.get('jamba'))
        print("Clicked Jamba")
        bulb.turn_on()
        bulb.set_color_temp(6500)
    elif request.GET.get('panda'):
        print(request.GET.get('panda'))
        print("Clicked Panda")
        bulb.turn_on()
        bulb.set_color_temp(2700)
    else:
        print(request.GET.get('turnoff'))
        print("NO REQUEST")
    return render(request, 'users/userhome.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            return redirect('users:userhome')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def restaurant_directory(request):
    try:
        # test for specific restaurants
        myid = request.GET['id']
        print("id=" + myid)
        bulb = Bulb("192.168.1.167")
        if myid == '0':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            print("Da Spot")
        elif myid == '1':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Dunkin' Donuts")
        elif myid == '2':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Govindas")
        elif myid == '3':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Holoholo Grill")
        elif myid == '4':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Hot Tacos")
        elif myid == '5':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Kamitoku Ramen")
        elif myid == '6':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("LL BBQ")
        elif myid == '7':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Lasoon")
        elif myid == '8':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Le Crepe Cafe")
        elif myid == '9':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Panda Express")
        elif myid == '10':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Peace Cafe")
        elif myid == '11':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Punchbowl Cafe")
        elif myid == '12':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Sistah Truck")
        elif myid == '13':
            # do stuff to the light bulb
            print("Turning On")
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("The Bean Counter")
    except:
        print(request.GET)
    try:
        # test for locations
        locationid = request.GET['locationid']
        print("locationid=" + locationid)
        bulb = Bulb("192.168.1.167")
        if locationid == '0':
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Center for Korean Studies")
        elif locationid == '1':
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Holmes Hall")
        elif locationid == '2':
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Krauss Hall")
        elif locationid == '3':
            bulb.turn_on()
            bulb.set_color_temp(6500)
            print("Paradise Palms")
        elif locationid == '4':
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("POST")
        elif locationid == '5':
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Shidler College of Business")
        elif locationid == '6':
            bulb.turn_on()
            bulb.set_color_temp(2700)
            print("Sustainability Courtyard")
    except:
        print(request.GET)
    return render(request, 'users/restaurantDirectory.html')
