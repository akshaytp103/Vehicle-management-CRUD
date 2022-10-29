from django.shortcuts import render, redirect
from .form import RegistrationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from vehicle.views import Vehicle_list
from django.contrib import messages , auth
from .models import Account

# Create your views here.

def signup(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            
            # username      = form.cleaned_data['username']
            email      = form.cleaned_data['email']
            password   = form.cleaned_data['password']

            # request.session['username']   = username
            request.session['email']      = email
            request.session['password']   = password
            user = form.save()
            return redirect('login')
        
        else:
            return redirect('login')
    context = {'form' : form}
    return render(request,'registration/sign_up.html',context)

    


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('list')

    if request.method == "POST":
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Account.objects.get(email=email)
        except :
            messages.error(request,"user Does not exist..")

        user = authenticate(request,email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('list')
        else:
            messages.error(request,'user does not exist..')
            return redirect('login')

    return render(request,'registration/login.html')


       
def logoutuser(request):
    logout(request)
    return redirect('login')