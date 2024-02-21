from django.db import models
from django.contrib.auth.models import User


# Create your models here

class Guru(models.Model):
    nama_guru = models.CharField(max_length=32)
    status = models.CharField(max_length=10)
    pendidikan_terakhir = models.CharField(max_length=10)
    no_telp = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    code_color = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    @property
    def set_nama(self, firts_name, last_name):
        self.user.first_name = firts_name
        self.user.last_name = last_name
        self.user.save()
        return self
    def __str__(self):
        return  self.nama_guru

class Jadwal(models.Model):
    hari = models.CharField(max_length=6)
    jumlah_sesi = models.IntegerField()
    lama_sesi = models.IntegerField()
    jam_mulai = models.TimeField()
    @property
    def set_hari(self, hari):
        self.hari = hari
        return self
    def __str__(self):
        return self.hari
class JadwalKhusus(models.Model):
    kelas = models.CharField(max_length=3)
    keterangan = models.CharField(max_length=32)
    sesi = models.CharField(max_length=2)
    hari = models.CharField(max_length=6)
    durasi = models.IntegerField()
    def __str__(self):
        return self.kelas

class Kelas(models.Model):
    id_kelas = models.CharField(max_length=16)
    kelas = models.CharField(max_length=3)
    nama_kelas = models.CharField(max_length=1)
    Walikelas = models.ForeignKey(Guru, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.kelas} {self.nama_kelas} '

class Mapel(models.Model):
    kode_mapel = models.CharField(max_length=10)
    nama_mapel = models.CharField(max_length=255)
    kelompok_mapel = models.CharField(max_length=1)
    kelas = models.CharField(max_length=3)
    beban_jam = models.IntegerField()
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    def __str__(self):
        return self.kode_mapel

class Penjadwalan(models.Model):
    id_kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE, null=True)
    id_mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE, null=True)
    hari = models.CharField(max_length=6)
    sesi = models.IntegerField()
    kode_jadwal = models.CharField(max_length=16)
    keterangan = models.CharField(max_length=64)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    def __str__(self):
        return self.kode_jadwal

class RequestJadwal(models.Model):
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE, null=True) 
    hari = models.CharField(max_length=255)
    def __str__(self):
        return self.id_guru

class Rumusan(models.Model):
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    hari_request = models.CharField(max_length=255)
    kelas = models.TextField()
    total = models.IntegerField()
    beban_kerja = models.IntegerField()
    hasil_rumusan = models.FloatField()
    def __str__(self):
        return self.id_guru

class TugasGuru(models.Model):
    id_tugas = models.CharField(max_length=16)
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    id_mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
    id_kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    tahun_ajaran = models.CharField(max_length=9)
    sisa_jam = models.IntegerField()
    status = models.CharField(max_length=1, default='0')
    beban_jam = models.IntegerField()
    def __str__(self):
        return self.id_tugas

