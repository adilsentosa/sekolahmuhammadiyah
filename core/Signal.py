from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if not Group.objects.filter(name='admin').exists():
        Group.objects.create(name='admin')
    if not Group.objects.filter(name='pegawai').exists():
        Group.objects.create(name='pegawai')
