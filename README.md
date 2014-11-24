django-dynamic-settings
=======================

## Installation

Install via `Pip`:

```
$ pip install git+https://github.com/koralarts/django-dynamic-settings
```

Add module to `Installed Apps`:

```
INSTALLED_APPS = (
	...
	'dynamic_setting',
	...
)
```

## Migrate

```
$ ./manage migrate dynamic_setting
```

## Getting a Setting
```
from dynamic_setting.models import Setting

setting_obj = Setting.objects.get_setting('TEST_SETTING')

# Print the name of the Setting:
print(setting_obj.name)

# Print the value of the Setting:
print(setting_obj.value)
```
