#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="numword-georgia",
    version="0.1",
    description="Python library for translate numbers to words in "
                "Georgia language",
    author='awnion',
    author_email='blinovsv@gmail.com',
    url='https://bitbucket.org/awnion/numword-georgia',
    packages=['numword_georgia'],
)
