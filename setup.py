#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from html5css3 import __version__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='rst2html5',
    version=__version__,
    author='André Felipe Dias <andref.dias@gmail.com>',
    url='https://bitbucket.org/tin_nqn/rst2slides',
    packages=find_packages(),
    test_suite='tests',
    keywords = "rst html5 doctutils",
    description='Generates (X)HTML5 documents from standalone reStructuredText sources',
    long_description=long_description,
    license='MIT License',
    include_package_data=True,
    install_requires=['distribute', 'docutils >= 0.9.1', 'Genshi >= 0.6.1'],
    scripts=['rst2html5'],
    classifiers = [
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup',
      ],
)
