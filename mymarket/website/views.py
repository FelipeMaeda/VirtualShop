from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('teste')

def home(request):
    return render(request, 'website/index.html')

def carrinho(request):
    return render(request, 'website/cart.html')

def login(request):
    return render(request, 'website/login.html')

# Create your views here.
