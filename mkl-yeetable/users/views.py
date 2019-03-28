from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
