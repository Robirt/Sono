from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group

class appConfig(AppConfig):
    name = 'app'
    def ready(self):
        post_migrate.connect(create_groups, sender=self)

def create_groups(sender):
    if sender.name == 'auth':
       Group.objects.get_or_create(name='user')
       Group.objects.get_or_create(name='admin')
