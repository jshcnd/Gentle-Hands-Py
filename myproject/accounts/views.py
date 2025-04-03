from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import RegisterForm, ChildRegistrationForm

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required
def medication_view(request):
    return render(request, 'medication.html')

@login_required
def medication_list(request):
    return render(request, 'medication_list.html')

@login_required
def illness_list(request):
    return render(request, 'illness_list.html')

@login_required
def appointment_list(request):
    return render(request, 'appointment_list.html')

@login_required
def immunization_list(request):
    return render(request, 'immunization.html')

@login_required
def medic(request):
    return render(request, 'medic.html')

@login_required
def growth_data(request):
    return render(request, 'growth_data.html')

@login_required
def growth_record(request):
    return render(request, 'growth_record.html')

@login_required
def change_user(request):
    return render(request, 'changeuser.html')

@login_required
def change_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        if new_username:
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Username already taken.')
            else:
                request.user.username = new_username
                request.user.save()
                messages.success(request, 'Username updated successfully.')
        else:
            messages.error(request, 'Please provide a valid username.')
    return redirect('changeuser')

@login_required
def change_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        if new_email:
            if User.objects.filter(email=new_email).exists():
                messages.error(request, 'Email already in use.')
            else:
                request.user.email = new_email
                request.user.save()
                messages.success(request, 'Email updated successfully.')
        else:
            messages.error(request, 'Please provide a valid email address.')
    return redirect('changeuser')

@login_required
def change_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 and password2:
            if password1 == password2:
                request.user.set_password(password1)
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Password updated successfully.')
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Please fill out both password fields.')
    return redirect('changeuser')

def register_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('childrecord')
    else:
        form = ChildRegistrationForm()
    return render(request, 'registerChild.html', {'form': form})