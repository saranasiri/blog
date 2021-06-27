from django.shortcuts import render,redirect
from .form import Userloginform,Userregisterform
from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def user_login(request):
    if request.method == 'POST':
        form =Userloginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'your login is successful','success')
                return redirect('blog:all_articles')
            else:
                messages.error(request,'your username or password is wrong','danger')
    else:
        form = Userloginform()
    return render(request,'form.html',{'form':form})
def user_register(request):
     if request.method == 'POST':
          form = Userregisterform(request.POST)
          if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            emailadress = form.cleaned_data['emailadress']
            user = authenticate(request, username=username, password=password,emailadress=emailadress)
            messages.success(request, 'your  register is successful', 'success')
            return redirect('accounts:user-login')
     else:
        form = Userregisterform()
        return render(request,'register.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'you logout successfully','success')
    return redirect('blog:all_articles')
