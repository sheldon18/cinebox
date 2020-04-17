from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.
def index(request):
    """Return index.html"""
    return render(request, 'index.html')

def logout(request):
    """Log out the user"""
    auth.logout(request)
    return redirect(reverse('index'))