from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
      #put a check in place
    if request.method=='POST':
        form = UserCreationForm(request.POST)#create an instance
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('account')
    else:
        form = UserCreationForm(request.POST)
    return render(request,'users/register.html',{'form':form})  

