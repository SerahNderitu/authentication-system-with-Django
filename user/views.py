from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def index(request):
    return render(request, 'user/index.html', {'title': 'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            email_template = get_template('user/email.html')
            data = {'username': username}
            subject, from_email, to = 'Welcome', 'your_email@gmail.com', email
            html_content = email_template.render(data)
            message = EmailMultiAlternatives(subject, html_content, from_email, [to])
            message.attach_alternative(html_content, "text/html")
            message.send()

            messages.success(request, f'Your account has been created ! You can now login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'register here'})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:  # verify user input and validate variables
            form = login(request, user)
            messages.success(request, f'Welcome {username} !!')
            return redirect('index', form.cleaned_data)
        else:
            messages.info(request, f'Account not known. Please sign in again')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})





