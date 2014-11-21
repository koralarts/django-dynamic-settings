from django.core import validators
from django.db import models
from django.utils.translation import ugettext as _

from dynamic_setting.managers import SettingManager

class Setting(models.Model):
    """
    Model that will hold the Setting data.
    """
    name = models.CharField(_('Setting Name'), max_length=50, unique=True, db_index=True,
        validators=[
            validators.RegexValidator(r'^[A-Z][A-Z0-9_]*[A-Z0-9]$',
                'Enter a valid setting name. Example: SETTING_NAME_ITEM.'
            ),
        ],
    )
    data = models.TextField(_('Data'), default='-')

    objects = SettingManager()

    def __str__(self):
        return self.name