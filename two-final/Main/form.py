from django.forms import ModelForm
from Main.models import *
from django import forms
from phonenumber_field.formfields import PhoneNumberField




class CareerForm(forms.ModelForm):
    class Meta:
        model = cadidate
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        
