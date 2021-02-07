from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,'index.html')

def user(request):

    users = User.objects.all()
    return render(request, 'users.html',{"users": users})
