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

## Usage

### Inside Python:
```
import dynamic_setting.models import Setting

Setting.objects.setting('NAME_OF_SETTING')
```

### Inside Template:
```
{% load dynamic_setting %}

{% get_setting 'NAME_OF_SETTING' %}
```