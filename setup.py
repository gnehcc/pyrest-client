#!/usr/bin/env python

from setuptools import setup

setup(
        name='pyrest-client',
        version='0.1.1',
        description='A simple rest client based on requests',
        long_description=open('README.md', 'r').read(),
        license='Apache Software License',
        author='Wu Cheng',
        author_email='iwucheng@outlook.com',
        url='https://github.com/iamwucheng/pyrest-client',
        download_url='https://github.com/iamwucheng/pyrest-client',
        packages=['pyrest_client'],
        install_requires=['requests'],
        tests_require=['mock', 'nose', 'coverage'],
        test_suite="nose.collector",
        classifiers=[
            'Programming Language :: Python',
            'Natural Language :: English',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ]
)
