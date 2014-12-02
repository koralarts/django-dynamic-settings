from django.db import models

class SettingManager(models.Manager):

    def setting(self, name):
        """Gets the setting or creates it with a default data value."""
        defaults = {'name': name, 'data': '-'}
        obj, _ = self.get_or_create(name__iexact=name, defaults=defaults)
        return obj