from market import forms
from django import forms
from django.db.models import fields
from .models import Register

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        

