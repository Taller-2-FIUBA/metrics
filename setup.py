#!/usr/bin/env python
# pylint: disable= missing-module-docstring
from setuptools import setup

setup(
    name='metrics',
    version='1.0',
    description='Service to interact with metrics',
    author='Grupo 5',
    packages=[''],
    include_package_data=True,
    exclude_package_data={'': ['tests', 'kubernetes']},
)
