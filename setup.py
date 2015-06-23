#!/usr/bin/env python

from distutils.core import setup

setup(
    name='gitlabpy',
    version='0.1.1',
    description='Gitlab for humans',
    author='Nathaniel Gentile',
    author_email='ncg09@hampshire.edu',
    package_dir={'gitlabpy': ''},
    packages=['gitlabpy', 'gitlabpy.api'])
