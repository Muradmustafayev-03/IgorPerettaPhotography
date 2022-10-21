from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def redirect_home(request):
    return redirect('home')


def register_request(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = RegisterForm()
    return render(request=request, template_name='register.html', context={'register_form': form})


def login_request(request):
    pass


def comment(request):
    pass


def contact(request):
    pass


def create_a_post(request):
    pass
