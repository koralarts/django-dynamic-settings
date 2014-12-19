from django.test import TestCase
from dynamic_setting.models import Setting


class SettingTestCase(TestCase):
    
    def _create_setting(self, name, **kwargs):
        return Setting.objects.create(name=name, **kwargs)

    def test_create_setting(self):
        """ Test Creating a new Setting. """
        name = 'TEST_SETTING'
        data = 'Setting Data'
        setting = self._create_setting(name, data=data)
        self.assertEqual(setting.name, name)
        self.assertEqual(setting.__str__(), name)
        self.assertEqual(setting.data, data)

    def test_create_setting_no_data(self):
        """ Test Creating a new setting without Data. """
        name = 'TEST_SETTING'
        data = '-'
        setting = self._create_setting(name)
        self.assertEqual(setting.name, name)
        self.assertEqual(setting.__str__(), name)
        self.assertEqual(setting.data, data)

    def test_delete_setting(self):
        """ Test Deleting a setting object. """
        name = 'TEST_SETTING'
        setting = self._create_setting(name)
        setting_pk = setting.pk
        setting.delete()
        try:
            Setting.objects.get(pk=setting_pk)
        except Setting.DoesNotExist:
            pass
        else:
            self.fail('Setting with ID {} should not exist.'.format(setting_pk))

    def test_get_setting(self):
        """ Test Getting a setting object. """
        name = 'TEST_SETTING'
        data = 'Setting data'
        setting = self._create_setting(name, data=data)
        try:
            setting2 = Setting.objects.get(pk=setting.pk)
        except Setting.DoesNotExist:
            self.fail('Setting with ID {} should exist'.format(setting.pk))
        self.assertEqual(setting.name, setting2.name)
        self.assertEqual(setting.__str__(), setting2.__str__())
        self.assertEqual(setting.data, setting2.data)
        self.assertEqual(setting.pk, setting2.pk)

    def test_update_setting(self):
        """ Test Updating a setting object. """
        name = 'TEST_SETTING'
        data = 'Setting data'
        data2 = 'New Setting Data'
        setting = self._create_setting(name, data=data)
        setting.data = data2
        setting.save()
        setting2 = Setting.objects.get(pk=setting.pk)
        self.assertEqual(setting2.data, data2)