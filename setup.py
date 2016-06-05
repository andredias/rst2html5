# -*- encoding: utf-8 -*-
import io
import re
from os.path import dirname
from os.path import join
from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()

setup(
    name='rst2html5',
    version='1.8',
    license='MIT License',
    author='André Felipe Dias',
    author_email='andref.dias@gmail.com',
    url='https://bitbucket.org/andre_felipe_dias/rst2html5',
    keywords=["restructuredtext", "rst", "html5", "doctutils"],
    description='Generates (X)HTML5 documents from standalone reStructuredText sources',
    long_description="%s\n%s" % (read("README.rst"),
                                 re.sub(":obj:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst"))),
    platforms='any',
    install_requires=read('requirements.txt').split(),
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
    py_modules=['rst2html5'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rst2html5 = rst2html5:main',
        ],
    },
)
