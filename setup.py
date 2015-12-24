#!/usr/bin/env python

from setuptools import setup
from pyrest_client import rest_client

setup(
    name='pyrest-client',
    version=rest_client.__version__,
    description='A simple rest client based on requests',
    long_description=open('README.md', 'r').read(),
    author='Wu Cheng',
    author_email='iwucheng@outlook.com',
    url='https://github.com/iamwucheng/pyrest-client',
    download_url='https://github.com/iamwucheng/pyrest-client',
    packages=['pyrest_client'],
    install_requires=['requests'],
    tests_require=['mock', 'nose', 'coverage'],
    test_suite="nose.collector"
)
