from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.   we will be using user creation form in django

def register(request):
    if request.method=='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'welcome {username}, your account is created')
            return redirect('login')     #name
    else:
        form= RegisterForm()
    
    return render(request, 'users/register.html', {'form':form})

#decorator
@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

# only accessible when loged in if not then by default django redirevt it to account/login url
# so we need to add login url in settings.py of main app