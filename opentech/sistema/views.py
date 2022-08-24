from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuario com este username.')

        return HttpResponse(username)


def cadastro_user(request):
    return render(request, 'cadastro.html')
