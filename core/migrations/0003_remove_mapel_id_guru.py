# Generated by Django 4.2.10 on 2024-02-21 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_kelas_walikelas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapel',
            name='id_guru',
        ),
    ]
