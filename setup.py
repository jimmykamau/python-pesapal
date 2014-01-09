#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pesapal',
    version='0.0.5',
    description='Pesapal API python library.',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/python-pesapal',
    packages=['pesapal',],
    package_dir = {'pesapal': 'lib'},
    license='MIT License',
    zip_safe=True)
