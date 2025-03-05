from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User  # Model com configurações para usuários
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).exists()  # Verifica se o usuário já existe

        if user:
            return HttpResponse('Já existe um usuário cadastrado.')

        user = User.objects.create_user(username=username, email=email, password=senha)  # Criando usuário

        return HttpResponse(f'Usuário {username} cadastrado com sucesso!')
    
def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha) # Verifica se existe esses dados

        if user: #true
            login_django(request, user) 
            return HttpResponse("Autenticado.")
        else: 
            return HttpResponse("Email ou senha invalidos.")

@login_required(login_url='/auth/login/')       #Usuario que tentar acessar a view plataforma sem está logado                       
def plataforma(request):                        #será redirecionado para view login
    return HttpResponse("Plataforma")           #essa view so será acessada quando o usuario estiver logado/autentificado.

