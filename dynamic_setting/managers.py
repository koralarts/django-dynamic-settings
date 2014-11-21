from django.db import models

class SettingManager(models.Manager):

    def setting(self, name):
        obj, _ = self.get_or_create(name__iexact=name, defaults={'name': name, 'data': '-'})
        return obj