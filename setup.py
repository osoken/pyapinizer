# -*- coding: utf-8 -*-

from setuptools import setup

from pyapinizer import (
    __version__, __author__, __description__, __long_description__,
    __package_name__
)

setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email='osoken.devel@outlook.jp',
    url='https://github.com/osoken/pyapinizer',
    description=__description__,
    long_description=__long_description__,
    license='MIT',
    packages=[__package_name__],
    install_requires=[]
)
