from django.urls import path

from . import views



urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('registeruser/', views.registerPage, name='registerpage'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('guru/', views.get_guru, name='guru'),
    path('guru/add_guru/', views.add_guru, name='create_guru'),
    path('guru/update_guru/<str:pk>/', views.update_guru, name='update_guru'),
    path('guru/delete/<str:pk>/', views.delete_guru, name='delete_guru'),
    
    path('requestjadwal/', views.get_requestjadwal, name='requestjadwal'),
    path('requestjadwal/add_requestjadwal/', views.add_requestjadwal, name='create_requestjadwal'),
    path('requestjadwal/update_requestjadwal/<str:pk>/', views.update_requestjadwal, name='update_requestjadwal'),
    path('requestjadwal/delete/<str:pk>/', views.delete_requestjadwal, name='delete_requestjadwal'),
    
    path('jadwal_khusus/', views.get_jadwalkhusus, name='jadwalkhusus'),
    path('jadwal_khusus/add_jadwal_khusus/', views.add_jadwalkhusus, name='create_jadwalkhusus'),
    path('jadwal_khusus/update_jadwal_khusus/<str:pk>/', views.update_jadwalkhusus, name='update_jadwalkhusus'),
    path('jadwal_khusus/delete/<str:pk>/', views.delete_jadwalkhusus, name='delete_jadwalkhusus'),
    
    path('mapel/', views.get_mapel, name='mapel'),
    path('mapel/add_mapel/', views.add_mapel, name='create_mapel'),
    path('mapel/update_mapel/<str:pk>/', views.update_mapel, name='update_mapel'),
    path('mapel/delete/<str:pk>/', views.delete_mapel, name='delete_mapel'),
    
    path('penugasan/', views.get_penugasan, name='penugasan'),
    path('penugasan/add_penugasan/', views.add_penugasan, name='create_penugasan'),
    path('penugasan/update_penugasan/<str:pk>/', views.update_penugasan, name='update_penugasan'),
    path('penugasan/delete/<str:pk>/', views.delete_penugasan, name='delete_penugasan'),

    path('jadwal/', views.get_jadwal, name='get_jadwal'),
    path('jadwal/add/', views.create_jadwal, name='add_jadwal'),
    path('jadwal/delete/<str:pk>/', views.delete_jadwal, name='delete_jadwal'),
    path('jadwal/update/<str:pk>/', views.update_jadwal, name='update_jadwal'),
    
    path('kelas/', views.get_kelas, name='get_kelas'),
    path('kelas/add/', views.add_kelas, name='add_kelas'),
    path('kelas/delete/<str:pk>/', views.delete_kelas, name='delete_kelas'),


    path('rumusan/', views.get_rumusan, name='get_rumusan'),
    path('rumusan/add/', views.rumusan_add, name='add_rumusan'),
    path('rumusan/update/<str:pk>/', views.rumusan_update, name='rumusan_update'),
    path('rumusan/delete/<str:pk>/', views.rumusan_delete, name='rumusan_delete'),

    path('penjadwalan/', views.get_penjadwalan, name='get_penjadwalan'),
    path('penjadwalan/add/', views.add_penjadwalan, name='add_penjadwalan'),
    path('penjadwalan/update/<str:pk>/', views.update_penjadwalan, name='update_penjadwalan'),
    path('penjadwalan/delete/<str:pk>/', views.delete_penjadwalan, name='delete_penjadwalan'),
]