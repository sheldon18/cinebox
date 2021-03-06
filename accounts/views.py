from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    """Return index.html"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Log out the user"""
    auth.logout(request)
    messages.success(request, "You have been successfully been logged out!")
    return redirect(reverse('index'))
    
def login(request):
    """Return login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'].lower(),     # case insensitive login
                                     password=request.POST['password'])
                                     
            if user:
                auth.login(user=user, request=request)
                
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or pasword is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    
def registration(request):
    """Return registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request = request)
                messages.success(request, "Your account has been registered!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "We are unable to register your account at this time")
    else:        
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {"registration_form": registration_form})
    

def profile(request):
    """My Account Page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
    