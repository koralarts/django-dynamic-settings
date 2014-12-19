from django.test import TestCase
from dynamic_setting.models import Setting
from dynamic_setting.templatetags.dynamic_setting import get_setting


class GetSettingTestCase(TestCase):

    def _create_setting(self, name, data):
        return Setting.objects.create(name=name, data=data)

    def test_get_setting(self):
        name = 'TEST_SETTING'
        data = 'Test data'
        self._create_setting(name, data)
        self.assertEqual(get_setting(name), data)