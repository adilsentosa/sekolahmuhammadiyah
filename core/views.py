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

#crud Penugasan
@login_required(login_url='login')
def get_penugasan (request):
    context = {
        'penugasan_form': TugasGuru.objects.all()
    }
    return render(request, 'penugasan/penugasan.html', context)

@login_required(login_url='login')
def add_penugasan(request):
    form = PenugasanForm()
    if request.method == 'POST':
        form = PenugasanForm(request.POST)        
        if form.is_valid() :
            form.save()
            messages.success(request, "Data Berhasil Ditambah")
            return redirect('create_penugasan')
    context = { 'form': form}
    return render(request, 'penugasan/penugasan_form.html', context)

@login_required(login_url='login')
def update_penugasan(request, pk):
  p = Kelas.objects.get(id=pk)
  form = PenugasanForm(instance= p)
  if request.method == 'POST' :
    form = PenugasanForm(request.POST, instance= p)
    if form.is_valid():
      form.save()
      messages.success(request, "Data Berhasil Diperbaharui")
      return redirect('create_penugasan')
  context = {'form':form}
  return render(request,'penugasan/penugasan_create.html', context)

@login_required(login_url='login')
def delete_penugasan(request, pk):
  p = get_object_or_404(TugasGuru, id=pk)
  p.delete()
  messages.success(request, "Data Berhasil Dihapus")
  return redirect('penugasan')

#crud RequestJadwal
@login_required(login_url='login')
def get_requestjadwal (request):
    context = {
        'requestjadwal_form': RequestJadwal.objects.all()
    }
    return render(request, 'requestjadwal/requestjadwal.html', context)
@login_required(login_url='login')
def add_requestjadwal(request):
    form = RequestJadwalForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():    
            form.save()
            messages.success(request, "Data Berhasil Ditambah")
            return redirect('create_requestjadwal')
    context = { 'form': form}
    return render(request, 'requestjadwal/requestjadwal_form.html', context)

def update_requestjadwal(request, pk):
    r = RequestJadwal.objects.get(id=pk)
    form = RequestJadwalForm(request.POST or None, instance=r)
    if request.method == 'POST' and form.is_valid() :
        form.save                    
        messages.success(request, "Data Berhasil Diperbaharui")
        return redirect('create_requestjadwal')
    context = {'form': form}
    return render(request, 'requestjadwal/requestjadwal_form.html', context)

@login_required(login_url='login')
def delete_requestjadwal(request, pk):
  r = get_object_or_404(RequestJadwal, id=pk)
  r.delete()
  messages.success(request, "Data Berhasil Dihapus")
  return redirect('requestjadwal')

# crud jadwal khusus
@login_required(login_url='login')
def get_jadwalkhusus (request):
    context = {
        'jadwalkhusus_form': JadwalKhusus.objects.all()
    }
    return render(request, 'jadwalkhusus/jadwalkhusus.html', context)
@login_required(login_url='login')
def add_jadwalkhusus(request):
    form = JadwalKhususForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():    
            form.save()
            messages.success(request, "Data Berhasil Ditambah")
            return redirect('create_jadwalkhusus')
    context = { 'form': form}
    return render(request, 'jadwalkhusus/jadwalkhusus_form.html', context)

def update_jadwalkhusus(request, pk):
    j = JadwalKhusus.objects.get(id=pk)
    form = JadwalKhususForm(request.POST or None, instance=j)
    if request.method == 'POST' and form.is_valid() :
        form.save                    
        messages.success(request, "Data Berhasil Diperbaharui")
        return redirect('create_jadwalkhusus')
    context = {'form': form}
    return render(request, 'jadwalkhusus/jadwalkhusus_form.html', context)

@login_required(login_url='login')
def delete_jadwalkhusus(request, pk):
  j = get_object_or_404(JadwalKhusus, id=pk)
  j.delete()
  messages.success(request, "Data Berhasil Dihapus")
  return redirect('jadwalkhusus')

# crud mapel
@login_required(login_url='login')
def get_mapel(request):
    context = {
        'mapel_form': Mapel.objects.all()
    }
    return render(request, 'mapel/mapel.html', context)
@login_required(login_url='login')
def add_mapel(request):
    form = MapelForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():    
            form.save()
            messages.success(request, "Data Berhasil Ditambah")
            return redirect('create_mapel')
    context = { 'form': form}
    return render(request, 'mapel/mapel_form.html', context)

def update_mapel(request, pk):
    m = Mapel.objects.get(id=pk)
    form = MapelForm(request.POST or None, instance=m)
    if request.method == 'POST' and form.is_valid() :
        form.save                    
        messages.success(request, "Data Berhasil Diperbaharui")
        return redirect('create_mapel')
    context = {'form': form}
    return render(request, 'mapel/mapel_form.html', context)

@login_required(login_url='login')
def delete_mapel(request, pk):
  m = get_object_or_404(Mapel, id=pk)
  m.delete()
  messages.success(request, "Data Berhasil Dihapus")
  return redirect('mapel')


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


def get_rumusan (request):
    form = Rumusan.objects.all()
    context = {
        'form': form
    }
    return render(request, 'rumusan/rumusan.html', context)

def rumusan_add (request):
    form = RumusanForm()
    if request.method == 'POST':
        form = RumusanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_rumusan')
    context = {
        'form': form
    }
    return render(request, 'rumusan/rumusan_form.html', context)

def rumusan_update (request, pk):
    rumusan = Rumusan.objects.get(id=pk)
    form = RumusanForm(instance=rumusan)
    if request.method == 'POST':
        form = RumusanForm(request.POST, instance=rumusan)
        if form.is_valid():
            form.save()
            return redirect('get_rumusan')
    context = {
        'form': form
    }
    return render(request, 'rumusan/rumusan_form.html', context)

def rumusan_delete(request):
    rumusan = Rumusan.objects.get(id=pk)
    if request.method == 'POST':
        rumusan.delete()
        return redirect('get_rumusan')
    context = {
        'obj': rumusan
    }
    return render(request, 'rumusan/rumusan_delete.html', context)



def get_penjadwalan (request):
    form = Penjadwalan.objects.all()
    context = {
        'form': form

    }
    return render(request, 'penjadwalan/penjadwalan.html', context)


def add_penjadwalan (request):
    form = PenjadwalanForm()
    if request.method == 'POST':
        form = PenjadwalanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_penjadwalan')
    context = {
        'form': form

    }
    return render(request, 'penjadwalan/penjadwalan_form.html', context)

def update_penjadwalan (request, pk):
    penjadwalan = Penjadwalan.objects.get(id=pk)
    form = PenjadwalanForm(instance=penjadwalan)
    if request.method == 'POST':
        form = PenjadwalanForm(request.POST, instance=penjadwalan)
        if form.is_valid():
            form.save()
            return redirect('get_penjadwalan')
    context = {
        
        'form': form

    }
    return render(request, 'penjadwalan/penjadwalan_form.html', context)


def delete_penjadwalan(request):
    penjadwalan = Penjadwalan.objects.get(id=pk)
    if request.method == 'POST':
        penjadwalan.delete()
        return redirect('get_penjadwalan')
    context = {
        
        'obj': penjadwalan

    }
    return render(request, 'penjadwalan/penjadwalan_delete.html', context)

