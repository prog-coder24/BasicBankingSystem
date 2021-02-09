from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request,'home.html')

def user(request):

    users = User.objects.all()
    return render(request, 'users.html',{"users": users})

def transfer(request, pk):
    user = User.objects.get(pk=pk)
    receiver = User.objects.all()
    return render(request, 'transfer.html',{"user":user,"receiver":receiver})
    
def history(request):

    transactions = Transaction.objects.all()
    return render(request, 'history.html', {"transactions":transactions})

def add_transfer(request):

     if request.method == 'POST':

         sender = request.POST.get('sender',None)
         receiver = request.POST.get('receiver',None)
         amount = request.POST.get('amount',None)
         sender_instance = User.objects.get(full_name=sender)
         curr_balance = sender_instance.current_balance
         receiver_instance = User.objects.get(full_name=receiver)
        
         if curr_balance > int(amount):
              status = 'Successful'
         else:
              status = 'Failed'
         
         Transaction.objects.create(sender=sender_instance,recipient=receiver_instance,amount=amount,status=status)
         
         return redirect(history)


