# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name         = 'rootmeapi',
    version      = '1.0',
    description  = 'Root Me API',
    url          = 'http://github.com/Remigascou/rootmeapi',
    author       = 'Podalirius',
    author_email = 'podalirius@protonmail.com',
    license      = 'GPL2',
    packages     = [
        'rootmeapi',
        'rootmeapi/types'
    ],
    zip_safe     = False
)
