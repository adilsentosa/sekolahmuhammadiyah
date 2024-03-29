# Generated by Django 5.0.2 on 2024-02-18 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_guru', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=10)),
                ('pendidikan_terakhir', models.CharField(max_length=10)),
                ('no_telp', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=32)),
                ('code_color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=6)),
                ('jumlah_sesi', models.IntegerField()),
                ('lama_sesi', models.IntegerField()),
                ('jam_mulai', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='JadwalKhusus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.CharField(max_length=3)),
                ('keterangan', models.CharField(max_length=32)),
                ('sesi', models.CharField(max_length=2)),
                ('hari', models.CharField(max_length=6)),
                ('durasi', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_jurusan', models.CharField(max_length=20)),
                ('nama_jurusan', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='RequestJadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_guru', models.CharField(max_length=10)),
                ('hari', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kelas', models.CharField(max_length=16)),
                ('kelas', models.CharField(max_length=3)),
                ('nama_kelas', models.CharField(max_length=1)),
                ('id_jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jurusan')),
            ],
        ),
        migrations.CreateModel(
            name='Mapel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_mapel', models.CharField(max_length=10)),
                ('nama_mapel', models.CharField(max_length=255)),
                ('kelompok_mapel', models.CharField(max_length=1)),
                ('kelas', models.CharField(max_length=3)),
                ('beban_jam', models.IntegerField()),
                ('id_jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jurusan')),
            ],
        ),
        migrations.CreateModel(
            name='Penjadwalan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=6)),
                ('sesi', models.IntegerField()),
                ('kode_jadwal', models.CharField(max_length=16)),
                ('keterangan', models.CharField(max_length=64)),
                ('jam_mulai', models.TimeField()),
                ('jam_selesai', models.TimeField()),
                ('id_guru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.guru')),
                ('id_kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.kelas')),
                ('id_mapel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.mapel')),
            ],
        ),
        migrations.CreateModel(
            name='Rumusan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari_request', models.CharField(max_length=255)),
                ('kelas', models.TextField()),
                ('total', models.IntegerField()),
                ('beban_kerja', models.IntegerField()),
                ('hasil_rumusan', models.FloatField()),
                ('id_guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guru')),
            ],
        ),
        migrations.CreateModel(
            name='TugasGuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tugas', models.CharField(max_length=16)),
                ('tahun_ajaran', models.CharField(max_length=9)),
                ('sisa_jam', models.IntegerField()),
                ('status', models.CharField(default='0', max_length=1)),
                ('beban_jam', models.IntegerField()),
                ('id_guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guru')),
                ('id_kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.kelas')),
                ('id_mapel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mapel')),
            ],
        ),
    ]
