#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='python3_pesapal',
    version='0.0.1',
    description='Pesapal API python3 library. A fork of https://github.com/kelonye/python-pesapal.',
    author='Jimmy Kamau',
    author_email='jimmykambiz@gmail.com',
    url='https://github.com/jimmykamau/python-pesapal',
    packages=['python3_pesapal',],
    package_dir = {'python3_pesapal': 'lib'},
    license='MIT License',
    zip_safe=True)
