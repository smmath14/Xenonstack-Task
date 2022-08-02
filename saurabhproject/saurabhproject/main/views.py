from wsgiref.handlers import read_environ
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'main/homepage.html')


@csrf_exempt
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'main/sign.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('monuments')

            except IntegrityError:
                return render(request, 'main/sign.html',
                              {
                                  'form': UserCreationForm,
                                  'error': 'That username has already been taken. Please choose a new username.'
                              }
                              )

        else:
            return render(request, 'main/sign.html',
                          {
                              'form': UserCreationForm,
                              'error': 'Password did not match'
                          }
                          )


@csrf_exempt
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(
                request, 'main/login.html',
                {
                    'form': AuthenticationForm(),
                    'error': 'Username and password did not match'
                }
            )
        else:
            login(request, user)
            return redirect('monuments')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


def monuments(request):
    return render(request, 'main/monuments.html')
