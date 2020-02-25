from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('teste')

def home(request):
    return render(request, 'website/index.html')

# Create your views here.
