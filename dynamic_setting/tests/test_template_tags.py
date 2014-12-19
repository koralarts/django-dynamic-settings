from django.template import Context, Template
from django.test import TestCase
from dynamic_setting.models import Setting


class GetSettingTestCase(TestCase):

    def _create_setting(self, name, data):
        return Setting.objects.create(name=name, data=data)

    def test_get_setting(self):
        name = 'TEST_SETTING'
        data = 'Test data'
        self._create_setting(name, data)
        template = Template(
            '{% load dynamic_setting_tags %}'
            '{% get_setting setting_name %}'
        )
        context = Context({'setting_name': name})
        self.assertEqual(template.render(context), data)