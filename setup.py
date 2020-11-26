#!/usr/bin/python3

from setuptools import find_packages, setup

#  with open('requirements.txt', 'r') as requirements:
#      required = requirements.read().splitlines()

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='dreamutils',
    version='0.1.0',
    packages=find_packages(),
    url='',
    license='LGPL-3.0',
    author='ByteDream',
    author_email='',
    description='A collection of useful and often repeated python methods',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6.*',
    # install_requires=required
)
