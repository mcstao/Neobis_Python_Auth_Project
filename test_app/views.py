from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm, LoginUserForm


def test_app(request):
    return render(request, 'test_app/test_app.html', {"title": "Главная страница"})


def login_view(request):
    if request.method == 'GET':
        data = {
            'form': LoginUserForm
        }
        return render(request, 'test_app/login.html', context=data)

    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/login/')
        data = {
            'form': form
        }
        return render(request, 'test_app/login.html', context=data)


def logout_view(request):
    logout(request)
    return redirect("/login/")


def register_view(request):
    if request.method == 'GET':
        data = {
            'form': RegisterUserForm
        }
        return render(request, 'test_app/register.html', context=data)

    if request.method == 'POST':
        form = RegisterUserForm(data=request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register/')

        data = {
            'form': form
        }
        return render(request, 'test_app/register.html', context=data)


