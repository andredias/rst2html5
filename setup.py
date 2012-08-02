#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from html5css3 import __version__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='rst2html5',
    version=__version__,
    author='André Felipe Dias',
    author_email='andref dot dias at gmail dot com',
    url='https://bitbucket.org/andre_felipe_dias/rst2html5',
    packages=find_packages(),
    test_suite='tests',
    setup_requires=['nose >= 1.0'],
    keywords = "rst html5 doctutils",
    description='Generates (X)HTML5 documents from standalone reStructuredText sources',
    long_description=long_description,
    license='MIT License',
    include_package_data=True,
    install_requires=['distribute', 'docutils', 'Genshi >= 0.6'],
    scripts=['rst2html5'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Markup :: HTML',
      ],
)
