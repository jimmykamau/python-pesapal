#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pesapal',
    version='0.0.1',
    description='Pesapal API python library.',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/python_pesapal',
    packages=find_packages(exclude=['test.py']),
    #install_requires = ['oauth'],
    license='MIT License',
    zip_safe=True)
