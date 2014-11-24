from setuptools import setup, find_packages

VERSION = "1.0.0"

LONG_DESCRIPTION = """
=================================
django-dynamic-setting
=================================
Django Dynamic Setting is a small module that allows you to create settings that can be edited
using the Django admin dashboard.
"""

setup(
    name='django-dynamic-settings',
    version=VERSION,
    url='https://github.com/koralarts/django-dynamic-settings',
    download_url='https://github.com/koralarts/django-dynamic-settings/tarball/1.0',
    description='Small module that allows you to generate dynamic settings that can be edited inside the Django admin dashboard',
    long_description=LONG_DESCRIPTION,
    author='Karl Castillo',
    author_email='karl@karlworks.com',
    maintainer='Karl Castillo',
    maintainer_email='karl@karlworks.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management'
    ],
    keywords=['django','settings','utility'],
    packages=['django-dynamic-settings'],
    include_package_data=True
)