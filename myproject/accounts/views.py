from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_backends
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import RegisterForm, ChildRegistrationForm, DentalRecordForm
from .models import Child, DentalRecord, Medication, Illness, Appointment, Immunization, GrowthRecord

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully.')
        else:
            messages.error(request, 'There was an error registering the user.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('dashboard')
        elif request.user.is_superuser:
            return redirect('admin_dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_dashboard')
                elif user.is_staff:
                    return redirect('dashboard')
                else:
                    return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def user_management(request):
    users = User.objects.all()
    return render(request, 'user_management.html', {'users': users})

@login_required
def delete_user(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)
    if request.user.id == user_to_delete.id:
        messages.error(request, "You cannot delete your own account.")
    elif request.method == 'POST':
        user_to_delete.delete()
        messages.success(request, "User deleted successfully.")
    else:
        messages.error(request, "Invalid request method.")
    return redirect('user_management')

@login_required
def medication_view(request):
    return render(request, 'medication.html')

@login_required
def medication_list(request, child_id=None):
    children = Child.objects.all()
    groups = ['A', 'B', 'C']
    medications = Medication.objects.all()

    if child_id:
        child = get_object_or_404(Child, id=child_id)
        medications = medications.filter(patient_name=child)

    if request.method == 'POST':
        Medication.objects.create(
            group=request.POST.get('group'),
            patient_name_id=request.POST.get('patient_name'),
            prescribed_by=request.POST.get('prescribed_by'),
            medicine_name=request.POST.get('medicine_name'),
            strength=request.POST.get('strength'),
            mg_per_kg_per_day=request.POST.get('mg_per_kg_per_day'),
            dose=request.POST.get('dose'),
            frequency=request.POST.get('frequency'),
            duration=request.POST.get('duration'),
            dwm=request.POST.get('dwm'),
        )
        return redirect('medication_list')

    return render(request, 'medication_list.html', {
        'children': children,
        'groups': groups,
        'medications': medications,
        'child_id': child_id
    })

@login_required
def illness_list(request, child_id=None):
    children = Child.objects.all()
    groups = ['A', 'B', 'C'] 

    if child_id:
        child = get_object_or_404(Child, id=child_id)
        illnesses = Illness.objects.filter(patient_name=child)
    else:
        illnesses = Illness.objects.all()  

    if request.method == 'POST':
        Illness.objects.create(
            group=request.POST.get('group'),
            patient_name_id=request.POST.get('patient_name'),
            reason=request.POST.get('reason'),
            treatment=request.POST.get('treatment'),
            date_logged=request.POST.get('date_logged'),
        )
        return redirect('illness_list', child_id=child_id)

    return render(request, 'illness_list.html', {
        'illnesses': illnesses,
        'children': children,
        'groups': groups,
        'child_id': child_id
    })

@login_required
def appointment_list(request):
    category = request.GET.get('category', '')
    if category:
        appointments = Appointment.objects.filter(medical_type=category)
    else:
        appointments = Appointment.objects.all()

    children = Child.objects.all() 

    if request.method == 'POST':
        Appointment.objects.create(
            patient_name_id=request.POST.get('patient_name'),
            medical_type=request.POST.get('medical_type'),
            appointment_date=request.POST.get('appointment_date'),
            hospital_name=request.POST.get('hospital_name'),
            medic_name=request.POST.get('medic_name'),
            reason=request.POST.get('reason'),
        )
        return redirect('appointment_list') 

    return render(request, 'appointment_list.html', {
        'appointments': appointments,
        'selected_category': category,
        'children': children,
    })

@login_required
def immunization_list(request):
    immunizations = Immunization.objects.all() 
    children = Child.objects.all() 

    if request.method == 'POST':
        Immunization.objects.create(
            patient_name_id=request.POST.get('patient_name'),  
            group_name=request.POST.get('group_name'),
            vaccine=request.POST.get('vaccine'),
            dose_no=request.POST.get('dose_no'),
            date_due=request.POST.get('date_due'),
            age_when_due=request.POST.get('age_when_due'),
            comments=request.POST.get('comments'),
        )
        return redirect('immunization_list')  

    return render(request, 'immunization.html', {
        'immunizations': immunizations,
        'children': children,
    })

@login_required
def medic(request):
    return render(request, 'medic.html')

@login_required
def growth_data(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    return render(request, 'growth_data.html', {'child': child})

@login_required
def growth_record(request, child_id=None):
    if child_id:
        growth_records = GrowthRecord.objects.filter(child_id=child_id)
    else:
        growth_records = GrowthRecord.objects.all()

    children = Child.objects.all()

    if request.method == 'POST':
        GrowthRecord.objects.create(
            child_id=request.POST.get('child_id'),
            age=request.POST.get('age'),
            weight=request.POST.get('weight'),
            height=request.POST.get('height'),
            head_circumference=request.POST.get('head_circumference') or None,
            chest_circumference=request.POST.get('chest_circumference') or None,
            teeth_upper=request.POST.get('teeth_upper') or None,
            teeth_lower=request.POST.get('teeth_lower') or None,
        )
        return redirect('growth_record')

    return render(request, 'growth_record.html', {
        'children': children,
        'growth_records': growth_records,
    })

@login_required
def change_user(request):
    return render(request, 'changeuser.html')

@login_required
def dental_record(request):
    return render(request, 'dental_record.html')

@login_required
def dental_record_view(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    if request.method == 'POST':
        form = DentalRecordForm(request.POST)
        if form.is_valid():
            dental_record = form.save(commit=False)
            dental_record.child = child
            dental_record.save()
            return redirect('dental_record', child_id=child.id)
    else:
        form = DentalRecordForm()
        records = DentalRecord.objects.filter(child=child)
    return render(request, 'dental_record.html', {'form': form, 'records': records, 'child': child})

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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        category = request.POST.get('category')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        current_age = request.POST.get('current_age')
        date_of_admission = request.POST.get('date_of_admission')
        age_of_admission = request.POST.get('age_of_admission')

        Child.objects.create(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            category=category,
            gender=gender,
            date_of_birth=date_of_birth,
            current_age=current_age,
            date_of_admission=date_of_admission,
            age_of_admission=age_of_admission
        )

        return redirect('childrecord')

    return render(request, 'registerChild.html')

def child_record(request):
    children = Child.objects.all()
    return render(request, 'childrecord.html', {'children': children})

def edit_child(request):
    if request.method == 'POST':
        child_id = request.POST.get('child_id')
        child = get_object_or_404(Child, id=child_id)

        child.first_name = request.POST.get('first_name')
        child.middle_name = request.POST.get('middle_name')
        child.last_name = request.POST.get('last_name')
        child.category = request.POST.get('category')
        child.gender = request.POST.get('gender')
        child.date_of_birth = request.POST.get('date_of_birth')
        child.date_of_admission = request.POST.get('date_of_admission')
        child.current_age = request.POST.get('current_age')
        child.age_of_admission = request.POST.get('age_of_admission')
        child.save()

        return redirect('childrecord')