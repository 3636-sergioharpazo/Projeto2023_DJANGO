from django.shortcuts import render,redirect
from  .models import Pessoa
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def home(request):
    pessoa=Pessoa.objects.all()
    return render(request,"index.html",{"pessoas":pessoa})

def cad(request):
    nome_new=request.POST.get('nome')
    pessoa=Pessoa.objects.create(nome=nome_new)
    pessoa=Pessoa.objects.all()
    return render(request,"index.html",{"pessoas":pessoa})

@login_required(login_url="login")
def editar(request,id):
    pessoa=Pessoa.objects.get(id=id)
    return render(request,"editar.html",{"pessoa":pessoa})

@login_required
def update(request,id):
    nome_new=request.POST.get('nome')
    pessoa=Pessoa.objects.get(id=id)
    pessoa.nome=nome_new
    pessoa.save()
    return redirect(home)

@login_required(login_url="login")
def delete(request,id):
    pessoa=Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

@login_required(login_url="login")
def usercreate(request):
    if request.method=="GET":
        return render(request,"usercreate.html")
    else:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=User.objects.filter(username=username).first()
        if user:
           return HttpResponse("Já existe o usuário")
            

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect(login)
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login_django(request,user)
            return render(request,'index.html',{'user':user})
        else:
            return HttpResponse('E-mail ou senha invalida')
def plataforma(request):
    if request.user.is_authenticated:
            return redirect(home)
    else:
            return HttpResponse('Precisa está logado')

def logout(request):
    if request.method=="GET":
        return render(request,"login.html")

        

