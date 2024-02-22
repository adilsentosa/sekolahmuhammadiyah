from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import Group



class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
            model = User
            fields =["username", "email", "password1", "password2"]   
    def clean_username(self):
        username = self.cleaned_data['username']
        exclude_user = self.instance
        if User.objects.filter(username=username).exclude(pk=exclude_user.pk).exists():
            raise forms.ValidationError('Username sudah digunakan.')
        return username
    def clean_password(self):
        password = self.cleaned_data['password1','password2']
        if not password:
            return None
        return super().clean_password()
    
# class GuruCreateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
           
#     nama_guru = models.CharField(max_length=32)
#     status = models.CharField(max_length=10)
#     pendidikan_terakhir = models.CharField(max_length=10)
#     no_telp = models.CharField(max_length=16)
#     code_color = models.CharField(max_length=10)    

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#             group = Group.objects.get_or_create(name='pegawai')[0]
#             group.user_set.add(user)
            
#             guru = Guru.objects.create(
#                 user=user,
#                 nama_guru=self.cleaned_data['nama_guru'],
#                 status=self.cleaned_data['status'],
#                 pendidikan_terakhir=self.cleaned_data['pendidikan_terakhir'],
#                 no_telp=self.cleaned_data['no_telp'],
#                 email=self.cleaned_data['email'],
#                 code_color=self.cleaned_data['code_color'],
#             )
#         return user

class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        fields = '__all__'
        exclude = ['user']
        
class PenugasanForm(forms.ModelForm):
    class Meta:
        model = TugasGuru
        fields = '__all__'

class RequestJadwalForm(forms.ModelForm):
    class Meta:
        model = RequestJadwal
        fields = '__all__'

class JadwalKhususForm(forms.ModelForm):
    class Meta:
        model = JadwalKhusus
        fields = '__all__'

class MapelForm(forms.ModelForm):
    class Meta:
        model = Mapel
        fields = '__all__'
class JadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = '__all__'  

class KelasForm(ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'

class RumusanForm(ModelForm):
    class Meta:
        model = Rumusan
        fields = '__all__'

class PenjadwalanForm(ModelForm):
    class Meta:
        model = Penjadwalan
        fields = '__all__'