from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import formcadastro
# Create your views here.

def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:

        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Usuario ou senha invalida!!!')
            return redirect('login')




def cadastro_user(request):
    if request.method == "GET":
        form = formcadastro()
        context = {
            'form': form
        }
        return render(request, 'cadastro.html', context=context)
    else:
        form = formcadastro(request.POST)
        username = form.data['nome']
        email = form.data['email']
        senha = form.data['senha']

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com este nome')
        else:
            usuario = User.objects.create_user(username=username, email=email, password=senha)
            usuario.save()
            return redirect('login')


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        return HttpResponse('plataforma')