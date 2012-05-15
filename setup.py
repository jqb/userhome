# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    version='1.0',
    name='userhome',
    description='Get current user home path.',
    author='Kuba Janoszek',
    author_email='kuba.janoszek@gmail.com',
    py_modules=['userhome'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    setup_requires=['setuptools_git'],
)
