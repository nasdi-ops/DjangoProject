from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import User
from playground.forms import UserLoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psw = request.POST.get('psw')
        if User.objects.filter(username=username).exists():
            return HttpResponseRedirect('/taken')
        else:
            usr = User(username=username, password=psw)
            usr.save()
        return HttpResponseRedirect('/success')
    return render(request, 'playground/login.html', {})

def home(request):
    return render(request, 'playground/home.html', {})

def success(request):
    return render(request, 'playground/success.html', {})

def taken(request):
    return render(request, 'playground/taken.html', {})
    