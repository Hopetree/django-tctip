# -*- coding:utf-8 -*-
# Author: https://github.com/Hopetree
# Date: 2020/7/11
from setuptools import find_packages, setup

VERSION = '1.4.4'

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name='django-tctip',
    version=VERSION,
    author='Hopetree',
    author_email='zlwork2014@163.com',
    description='A web tip of Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Hopetree/django-tctip',
    keywords='django tctip tip',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django >= 1.8'
    ],
    python_requires='>=3.5',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
    ],
)
