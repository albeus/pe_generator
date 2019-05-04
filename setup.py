#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pe_generator',
    version='1.0.0',
    description='pe_generator generates Person entities represented as data structures',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/albeus/pe_generator',
    author="Alberto Eusebi",
    author_email='alberto.eusebi@albeus.eu',
    packages=find_packages(include=['pe_generator']),
    install_requires=[
        'Click>=6.0',
        'pathlib2>=2.2.0;python_version<"3.6"',
    ],
    entry_points={
        'console_scripts': [
            'pe_generator=pe_generator.cli:main',
        ],
    },
)
