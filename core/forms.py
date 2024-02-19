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

class RemoveUser(forms.Form):
    username = forms.CharField()    
    
class GuruForm(ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Guru
        fields = '__all__'
        exclude = ['user']
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        guru = super().save(commit=False)
        guru.user = user
        if commit:
            user.save()
            guru.save()
        return guru


class jadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'  

class kelasForm(ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'