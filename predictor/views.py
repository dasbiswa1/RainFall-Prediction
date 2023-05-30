from django.http import HttpResponse
from django.shortcuts import render
from .models import weather


# Create your views here.
def index(request):
    return render(request,'predictor/index.html')

def about(request):
    return render(request,'predictor/about.html')
def contact(request):
    return render(request,'predictor/contact.html')
def input(request):
    return render(request,'predictor/input.html')
def output(request):
    context={'weatherdata':weather.objects.all()}
    return render(request,'predictor/ot.html',context)