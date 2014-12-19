from django import template
from dynamic_setting.models import Setting

register = template.Library()

@register.simple_tag
def get_setting(setting_name):
    """ Gets the data stored inside the setting. """
    setting = Setting.objects.setting(setting_name)
    return setting.data