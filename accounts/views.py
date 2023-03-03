from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import RegisterForm


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
        return redirect('home')


def cadastro(request):

    form = RegisterForm(request.POST or None)

    if request.method == 'GET':
        return render(request, 'accounts/cadastro.html', {'form': form})
    
    elif request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('/accounts/login')
        else:
            return render(request, 'accounts/cadastro.html', {'form': form})
        

def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')