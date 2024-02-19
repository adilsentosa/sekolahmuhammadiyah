from django.urls import path

from . import views



urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('registeruser/', views.registerPage, name='registerpage'),
    path('logout/', views.logoutUser, name='logout'),
    path('jadwal/', views.get_jadwal, name='get_jadwal'),
    path('jadwal/add/', views.create_jadwal, name='add_jadwal'),
    path('jadwal/delete/<str:pk>/', views.delete_jadwal, name='delete_jadwal'),
    path('jadwal/update/<str:pk>/', views.update_jadwal, name='update_jadwal'),
    path('kelas/', views.get_kelas, name='get_kelas'),
    path('kelas/add/', views.add_kelas, name='add_kelas'),
    path('kelas/delete/<str:pk>/', views.delete_kelas, name='delete_kelas'),
]