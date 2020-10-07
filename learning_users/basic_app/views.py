from django.shortcuts import render
from basic_app.forms import UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def login_index(request):
    return render(request,'basic_app/login_index.html')

@login_required
def special(request):
    return HttpResponse('Your are login, nice!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'basic_app/registration.html',
                        context={'user_form':user_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        #authenticate the user if user is registered
        user = authenticate(username=username,password=password,email=email)

        if user:
            if user.is_active:
                #really login the user
                login(request,user)
                #we could redirect to page that customized for login users not just index
                return HttpResponseRedirect(reverse('basic_app:login_index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('someone try to login and failed')
            print('username:{},password:{}'.format(username,password))
            return HttpResponse('invalid login details')
    else:
        return render(request,'basic_app/login.html')
