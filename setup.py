#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup

with open('README.txt') as f:
    long_description = f.read()

setup(
    name='rst2html5',
    version='1.2',
    author='André Felipe Dias',
    author_email='andref.dias@gmail.com',
    url='https://bitbucket.org/andre_felipe_dias/rst2html5',
    keywords=["restructuredtext", "rst", "html5", "doctutils"],
    description='Generates (X)HTML5 documents from standalone reStructuredText sources',
    long_description=long_description,
    license='MIT License',
    platforms='any',
    install_requires=['docutils', 'Genshi', 'Pygments'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    zip_safe=False,
    py_modules=['rst2html5'],
    entry_points={
        'console_scripts': [
            'rst2html5 = rst2html5:main',
        ],
    },
)
