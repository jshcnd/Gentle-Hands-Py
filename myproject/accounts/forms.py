from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Child, DentalRecord
from django.core.management.base import BaseCommand
from datetime import date

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('staff', 'Staff'), ('admin', 'Admin')], required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        role = self.cleaned_data['role']

        if role == 'staff':
            user.is_staff = True
        elif role == 'admin':
            user.is_superuser = True

        if commit:
            user.save()
        return user

class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = [
            'first_name', 'last_name', 'middle_name', 'category', 'gender',
            'date_of_birth', 'current_age', 'date_of_admission', 'age_of_admission'
        ]

class DentalRecordForm(forms.ModelForm):
    class Meta:
        model = DentalRecord
        fields = ['record_date', 'dental_center', 'reason', 'investigations', 'outcome']

class Command(BaseCommand):
    help = 'Update current_age and age_of_admission for all children'

    def handle(self, *args, **kwargs):
        today = date.today()
        children = Child.objects.all()
        for child in children:
            if child.date_of_birth:
                dob = child.date_of_birth
                child.current_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            if child.date_of_birth and child.date_of_admission:
                doa = child.date_of_admission
                child.age_of_admission = doa.year - dob.year - ((doa.month, do.day) < (dob.month, dob.day))

            child.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated ages for all children'))