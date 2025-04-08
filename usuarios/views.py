from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth

#auth é para identificação de usuario


def cadastro(request):
    if request.method =='GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha =  request.POST.get('senha')
        confirmar_senha = request.POST.get ('confirmar_senha')

        if not senha == confirmar_senha:
            message.add_message(request, constants.ERROR, 'As senhas não conferem.')
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter mais de 6 caracteres.')    
            return redirect('/usuarios/cadastro')
        
        users = User.objects.filter(username = username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Esse usuario já existe.')
            #messages.error(request, 'Esse usuario já existe.')
            return redirect('/usuarios/cadastro')
        print(f'username {username}, ja existe.')
        
        User.objects.create_user( username = username, password = senha)

        return redirect('/usuarios/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/home/')
        
        messages.add_message(request, constants.ERROR, 'Usuario ou senha invalidos.')
        return redirect('login')


       