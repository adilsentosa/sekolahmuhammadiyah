from django.db import models

# Create your models here

class Guru(models.Model):
    nama_guru = models.CharField(max_length=32)
    status = models.CharField(max_length=10)
    pendidikan_terakhir = models.CharField(max_length=10)
    no_telp = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    code_color = models.CharField(max_length=10)

class Jadwal(models.Model):
    hari = models.CharField(max_length=6)
    jumlah_sesi = models.IntegerField()
    lama_sesi = models.IntegerField()
    jam_mulai = models.TimeField()

class JadwalKhusus(models.Model):
    kelas = models.CharField(max_length=3)
    keterangan = models.CharField(max_length=32)
    sesi = models.CharField(max_length=2)
    hari = models.CharField(max_length=6)
    durasi = models.IntegerField()

class Jurusan(models.Model):
    id_jurusan = models.CharField(max_length=20)
    nama_jurusan = models.CharField(max_length=32)

class Kelas(models.Model):
    id_kelas = models.CharField(max_length=16)
    kelas = models.CharField(max_length=3)
    id_jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)
    nama_kelas = models.CharField(max_length=1)

class Mapel(models.Model):
    kode_mapel = models.CharField(max_length=10)
    nama_mapel = models.CharField(max_length=255)
    kelompok_mapel = models.CharField(max_length=1)
    kelas = models.CharField(max_length=3)
    beban_jam = models.IntegerField()
    id_jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)

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

class RequestJadwal(models.Model):
    id_guru = models.CharField(max_length=10)
    hari = models.CharField(max_length=255)

class Rumusan(models.Model):
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    hari_request = models.CharField(max_length=255)
    kelas = models.TextField()
    total = models.IntegerField()
    beban_kerja = models.IntegerField()
    hasil_rumusan = models.FloatField()

class TugasGuru(models.Model):
    id_tugas = models.CharField(max_length=16)
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    id_mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
    id_kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    tahun_ajaran = models.CharField(max_length=9)
    sisa_jam = models.IntegerField()
    status = models.CharField(max_length=1, default='0')
    beban_jam = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
