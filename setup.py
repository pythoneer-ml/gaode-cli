#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='gaode_api_cli',
    version='0.0.2',
    description=(
      '简易高德API命令行工具'
    ),
    long_description=open('README.md').read(),
    author='Albin',
    author_email='binwei.zeng3@gmail.com',
    maintainer='albin3',
    maintainer_email='binwei.zeng3@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/pythoneer-ml/pypi-gaode-api',
    install_requires=[
        'fire>=0.1.3',
        'urllib3>=1.22'
    ],
    scripts=[
      'bin/gaode-api-intersection'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
