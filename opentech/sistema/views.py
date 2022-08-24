from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, senha=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("sai daqui malandro"))
            return redirect('login')
    else:
        return render(request, 'autenticate/login.html', {})



def home_sistema(request):
    return render(request, 'templates/home_sistema.html')
