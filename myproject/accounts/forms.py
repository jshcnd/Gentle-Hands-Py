from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Child, DentalRecord

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

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