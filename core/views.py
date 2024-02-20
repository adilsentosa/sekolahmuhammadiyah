from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *
from .forms import CreateUserForm

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect') 
    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
            
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html',)
  
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='pegawai')
            user.groups.add(group)
            Guru.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/signup.html', context)


#crud kelas
@login_required(login_url='login')
def get_kelas (request):
    form = Kelas.objects.all()
    context = {
        'form': form
    }
    return render(request, 'kelas/kelas.html', context)
@login_required(login_url='login')
def add_kelas(request):
    form = kelasForm()
    if request.method == 'POST':
        form = kelasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_kelas')
    context = {
        'form': form
    }
    return render(request, 'kelas/kelas_form.html', context)

@login_required(login_url='login')
def update_kelas(request, pk):
    kelas = Kelas.objects.get(id=pk)
    form = kelasForm(instance=kelas)
    if request.method == 'POST':
        form = kelasForm(request.POST, instance=kelas)
        if form.is_valid():
            form.save()
            return redirect('get_kelas')
    context = {
        'form': form
    }
    return render(request, 'kelas/kelas_form.html', context)

@login_required(login_url='login')
def delete_kelas(request, pk):
    kelas = Kelas.objects.get(id=pk)
    if request.method == 'POST':
        kelas.delete()
        return redirect('get_kelas')
    context = {
        'obj': kelas
    }
    return render(request, 'kelas/kelas_delete.html', context)

#crud jadwal
def get_jadwal(request):
    form = Jadwal.objects.all()
    context = {
        'form': form
    }
    return render(request, 'jadwal/jadwal.html', context)

def create_jadwal(request):
    form = jadwalForm()
    if request.method == 'POST':
        form = jadwalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_jadwal')
    context = {
        'form': form
    }
    return render(request, 'jadwal/jadwal_form.html', context)

def update_jadwal(request, pk):
    jadwal = Jadwal.objects.get(id=pk)
    form = jadwalForm(instance=jadwal)
    if request.method == 'POST':
        form = jadwalForm(request.POST, instance=jadwal)
        if form.is_valid():
            form.save()
            return redirect('get_jadwal')
    context = {
        'form': form
    }
    return render(request, 'jadwal/jadwal_form.html', context)

def delete_jadwal(request, pk):
    jadwal = Jadwal.objects.get(id=pk)
    if request.method == 'POST':
        jadwal.delete()
        return redirect('get_jadwal')
    context = {
        'obj': jadwal
    }
    return render(request, 'jadwal/jadwal_delete.html', context)
