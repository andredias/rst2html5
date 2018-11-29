# -*- encoding: utf-8 -*-
from pathlib import Path
from setuptools import find_packages
from setuptools import setup


basedir = Path(__file__).parent
with (basedir / 'README.rst').open(encoding='utf-8') as f:
    readme = f.read()
with (basedir / 'CHANGELOG.rst').open(encoding='utf-8') as f:
    changelog = f.read()
long_description = '\n'.join([readme, changelog])


setup(
    name='rst2html5',
    version='1.10',
    license='MIT License',
    author='André Felipe Dias',
    author_email='andref.dias@gmail.com',
    url='https://bitbucket.org/andre_felipe_dias/rst2html5',
    keywords=["restructuredtext", "rst", "html5", "doctutils"],
    description='Generates (X)HTML5 documents from standalone reStructuredText sources',
    long_description=long_description,
    platforms='any',
    install_requires=[
        'docutils>=0.14',
        'genshi>=0.7',
        'pygments==2.0.2',
    ],
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
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=['rst2html5_'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rst2html5 = rst2html5_:main',
            'rst2html5.py = rst2html5_:main',  # overrides docutils' rst2html5.py
        ],
    },
)
