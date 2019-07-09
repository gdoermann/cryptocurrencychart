#!/usr/bin/env python
import os
from setuptools import setup, find_packages

PACKAGE_DIR = 'cryptocurrencychart'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

required = []
with open('requirements.txt') as f:
    required.extend(f.read().splitlines())

version = __import__('{}.version'.format(PACKAGE_DIR)).get_version()


setup(
    name=PACKAGE_DIR,
    version=version,
    description='cryptocurrencychart is a wrapper around the cryptocurrencychart.com api.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Greg Doermann',
    author_email='greg@that.bz',
    url='https://github.com/gdoermann/cryptocurrencychart',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    test_suite='tests',
)
