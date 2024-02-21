from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
            model = User
            fields =["username", "email", "password1", "password2"]   
    
class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        fields = '__all__'
        exclude = ['user']
 
class jadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'  

class kelasForm(ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'