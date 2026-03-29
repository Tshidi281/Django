from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, RegistrationForm

def home(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'login':
            login_form = LoginForm(request.POST)
            registration_form = RegistrationForm()
            
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome back, {username}!')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password.')
        else:
            registration_form = RegistrationForm(request.POST)
            login_form = LoginForm()
            
            if registration_form.is_valid():
                user = registration_form.save(commit=False)
                password = registration_form.cleaned_data.get('password')
                user.set_password(password)
                user.save()
                
                username = registration_form.cleaned_data.get('username')
                messages.success(request, f'Account created successfully for {username}!')
                
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
    else:
        login_form = LoginForm()
        registration_form = RegistrationForm()
    
    return render(request, 'home.html', {
        'login_form': login_form,
        'registration_form': registration_form
    })