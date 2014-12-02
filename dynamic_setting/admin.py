from django.contrib import admin
from dynamic_setting.models import Setting

class SettingAdmin(admin.ModelAdmin):
    fields = ('name', 'data')
    list_display = ('name', 'data')
    list_editable = ('data',)
    list_search = ('name', 'data')

admin.site.register(Setting, SettingAdmin)