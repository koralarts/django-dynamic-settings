[![Build Status](https://travis-ci.org/koralarts/django-dynamic-settings.svg)](https://travis-ci.org/koralarts/django-dynamic-settings)

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

setting = Setting.objects.setting('NAME_OF_SETTING')

# Get the name of the setting object:
setting.name

# Get the data of the setting object:
setting.data
```

### Inside Template:
```
{% load dynamic_setting_tag %}

{% get_setting 'NAME_OF_SETTING' %}
```
