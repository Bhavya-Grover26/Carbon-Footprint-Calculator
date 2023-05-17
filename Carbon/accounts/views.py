from time import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from .forms import UserForm

# Create your views here.
def login(request):

    form= UserForm()
    context = {
        'form': form
    }
    if request.method=='POST':
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'accounts/login.html',context )

def home(request):
    return render(request,'accounts/dashboard.html')

def request(request):
    return render(request,'accounts/request.html')

def calculatetransport(request):
    return render(request,'accounts/calculatetransport.html')

def calculate(request):
    return render(request,'accounts/calculate.html')

#def login(request):
    #return render(request,'accounts/login.html')

def calculatehouse(request):
    return render(request,'accounts/calculatehouse.html')

def option(request):
    return render(request,'accounts/option.html')

def monitor(request):
    return render(request,'accounts/monitor.html')

def individual(request):
    return render(request,'accounts/individual.html')

def organisation(request):
    return render(request,'accounts/organisation.html')

def reduces(request):
    return render(request,'accounts/reduces.html')

def leaderboard(request):
    return render(request,'accounts/leaderboard.html')

def howitworks(request):
    return render(request,'accounts/howitworks.html')



