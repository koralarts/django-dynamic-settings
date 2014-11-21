from setuptools import setup, find_packages

VERSION = "1.0.0"

LONG_DESCRIPTION = """
=================================
django-dynamic-setting
=================================
Django Dynamic Setting is a small module that allows you to create settings that can be edited
using the Django admin dashboard.
"""

setup = (
    name='django-dynamic-setting',
    version=VERSION,
    url='https://github.com/koralarts/django-dynamic-settings',
    license='MIT',
    description='Small module that allows you to generate dynamic settings that can be edited inside the Django admin dashboard',
    long_description=LONG_DESCRIPTION,
    author='Karl Castillo',
    author_email='karl@karlworks.com',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: MIT",
        "Programming Language :: Python",
        "Topic :: Internet :: Dynamic Content",
    ],
    keywords="django,settings",
    zip_safe=False,
    package=find_packages(),
    include_package_data=True
)