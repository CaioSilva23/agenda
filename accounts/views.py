from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated: # VERIFICA SE O USUÁRIO JÁ ESTÁ LOGADO
            return redirect('/contatos/home/')
        else:
            return render(request, 'accounts/login.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(request, username=nome, password=senha)
    if not usuario:
        messages.error(request, 'Username ou senha inválidos')
        return redirect('/accounts/login')
    else:
        auth.login(request, usuario)
        return redirect('/contatos/home/')


def cadastro(request):
    pass



def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')