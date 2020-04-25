from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form =UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'your account has been created. You can now login. ')
            return redirect('login')
    else:    
        form =UserRegisterationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile (request):
    if request.method=='POST':
        userForm= UserUpdateForm(request.POST,instance =request.user)
        profileUpdateForm=ProfileUpdateForm(request.POST
                ,request.FILES
                ,instance=request.user.profile)
        if userForm.is_valid() and profileUpdateForm.is_valid():
            userForm.save()
            profileUpdateForm.save()
            messages.success(request,f'your account has been updates.')
            return redirect('profile')    
    else :
        userForm= UserUpdateForm(instance =request.user)
        profileUpdateForm=ProfileUpdateForm(instance=request.user.profile)

    context={
        'userForm':userForm,
        'profileForm':profileUpdateForm
    }
    return render(request,'users/profile.html',context)

