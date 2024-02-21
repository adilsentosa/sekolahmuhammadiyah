from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *
from .forms import CreateUserForm

# Create your views here.

#dashboard
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html',)
 
# login & register
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

#crud guru
@login_required(login_url='login')
def get_guru (request):
    context = {
        'guru_form': Guru.objects.all()
    }
    return render(request, 'guru/guru.html', context)
@login_required(login_url='login')
def add_guru(request):
    form = CreateUserForm()
    form2 = GuruForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = GuruForm(request.POST)
        if form.is_valid() and form2.is_valid() :
            user = form.save()
            f2 = form2.save(commit=False)
            f2.user=user
            f2.save()
            group = Group.objects.get_or_create(name='pegawai')
            group[0].user_set.add(user)
            messages.success(request, "Data Berhasil Ditambah")
            return redirect('create_guru')
    context = { 'form': form, 'form2': form2}
    return render(request, 'guru/guru_form.html', context)
# @login_required(login_url='login')
# def add_guru(request):
#     if request.method == 'POST':
#         form = GuruCreateForm(request.POST)
#         if form.is_valid():
#             form.save()        
#             messages.success(request, "Data Berhasil Ditambah")
#             return redirect('create_guru')
#         else:
#             form = GuruCreateForm()
#     context = {'form': form}
#     return render(request, 'guru/guru_form.html', context)

@login_required(login_url='login')
def update_guru(request, pk):
    g = Guru.objects.get(id=pk)
    form = CreateUserForm(request.POST or None, instance=g.user)
    form2 = GuruForm(request.POST or None, instance=g)
    if request.method == 'POST' and form.is_valid() and form2.is_valid():
        form.save          
        form2.save()            
        messages.success(request, "Data Berhasil Diperbaharui")
        return redirect('create_guru')
    context = {'form': form, 'form2': form2}
    return render(request, 'guru/guru_form.html', context)

@login_required(login_url='login')
def delete_guru(request, pk):
    g = get_object_or_404 (Guru, id=pk)
    g.delete()
    g.user.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('guru')

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
